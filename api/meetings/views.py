from django.shortcuts import render
from .serializers import *
from meetings.models import *
from rest_framework import viewsets
from PIL import Image
from pyzbar import pyzbar
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class MeetingScheduleViewSet(viewsets.ModelViewSet):
    queryset = MeetingSchedule.objects.all()
    serializer_class = MeetingScheduleSerializer

    def update(self, request, pk=None):
        instance = MeetingSchedule.objects.get(pk=pk)
        serializer = MeetingScheduleSerializer(instance,data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    @action(detail=False, methods=['post'], name='scan_qr_code',url_path='scan_qr_code/(?P<id>[^/.]+)')
    def scan_qr_code(self,request,id):
        qr_code_id = request.data.get['qr_code_id']
        meeting_id = MeetingSchedule.objects.get(id=qr_code_id)
        attendence = MeetingParticipant.objects.get(id=id)
        attendence.meeting=meeting_id
        attendence.meeting_attendence= True
        attendence.save()
            
        return Response('Scanned Sucessfully')

    @action(detail=False, methods=['get'], name='get_meetings',url_path='get_meetings/(?P<id>[^/.]+)')
    def get_meetings(self,request,id):
        email = request.data.get['email']
        properties = Realestatepropertymanagement.objects.filter(manageby_id=id,manager_email=email)
        serializer = MeetingScheduleSerializer(properties,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# Create your views here.
class MeetingParticipantViewSet(viewsets.ModelViewSet):
    queryset = MeetingParticipant.objects.all()
    serializer_class = MeetingParticipantSerializer
    
    
