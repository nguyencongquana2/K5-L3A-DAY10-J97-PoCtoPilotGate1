# Kế hoạch làm bài · Nhóm J97

Tài liệu này là bảng điều phối chung. Mọi người đọc `README.md`, `RULES.md` và phần việc dưới đây trước khi sửa file.

## 1. Gán người vào ghế

Trưởng nhóm điền họ tên/MSSV vào cột cuối trước khi bắt đầu. Nếu nhóm có ba người, trưởng nhóm đồng thời nhận một trong ba vai chuyên môn.

| Ghế | Trách nhiệm chính | Người nhận |
|---|---|---|
| Trưởng nhóm · tích hợp và phát hành | Điều phối branch/PR, giữ timeline, chạy test, thực hiện các lệnh ký/chốt/gom bài sau khi cả nhóm duyệt | Nguyễn Công Quân · `2A202603675` |
| Kỹ sư cổng | Eval/trace, guard, test hồi quy, monitor và bằng chứng lần chạy | Nguyễn Công Quân · `2A202603675` |
| Sản phẩm và kinh doanh | Mục tiêu, tiêu chí/ngưỡng, chi phí–ROI–phạm vi pilot, quyết định v1/v2 | Vũ Quang Minh · `2A202603657` |
| Vận hành và pháp lý | HAZOP, checklist/PIC, hàng chờ duyệt, PII, runbook, risk register và kiểm bài nộp | Trần Việt Thịnh · `2A202603661` |

## 2. Quy tắc Git và quyền sửa file

1. Không commit trực tiếp lên `main`, trừ trưởng nhóm khi tích hợp hoặc chạy lệnh tạo mốc bắt buộc.
2. Mỗi người tạo branch: `gate/<mssv>`, `product/<mssv>`, `ops/<mssv>` hoặc `docs/<mssv>`.
3. Trước khi làm: `git switch main`, `git pull --ff-only origin main`, rồi tạo/chuyển branch.
4. Mỗi commit chỉ nên chứa một phần việc; push branch và báo trưởng nhóm review trước khi merge.
5. Không sửa file của người khác đang giữ. Ba phiếu dùng chung có một người cầm bút; người còn lại gửi nội dung cho người cầm bút tích hợp.
6. Không sửa `config/acceptance_criteria.json` sau khi ký; không sửa `lab10/guards_round1.py`, `config/operating_gates.round1.json` hoặc các file `.lock` sau khi tạo.
7. Không chạy `lab10.eval` trước khi tiêu chí đã ký, commit và push. Không chạy `lab10.checkpoint` khi cả nhóm chưa duyệt cổng vòng 1.
8. Không mở hoặc làm thẻ sự cố khác thẻ bàn đã bốc.

Quyền sở hữu file chính:

| File | Người giữ chính | Cách phối hợp |
|---|---|---|
| `templates/form-a-criteria.md` | Sản phẩm và kinh doanh | Kỹ sư cổng gửi A2/1.3; Vận hành–pháp lý gửi A1/1.2 và A2/1.4 |
| `config/acceptance_criteria.json` | Sản phẩm và kinh doanh | Cả nhóm duyệt mọi ngưỡng; trưởng nhóm chỉ chạy lệnh ký |
| `templates/form-b-evaluation-gates.md` | Vận hành và pháp lý | Hai vai còn lại gửi nội dung đúng mục B được giao |
| `lab10/guards.py`, `lab10/monitors.py` | Kỹ sư cổng | Chỉ merge sau khi test công khai đạt |
| `config/operating_gates.json` | Sản phẩm rồi Vận hành–pháp lý | Sản phẩm sửa `business` và commit trước; Vận hành pull commit đó rồi sửa `operations`, `legal` |
| `templates/form-c-incident.md` | Trưởng nhóm tích hợp | Cả ba vai cung cấp bằng chứng/mục được giao sau khi biết thẻ |
| `submission/submission.json`, `TEAM.md` | Trưởng nhóm | Không điền quyết định hoặc thẻ khi chưa có bằng chứng |

## 3. Phân công theo checkpoint

### CP1 · Khởi tạo

**Trưởng nhóm**

- Mời thành viên quyền Write và team chấm quyền Read trên GitHub.
- Điền bảng thành viên trong `TEAM.md`, gán người vào bốn ghế ở mục 1 và điền `members` trong `submission/submission.json`.
- Kiểm tra `origin`, thêm `upstream`, chạy `python -m unittest discover -s tests`.
- Commit/push kế hoạch để mọi người clone và nhận việc.

**Mỗi thành viên**

- Chấp nhận lời mời, clone repo, đặt `user.name` là MSSV và email `<MSSV>@example.com`.
- Viết sẵn mục cá nhân `## HoVaTen-MSSV` trong `TEAM.md`; cập nhật đóng góp/bằng chứng trong suốt bài.

### CP2 · Phiếu A và ký tiêu chí

