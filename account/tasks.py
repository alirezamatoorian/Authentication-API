from celery import shared_task
from datetime import timedelta
from django.utils.timezone import now
from .models import Otp


@shared_task
def cleanup_otps():
    expired = Otp.objects.filter(is_used=True) | Otp.objects.filter(created_at__lt=now() - timedelta(minutes=5))
    count = expired.count()
    expired.delete()
    return f"{count} expired/used OTPs deleted."
