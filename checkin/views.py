from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt


class SignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer



class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)



class CheckInOutListCreateView(generics.ListCreateAPIView):
    queryset = CheckInOut.objects.all()
    serializer_class = CheckInOutSerializer

class CheckInOutRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CheckInOut.objects.all()
    serializer_class = CheckInOutSerializer
