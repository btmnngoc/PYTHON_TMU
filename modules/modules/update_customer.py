import streamlit as st
from modules.customer_ops import list_customers, update_customer

def update_customer_ui(file_path):
    st.subheader("✏️ Cập nhật thông tin")
    customers = list_customers(file_path)
    if not customers:
        st.info("📭 Không có khách hàng để cập nhật.")
        return

    ids = [c["id"] for c in customers]
    id_to_update = st.selectbox("Chọn mã KH cần cập nhật", ids)

    selected = next((c for c in customers if c["id"] == id_to_update), None)
    if selected:
        name = st.text_input("Tên KH", selected["name"])
        phone = st.text_input("SĐT", selected["phone"])
        email = st.text_input("Email", selected["email"])
        address = st.text_input("Địa chỉ", selected["address"])
        if st.button("Cập nhật"):
            update_customer(file_path, id_to_update, {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            })
            st.success("✅ Cập nhật thành công!")
