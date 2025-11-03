import pytest
from ..serializers import *
from ..models import Profile, Otp
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(email="ali@example.com", password="1234")
    assert user.email == "ali@example.com"
    assert user.is_active is True
    assert user.is_staff is False
    assert user.check_password("1234") is True


@pytest.mark.django_db
def test_user_str():
    user = User.objects.create_user(email="test@example.com", password="test123")
    assert str(user) == "test@example.com"


@pytest.mark.django_db
def test_user_default_fields():
    user = User.objects.create_user(email="a@a.com", password="pass123")
    assert user.is_active is True
    assert user.is_staff is False


@pytest.mark.django_db
def test_create_user_without_email():
    with pytest.raises(ValueError):
        User.objects.create_user(email="", password="1234")
