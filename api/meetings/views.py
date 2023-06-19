from django.shortcuts import render
from .serializers import *
from meetings.models import *
from rest_framework import viewsets


# Create your views here.
class MeetingScheduleViewSet(viewsets.ModelViewSet):
    queryset = MeetingSchedule.objects.all()
    serializer_class = MeetingScheduleSerializer

