# README

## Thông tin cá nhân
- **Họ tên**: Nguyễn Ngọc Minh - 22685841

## Mô tả project
Dự án này là một website blog cơ bản, có chức năng đăng ký, đăng nhập, quản lý user, user có thể quản lý các bài blog của mình, có tính năng phân trang

### Tính năng dự kiến:

## Hướng dẫn cài đặt và chạy

### Yêu cầu hệ thống
- Python 3.12.1
- Django 5.0

### Cài đặt
1. Clone repo:
   ```sh
   git clone https://github.com/xiaoMing-04/flask-tiny-app.git
   cd anime
   ```
2. Cài đặt thư viện cần thiết
   ```sh
   pip install -r requirements.txt
   ```
3. Chạy cơ sở dữ liệu:
   ```sh
   python manage.py migrate
   ```
4. Chạy server:
   ```sh
   python manage.py runserver
   ```
5. Tạo superuser:
   ```sh
   python manage createsuperuser
   ```
- Truy cập liên kết: `http://127.0.0.1:8000/admin` để đăng nhập dưới quyền admin
6. Truy cập trang web tại `http://127.0.0.1:8000/`# ptud-gk-de-2
