from rest_framework import serializers
from .utils import generate_otp
from .models import Otp, Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class SendOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def create(self, validated_data):
        email = validated_data['email']
        code = generate_otp()
        otp = Otp.objects.create(email=email, code=code)
        return otp


class VerifyOtpSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    email = serializers.EmailField()

    def validate(self, attrs):
        code = attrs['code']
        email = attrs['email']
        try:
            otp = Otp.objects.filter(code=code, email=email, is_used=False).latest('created_at')
        except Otp.DoesNotExist:
            raise serializers.ValidationError("کد صحیح نیست")
        if otp.is_expired():
            raise serializers.ValidationError("کد منقضی شده است")
        attrs['otp'] = otp
        return attrs

    def create(self, validated_data):
        otp = validated_data['otp']
        otp.is_used = True
        otp.save()
        user, created = User.objects.get_or_create(email=validated_data['email'])
        return user


class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]
        read_only_fields = ['email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserMiniSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone', 'first_name', 'last_name', 'bio', 'avatar']
