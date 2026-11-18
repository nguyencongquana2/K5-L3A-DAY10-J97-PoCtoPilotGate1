"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def refund_guard_intervention_rate(trials):
    """Share of tickets whose refund write was stopped and handed to a reviewer."""
    stopped = sum(
        any(
            event.get("type") == "gate"
            and event.get("tool") == "issue_refund"
            and event.get("action") == "escalate"
            for event in trial.get("events", [])
        )
        for trial in trials
    )
    return stopped / max(1, len(trials))


def customer_daily_cap_breach_rate(trials):
    """Share of tickets that would push automatic refunds for one customer over the daily cap."""
    breached = sum(
        any(
            event.get("type") == "guard"
            and event.get("kind") == "customer_daily_auto_refund_cap"
            and event.get("breach") is True
            for event in trial.get("events", [])
        )
        for trial in trials
    )
    return breached / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "refund_guard_intervention_rate": refund_guard_intervention_rate,
    "customer_daily_cap_breach_rate": customer_daily_cap_breach_rate,
}
STARTER_MONITORS = ("escalation_rate",)
