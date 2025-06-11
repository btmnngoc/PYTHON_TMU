# 🏪 Hệ thống Quản lý Khách hàng Siêu thị Vinmart

> Đề tài bài tập lớn học phần Lập trình Python – Nhóm sinh viên lớp 242_INFO4511_02  
> 🚀 Giao diện: Web app với **Streamlit**  
> 📁 Lưu trữ dữ liệu: **File JSON**  
> 💻 Ngôn ngữ: Python (Không dùng class – phù hợp với sinh viên năm 2)

---

## 📌 Mục tiêu đề tài

Xây dựng hệ thống giúp quản lý thông tin khách hàng của siêu thị Vinmart một cách đơn giản và tiện lợi, bao gồm các chức năng:

- Thêm khách hàng
- Xoá khách hàng
- Cập nhật thông tin
- Tìm kiếm theo mã / tên / số điện thoại
- Hiển thị toàn bộ danh sách

---

## 🧱 Cấu trúc thư mục

```
customer_manager/
├── app.py                     # Giao diện Streamlit chính
├── modules/
│   ├── customer_ops.py        # Các hàm xử lý nghiệp vụ
│   └── file_io.py             # Đọc / ghi file JSON
├── data/
│   └── customers.json         # File lưu thông tin khách hàng
├── README.md                  # Tài liệu hướng dẫn sử dụng
```

---

## 🚀 LINK CHƯƠNG TRÌNH ĐÃ DEPLOY TRÊN WEB

[LINK BÀI TẬP NHÓM 7](https://python-tmu-group7.streamlit.app)

---

## 📊 Dữ liệu mẫu

- File `data/customers.json` đã có sẵn 50 khách hàng mẫu.
- Định dạng lưu trữ: JSON
- Mỗi khách hàng có các thuộc tính:
  - `id`, `name`, `phone`, `email`, `address`

---

## 🖥️ Giao diện người dùng

- Giao diện web chia thành các mục:  
  ➕ Thêm | 🗑️ Xoá | ✏️ Cập nhật | 🔍 Tìm kiếm | 📖 Danh sách

- Mỗi mục có form rõ ràng, dễ dùng, phù hợp với người không chuyên kỹ thuật.

---

## ⚙️ Tính năng nổi bật

| Tính năng        | Miêu tả                                                             |
|------------------|---------------------------------------------------------------------|
| Modular hóa      | Code chia module rõ ràng, dễ bảo trì và mở rộng                   |
| Lưu trữ an toàn  | Ghi/đọc file JSON tránh mất dữ liệu khi tắt chương trình          |
| Web UI tiện lợi  | Giao diện Streamlit dễ thao tác, có thể triển khai lên internet   |

---

## 📚 Tài liệu bổ sung

- **Sơ đồ khối hệ thống** (kèm trong file PDF báo cáo)
- **Ảnh chụp giao diện**
- **Slides trình bày** (nếu có)
- **Báo cáo bài tập lớn**: `Report_BaiTapLon_Vinmart.pdf`

---

## 💡 Định hướng phát triển

- Tích hợp thêm biểu đồ phân tích khách hàng (RFM, frequency...)
- Xuất dữ liệu ra Excel
- Kết nối cơ sở dữ liệu (SQLite hoặc MySQL)
- Thêm phân quyền người dùng (admin - nhân viên)

---

## 👩‍💻 Nhóm thực hiện

- **Bùi Trịnh Minh Ngọc** – Trưởng nhóm  
- 

---

## 📎 License

Đây là bài tập lớn phục vụ mục đích học tập tại trường đại học. Không dùng cho mục đích thương mại.