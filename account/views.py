from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import SendOtpSerializer, VerifyOtpSerializer, ProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .throttles import SendOtpThrottle
from rest_framework.permissions import IsAuthenticated
from .tasks import send_otp_email_task


# Create your views here.


class SendOtpView(APIView):
    throttle_classes = [SendOtpThrottle]

    def post(self, request, *args, **kwargs):
        serializer = SendOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp = serializer.save()
        # send_otp_email_task.delay(otp.email, otp.code)
        print(otp.code)
        return Response({"message": "OTP sent successfully!"}, status=200)


class VerifyOtpView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VerifyOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(tokens, status=status.HTTP_200_OK)


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
