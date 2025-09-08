from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("send-otp/", views.SendOtpView.as_view(), name='send-otp'),
    path("verify-otp", views.VerifyOtpView.as_view(), name='verify-otp')

]
