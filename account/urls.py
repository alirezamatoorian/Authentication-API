from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "account"

urlpatterns = [
    path("send-otp/", views.SendOtpView.as_view(), name='send-otp'),
    path("verify-otp/", views.VerifyOtpView.as_view(), name='verify-otp'),
    path("refresh/", TokenRefreshView.as_view(), name='refresh-token')

]
