from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics
from checkin.models import *
from .serializers import *

class CheckInOutListCreateView(generics.ListCreateAPIView):
    queryset = CheckInOut.objects.all()
    serializer_class = CheckInOutSerializer

class CheckInOutRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CheckInOut.objects.all()
    serializer_class = CheckInOutSerializer
