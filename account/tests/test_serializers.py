import pytest
from ..serializers import SendOtpSerializer
from ..models import Otp


@pytest.mark.django_db
def test_send_otp_serializer_valid_email():
    data = {'email': "test@email.com"}
    serializer = SendOtpSerializer(data=data)
    assert serializer.is_valid() is True
    assert 'email' in serializer.validated_data
    assert serializer.validated_data["email"] == "test@email.com"


@pytest.mark.django_db
def test_send_otp_serializer_invalid_email():
    data = {'email': 'not-email'}
    serializer = SendOtpSerializer(data=data)
    assert serializer.is_valid() is False
    assert 'email' in serializer.errors


@pytest.mark.django_db
def test_send_otp_serializer_create_method():
    data = {'email': 'test@email.com'}
    serializer = SendOtpSerializer(data=data)
    assert serializer.is_valid() is True
    otp_instance = serializer.save()
    assert Otp.objects.count() == 1
    otp = Otp.objects.first()
    assert otp.email == "test@email.com"
    assert isinstance(otp.code, str)
    assert len(otp.code) == 6
    assert otp_instance == otp
