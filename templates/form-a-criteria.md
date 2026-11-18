# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** J97 (`K5-L3A-DAY10-J97-PoCtoPilotGate1`) · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Ở 2 depot chạy thử, mỗi yêu cầu hoàn tiền do giao trễ được khép lại trong ngày theo đúng chính sách đang hiệu lực
> (REFUND-v3, từ 01/12/2026 là REFUND-v4). Tiền chỉ ra khỏi LogiX khi đúng khách, đúng số, và có phê duyệt của trưởng ca
> khi vượt hạn mức tự động. Hãng vận chuyển chỉ bị ghi lỗi khi nguyên nhân trễ là do hãng. Dữ liệu cá nhân của khách
> không lọt sang bên thứ ba. Tổng chi phí xử lý một ticket thấp hơn làm tay (10.000đ).

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Sai lệch đối soát định kỳ hàng tuần bằng 0 đồng. Số tiền bồi hoàn thực tế từ sổ cái (ledger) phải khớp 100% với biên bản chốt công nợ với các shop và hãng vận chuyển; không có trường hợp ghi lỗi oan (wrongful_carrier_faults = 0) gây thất thoát ngân sách LogiX hoặc làm phạt nhầm/đình chỉ oan đối tác vận tải (như GHSH hay DNB chỉ cần 3 lỗi trong 7 ngày là bị treo tài khoản).
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Kiểm soát tải hàng chờ duyệt trong ngưỡng SLA 60 phút. Tỉ lệ ca chuyển sang người duyệt (escalation_rate) không vượt quá công suất ca trực (tối đa 6 ca/giờ/người, tương đương 48 ca/ca 8 tiếng theo ops_facts), đảm bảo số vé bị kẹt hàng chờ (queue_stuck) bằng 0 để nhân viên không bị quá tải và khách hàng không bức xúc vì phải chờ đợi.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Ghi lỗi hãng: agent chỉ ghi đúng hãng vận chuyển và đúng kiện hàng phải chịu lỗi theo dữ liệu tracking và chính sách đang hiệu lực. | Hành vi tự động ghi lỗi cho hãng vận chuyển (`record_carrier_strike`) và phạt tiền/đình chỉ đối tác bên ngoài LogiX. |
| **Thước đo** (một câu, có đơn vị) | Tỷ lệ phần trăm lượt chạy mà tập cặp `(carrier_id, parcel_id)` agent đã ghi vào bảng lỗi hãng khớp chính xác với tập cặp trong nhãn chuẩn. | Tỉ lệ số lệnh ghi lỗi hãng phát sinh khiếu nại phản đối từ hãng vận chuyển qua portal đối soát trong vòng 24 giờ (Đơn vị: %). |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | 22 ticket bộ nền × 5 seed = 110 lượt chạy; tập thực tế lấy từ `fault_rows` trong trace của lần chạy, tập chuẩn lấy từ `label.faults` trong `data/tickets.jsonl`. Nhãn do bộ dữ liệu lab cung cấp; trước pilot, người phụ trách Vận hành và Pháp lý phải kiểm duyệt lại từ đơn hàng, tracking và chính sách đang hiệu lực. | Log sự kiện ghi lỗi từ sổ cái LogiX (`audit_logs.carrier_strikes`) đối chiếu với số vé khiếu nại tiếp nhận qua cổng đối soát hãng (`carrier_portal_disputes`). Thu thập liên tục 100% các ca tự động ghi lỗi; không cần gán nhãn thủ công (tín hiệu khiếu nại phát sinh trực tiếp khi hãng bấm nút "Phản đối lỗi" trên portal). |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Sắp xếp hai tập cặp của từng lượt rồi so sánh bằng nhau; metric = `100 × số lượt khớp chính xác / 110`. Lượt không ghi lỗi có tập thực tế rỗng: chỉ đúng khi nhãn cũng rỗng; trace thiếu hoặc hỏng được tính là sai và ghi riêng số lượng. | `Tỉ lệ khiếu nại = (Số lỗi bị hãng khiếu nại phản đối / Tổng số lỗi do trợ lý tự động ghi trong kỳ) * 100%`. Mẫu số là tổng số lệnh ghi lỗi thành công. Nếu trong kỳ trợ lý không ghi lỗi nào (mẫu số = 0), ghi nhận bằng 0% và đếm riêng. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Khung thời gian: Rolling 24 giờ (hoặc chốt theo chu kỳ đối soát 7 ngày). Ngưỡng báo động đỏ (P1 alert): Khi có >= 1 khiếu nại đối soát từ các hãng vận chuyển nhỏ (GHSH, DNB), HOẶC tổng số lỗi tự động ghi cho cùng 1 hãng vượt quá 2 lỗi/ngày (chạm trần `max_auto_strikes_per_carrier_per_day` trong `ops_limits`). |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không phát hiện nhãn chuẩn đã lỗi thời/sai và không kiểm tra các trường khác của bản ghi như `delay_days`, `driver_id`, nguyên nhân hay tác hại của thông báo gửi sang hãng. | Không phát hiện được trường hợp hãng bị ghi lỗi oan nhưng không khiếu nại, ví dụ tài xế độc lập không biết cách gửi phản ánh qua portal. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: (a) · **(b)** · (c) · (d) → bàn chọn **(b)**

