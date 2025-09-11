import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# تنظیمات celery رو از django settings میگیره
app.config_from_object('django.conf:settings', namespace='CELERY')

# اپلیکیشن‌ها رو برای پیدا کردن tasks لود میکنه
app.autodiscover_tasks()