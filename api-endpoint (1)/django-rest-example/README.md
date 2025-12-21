# Django REST Framework - Message API

یک API ساده برای دریافت پیام متنی و بازگشت پاسخ JSON

## نصب و راه‌اندازی

### 1. نصب وابستگی‌ها

```bash
cd django-rest-example
pip install -r requirements.txt
```

### 2. اجرای migrations

```bash
python manage.py migrate
```

### 3. اجرای سرور

```bash
python manage.py runserver
```

سرور روی `http://localhost:8000` اجرا می‌شود.

## استفاده از API

### Endpoint

- **URL**: `http://localhost:8000/api/message/`
- **Method**: POST
- **Content-Type**: application/json

### مثال با curl

```bash
curl -X POST http://localhost:8000/api/message/ \
  -H "Content-Type: application/json" \
  -d '{"message": "سلام دنیا"}'
```

### مثال با Python requests

```python
import requests

url = "http://localhost:8000/api/message/"
data = {"message": "سلام دنیا"}

response = requests.post(url, json=data)
print(response.json())
```

### پاسخ نمونه

```json
{
  "success": true,
  "received_message": "سلام دنیا",
  "message_length": 9,
  "response": "پیام شما با موفقیت دریافت شد: سلام دنیا",
  "timestamp": "2024-01-15T10:30:00.123456"
}
```

## ساختار پروژه

```
django-rest-example/
├── manage.py
├── requirements.txt
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── api/
    ├── __init__.py
    ├── apps.py
    ├── views.py
    ├── serializers.py
    └── urls.py
```
