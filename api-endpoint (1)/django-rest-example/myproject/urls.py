from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home_page(request):
    """صفحه اصلی با ظاهر زیبا"""
    html = '''
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Text to JSON API</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">
        <style>
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                font-family: 'Vazir', 'Segoe UI', Tahoma, sans-serif;
            }
            .main-card {
                background: rgba(255, 255, 255, 0.95);
                border-radius: 20px;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
                margin-top: 50px;
                padding: 40px;
            }
            .api-box {
                background: #f8f9fa;
                border-radius: 10px;
                padding: 20px;
                margin: 20px 0;
                border-right: 5px solid #667eea;
            }
            .code-box {
                background: #2d3748;
                color: #e2e8f0;
                padding: 15px;
                border-radius: 8px;
                direction: ltr;
                overflow-x: auto;
                font-family: 'Courier New', monospace;
            }
            .btn-primary {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border: none;
                padding: 12px 30px;
                font-size: 16px;
                border-radius: 50px;
                transition: all 0.3s;
            }
            .btn-primary:hover {
                transform: translateY(-3px);
                box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
            }
            h1 {
                color: #2d3748;
                font-weight: 700;
                margin-bottom: 20px;
            }
            .icon-large {
                font-size: 3rem;
                color: #667eea;
                margin-bottom: 20px;
            }
            .feature-icon {
                color: #48bb78;
                font-size: 1.5rem;
                margin-left: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="main-card">
                        <div class="text-center">
                            <div class="icon-large">
                                <i class="bi bi-chat-left-text"></i>
                            </div>
                            <h1>Text to JSON API</h1>
                            <p class="lead text-muted">
                                یک متن ساده ارسال کنید، یک پاسخ JSON زیبا دریافت کنید
                            </p>
                        </div>

                        <div class="api-box">
                            <h4><i class="bi bi-send feature-icon"></i> Endpoint اصلی</h4>
                            <p><strong>آدرس:</strong> <code>/api/message/</code></p>
                            <p><strong>متد:</strong> POST</p>
                            <p><strong>فرمت:</strong> text/plain</p>
                        </div>

                        <div class="api-box">
                            <h4><i class="bi bi-code-slash feature-icon"></i> روش استفاده</h4>
                            <p class="mb-2">با curl:</p>
                            <div class="code-box">
                                curl -X POST http://localhost:8000/api/message/ \<br>
                                &nbsp;&nbsp;-H "Content-Type: text/plain" \<br>
                                &nbsp;&nbsp;-d "متن شما اینجا"
                            </div>

                            <p class="mt-3 mb-2">با Python:</p>
                            <div class="code-box">
                                import requests<br><br>
                                text = "سلام دنیا"<br>
                                response = requests.post(<br>
                                &nbsp;&nbsp;&nbsp;&nbsp;"http://localhost:8000/api/message/",<br>
                                &nbsp;&nbsp;&nbsp;&nbsp;data=text,<br>
                                &nbsp;&nbsp;&nbsp;&nbsp;headers={"Content-Type": "text/plain"}<br>
                                )<br>
                                print(response.json())
                            </div>
                        </div>

                        <div class="api-box">
                            <h4><i class="bi bi-arrow-return-right feature-icon"></i> پاسخ نمونه</h4>
                            <div class="code-box">
                                {<br>
                                &nbsp;&nbsp;"received_text": "سلام دنیا",<br>
                                &nbsp;&nbsp;"text_length": 9,<br>
                                &nbsp;&nbsp;"timestamp": "2024-01-15T10:30:00.123456",<br>
                                &nbsp;&nbsp;"message": "متن شما دریافت شد: \\"سلام دنیا\\""<br>
                                }
                            </div>
                        </div>

                        <div class="text-center mt-4">
                            <a href="/api/" class="btn btn-primary me-3">
                                <i class="bi bi-play-circle"></i> شروع کار با API
                            </a>
                            <a href="/test/" class="btn btn-outline-primary">
                                <i class="bi bi-terminal"></i> صفحه تست
                            </a>
                        </div>
                    </div>

                    <div class="text-center mt-4 text-white">
                        <p class="mb-0">ساخته شده با Django REST Framework</p>
                        <p class="small">آدرس سرور: http://localhost:8000</p>
                    </div>
                </div>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    '''
    return HttpResponse(html)


def test_page(request):
    """صفحه تست API"""
    html = '''
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>تست API</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background: #f8f9fa;
                font-family: 'Vazir', 'Segoe UI', Tahoma, sans-serif;
                padding-top: 20px;
            }
            .test-card {
                background: white;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                padding: 30px;
                margin-bottom: 30px;
            }
            textarea {
                width: 100%;
                border-radius: 10px;
                padding: 15px;
                border: 2px solid #e2e8f0;
                font-size: 16px;
                resize: vertical;
            }
            textarea:focus {
                border-color: #667eea;
                outline: none;
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            }
            #result {
                background: #2d3748;
                color: #e2e8f0;
                padding: 20px;
                border-radius: 10px;
                margin-top: 20px;
                font-family: 'Courier New', monospace;
                white-space: pre-wrap;
                display: none;
            }
            .btn-send {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 50px;
                font-size: 16px;
                transition: all 0.3s;
            }
            .btn-send:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="test-card">
                        <h2 class="text-center mb-4">🧪 تست API</h2>

                        <div class="mb-3">
                            <label class="form-label">متن خود را وارد کنید:</label>
                            <textarea id="textInput" rows="4" placeholder="متن خود را اینجا بنویسید...">سلام API</textarea>
                        </div>

                        <div class="text-center">
                            <button onclick="sendText()" class="btn btn-send">
                                ارسال متن به API
                            </button>
                        </div>

                        <div id="result"></div>
                    </div>

                    <div class="text-center">
                        <a href="/" class="btn btn-outline-secondary">
                            بازگشت به صفحه اصلی
                        </a>
                    </div>
                </div>
            </div>
        </div>

        <script>
            async function sendText() {
                const text = document.getElementById('textInput').value;
                const resultDiv = document.getElementById('result');

                resultDiv.innerHTML = '⏳ در حال ارسال...';
                resultDiv.style.display = 'block';

                try {
                    const response = await fetch('/api/message/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'text/plain; charset=utf-8'
                        },
                        body: text
                    });

                    const data = await response.json();
                    resultDiv.innerHTML = JSON.stringify(data, null, 2);

                } catch (error) {
                    resultDiv.innerHTML = '❌ خطا: ' + error.message;
                }
            }
        </script>
    </body>
    </html>
    '''
    return HttpResponse(html)


urlpatterns = [
    path('', home_page, name='home'),
    path('test/', test_page, name='test'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]