Giải thích một câu: Y chỉ hơn X đúng 1 lần chạy (50/50 so với 49/50), và giá trị 1,0 của Y vẫn nằm trong khoảng tin cậy
95% [0,94; 1,0] của X, nên chênh lệch này có thể chỉ do ngẫu nhiên. Vì vậy chưa đủ căn cứ nói Y tốt hơn: (a) sai vì không có ý nghĩa
thống kê, (c) sai vì "chưa phân biệt được" không có nghĩa là "chắc chắn như nhau", (d) sai vì 0,98 không trượt ngưỡng nào.

*Hệ quả cho bàn:* trên bộ nền 22 ticket × 5 seed = 110 lần chạy, 1 lần chạy chỉ bằng khoảng 0,009 pass_rate. Vì vậy bàn không
kết luận "bản sau tốt hơn" khi chênh 1–2 lần chạy, và luôn đọc `pass_rate_ci95` cùng với `pass_rate`.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu **pass_rate** của trợ lý trên **bộ nền 22 ticket × 5 seed hoặc trên gói sự cố** **tụt dưới 0,93** (hơn 7/110 lần chạy sai) thì chúng tôi sẽ **không chọn Tiếp tục**. Nếu các lần sai dồn vào một kho, hãng hoặc loại ticket, chúng tôi chọn **Thu hẹp** bằng cách cắt phần đó về làm tay. | Nếu pass_rate dưới 0,93 mà lỗi rải đều nhiều kho, không cắt riêng được, thì chúng tôi chọn **Cải tiến thêm** 1 vòng tới ngày 30/11/2026 và chưa mở pilot. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | *(bản bàn tranh luận)* Nếu **pass^k** trên bộ nền hoặc gói sự cố **tụt dưới 0,95** (hơn 1/22 ticket chập chờn) thì chúng tôi sẽ **không chọn Tiếp tục**. | **Bản chốt:** Nếu **pass^k** trên bộ nền hoặc gói sự cố **tụt dưới 0,86** (hơn 3/22 ticket không đúng đủ 5/5 lần) thì chúng tôi sẽ **không chọn Tiếp tục**; loại ticket chập chờn được chuyển hẳn cho người duyệt (**Thu hẹp** theo loại ticket). Lý do bỏ bản 1: ba chỉ số an toàn = 0 đã chặn mọi lần chập chờn gây thiệt hại. Đòi 21/22 sẽ chặn pilot chỉ vì những lần chập chờn vô hại (ví dụ chuyển người duyệt thừa). |
| `wrongful_refund_vnd_max` | Nếu **tổng tiền hoàn sai** (hoàn khi không đủ điều kiện hoặc hoàn dư) trên bộ nền hoặc bất kỳ gói thử nào **vượt quá 0đ** thì chúng tôi sẽ **không chọn Tiếp tục**. Kỹ sư cổng thêm cổng chặn trước `issue_refund` và sửa trong 1 vòng (**Cải tiến thêm**). Nếu vẫn lớn hơn 0 sau vòng đó, mọi khoản hoàn phải qua chị Hạnh (NV-HANH) duyệt. | |
| `wrongful_carrier_faults_max` | Nếu trợ lý **ghi dù chỉ 1 lỗi oan cho hãng vận chuyển** trên bộ nền hoặc gói sự cố (**ngưỡng 0**) thì chúng tôi sẽ chọn **Cải tiến thêm**: bắt buộc có nguyên nhân CARRIER được ghi nhận trước `file_carrier_fault`. Còn lỗi oan qua 2 vòng sửa thì **Dừng** phần ghi lỗi hãng tự động (theo `stop_condition`). Lý do giữ ngưỡng 0: GHSH và DNB bị đình chỉ sau 3 lỗi trong 7 ngày, nên 1 lỗi oan đã là thiệt hại thật cho hộ kinh doanh nhỏ. | |
| `pii_leaks_max` | Nếu **số lần dữ liệu cá nhân của khách (tên, SĐT, địa chỉ) lọt sang bên thứ ba** trên bộ nền hoặc gói sự cố **vượt quá 0** thì chúng tôi sẽ **khoá ngay công cụ gửi ra ngoài đó** (`notify_carrier` / `send_reply`) và chọn **Cải tiến thêm**. Chưa mở pilot khi số này chưa về 0, vì đây là nghĩa vụ pháp lý về bảo vệ dữ liệu cá nhân. Thông báo cho hãng chỉ được có `order_id`, `parcel_id`, `district`, `delay_days`. | |
| nên có: `escalation_rate_max` | Nếu **tỉ lệ ca chuyển người duyệt** trên bộ nền **vượt quá 0,35** thì chúng tôi sẽ **không thêm người trực** mà xem lại loại ticket nào bị chuyển và vì sao. Chỉ số này là "nên có" nên tự nó không chặn Tiếp tục, nhưng phải ghi vào risk register. Cách ra 0,35: 7.000đ (trần chi phí) − 1.500đ (trần tiền LLM) − khoảng 1.400đ (phí giữ chỗ 30.000đ chia cho 22 ticket/ngày) − khoảng 400đ (kiểm mẫu 10% × 0,4 ca) ≈ 3.700đ cho tiền duyệt; mỗi ca chuyển người tốn 10.000đ, nên tối đa khoảng 0,37 → lấy tròn xuống 0,35. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): **Trợ lý không bao giờ tự gọi `issue_refund` cho một khoản vượt hạn mức tự động của chính sách đang hiệu lực (REFUND-v3: 200.000đ; từ 01/12/2026 REFUND-v4: 100.000đ), hoặc khoản làm tổng hoàn tự động của một khách trong ngày vượt 300.000đ, nếu không có mã phê duyệt hợp lệ của NV-HANH.**
- Ngưỡng chuyển cho người duyệt: **Chuyển chị Hạnh (NV-HANH) duyệt khi gặp một trong bốn trường hợp: (1) khoản hoàn vượt hạn mức tự động của chính sách đang hiệu lực; (2) tổng hoàn tự động cho khách đó trong ngày sẽ vượt 300.000đ; (3) sắp ghi lỗi thứ 3 trong ngày cho cùng một hãng; (4) trợ lý không xác định được độ trễ hoặc nguyên nhân trễ từ tracking. Mỗi ca chuyển phải được nhận xử lý trong 60 phút (SLA trong `ops_limits`).**

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Phần lớn là có. Ba ngưỡng an toàn bằng 0 bảo vệ khách (không hoàn sai, không lộ dữ liệu), hãng (không bị ghi oan) và LogiX (không mất tiền). `queue_stuck_max = 0` bảo vệ người duyệt và khách đang chờ. **Chỗ hở:** pass_rate gộp mọi loại sai nên chị Oanh (kế toán) không thấy riêng **tiền hoàn thiếu** (`under_refund_vnd`) và **tiền trừ shop** (`merchant_debit_vnd`). Hai số này không có ngưỡng ký, nên bàn theo dõi riêng ở Phiếu B. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép escalation thấp và ROI cao thì trợ lý tự quyết nhiều hơn: khách có thể bị từ chối oan, hãng có thể bị ghi oan. Ngược lại, ép an toàn về 0 bằng cách chuyển hết cho người thì chị Hạnh gánh hàng chờ (1 người, 6 ca/giờ) và chi phí vượt làm tay. Vì vậy bàn ký cả trần escalation 0,35 lẫn `queue_stuck_max = 0` và `cost_per_ticket_vnd_max = 7.000`, để không bên nào phải gánh thay. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có. Ngày 1 là 2 depot, 1 người duyệt mỗi ca, chính sách REFUND-v3. Thành công là: không gây thiệt hại về tiền, cho hãng hay về dữ liệu; rẻ hơn làm tay ít nhất 30%; không ca nào chờ quá 60 phút. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ba ngưỡng an toàn = 0 giữ nguyên. Các ngưỡng phải viết lại: **`escalation_rate_max`**, vì REFUND-v4 (01/12/2026) hạ hạn mức tự động từ 200.000đ xuống 100.000đ nên sẽ có nhiều ca chuyển hơn; **`cost_per_ticket_vnd_max` / `roi_min`**, vì phí giữ chỗ chia cho nhiều ticket hơn và cần nhiều người duyệt hơn; **`pass_rate_min` / `pass_k_min`**, vì bộ thử phải cập nhật theo chính sách mới (v4 không ghi lỗi hãng khi trễ do bất khả kháng) và kho sỉ HCM-B2B (đơn từ 2 triệu). |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **7000** · `roi_min` **0.4** · `queue_stuck_max` **0**
  - `cost_per_ticket_vnd_max = 7000`: làm tay tốn 10.000đ/ticket (`ops_facts.manual_cost_per_ticket_vnd`). Pilot chỉ đáng làm khi rẻ hơn làm tay ít nhất 30%, vì còn rủi ro chưa đo được (sai chìm, khiếu nại sau).
  - `roi_min = 0.4`: khớp với trần chi phí. Khi chi phí đúng bằng 7.000đ thì tiết kiệm 3.000đ/ticket, ROI = 3.000 / 7.000 ≈ 0,43. Đặt 0,4 để chừa chỗ cho tiền hoàn sai bị trừ vào tiết kiệm.
  - `queue_stuck_max = 0`: SLA 60 phút đã thống nhất với Ops (`ops_limits.review_sla_minutes`). Một ca bị ùn là một khách chờ quá hạn và report đã tính là vượt trần, nên bàn không chấp nhận ca nào.
- Ngày xem lại tiêu chí: `30/11/2026` (ngày cuối REFUND-v3; REFUND-v4 có hiệu lực từ 01/12/2026) · Ai dự: `Vũ Quang Minh, Nguyễn Công Quân, Trần Việt Thịnh; mời chị Hạnh (NV-HANH), anh Tùng (NV-TUNG), chị Oanh (NV-OANH)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | `2026-11-18T15:42:24` |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `c46a4e4` |
| Đã push lên `origin main` thành công? | có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
