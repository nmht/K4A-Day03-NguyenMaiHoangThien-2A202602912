"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA
# ==============================================================================

TOOLS_SCHEMA = [
    # --- NHÓM TOOL HỌC VỤ (ACADEMIC) ---
    {
        "name": "academic_query",
        "description": "Tra cứu hồ sơ và thông tin học vụ của sinh viên VinUni bằng mã sinh viên.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần tra cứu (ví dụ: 'SV2026001')"
                }
            },
            "required": ["student_id"]
        }
    },
    {
        "name": "schedule_appointment",
        "description": "Đặt lịch hẹn tư vấn học vụ với Cố vấn học tập VinUni.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần đặt lịch (ví dụ: 'SV2026001')"
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian hẹn (ví dụ: '14:00 15/09/2026')"
                },
                "advisor_name": {
                    "type": "string",
                    "description": "Tên cố vấn học tập"
                }
            },
            "required": ["student_id", "datetime_str", "advisor_name"]
        }
    },

    # --- NHÓM TOOL KHO VẬN (SUPPLY CHAIN) ---
    {
        "name": "order_tracking",
        "description": "Tra cứu trạng thái, vị trí lưu kho và lịch sử vận chuyển của một đơn hàng theo mã vận đơn.",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "Mã vận đơn cần tra cứu (ví dụ: 'DH2026001')"
                }
            },
            "required": ["order_id"]
        }
    },
    {
        "name": "order_status_update",
        "description": "Cập nhật trạng thái xử lý của một đơn hàng theo mã vận đơn.",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "Mã vận đơn cần cập nhật (ví dụ: 'DH2026001')"
                },
                "new_status": {
                    "type": "string",
                    "description": "Trạng thái mới của đơn hàng (ví dụ: 'Đã giao thành công', 'Đang điều phối xuất kho')"
                }
            },
            "required": ["order_id", "new_status"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

# --- Database học vụ ---
MOCK_STUDENT_DATABASE = {
    "SV2026001": {
        "full_name": "Nguyễn Văn An",
        "class": "AI-K4",
        "gpa": 3.85,
        "email": "an.nv@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "PGS.TS Nguyễn Văn A"
    },
    "SV2026002": {
        "full_name": "Trần Thị Bình",
        "class": "AI-K4",
        "gpa": 3.60,
        "email": "binh.tt@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "TS. Lê Thị B"
    }
}

# Alias để tương thích với code cũ
MOCK_DATABASE = MOCK_STUDENT_DATABASE

# --- Database kho vận ---
MOCK_ORDER_DATABASE = {
    "DH2026001": {
        "order_id": "DH2026001",
        "customer": "Nguyễn Thị Mai",
        "product": "Laptop Dell Inspiron 15",
        "quantity": 1,
        "location": "Kho Tổng - HCM",
        "status": "Đang chờ xuất kho",
        "history": ["Tiếp nhận đơn hàng", "Kiểm tra hàng hoá", "Đang chờ xuất kho"]
    },
    "DH2026002": {
        "order_id": "DH2026002",
        "customer": "Trần Văn Hùng",
        "product": "Bàn phím cơ Keychron K2",
        "quantity": 2,
        "location": "Kho Tổng - HN",
        "status": "Đang điều phối xuất kho",
        "history": ["Tiếp nhận đơn hàng", "Kiểm tra hàng hoá", "Đang điều phối xuất kho"]
    },
    "DH2026003": {
        "order_id": "DH2026003",
        "customer": "Lê Thu Hà",
        "product": "Màn hình LG 27 inch",
        "quantity": 1,
        "location": "Đang vận chuyển - Hà Nội",
        "status": "Đang giao hàng",
        "history": ["Tiếp nhận đơn hàng", "Kiểm tra hàng hoá", "Xuất kho", "Đang giao hàng"]
    }
}


def execute_academic_query(student_id: str) -> str:
    """Thực thi tra cứu học vụ theo mã sinh viên"""
    student = MOCK_STUDENT_DATABASE.get(student_id.strip().upper())
    if student:
        return json.dumps({
            "status": "SUCCESS",
            "student_id": student_id,
            "data": student
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu sinh viên có mã '{student_id}'"
        }, ensure_ascii=False)


def execute_schedule_appointment(student_id: str, datetime_str: str, advisor_name: str = "PGS.TS Nguyễn Văn A") -> str:
    """Thực thi đặt lịch hẹn tư vấn học vụ"""
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"BK-{student_id}-99",
        "student_id": student_id,
        "datetime": datetime_str,
        "advisor": advisor_name,
        "message": f"Đặt lịch thành công cho sinh viên {student_id} với {advisor_name} vào lúc {datetime_str}."
    }, ensure_ascii=False)


def execute_order_tracking(order_id: str) -> str:
    """Thực thi tra cứu trạng thái và vị trí đơn hàng theo mã vận đơn"""
    order = MOCK_ORDER_DATABASE.get(order_id.strip().upper())
    if order:
        return json.dumps({
            "status": "SUCCESS",
            "order_id": order_id,
            "data": order
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy đơn hàng có mã vận đơn '{order_id}'"
        }, ensure_ascii=False)


def execute_order_status_update(order_id: str, new_status: str) -> str:
    """Thực thi cập nhật trạng thái đơn hàng"""
    order = MOCK_ORDER_DATABASE.get(order_id.strip().upper())
    if order:
        old_status = order["status"]
        order["status"] = new_status
        order["history"].append(new_status)
        return json.dumps({
            "status": "SUCCESS",
            "order_id": order_id,
            "old_status": old_status,
            "new_status": new_status,
            "message": f"Cập nhật trạng thái đơn hàng {order_id} thành công: '{old_status}' → '{new_status}'."
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy đơn hàng có mã vận đơn '{order_id}' để cập nhật."
        }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "academic_query": execute_academic_query,
    "schedule_appointment": execute_schedule_appointment,
    "order_tracking": execute_order_tracking,
    "order_status_update": execute_order_status_update,
}


def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
