from django.urls import path
from .views import MessageAPIView, send_message

urlpatterns = [
    # Class-based view
    path('api/send-message/', MessageAPIView.as_view(), name='send-message'),
    
    # Function-based view alternative
    path('api/send-message-func/', send_message, name='send-message-func'),
]
