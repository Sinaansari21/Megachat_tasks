from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


@api_view(['POST'])
def send_message(request):
    """
    دریافت پیام متنی و بازگرداندن JSON
    """
    try:
        # خواندن متن از بدنه درخواست
        text = request.body.decode('utf-8').strip()

        if not text:
            return Response({
                'error': 'متن نمی‌تواند خالی باشد'
            }, status=status.HTTP_400_BAD_REQUEST)

        # ساخت پاسخ JSON
        return Response({
            'received_text': text,
            'text_length': len(text),
            'timestamp': datetime.now().isoformat(),
            'message': f'متن شما دریافت شد: "{text}"'
        })

    except Exception as e:
        return Response({
            'error': 'خطا در پردازش درخواست'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_root(request):
    """صفحه اصلی API"""
    return Response({
        'name': 'Text to JSON API',
        'description': 'متن ساده بفرستید، JSON دریافت کنید',
        'endpoint': '/api/message/',
        'method': 'POST',
        'content_type': 'text/plain',
        'example': 'curl -X POST http://localhost:8000/api/message/ -d "سلام"'
    })