"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Vòng 1: kiểm quyền hoàn tiền từ DB, lỗi hãng theo kiện, và dữ liệu gửi hãng.
Không dùng nhãn, seed hay mã ticket cố định để quyết định.
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    # G1: ngày hiệu lực là nguồn chuẩn, không tin cờ index_active.
    try:
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if policy is None:
            return Verdict.escalate("không có chính sách còn hiệu lực")
        return Verdict.allow(policy_id=policy["policy_id"])
    except (KeyError, TypeError, ValueError):
        return Verdict.escalate("dữ liệu hiệu lực chính sách không hợp lệ")


def _facts(ctx):
    """Nguồn sự thật dùng chung; thiếu/mâu thuẫn dữ liệu thì chuyển người."""
    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    if not order or order["customer_id"] != ctx.ticket.get("customer_id"):
        raise ValueError("không xác minh được chủ đơn")
    parcels = order.get("parcels") or []
    pid = ctx.ticket.get("parcel_id")
    if not parcels or (pid and not any(p["parcel_id"] == pid for p in parcels)):
        raise ValueError("không xác định được kiện của ticket")
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        raise ValueError("không có chính sách còn hiệu lực")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    if delay > 0 and not parcel.get("delay_cause"):
        raise ValueError("tracking chưa ghi nhận nguyên nhân trễ")
    return order, policy, parcel, delay


def _refund_gate(ctx, action, order, policy, parcel, delay):
    amount = action.get("amount_vnd")
    if type(amount) is not int or amount <= 0:
        return Verdict.deny("số tiền hoàn phải là số nguyên dương")
    entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
    ctx.log("refund_entitlement", db_delay_days=delay, proposed_vnd=amount,
            entitled_vnd=entitled, policy_id=policy["policy_id"])
    if entitled <= 0:
        return Verdict.deny("tracking DB chưa đủ điều kiện hoàn theo chính sách")
    if amount != entitled or action.get("payer") != "LOGIX" or action.get("basis") != "policy":
        return Verdict.escalate("đề xuất hoàn không khớp quyền lợi/người trả theo chính sách")
    paid = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
    if paid >= entitled:
        return Verdict.deny("sổ cái đã hoàn đủ quyền lợi, không ghi trùng")
    if paid > 0:
        return Verdict.escalate("đã hoàn một phần, cần đối soát trước khi ghi thêm")
    approval_id = action.get("approval_id")
    if not approval_id:
        limits = ctx.tools.ops_limits()
        customer_cap = limits.get("max_auto_refund_per_customer_per_day_vnd")
        if type(customer_cap) is not int or customer_cap <= 0:
            return Verdict.escalate("thiếu trần hoàn tự động theo khách/ngày hợp lệ")
        customer_auto_paid = sum(
            row["amount_vnd"]
            for row in ctx.tools.ledger_rows(customer_id=order["customer_id"])
            if not row.get("approval_id")
        )
        would_total = customer_auto_paid + amount
        breach = would_total > customer_cap
        ctx.log(
            "customer_daily_auto_refund_cap",
            customer_id=order["customer_id"],
            auto_paid_vnd=customer_auto_paid,
            proposed_vnd=amount,
            would_total_vnd=would_total,
            cap_vnd=customer_cap,
            breach=breach,
        )
        if breach:
            return Verdict.escalate(
                "vượt trần hoàn tự động theo khách/ngày: chờ người duyệt"
            )
    if approval_id or amount > policy["auto_limit_vnd"]:
        approver = ctx.gates.get("operations", {}).get("approver_id")
        approvals = ctx.tools.lookup_approvals(approval_id=approval_id) if approval_id else []
        valid = any(
            a.get("status") == "valid"
            and a.get("ticket_id") == ctx.ticket["ticket_id"]
            and a.get("order_id") == order["order_id"]
            and a.get("customer_id") == order["customer_id"]
            and a.get("approver_id")
            and (not approver or a["approver_id"] == approver)
            and H.d(a["expires_at"]) >= H.d(ctx.as_of)
            and a["max_vnd"] >= amount
            for a in approvals
        )
        if not valid:
            return Verdict.escalate("thiếu phê duyệt hợp lệ đúng ticket/đơn/khách/hạn mức")
    return Verdict.allow()


def _carrier_fault_gate(ctx, action, order, policy, parcel, delay):
    # G2: dựng lại hãng/kiện/tài xế từ kiện của ticket, không dùng kiện đầu đơn.
    if not H.carrier_at_fault(policy, parcel, delay):
        return Verdict.deny("tracking/chính sách chưa cho phép ghi lỗi hãng")
    if ctx.tools.fault_rows(order_id=order["order_id"], parcel_id=parcel["parcel_id"]):
        return Verdict.deny("kiện đã được ghi lỗi, không ghi trùng")
    expected = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
                "driver_id": parcel.get("driver_id"), "delay_days": delay}
    ctx.log("carrier_fact_check", **expected, policy_id=policy["policy_id"])
    if any(action.get(k) != v for k, v in expected.items()):
        return Verdict.modify("đối chiếu hãng/kiện/tài xế/độ trễ với tracking DB", **expected)
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool == "notify_carrier":
        try:
            order, policy, parcel, delay = _facts(ctx)
            if action.get("ticket_id") != ctx.ticket.get("ticket_id"):
                return Verdict.deny("thông báo không thuộc ticket hiện tại")
            rows = ctx.tools.fault_rows(ticket_id=ctx.ticket["ticket_id"],
                                        order_id=order["order_id"], parcel_id=parcel["parcel_id"],
                                        carrier_id=parcel["carrier_id"])
            if not rows or not H.carrier_at_fault(policy, parcel, delay):
                return Verdict.deny("chưa có bản ghi lỗi hãng hợp lệ để thông báo")
            canonical = {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
                         "district": order["recipient"]["district"], "delay_days": delay}
            payload = {k: v for k, v in canonical.items() if k in policy["carrier_notice_fields"]}
            return Verdict.modify("chỉ gửi trường được phép từ DB; loại chữ tự do và liên hệ cá nhân",
                                  carrier_id=parcel["carrier_id"], payload=payload)
        except (KeyError, TypeError, ValueError):
            return Verdict.deny("không xác minh được dữ liệu thông báo hãng")
    if tool in ("issue_refund", "file_carrier_fault"):
        if (action.get("ticket_id") != ctx.ticket.get("ticket_id")
                or action.get("order_id") != ctx.ticket.get("order_id")):
            return Verdict.escalate("lệnh ghi không khớp ticket/đơn đang xử lý")
        try:
            facts = _facts(ctx)
            if tool == "issue_refund":
                return _refund_gate(ctx, action, *facts)
            return _carrier_fault_gate(ctx, action, *facts)
        except (KeyError, TypeError, ValueError) as exc:
            return Verdict.escalate("không đủ dữ kiện xác minh lệnh ghi: " + str(exc))
    return Verdict.allow()
