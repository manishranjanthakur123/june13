from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

# app_name = 'authentication'

urlpatterns = [
    path('register', RegistrationAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('user', UserRetrieveUpdateAPIView.as_view()),
]