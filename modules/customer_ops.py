from modules.file_io import read_customers, write_customers
from datetime import datetime

def update_customer(file_path, customer_id, new_data):
    data = read_customers(file_path)
    updated = False

    for customer in data:
        if customer["id"] == customer_id:
            for key, value in new_data.items():
                if value != "" and key in customer:
                    customer[key] = value
            customer["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            updated = True
            break

    if updated:
        write_customers(file_path, data)
        print(f"✅ Đã cập nhật khách hàng ID {customer_id}")
    else:
        print(f"⚠️ Không tìm thấy khách hàng ID {customer_id}")
        
def delete_customer(file_path, customer_id):
    data = read_customers(file_path)
    data = [c for c in data if c["id"] != customer_id]
    write_customers(file_path, data)

def update_customer(file_path, customer_id, new_data):
    data = read_customers(file_path)
    for customer in data:
        if customer["id"] == customer_id:
            customer.update({k: v for k, v in new_data.items() if v != ""})
    write_customers(file_path, data)

def search_customers(file_path, keyword):
    data = read_customers(file_path)
    keyword = keyword.lower()
    return [c for c in data if keyword in c["id"].lower() or keyword in c["name"].lower() or keyword in c["phone"]]

def list_customers(file_path):
    return read_customers(file_path)
