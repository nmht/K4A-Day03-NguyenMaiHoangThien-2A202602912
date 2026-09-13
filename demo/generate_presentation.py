"""
🎨 PYTHON-PPTX PRESENTATION GENERATOR
Tạo slide thuyết trình chuyên nghiệp file demo/Supply_Chain_ReAct_Agent_Presentation.pptx
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank slide layout

    # Colors
    BG_DARK = RGBColor(11, 15, 25)
    CARD_BG = RGBColor(17, 24, 39)
    TEXT_LIGHT = RGBColor(243, 244, 246)
    TEXT_MUTED = RGBColor(156, 163, 175)
    PURPLE_ACCENT = RGBColor(168, 85, 247)
    BLUE_ACCENT = RGBColor(99, 102, 241)
    EMERALD_ACCENT = RGBColor(16, 185, 129)
    AMBER_ACCENT = RGBColor(245, 158, 11)

    def set_slide_background(slide, color=BG_DARK):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = color

    def add_header(slide, title_text, category_text="VINUNI AI COURSE - DAY 03 LAB"):
        # Category Tag
        tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.4))
        tf = tx_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = category_text.upper()
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = PURPLE_ACCENT

        # Title
        tx_box2 = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.5), Inches(0.8))
        tf2 = tx_box2.text_frame
        tf2.word_wrap = True
        p2 = tf2.paragraphs[0]
        p2.text = title_text
        p2.font.size = Pt(24)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_LIGHT

    # ==========================================
    # SLIDE 1: Title Slide
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)

    # Title Container Box
    shape = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.5), Inches(10.33), Inches(4.5))
    shape.fill.solid()
    shape.fill.fore_color.rgb = CARD_BG
    shape.line.color.rgb = BLUE_ACCENT
    shape.line.width = Pt(2)

    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.6)
    tf.margin_top = Inches(0.6)

    p0 = tf.paragraphs[0]
    p0.text = "VINUNI AI COURSE - DAY 03 LAB REPORT"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = EMERALD_ACCENT

    p1 = tf.add_paragraph()
    p1.text = "Trợ Lý Thông Minh Chuỗi Cung Ứng & Kho Vận"
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_LIGHT

    p2 = tf.add_paragraph()
    p2.text = "Kiến trúc ReAct Pattern (Reasoning + Acting) Tích hợp MCP Server Protocol"
    p2.font.size = Pt(18)
    p2.font.color.rgb = PURPLE_ACCENT

    p3 = tf.add_paragraph()
    p3.text = "\n• Mô hình LLM: Gemini 1.5 / 3.1 Pro API\n• Nghiệp vụ: Kho vận đơn hàng (WMS) & Học vụ Đại học VinUni\n• Kết quả: 5/5 Test Cases hoàn thành chính xác 100%"
    p3.font.size = Pt(14)
    p3.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 2: Đề tài & Lý do lựa chọn
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, "1. Đề Tài Lựa Chọn & Lý Do Chọn Đề Tài")

    # Card 1: Context
    c1 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = PURPLE_ACCENT
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = Inches(0.4)
    tf1.margin_top = Inches(0.4)

    p = tf1.paragraphs[0]
    p.text = "🎯 Đề Tài Nghiên Cứu"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = PURPLE_ACCENT

    p = tf1.add_paragraph()
    p.text = "\nXây dựng Agent Kho Vận & Chuỗi Cung Ứng kết hợp Trợ Lý Học Vụ VinUni có khả năng:\n\n1. Tra cứu vị trí lưu kho & trạng thái vận đơn thời gian thực.\n2. Tự động cập nhật trạng thái đơn hàng trên WMS.\n3. Xử lý chính xác dữ liệu, không ảo giác (No Hallucination).\n4. Đặt lịch hẹn cố vấn học tập VinUni."
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_LIGHT

    # Card 2: Why Choose
    c2 = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = BLUE_ACCENT
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = Inches(0.4)
    tf2.margin_top = Inches(0.4)

    p = tf2.paragraphs[0]
    p.text = "💡 Lý Do Lựa Chọn Kho Vận"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    p = tf2.add_paragraph()
    p.text = "\n• Dữ liệu biến động thời gian thực:\nVị trí lưu kho và trạng thái vận chuyển liên tục thay đổi.\n\n• Yêu cầu tương tác 2 chiều (Read/Write):\nKhông chỉ đọc thông tin mà phải tự thực thi lệnh Cập nhật DB qua API.\n\n• Phân tách kiến trúc chuẩn MCP:\nBộ não suy luận (Agent) kết nối an toàn với MCP Server phơi duyệt các Tools nghiệp vụ."
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_LIGHT

    # ==========================================
    # SLIDE 3: 4 Tiêu chí Agent Fit
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, "2. 4 Tiêu Chí Phù Hợp Của ReAct Agent (Agent Fit Matrix)")

    fits = [
        ("1. Dynamic Decision", "Luồng Quyết Định Động", "Tự phân tích Intent để chọn Tool hoặc trả lời trực tiếp mà không cần gò bó `if-else` cố định.", BLUE_ACCENT, Inches(0.8), Inches(1.6)),
        ("2. Multi-Step Reasoning", "Suy Luận Nhiều Bước", "Thực hiện chuỗi Thought-Action nhiều vòng: Tra cứu vị trí ➔ Kiểm tra điều kiện ➔ Cập nhật trạng thái (TC04).", PURPLE_ACCENT, Inches(6.8), Inches(1.6)),
        ("3. MCP Tool Integration", "Tích Hợp Công Cụ MCP", "Gửi request chuẩn JSON-RPC qua MCP Server để truy xuất WMS DB, đảm bảo dữ liệu đúng 100%.", EMERALD_ACCENT, Inches(0.8), Inches(4.4)),
        ("4. Feedback Loop", "Vòng Lặp Phản Hồi Xử Lý Lỗi", "Đọc kết quả Observation khi không tìm thấy đơn (TC05 `NOT_FOUND`) để tự điều chỉnh phản hồi trung thực.", AMBER_ACCENT, Inches(6.8), Inches(4.4))
    ]

    for title, subtitle, desc, color, left, top in fits:
        card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(5.7), Inches(2.5))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = f"{title} - {subtitle}"
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = color

        p = tf.add_paragraph()
        p.text = f"\n{desc}"
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_LIGHT

    # ==========================================
    # SLIDE 4: Kiến Trúc Hệ Thống (Architecture)
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, "3. Sơ Đồ Kiến Trúc Phân Tầng Hệ Thống (Architecture)")

    arch_cards = [
        ("👤 CLIENT / UI LAYER", "Web UI Dashboard (demo/index.html) & Terminal Console", BLUE_ACCENT, Inches(0.8)),
        ("🧠 REACT AGENT CORE", "Vòng lặp ReAct App (src/app.py) & Gemini 1.5/3.1 LLM Provider", PURPLE_ACCENT, Inches(3.8)),
        ("🌐 MCP SERVER LAYER", "Model Context Protocol Server (src/mcp_server.py) - JSON-RPC", EMERALD_ACCENT, Inches(6.8)),
        ("🛠️ TOOLS & DATABASE", "order_tracking, order_status_update, academic_query (src/tools.py)", AMBER_ACCENT, Inches(9.8))
    ]

    for title, desc, color, left in arch_cards:
        card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(2.0), Inches(2.7), Inches(4.5))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color
        card.line.width = Pt(2)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.4)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = color

        p = tf.add_paragraph()
        p.text = f"\n\n{desc}"
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_LIGHT

    # ==========================================
    # SLIDE 5: Luồng Vòng Lặp ReAct (Sequence)
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, "4. Quy Trình Vòng Lặp ReAct Loop (Step-by-Step Flow)")

    steps = [
        ("Step 1: Input", "Người dùng gửi câu hỏi kho vận", BLUE_ACCENT, Inches(0.8)),
        ("Step 2: Thought", "LLM phân tích Intent & chọn Tool", PURPLE_ACCENT, Inches(3.8)),
        ("Step 3: Action", "Gọi MCP Server thực thi Tool", AMBER_ACCENT, Inches(6.8)),
        ("Step 4: Observation", "Nhận JSON kết quả từ WMS DB", EMERALD_ACCENT, Inches(9.8))
    ]

    for title, desc, color, left in steps:
        card = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.8), Inches(2.7), Inches(2.2))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color
        
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.2)
        tf.margin_top = Inches(0.3)
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = color
        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_LIGHT

    # Result Box
    res_box = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.5), Inches(11.7), Inches(2.2))
    res_box.fill.solid()
    res_box.fill.fore_color.rgb = CARD_BG
    res_box.line.color.rgb = EMERALD_ACCENT
    tf = res_box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.4)
    tf.margin_top = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = "🏁 Step 5: Final Answer (Kết luận cuối cùng)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT
    p = tf.add_paragraph()
    p.text = "LLM tổng hợp toàn bộ tri thức từ Observation nhận được để đưa ra câu trả lời tự nhiên, đầy đủ cho người dùng và kết thúc vòng lặp ReAct Loop."
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_LIGHT

    # ==========================================
    # SLIDE 6: Danh sách MCP Tools
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, "5. Danh Sách Các MCP Tools Nghiệp Vụ")

    tools = [
        ("`order_tracking`", "Input: order_id", "Tra cứu vị trí lưu kho hiện tại, trạng thái vận đơn, thông tin người nhận và lịch sử di chuyển đơn hàng.", BLUE_ACCENT, Inches(0.8), Inches(1.6)),
        ("`order_status_update`", "Input: order_id, new_status", "Cập nhật trạng thái đơn hàng mới vào cơ sở dữ liệu WMS và thông báo thay đổi.", EMERALD_ACCENT, Inches(6.8), Inches(1.6)),
        ("`academic_query`", "Input: student_id", "Tra cứu điểm tích lũy GPA, lớp học, email và Cố vấn học tập của sinh viên Đại học VinUni.", PURPLE_ACCENT, Inches(0.8), Inches(4.4)),
        ("`academic_advisor_booking`", "Input: student_id, date, time", "Đặt lịch hẹn gặp Cố vấn học tập trực tiếp cho sinh viên theo khung giờ mong muốn.", AMBER_ACCENT, Inches(6.8), Inches(4.4))
    ]

    for name, inp, desc, color, left, top in tools:
        card = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(5.7), Inches(2.5))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.3)
        p = tf.paragraphs[0]
        p.text = f"{name} ({inp})"
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = color
        p = tf.add_paragraph()
        p.text = f"\n{desc}"
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_LIGHT

    # ==========================================
    # SLIDE 7: Kết quả Test Cases & Waterfall Trace
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, "6. Kết Quả Thử Nghiệm & Trace Log Analysis")

    c1 = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = PURPLE_ACCENT
    tf = c1.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.4)
    tf.margin_top = Inches(0.4)

    p = tf.paragraphs[0]
    p.text = "📊 Tổng Kết Thực Thi 5/5 Test Cases Thành Công:"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT

    p = tf.add_paragraph()
    p.text = "\n• [TC01] Hỏi quy chế chung VinUni ➔ Agent trả lời ngay (0 tool call, ~3.6s)\n• [TC02] Tra cứu sinh viên SV2026001 ➔ Gọi `academic_query` thành công (~2.0s)\n• [TC03] Cập nhật đơn DH2026001 ➔ Gọi `order_status_update` cập nhật WMS (~2.9s)\n• [TC04] Suy luận 2 bước đơn DH2026002 ➔ Gọi `order_tracking` suy luận điều kiện (~2.4s)\n• [TC05] Tra mã không tồn tại DH9999999 ➔ Nhận `NOT_FOUND` và xử lý lịch sự (~1.9s)\n\n👉 Toàn bộ 9 sự kiện Waterfall Trace Log đã được ghi nhận tại file docs/trace_waterfall.json"
    p.font.size = Pt(14)
    p.font.color.rgb = TEXT_LIGHT

    # ==========================================
    # SLIDE 8: Hướng dẫn Demo Web UI
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(slide8, "7. Khởi Chạy Web UI Interactive Demo")

    card = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.8), Inches(10.33), Inches(4.8))
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = EMERALD_ACCENT
    card.line.width = Pt(2)

    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.6)
    tf.margin_top = Inches(0.6)

    p = tf.paragraphs[0]
    p.text = "🖥️ HƯỚNG DẪN KHỞI CHẠY WEB DEMO DASHBOARD"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT

    p = tf.add_paragraph()
    p.text = "\n1. Mở Terminal tại thư mục dự án và chạy lệnh:"
    p.font.size = Pt(15)
    p.font.color.rgb = TEXT_LIGHT

    p = tf.add_paragraph()
    p.text = "   python demo/server.py"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = AMBER_ACCENT

    p = tf.add_paragraph()
    p.text = "\n2. Mở trình duyệt truy cập: http://localhost:8000"
    p.font.size = Pt(15)
    p.font.color.rgb = TEXT_LIGHT

    p = tf.add_paragraph()
    p.text = "\n✨ Tính năng Web UI:\n  • Tương tác gửi câu hỏi trực tiếp & xem ReAct Trace thời gian thực.\n  • Biểu đồ luồng Mermaid tương tác trực quan.\n  • Bảng tổng hợp Waterfall Trace Timeline & Latency Analysis."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED

    # Save presentation
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Supply_Chain_ReAct_Agent_Presentation.pptx")
    prs.save(output_path)
    print(f"[OK] Da tao thanh cong file PowerPoint thuyet trinh tai: {output_path}")

if __name__ == "__main__":
    create_deck()
