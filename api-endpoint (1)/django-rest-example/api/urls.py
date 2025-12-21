from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api_root'),
    path('message/', views.send_message, name='send_message'),
]