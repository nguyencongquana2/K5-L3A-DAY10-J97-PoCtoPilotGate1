# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** J97 · **Thẻ đã bốc:** S2 *(đối soát: shop bị trừ tiền lạ)*

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | | Sx · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | | | | | |
| 2 | | Sx · after | | | | | | |
| 3 | | Sx · after | | | | | | |
| 4 | | base · after | (kiểm không regression) | | | | | |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `__________` · base: `__________` · prepared: `__________`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): …
- Khối kinh doanh và vận hành còn dòng nào vượt trần: …

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? …
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? …
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| | | |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `____` · đo bằng gì `____` · bao nhiêu ở mốc base `____`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | | | |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | | | |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | | | |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | | | |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | | | |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | | | |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | | | |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | | | |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | Có | Bảng đối soát shop bị trừ tiền lạ: Gốm Bát Tràng Cô Lụa bị trừ 475.000đ và 3.230.000đ do đơn giao trễ; Cô Lụa gọi khiếu nại 2 lần, đe dọa trực tiếp quan hệ kinh doanh và đối tác đối soát của LogiX. |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | Có | Khoản 3.230.000đ không có mã phê duyệt nào nhưng AI vẫn tự ý ghi sổ cái trừ nợ shop; đối tác chưa tin tưởng trợ lý tự động và đòi hỏi chứng từ do con người ký duyệt. |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | Có | Model nhầm lẫn giữa lỗi giao hàng trễ (thuộc trách nhiệm LogiX) với lỗi do người bán (`MERCHANT`), dẫn đến gán sai người trả tiền `payer`; cần người duyệt thủ công với mọi khoản trừ tiền shop. |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | Có | 1 khách hàng nhận liên tiếp 5 khoản hoàn tự động trong cùng 1 ngày (ticket `S2-40` đến `S2-44`) vượt mức Ops từng thống nhất; hệ thống thiếu cơ chế kiểm soát tần suất/hạn mức ngày của từng khách. |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | Có | Các khoản hoàn vượt trần tự động (> 200.000đ theo REFUND-v3) phải có `approval_id` còn hiệu lực của chị Hạnh (`NV-HANH`); trợ lý không được tự ý hoàn tiền khi thiếu mã phê duyệt hợp lệ. |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| Trưởng ca CSKH (Trần Thị Hạnh) | `issue_refund` dưới hạn mức tự động | Thấp (chỉ cần hậu kiểm mẫu 10%, cho phép trợ lý tự động hoàn nếu đủ căn cứ tracking DB và người trả là LOGIX) | Cao (hệ thống tự động thực hiện hoàn tiền) | Không |
| Trưởng ca CSKH (Trần Thị Hạnh) | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | Cao (bắt buộc có mã phê duyệt `approval_id` hợp lệ còn hạn, đúng thẩm quyền và số tiền) | Thấp (hệ thống tự động cho qua hoặc bỏ qua kiểm tra approval, hoàn 3.230.000đ mà không có mã duyệt) | Lệch → Trả quyền cho chị Hạnh: thiếu approval_id hợp lệ thì chặn và chuyển người duyệt. |
| Kế toán đối soát (Phạm Kiều Oanh) | `issue_refund` mà người trả là shop | Cao (tuyệt đối không cho AI tự trừ nợ shop khi giao trễ; phải có biên bản đối soát và xác nhận lỗi shop) | Thấp (AI tự động ghi sổ cái nợ shop `payer: MERCHANT`, tự trừ 475.000đ của shop Cô Lụa) | Lệch nghiêm trọng → Trả quyền cho chị Oanh: cấm AI tự động trừ tiền shop, `payer` tự động chỉ được là `LOGIX`. |
| Giám sát vận hành (Lê Thanh Tùng) | nhiều khoản hoàn tự động cho một khách trong ngày | Cao (cần trần tích lũy ngày/khách hàng để phát hiện và ngăn chặn hành vi lạm dụng trục lợi) | Thấp (hệ thống xử lý từng ticket rời rạc, để 1 khách nhận 5 khoản hoàn trong ngày) | Lệch → Trả quyền cho Ops/CSKH: thiết lập trần hoàn khách/ngày, vượt trần chuyển người thẩm định. |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `issue_refund` (lệnh ghi sổ cái hoàn tiền / trừ tiền)

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `payer` | WRONG | Ticket `S2-01`, `S2-04`: Đơn hàng trễ 4 ngày do vận chuyển (trách nhiệm của LogiX), nhưng model gán `payer: MERCHANT`, trừ tiền của shop Gốm Bát Tràng Cô Lụa 475.000đ. | Shop Cô Lụa bị mất tiền oan, khiếu nại đối soát 2 lần với chị Oanh; LogiX có nguy cơ mất khách hàng doanh nghiệp và bị phạt vi phạm hợp đồng hợp tác. | Chưa có gì ngăn ở mốc base; model tự quyết định `payer` từ suy luận prompt. | Cổng kỹ thuật trong `write_gate(issue_refund)` cưỡng chế `payer == "LOGIX"` đối với các đơn giao trễ; cấm tự động trừ tiền shop (`legal.forbid_auto_merchant_debit = true`). (Tầng: Chặn). |
| `approval_id`, `amount_vnd` | INVALID | Ticket `S2-20`: Khoản hoàn trị giá 3.230.000đ (vượt hạn mức tự động 200.000đ), nhưng tham số `approval_id` bị để trống hoặc dùng mã phê duyệt không tồn tại / hết hạn. | Thất thoát ngân sách tài chính nghiêm trọng cho LogiX, phá vỡ hạn mức chi tiêu đã ký với Finance, chị Hạnh CSKH bị liên đới trách nhiệm kiểm toán. | Host chỉ kiểm tra kiểu dữ liệu chuỗi cơ bản, không đối soát tính hợp lệ của mã phê duyệt trong bảng `approvals`. | Cổng `write_gate(issue_refund)` kiểm tra bắt buộc: nếu `amount_vnd > auto_limit_vnd`, phải có `approval_id` hợp lệ trong `data/world.json`, còn hạn (`expires_at >= as_of`), đúng số tiền (`amount_vnd <= max_vnd`); không đạt thì chuyển người. (Tầng: Chặn / Trao quyền cho người). |
| `customer_id`, tần suất lệnh trong ngày | PERTURBED | Loạt ticket `S2-40` đến `S2-44`: Cùng một khách hàng gửi 5 yêu cầu hoàn tiền riêng lẻ trong cùng một ngày; mỗi yêu cầu dưới 200.000đ nhưng tổng tiền vượt ngân sách và hạn mức Ops. | Bị khách hàng lạm dụng/trục lợi chính sách hoàn tiền tự động (sybil attack), ngân sách hoàn tiền trong ngày bị cạn kiệt nhanh chóng. | Hệ thống hiện chỉ xử lý stateless từng ticket độc lập, không kiểm tra lịch sử sổ cái tích lũy trong ngày của khách hàng. | Cổng `pre_guard` / `write_gate` kiểm tra `ledger`: nếu số lần hoàn tiền của khách trong ngày > 1 hoặc tổng tiền nhận trong ngày vượt trần `customer_daily_refund_cap_vnd = 200000`, lập tức chuyển sang hàng chờ duyệt tay. (Tầng: Giới hạn thiệt hại / Chuyển người). |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: …

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): …

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): …

