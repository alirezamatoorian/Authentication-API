import pytest
from ..serializers import *
from ..models import Profile, Otp
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


# tests for User model---------
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


# tests for Otp model----------

@pytest.mark.django_db
def test_create_otp():
    otp = Otp.objects.create(email="test@email.com", code='123456')
    assert otp.email == "test@email.com"
    assert otp.code == "123456"
    assert otp.is_used is False
    assert otp.created_at is not None


@pytest.mark.django_db
def test_is_expired_false():
    otp = Otp.objects.create(email="ali@example.com", code="123456")
    otp.created_at = timezone.now() - timedelta(minutes=2)
    otp.save()
    assert otp.is_expired() is False


@pytest.mark.django_db
def test_is_expired_true():
    otp = Otp.objects.create(email="ali@example.com", code="999999")
    otp.created_at = timezone.now() - timedelta(minutes=5)
    otp.save()
    assert otp.is_expired() is True


# tests for Profile model---------

@pytest.mark.django_db
def test_profile_created_on_user_creation():
    user = User.objects.create_user(email="ali@example.com", password="1234")
    assert hasattr(user, "profile")
    assert isinstance(user.profile, Profile)
    assert user.profile.user == user


@pytest.mark.django_db
def test_profile_not_duplicated_on_user_update():
    user = User.objects.create_user(email="ali@example.com", password="1234")
    profile_id = user.profile.id
    user.email = "new@example.com"
    user.save()
    assert user.profile.id == profile_id
    assert Profile.objects.count() == 1


@pytest.mark.django_db
def test_delete_profile():
    user = User.objects.create_user(email="ali@example.com", password="1234")
    user.delete()
    assert Profile.objects.count() == 0
