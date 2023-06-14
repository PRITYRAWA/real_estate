from typing import Dict
from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken
from api.foundation.serializers import (
    LoginSerializer,RegistrationSerializer,LogoutSerializer
    
)
from foundation.models import CustomUser


def get_tokens_for_user(user: CustomUser) -> Dict:
    """Token generate"""

    refresh_token = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh_token),
        "access": str(refresh_token.access_token),
    }


class RegisterationAPIView(generics.GenericAPIView):
    """
    Register new users usingemail and password.
    """

    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "user": RegistrationSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": get_tokens_for_user(user),
            },
            status=status.HTTP_200_OK,
        )


class LoginAPIView(generics.GenericAPIView):
    """
    Getting otp existing users using email and password if the two_step_verification is enabled.
    Or,
    Getting token using email and password.
    """

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data.get("email")
        user = CustomUser.objects.get(email=email, is_active=True)
        try:
            login(request, user)
            return Response(get_tokens_for_user(user), status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(views.APIView):
    """
    Logout an authenticated user.
    """
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "The refresh token blacklisted"},
                status=status.HTTP_205_RESET_CONTENT,
            )
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)




