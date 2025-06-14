import streamlit as st
from modules.customer_ops import *
import os

FILE_PATH = "data/customers.json"
os.makedirs("data", exist_ok=True)

st.set_page_config(page_title="Quản lý Khách hàng", layout="centered")
st.title("HỆ THỐNG QUẢN LÝ KHÁCH HÀNG VINMART")

menu = st.sidebar.radio("Chọn chức năng", 
    ["Thêm khách hàng", "Xoá khách hàng", "Cập nhật", "Tìm kiếm", "Xem danh sách"])

if menu == "Thêm khách hàng":
    st.subheader("Thêm khách hàng mới")
    name = st.text_input("Tên KH")
    phone = st.text_input("SĐT")
    email = st.text_input("Email")
    address = st.text_input("Địa chỉ")
    
    if st.button("Thêm"):
        customer = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        success, msg = add_customer(FILE_PATH, customer)
        if success:
            st.success(msg)
        else:
            st.error(msg)


elif menu == "Xoá khách hàng":
    customers = list_customers(FILE_PATH)
    ids = [c["id"] for c in customers]

    if ids:
        selected_id = st.selectbox("Chọn mã KH để xoá", ids)
        selected_customer = next((c for c in customers if c["id"] == selected_id), None)

        if selected_customer:
            st.write("Thông tin khách hàng sẽ bị xoá:")
            st.table({
                "Mã KH": [selected_customer["id"]],
                "Tên": [selected_customer["name"]],
                "SĐT": [selected_customer["phone"]],
                "Email": [selected_customer["email"]],
                "Địa chỉ": [selected_customer["address"]]
            })

            if st.button("Xác nhận xoá"):
                success, msg = delete_customer(FILE_PATH, selected_id)
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
    else:
        st.info("Không có khách hàng nào để xoá.")

elif menu == "Cập nhật":
    customers = list_customers(FILE_PATH)
    ids = [c["id"] for c in customers]
    if ids:
        selected_id = st.selectbox("Chọn mã KH", ids)
        selected = next((c for c in customers if c["id"] == selected_id), None)
        name = st.text_input("Tên KH", selected["name"])
        phone = st.text_input("SĐT", selected["phone"])
        email = st.text_input("Email", selected["email"])
        address = st.text_input("Địa chỉ", selected["address"])
        if st.button("Cập nhật"):
            success, msg = update_customer(FILE_PATH, selected_id, {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            })
            st.success(msg) if success else st.error(msg)
    else:
        st.info("Không có khách hàng.")

elif menu == "Tìm kiếm":
    keyword = st.text_input("Từ khoá tìm kiếm")
    if keyword:
        results = search_customers(FILE_PATH, keyword)
        if results:
            st.dataframe(results)
        else:
            st.warning("Không tìm thấy.")

elif menu == "Xem danh sách":
    data = list_customers(FILE_PATH)
    if data and isinstance(data, list):
        st.dataframe(data)
    else:
        st.info("Chưa có khách hàng nào.")
