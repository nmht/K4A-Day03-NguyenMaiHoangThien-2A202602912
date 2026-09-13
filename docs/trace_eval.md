# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Mai Hoàng Thiện  
> **Mã Sinh Viên / Mã Học viên:** 2A202602912  
> **Chủ đề Lựa chọn:** *Trợ lý Đơn hàng & Kho vận (Supply Chain Agent):* Tra cứu mã vận đơn, vị trí lưu kho và cập nhật trạng thái đơn hàng. 

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Bài toán có yêu cầu chia nhỏ nhiều bước suy luận nối tiếp nhau không? |
| **2. Tool Interaction** | 5 / 5 | Hệ thống có cần kết nối với MCP Server / Cơ sở dữ liệu bên ngoài không? |
| **3. Dynamic Decision** | 4 / 5 | Bước tiếp theo có phụ thuộc vào kết quả quan sát bước trước không? |
| **4. Long Horizon Goal** | 4 / 5 | Hệ thống có phải giữ mục tiêu xuyên suốt qua nhiều lượt xử lý không? |
| **TỔNG ĐIỂM AGENTIC FIT** | **17 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Cập nhật trạng thái của mã vận đơn DH2026001 thành 'Đã giao thành công'.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "order_status_update",
    "arguments": {
      "new_status": "Đã giao thành công",
      "order_id": "DH2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "order_id": "DH2026001",
      "old_status": "Đang chờ xuất kho",
      "new_status": "Đã giao thành công",
      "message": "Cập nhật trạng thái đơn hàng DH2026001 thành công: 'Đang chờ xuất kho' → 'Đã giao thành công'."
    },
    "latency_ms": 974.6
  },
  {
    "step": 2,
    "query": "Cập nhật trạng thái của mã vận đơn DH2026001 thành 'Đã giao thành công'.",
    "action_type": "FINAL_ANSWER",
    "thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "**Thought:** Người dùng muốn cập nhật trạng thái đơn hàng và kết quả thực hiện từ công cụ `order_status_update` đã được trả về trong Observation. Tôi sẽ tổng hợp lại thông tin đó để thông báo cho người dùng một cách rõ ràng và chính xác.\n\n**Trả lời:**\nTrạng thái của đơn hàng **DH2026001** đã được cập nhật thành công!\n- **Trạng thái cũ:** Đang chờ xuất kho\n- **Trạng thái mới:** Đã giao thành công",
    "latency_ms": 1927.18
  },
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
