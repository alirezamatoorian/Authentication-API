from celery import shared_task
from datetime import timedelta
from django.core.mail import send_mail
from django.utils.timezone import now
from .models import Otp
from django.conf import settings


@shared_task
def remove_expired_otp():
    expired = Otp.objects.filter(is_used=True) | Otp.objects.filter(created_at__lt=now() - timedelta(minutes=5))
    expired.delete()
    return "expired/used OTPs deleted."


@shared_task
def send_otp_email_task(email, code):
    subject = "کد ورود شما"
    message = f"کد ورود یکبار مصرف شما: {code}"
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
