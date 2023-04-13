from .views import RegisterApiView, VerifyEmailView, LoginAPIView, PasswordTokenCheckAPIView, RequestPasswordResetEmail
from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path


urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('email-verify/', VerifyEmailView.as_view(), name='email-verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(), name='password-reset-confirm'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]