| Người phụ trách | Việc phải làm | Đầu ra |
|---|---|---|
| Sản phẩm và kinh doanh | A1 câu 1.1; A3; A4; tổng hợp toàn Phiếu A; điền tiêu chí, ngưỡng, `stop_condition`, `decision_rule` | `templates/form-a-criteria.md`, `config/acceptance_criteria.json` |
| Kỹ sư cổng | A2 câu 1.3: một offline metric, dữ liệu, công thức, mẫu số và điểm mù | Nội dung gửi người giữ Phiếu A |
| Vận hành và pháp lý | A1 câu 1.2 và A2 câu 1.4: góc nhìn người vận hành, telemetry production và ngưỡng báo động | Nội dung gửi người giữ Phiếu A |
| Cả nhóm | Phản biện từng ngưỡng; kiểm tra tên team và quy tắc bốn quyết định | Biên bản đồng thuận trong commit/PR |
| Trưởng nhóm | Chỉ sau khi cả nhóm duyệt: chạy `python -m lab10.criteria sign`, commit và push ngay | `config/acceptance_criteria.lock` và commit ký |

Điểm dừng bắt buộc: thấy `ĐÃ KÝ`, commit ký đã có trên `origin/main`; từ đó không ai sửa tiêu chí.

### CP3 · Baseline, rủi ro và cổng vòng 1

| Người phụ trách | Việc phải làm | Mục/file |
|---|---|---|
| Kỹ sư cổng | Chạy baseline và gate; trace `T-002@55`; phân loại lỗi; viết 2–3 guard; hai ticket hiểm; test hồi quy | B0–B2, B7.1–B7.3; `lab10/guards.py` |
| Sản phẩm và kinh doanh | Bản đồ dữ liệu/drift; đặt cổng business có lý do từ `data/world.json`; chuẩn bị quyết định v1 | B3, B7.4, B8; `operating_gates.json.business` |
| Vận hành và pháp lý | HAZOP ≥3 dòng; checklist 9 nhóm có PIC; pre-mortem; cổng operations/legal; runbook 1–3 và giờ cao điểm | B4–B7.6; `operations`, `legal`; tích hợp Phiếu B |
| Cả nhóm | Chọn 2–3 rủi ro thành cổng; kiểm tra không chặn hết, không thu hẹp pilot về 0 | Review PR và report vòng 1 |
| Trưởng nhóm | Chạy test; khi cả nhóm duyệt mới chạy `lab10.checkpoint`, prepared eval/gate; tích hợp quyết định v1 và push | Bản chốt vòng 1, lock và commit |

### CP4 · Nhận thẻ, phân tích và sửa vòng 2

Không làm mục này trước khi Lab Coach phát thẻ và bàn đã bốc số.

| Người phụ trách | Việc phải làm | Mục/file |
|---|---|---|
| Trưởng nhóm | Pull `upstream`, ghi đúng Sx, chạy grade trước khi sửa, giữ report prepared và điều phối Phiếu C | C0–C1, nhật ký lần chạy |
| Kỹ sư cổng | Dò ít nhất hai ticket hỏng; fault tree kỹ thuật; sửa guard; thêm ít nhất một monitor mới; chạy regression | C2, C6–C9; `guards.py`, `monitors.py` |
| Sản phẩm và kinh doanh | Đánh giá tác hại, specification/giả định, phạm vi/chi phí, risk register và bằng chứng cho quyết định v2 | C3/C5/C7/C10/C12 phần kinh doanh |
| Vận hành và pháp lý | HAZOP của thẻ, nguyên nhân ngoài kỹ thuật, thay đổi operations/legal, checklist và runbook 4–5 | C3–C5, C7, C10–C11; config vận hành/pháp lý |
| Cả nhóm | Chạy grade sau sửa; xác nhận integrity, visible, regression, monitor; chọn v2 theo tiêu chí đã ký | Report ba mốc và quyết định v2 |

### CP5 · Gom bài và nộp

**Vận hành và pháp lý** kiểm Phiếu A/B/C đủ mọi mục, tên PIC và số liệu khớp config.  
**Kỹ sư cổng** chạy test, grade cuối và xác nhận report dùng đúng code/config cuối.  
**Sản phẩm và kinh doanh** kiểm quyết định v1/v2 và ba dòng bắt buộc có số liệu.  
**Trưởng nhóm** điền `submission/submission.json`, chạy `python -m lab10.check_submission --collect` đến khi thấy `ĐỦ THÀNH PHẦN`, review diff rồi commit/push.

Mỗi thành viên phải hoàn thiện mục cá nhân trong `TEAM.md` và tự nộp link repo trên LMS.

## 4. Checklist review của trưởng nhóm

- [ ] `TEAM.md` đủ họ tên, MSSV, vai, trưởng nhóm và mục cá nhân.
- [ ] Test công khai in `Ran 13 tests` và `OK`.
- [ ] Tiêu chí được ký và push trước lần `eval` đầu tiên.
- [ ] Cổng vòng 1 được checkpoint trước khi nhận/sửa thẻ sự cố.
- [ ] Không có hai người cùng sửa một file dùng chung chưa merge.
- [ ] Mỗi PR ghi mục phiếu, file, lệnh test và bằng chứng lần chạy liên quan.
- [ ] Grade cuối có integrity, visible, regression và monitor đạt.
- [ ] Lệnh gom bài in `ĐỦ THÀNH PHẦN` trên code/config cuối.
- [ ] Repo không chứa API key, mật khẩu hoặc `.env`.
- [ ] Mỗi thành viên đã nộp link repo trên LMS.
