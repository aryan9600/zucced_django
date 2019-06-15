from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveAPIView

api_name = 'authentication'

urlpatterns = [
    path(r'users', RegistrationAPIView.as_view()),
    path(r'users/login', LoginAPIView.as_view()),
    path(r'user', UserRetrieveAPIView.as_view()),
]