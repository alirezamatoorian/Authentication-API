from rest_framework import serializers
from .utils import generate_otp
from .models import Otp
from django.contrib.auth import get_user_model

User = get_user_model()


class SendOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def create(self, validated_data):
        email = validated_data['email']
        code = generate_otp()
        otp = Otp.objects.create(email=email, code=code)
        print(code)
        return {
            "email": email,
            "message": "کد برای شما ارسال شد",
            "expires_in": "3 minutes"
        }


class VerifyOtpSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    email = serializers.EmailField()

    def create(self, validated_data):
        code = validated_data['code']
        email = validated_data['email']
        try:
            otp = Otp.objects.filter(code=code, email=email, is_used=False).latest('created_at')
        except Otp.DoesNotExist:
            raise serializers.ValidationError("کد صحیح نیست")
        if otp.is_expired():
            raise serializers.ValidationError("کد منقصی شده است")
        otp.is_used = True
        otp.save()
        user, created = User.objects.get_or_create(email=email)
        return user



