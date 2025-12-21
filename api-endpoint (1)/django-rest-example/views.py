from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class MessageAPIView(APIView):
    """
    API endpoint for messages with GET and POST methods
    """

    # اضافه کردن متد GET
    def get(self, request):
        response_data = {
            'status': 'success',
            'message': 'این endpoint پیام‌ها را دریافت می‌کند',
            'usage': {
                'POST': 'برای ارسال پیام جدید',
                'GET': 'برای دریافت اطلاعات endpoint'
            },
            'example_request': {
                'method': 'POST',
                'url': '/api/message/',
                'body': {'message': 'متن پیام شما'}
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        message = request.data.get('message', '')

        if not message:
            return Response(
                {'error': 'پیام نمی‌تواند خالی باشد'},
                status=status.HTTP_400_BAD_REQUEST
            )

        response_data = {
            'status': 'success',
            'received_message': message,
            'response': f'پیام شما با موفقیت دریافت شد: {message}',
            'message_length': len(message)
        }

        return Response(response_data, status=status.HTTP_200_OK)