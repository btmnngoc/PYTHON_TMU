from modules.file_io import read_customers, write_customers

def add_customer(file_path, customer):
    data = read_customers(file_path)
    if any(c["id"] == customer["id"] for c in data):
        return False, f"Mã khách hàng '{customer['id']}' đã tồn tại."

    required_fields = ["id", "name", "phone"]
    missing = [f for f in required_fields if not customer.get(f)]
    if missing:
        return False, f"Thiếu thông tin: {', '.join(missing)}"

    data.append(customer)
    write_customers(file_path, data)
    return True, f"Đã thêm khách hàng '{customer['id']}' thành công."

def delete_customer(file_path, customer_id):
    data = read_customers(file_path)
    if not any(c["id"] == customer_id for c in data):
        return False, f"Không tìm thấy khách hàng có mã '{customer_id}'."

    new_data = [c for c in data if c["id"] != customer_id]
    write_customers(file_path, new_data)
    return True, f"Đã xoá khách hàng '{customer_id}'."

def update_customer(file_path, customer_id, new_data):
    data = read_customers(file_path)
    for c in data:
        if c["id"] == customer_id:
            updates = {k: v for k, v in new_data.items() if v}
            if not updates:
                return False, "Không có dữ liệu mới để cập nhật."
            c.update(updates)
            write_customers(file_path, data)
            return True, f"Đã cập nhật khách hàng '{customer_id}'."
    return False, f"Không tìm thấy khách hàng có mã '{customer_id}'."

def search_customers(file_path, keyword):
    data = read_customers(file_path)
    keyword = keyword.lower()
    return [c for c in data if keyword in c["id"].lower() or keyword in c["name"].lower() or keyword in c["phone"]]

def list_customers(file_path):
    return read_customers(file_path)
