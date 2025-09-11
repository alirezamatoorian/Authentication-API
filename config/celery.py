import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')

app = Celery('blog_project')

# تنظیمات celery رو از django settings میگیره
app.config_from_object('django.conf:settings', namespace='CELERY')

# اپلیکیشن‌ها رو برای پیدا کردن tasks لود میکنه
app.autodiscover_tasks()