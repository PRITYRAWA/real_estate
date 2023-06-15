from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from checkin.models import *

class CheckInOutListCreateView(viewsets.ModelViewSet):
    queryset = CheckInOut.objects.all()
    serializer_class = CheckInOutSerializer




