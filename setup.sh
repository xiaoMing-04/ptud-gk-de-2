#!/bin/bash

echo "🚀 Bắt đầu cài đặt môi trường và chạy ứng dụng Django..."

# Tạo và kích hoạt virtual environment
echo "🐍 Tạo môi trường ảo..."
python3 -m venv venv
source venv/bin/activate

# Cập nhật pip
echo "⬆️  Cập nhật pip..."
pip install --upgrade pip

# Cài đặt các package từ requirements.txt
if [ -f "requirements.txt" ]; then
    echo "📦 Cài đặt các package từ requirements.txt..."
    pip install -r requirements.txt
else
    echo "❌ Không tìm thấy file requirements.txt!"
    exit 1
fi

# Thực hiện migrate
echo "🗃️  Thực hiện migrate..."
python manage.py migrate

# Tạo superuser tự động (tuỳ chọn)
if [ "$1" == "--createsuperuser" ]; then
    echo "👤 Tạo superuser..."
    python manage.py createsuperuser
fi

# Chạy server
echo "🌐 Chạy server Django..."
python manage.py runserver

echo "✅ Hoàn thành!"
