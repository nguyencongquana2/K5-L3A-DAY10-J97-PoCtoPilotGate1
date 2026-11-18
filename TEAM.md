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

Sản phẩm và kinh doanh; xem phân công chi tiết trong `WORKPLAN.md`.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## TranVietThinh-2A202603661

### Phần việc phụ trách

Vai Vận hành và pháp lý:
- Khối 1: Phiếu A (Mục A1 câu 1.2, A2 câu 1.4); rà soát ngưỡng an toàn, chi phí và vận hành trong `config/acceptance_criteria.json`.
- Khối 2: Giữ chính Phiếu B (`templates/form-b-evaluation-gates.md`); phân tích HAZOP mở rộng (B4), lập Checklist 9 nhóm việc Go-live kèm PIC (B5), cấu hình cổng vận hành và pháp lý trong `config/operating_gates.json` (mục operations, legal); viết Runbook 1–3 và phương án Giờ cao điểm (B7.5, B7.6).
- Khối 3: Phân tích sự cố vòng 2 dưới góc nhìn con người và quy trình (Phiếu C: C3, C4, C5, C10, C11); kiểm tra toàn bộ hồ sơ trước khi nộp.

### Đóng góp cụ thể

- Đã hoàn thành câu 1.2 (mục tiêu hệ thống dưới góc nhìn chị Oanh kế toán đối soát và chị Hạnh trưởng ca CSKH) trong Phiếu A.
- Đã hoàn thành câu 1.4 (thiết kế Telemetry production giám sát rủi ro ghi lỗi oan cho hãng vận chuyển đối tác bên ngoài) trong Phiếu A.
- Thống nhất cùng nhóm các ngưỡng an toàn vận hành: wrongful_refund_vnd_max = 0, wrongful_carrier_faults_max = 0, pii_leaks_max = 0, queue_stuck_max = 0, escalation_rate_max <= 0.3.

### Bằng chứng

- Phiếu A: `templates/form-a-criteria.md` dòng mục A1 (câu 1.2) và mục A2 (câu 1.4).
- Branch làm việc: `ops/2A202603661`.

### Exit ticket

- Một điều học được: Thước đo production telemetry không có sẵn ground-truth nhãn như offline test, do đó phải dựa vào các tín hiệu phản hồi gián tiếp (như khiếu nại qua cổng đối soát) và cần đặt ngưỡng báo động sớm trước khi vi phạm trần SLA/chính sách.
- Một điều còn chưa chắc: Cần đo lường chính xác năng lực thực tế của nhân viên CSKH khi vừa duyệt vé thủ công vừa xử lý các ca AI chuyển tiếp trong giờ cao điểm.
