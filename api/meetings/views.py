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

    @action(detail=False, methods=['post'], name='scan_qr_code',url_path='scan_qr_code/(?P<id>[^/.]+)')
    def scan_qr_code(self,request,id):
        qr_code_image = request.FILES['qr_code_image']
        # Load the image
        image = Image.open(qr_code_image)
        # Scan the QR code
        qr_codes = pyzbar.decode(image)
        if qr_codes:
            qr_code_data = qr_codes[0].data.decode('utf-8')
            # Save the ID in your model
            meeting_id = MeetingSchedule.objects.get(id=qr_code_data)
            attendence = MeetingParticipant.objects.get(id=id)
            attendence.meeting=meeting_id
            attendence.meeting_attendence= True
            attendence.save()
            
        return Response('Scanned Sucessfully')


# Create your views here.
class MeetingParticipantViewSet(viewsets.ModelViewSet):
    queryset = MeetingParticipant.objects.all()
    serializer_class = MeetingParticipantSerializer