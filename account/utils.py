import secrets
from django.core.mail import send_mail


def generate_otp():
    return ''.join(secrets.choice('0123456789') for _ in range(6))


def send_otp_email(email, code):
    subject = "کد ورود شما"
    message = f"کد ورود یکبار مصرف شما: {code}"
    send_mail(
        subject,
        message,
        None,  # یا DEFAULT_FROM_EMAIL
        [email],
        fail_silently=False,
    )
