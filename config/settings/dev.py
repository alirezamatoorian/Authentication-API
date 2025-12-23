from config.settings.base import *
environ.Env.read_env(BASE_DIR / '.env.dev')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ["*"]

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