Vì sao có thể sai: …

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `__________`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: ______________________________ (cho ai: __________, đo bằng: __________)
 └─ HOẶC
 ├─ [1] ______________________________ tầng: đầu vào / data / hành động / quyền hạn / vận hành / kinh doanh
 │ └─ vì: ________________________ bằng chứng: ticket ______@seed ____
 ├─ [2] ______________________________ tầng: ______
 │ └─ vì: ________________________ bằng chứng: ticket ______@seed ____
 └─ [3] ______________________________ tầng: ______
 └─ vì: ________________________ bằng chứng: ______
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | | |
| [2] | | |
| [3] | | |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | | | | | |
| [2] | | | | | |
| [3] | | | | | |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | |
| **Bước / hành vi được đo** | |
| **Thước đo** (một câu, có đơn vị) | |
| **Dữ liệu** (trường nào của trial, không có nhãn) | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | |
| **Khung thời gian / ngưỡng báo động** | |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `__________`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] ______________________________
 └─ HOẶC
 ├─ [1] ______________ VÀ [gate ______ hỏng]
 ├─ [2] ______________ VÀ [gate ______ hỏng]
 └─ [3] ______________ (còn hở?)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | | | | |
| [2] | | | | |
| [3] | | | | |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| Trợ lý tự ý trừ nợ shop đối tác (`merchant_debit_vnd > 0`) khi đơn giao trễ, hoặc bị cùng một khách hàng lợi dụng hoàn tiền nhiều lần trong ngày vượt hạn mức. | Vừa | Cao | Trần Việt Thịnh (Vận hành và pháp lý) | `merchant_debit_vnd > 0` trong report hoặc monitor `merchant_debit_rate > 0`; số ca hoàn/khách/ngày > 1. | Cấm tuyệt đối AI tự trừ nợ shop (`payer == LOGIX`); thêm trần hoàn khách/ngày; ca nợ shop chuyển chị Oanh đối soát thủ công; xin lỗi và hoàn trả tiền cho shop trong 4 giờ. | Bắt buộc chọn "Dừng" hoặc "Thu hẹp" nếu `merchant_debit_vnd > 0` trên mốc after; chỉ được "Tiếp tục" khi chỉ số này triệt tiêu về 0. | MANAGE & GOVERN |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| 4 (Quyền hạn) | Xong | Cổng `write_gate` chặn tự động trừ nợ shop (`payer == LOGIX`), kiểm tra `approval_id` còn hiệu lực cho mọi ca hoàn > hạn mức tự động; Phiếu C mục C3.1 và C7 | Lê Thanh Tùng (Giám sát vận hành) |
| 6 (Chi phí) | Xong | Thiết lập trần tích lũy hoàn tiền khách/ngày (`customer_daily_refund_cap_vnd`), chặn đứng trục lợi lặp lại ở loạt ticket `S2-40`..`S2-44`; `config/operating_gates.json` | Vũ Quang Minh (Sản phẩm và kinh doanh) |
| 8 (Con người, pháp lý) | Xong | Quy trình đối soát minh bạch, bảo vệ quyền lợi shop đối tác; cam kết `merchant_debit_vnd = 0`; Runbook 4 xử lý sự cố shop Cô Lụa; Phiếu C mục C3.1, C10, C11 | Trần Việt Thịnh (Vận hành và pháp lý) |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Tín hiệu tổng tiền trừ nợ shop (`merchant_debit_vnd`) và số ca hoàn/khách/ngày (`refunds_per_customer`). Ở Runbook 2 vòng 1 chưa có tín hiệu này mà chỉ mới theo dõi tiền hoàn sai cho khách (`wrongful_refund_vnd`) và lỗi hãng oan (`wrongful_carrier_faults`). |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Thêm ngưỡng an toàn bắt buộc: `merchant_debit_vnd_max = 0đ` (bất kỳ đồng nào trừ shop đều kích hoạt dừng khẩn cấp); thêm trần hoàn khách/ngày: `max_refunds_per_customer_day = 1` ca tự động (tổng tiền ≤ 200.000đ/ngày/khách). |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Chị Phạm Kiều Oanh (`NV-OANH`, kế toán đối soát) giữ quyền thẩm định và phê duyệt trực tiếp mọi trường hợp đề xuất trừ tiền shop; chị Trần Thị Hạnh (`NV-HANH`) đứng tên phê duyệt mọi khoản hoàn > 200.000đ; khi có khiếu nại shop, chị Oanh trực tiếp liên hệ xử lý. |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Phạm vi: Cấm 100% việc AI tự động trừ tiền shop; mọi khoản hoàn lớn bắt buộc kèm mã phê duyệt; tăng tỉ lệ kiểm mẫu từ 10% lên 30% đối với các đơn có giá trị hàng cao (> 1.000.000đ); bắt buộc đính kèm ghi chú giải thích căn cứ hoàn tiền. |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | Phạm Kiều Oanh (kế toán đối soát) gọi điện thoại trực tiếp cho đại diện shop Gốm Bát Tràng Cô Lụa trong vòng 2 giờ kể từ khi phát hiện; gửi thư xin lỗi chính thức giải thích do lỗi hệ thống thử nghiệm; cam kết hoàn trả lại 475.000đ và hủy khoản trừ sai 3.230.000đ trong kỳ chốt 16h cùng ngày. |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Không có dữ liệu cá nhân (PII) nào bị rò rỉ sang bên thứ ba trong sự cố S2 (đây là sự cố logic phân bổ tài chính giữa LogiX và shop); đã kiểm tra log payload sổ cái và xác nhận an toàn; báo cáo xác nhận cho PIC Pháp lý (Trần Việt Thịnh). |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Sự cố lộ ra qua phản hồi của con người (shop Cô Lụa gọi điện khiếu nại 2 lần cho chị Oanh) và kế toán đọc bảng đối soát định kỳ, chứ hệ thống máy đo mốc base không hề tự động báo động đỏ. Nguồn bàn còn thiếu là telemetry giám sát trường `payer` theo thời gian thực và cảnh báo tức thì khi phát sinh `payer: MERCHANT`. |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp 3 lần trong một giờ (đạt 15–18 ca/giờ) thì: Kích hoạt ngay nhân viên trực dự phòng ca 2 theo Runbook B7.6; nếu hàng chờ vượt quá 4 ca hoặc thời gian chờ vượt 30 phút thì tạm thời hạ hạn mức hoàn tự động xuống 50.000đ để xử lý nhanh ca nhỏ, chuyển toàn bộ ca lớn cho người duyệt nhằm giữ vững SLA 60 phút.
2. Nếu nhà cung cấp LLM lỗi quá 10 phút (mã lỗi 429 hoặc 5xx liên tiếp) thì: Tự động chuyển toàn bộ ticket sang hàng chờ thủ công của CSKH; gửi thông báo báo động lên kênh Slack `#ops-refund-alerts`; anh Lê Thanh Tùng tắt công tắc ghi sổ trong `config/switches.json` để tránh nghẽn luồng.
3. Nếu người duyệt báo không tin một quyết định của trợ lý (nghi ngờ số tiền hoàn hoặc bên chịu phí) thì: Tạm dừng xử lý tự động cho nhóm ticket liên quan; chuyển ca về chị Hạnh trưởng ca thẩm tra lại; ghi nhận mã ticket vào log soát lỗi để Kỹ sư cổng đối soát với tracking DB; nếu phát hiện lỗi logic thì ngắt công tắc ghi sổ tương ứng trong vòng 5 phút.


---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | phải giống v1 |
| Hash chốt cổng vòng 1 | phải giống v1 |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: ________ · prepared: ________ · after: ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | |
| Bằng chứng 2 | |
| Bằng chứng 3 | |
| Khớp dòng nào trong `decision_rule` đã ký? | |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: …
- Report tự kiểm tra: mã lần chạy `__________` · ô nào còn đỏ (nguyên nhân × tầng): …
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: …
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: …
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: …

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: …
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: …
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: …
