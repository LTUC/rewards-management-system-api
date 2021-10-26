from django.urls import path
from .views import RegisterView, VerifyEmail, LoginAPIView, RegisterSuperUserView, TeamMatesAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register-super/', RegisterSuperUserView.as_view(), name='register-super'),
    path('mates/', TeamMatesAPIView.as_view(), name='mates'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
