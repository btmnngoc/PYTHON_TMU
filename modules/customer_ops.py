from modules.file_io import read_customers, write_customers
from datetime import datetime

def update_customer(customers):
    a = input("Nhập ID khách hàng bạn muốn cập nhật: ")
    for i in range(len(customers)):
        if customers[i][0] == a:
            print("Nhập lựa chọn của bạn:")
            print("a. Sửa Tên")
            print("b. Sửa Email")
            print("c. Sửa Số điện thoại")
            print("d. Sửa Địa chỉ")
            res = input("Nhập lựa chọn (a/b/c/d): ").lower()

            if res == 'a':
                ten_moi = input("Nhập tên mới: ")
                customers[i][1] = ten_moi
                print("Đã cập nhật tên thành công!")

            elif res == 'b':
                email_moi = input("Nhập email mới: ")
                customers[i][4] = email_moi
                print("Đã cập nhật email thành công!")

            elif res == 'c':
                sdt_moi = input("Nhập số điện thoại mới: ")
                customers[i][5] = sdt_moi
                print("Đã cập nhật số điện thoại thành công!")

            elif res == 'd':
                diachi_moi = input("Nhập địa chỉ mới: ")
                customers[i][6] = diachi_moi
                print("Đã cập nhật địa chỉ thành công!")

            else:
                print("Thao tác không hợp lệ!")
            return

    print("Không tìm thấy khách hàng, vui lòng thao tác lại!")

        
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
