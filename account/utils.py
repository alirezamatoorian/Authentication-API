import secrets
from django.core.mail import send_mail


def generate_otp():
    return ''.join(secrets.choice('0123456789') for _ in range(6))
