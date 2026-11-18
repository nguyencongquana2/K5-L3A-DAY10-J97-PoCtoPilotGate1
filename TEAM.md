# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `J97`
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-J97-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S2` · Đối soát: shop bị trừ tiền lạ

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Công Quân | 2A202603675 | Kỹ sư cổng | X |
|   2 | Vũ Quang Minh | 2A202603657 | Sản phẩm và kinh doanh | |
|   3 | Trần Việt Thịnh | 2A202603661 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Kế hoạch phân công

Đọc [`WORKPLAN.md`](WORKPLAN.md) trước khi bắt đầu. Mỗi thành viên làm trên branch riêng, không tự chạy lệnh ký tiêu chí hoặc chốt vòng 1.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenCongQuan-2A202603675

### Phần việc phụ trách

Trưởng nhóm, tích hợp và Kỹ sư cổng; xem phân công chi tiết trong `WORKPLAN.md`.

### Đóng góp cụ thể

- Tích hợp và chốt Phiếu B; xác minh checkpoint vòng 1 `103a019b` và quyết định v1.
- Ghi nhận thẻ S2, chạy grade mốc prepared trước khi sửa và phân tích trace của injection, approval và giới hạn cộng dồn.
- Bổ sung cổng tổng hoàn tự động theo khách/ngày trong `lab10/guards.py`; thêm hai monitor sự cố trong `lab10/monitors.py`.
- Hoàn thiện Phiếu C, chạy regression trên bộ nền, chốt quyết định v2 và gom gói `submission/`.

### Bằng chứng

- Nhánh: `incident/s2-round2-2A202603675`.
- Grade cuối: `R-S2-grade-20261118-174301-f26ae8` (`PASS-VISIBLE`).
- S2 after: `R-S2-after-20261118-174301-f26ae8`; base regression: `R-base-after-20261118-174317-f26ae8`.
- Phiếu C: C0–C2, C6–C9; code: `lab10/guards.py`, `lab10/monitors.py`.

### Exit ticket

- Một điều học được: cổng đúng ở từng lệnh vẫn chưa đủ nếu rủi ro phát sinh từ trạng thái cộng dồn qua nhiều ticket; phải kiểm nguồn sự thật ở đúng phạm vi thời gian và chủ thể.
- Một điều còn chưa chắc: production cần kiểm chứng phép đọc-cộng-ghi ledger có nguyên tử và có nhìn thấy hoàn tay đủ nhanh hay không.

## VuQuangMinh-2A202603657

### Phần việc phụ trách

Sản phẩm và kinh doanh: mục tiêu, tiêu chí và ngưỡng, chi phí, ROI, phạm vi pilot, quyết định v1/v2. Người giữ Phiếu A và
`config/acceptance_criteria.json`; xem phân công chi tiết trong `WORKPLAN.md`.

### Đóng góp cụ thể

- **Khối 1, Phiếu A:** viết câu 1.1 (mục tiêu cấp hệ thống), câu 1.5 (đọc khoảng tin cậy, chọn (b)) và câu 1.6 (bản tiêu chí:
  6 câu "Nếu … thì chúng tôi sẽ …", 4 câu soát, 2 câu ranh giới đầu ra, ngày xem lại 30/11/2026); tổng hợp toàn Phiếu A.
- **Tiêu chí chấp nhận** (`config/acceptance_criteria.json`, trước khi ký): đặt 5 ngưỡng bắt buộc, `escalation_rate_max` 0,35,
  `business_ops` (chi phí ≤ 7.000đ/ticket, ROI ≥ 0,4, 0 ca ùn), `stop_condition` và bốn dòng `decision_rule`; mỗi ngưỡng có lý do
  từ `data/world.json` → `ops_facts`, `ops_limits`.
- **Khối 2, Phiếu B:** B3 (bản đồ dữ liệu; ví dụ drift REFUND-v3 → REFUND-v4 ngày 01/12/2026, khi trợ lý đọc cờ `index_active`
  thay vì ngày hiệu lực); dòng lăng kính **Kinh doanh** của pre-mortem B6 (2 lý do, cả hai thành cổng); B7.4 cổng `business`.
- **Cổng kinh doanh** (`config/operating_gates.json` mục `business`): đổi `cost_budget_per_ticket_vnd` 7.000 → 1.500 cho đúng
  nghĩa trần tiền LLM mỗi ticket (`ops_limits.max_llm_cost_per_ticket_vnd`); viết lý do cho trần hoàn trong ngày, phạm vi pilot, ROI.
- **Khối 3, Phiếu C (thẻ S2):** C5 (specification 3 vế cho `issue_refund` và giả định môi trường về `checkout_note`); dòng rủi ro
  kinh doanh "biên chi phí mỏng" ở C10; C12 quyết định v2 **Tiếp tục** đối chiếu `decision_rule` đã ký, kèm ba dòng bắt buộc.

### Bằng chứng

- Commit: `7691c24` (Phiếu A và tiêu chí, trước khi ký) · `58e9f24` (B3, B7.4, `cost_budget_per_ticket_vnd`) · `4115fcb` (B6)
  · `e2d7096` (C5, C10, C12). Pull request: #6, #8, #16. Tiêu chí ký ở commit `c46a4e4`.
- Mã lần chạy dùng trong phần của tôi: base `R-base-before-20261118-154403-bde05c` (B6, B7.4); prepared vòng 1
  `R-base-prepared-20261118-171734-0f18ac`; S2 prepared `R-S2-prepared-20261118-173329-0f18ac`; S2 after và grade cuối: mã ghi ở
  Phiếu C mục C12.
- Dòng trong phiếu: Phiếu A mục A1 (câu 1.1), A3, A4; Phiếu B mục B3, B6 (hai dòng Kinh doanh), B7.4; Phiếu C mục C5, C10
  (dòng thứ hai), C12.

### Exit ticket

- Một điều học được: viết `decision_rule` và ký trước khi thấy số buộc quyết định phải theo bằng chứng. Dòng Tiếp tục đòi đạt
  trên cả bộ nền **và** gói sự cố, nên ở v1 (mới có bộ nền) chỉ khẳng định được phần đã đo; đến v2, sau khi đo gói S2, mới đủ căn cứ.
- Một điều còn chưa chắc: trên dữ liệu mock, gói S2 sau khi sửa tốn 6.580đ/ticket, ROI 0,52, sát trần 7.000đ và ngưỡng 0,4. Tôi chưa
  chắc chi phí duyệt thật (kiểm mẫu 30%, thêm ca chuyển người khi REFUND-v4 hạ hạn mức tự động xuống 100.000đ) còn giữ được ROI ≥ 0,4.

## TranVietThinh-2A202603661

### Phần việc phụ trách

Vai Vận hành và pháp lý:
- Khối 1: Phiếu A (Mục A1 câu 1.2, A2 câu 1.4); rà soát ngưỡng an toàn, chi phí và vận hành trong `config/acceptance_criteria.json`.
- Khối 2: Giữ chính Phiếu B (`templates/form-b-evaluation-gates.md`); phân tích HAZOP mở rộng (B4), lập Checklist 9 nhóm việc Go-live kèm PIC (B5), cấu hình cổng vận hành và pháp lý trong `config/operating_gates.json` (mục operations, legal); viết Runbook 1–3 và phương án Giờ cao điểm (B7.5, B7.6).
- Khối 3: Phân tích sự cố vòng 2 dưới góc nhìn con người và quy trình (Phiếu C: C3.1, C4, C10, C11); kiểm tra toàn bộ hồ sơ trước khi nộp.

### Đóng góp cụ thể

- Khối 1: Đã hoàn thành câu 1.2 (mục tiêu hệ thống dưới góc nhìn chị Oanh kế toán đối soát và chị Hạnh trưởng ca CSKH) và câu 1.4 (thiết kế Telemetry production giám sát rủi ro ghi lỗi oan cho hãng vận chuyển đối tác) trong Phiếu A; thống nhất các ngưỡng an toàn vận hành.
- Khối 2: Hoàn thành HAZOP mở rộng B4 trên `file_carrier_fault`; Checklist 9 nhóm việc Go-live B5; Pre-mortem B6 ở lăng kính Con người & vận hành và Pháp lý; xây dựng Runbook 1–3 và phương án Giờ cao điểm B7.5, B7.6; cấu hình `operations` và `legal` trong `config/operating_gates.json`.
- Khối 3 (thẻ sự cố S2): Phân tích mức kiểm soát của con người C3.1; HAZOP C4 trên `issue_refund` (chặn trừ nợ shop oan, kiểm tra phê duyệt, trần lạm dụng hoàn tiền); bổ sung dòng Risk register C10; cập nhật Checklist và Runbook 4–5 trong C11; rà soát tính nhất quán toàn bộ hồ sơ trước khi nộp.

### Bằng chứng

- Phiếu A: `templates/form-a-criteria.md` mục A1 (câu 1.2) và mục A2 (câu 1.4).
- Phiếu B: `templates/form-b-evaluation-gates.md` mục B4, B5, B6 (dòng Con người & Pháp lý), B7.5, B7.6, B8.
- Phiếu C: `templates/form-c-incident.md` mục C3.1, C4, C10 (dòng 1), C11 (Checklist và Runbook 4–5), C12 (ký v2).
- Config: `config/operating_gates.json` mục `operations` (PIC `NV-TUNG`, stop_conditions có `merchant_debit_vnd > 0`, `review_sampling_pct` 30) và mục `legal` (chặn PII, nguyên nhân lỗi hãng).
- Branch làm việc: `ops/2A202603661`.

### Exit ticket

- Một điều học được: Thước đo production telemetry không có sẵn ground-truth nhãn như offline test, do đó phải dựa vào các tín hiệu phản hồi gián tiếp (như khiếu nại qua cổng đối soát) và cần đặt ngưỡng báo động sớm trước khi vi phạm trần SLA/chính sách.
- Một điều còn chưa chắc: Cần đo lường chính xác năng lực thực tế của nhân viên CSKH khi vừa duyệt vé thủ công vừa xử lý các ca AI chuyển tiếp trong giờ cao điểm.
