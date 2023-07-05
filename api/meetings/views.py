from django.shortcuts import render
from .serializers import *
from meetings.models import *
from rest_framework import viewsets
from PIL import Image
from pyzbar import pyzbar
from rest_framework.decorators import action
from rest_framework.response import Response
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from property.settings import BASE_DIR
import base64

# Create your views here.
class MeetingScheduleViewSet(viewsets.ModelViewSet):
    queryset = MeetingSchedule.objects.all()
    serializer_class = MeetingScheduleSerializer
    
    def create(self, request):
        serializer = MeetingScheduleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def update(self, request, pk=None):
        instance = MeetingSchedule.objects.get(pk=pk)
        serializer = MeetingScheduleSerializer(instance,data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def list(self,request):
        try:
            management = MeetingSchedule.objects.filter().order_by('id').reverse()
            serializer = GetMeetingScheduleSerializer(management, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e))


    @action(detail=False, methods=['post'], name='scan_qr_code',url_path='scan_qr_code/(?P<email>[^/.@]+@[^/.@]+\.[^/.@]+)/(?P<meetid>[^/.]+)')
    def scan_qr_code(self,request,email,meetid):
        meeting_id = MeetingSchedule.objects.get(id=meetid)
        attendence = MeetingParticipant.objects.get(meeting=meetid,participant_email=email)
        attendence.meeting_attendence= True
        attendence.attendence_in_person = True
        attendence.save()
        return Response('Scanned Sucessfully')

    @action(detail=False, methods=['get'], name='present_participants',url_path='present_participants/(?P<email>[^/.@]+@[^/.@]+\.[^/.@]+)/(?P<meetid>[^/.]+)')
    def present_participants(self,request,email,meetid):
        attendence = MeetingParticipant.objects.filter(meeting=meetid,meeting_attendence=True)
        serializer = GetMeetingParticipantSerializer(attendence, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], name='get_meetings')
    def get_meetings(self,request):
        try:
            email = request.query_params.get('email')
            meetings = MeetingVotingCircle.objects.filter(email=email)
            print("meetings_particpants")
            meeting_list=[]
            if meetings:
                for records in meetings:
                    print(records.meeting)
                    meeting_list.append(records.meeting.id)
                meeting_details = MeetingSchedule.objects.filter(id__in=meeting_list)
                serializer = MeetingScheduleSerializer(meeting_details,many=True)
                return Response(serializer.data)
            else:
                return Response("No Meeting found for this user")
        except Exception as e:
            return Response(str(e))


# Create your views here.
class MeetingParticipantViewSet(viewsets.ModelViewSet):
    queryset = MeetingParticipant.objects.all()
    serializer_class = MeetingParticipantSerializer

    @action(detail=False, methods=['put'], name='update_users',url_path='update_users/(?P<email>[^/.@]+@[^/.@]+\.[^/.@]+)/(?P<meetid>[^/.]+)')
    def update_users(self, request,email,meetid):
        try:
            instance = MeetingParticipant.objects.get(participant_email=email,meeting=meetid)
            serializer = MeetingParticipantSerializer(instance,data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Exception as e:
            return Response(str(e))

    @action(detail=False, methods=['post'], name='attorney_data',url_path='attorney_data/(?P<email>[^/.@]+@[^/.@]+\.[^/.@]+)/(?P<meetid>[^/.]+)')
    def attorney_data(self, request, email, meetid):
        getData = request.data
        base64_image = request.POST.get('signature')
        # Decode the base64 image data)
        image_data = base64.b64decode(base64_image)
        attorney_name = getData.get('power_of_attorney_name')
        appartment_name = getData.get('appartment_name')
        owner = getData.get('owner_name')
        print(attorney_name,appartment_name,owner)
        if image_data:
                #write the decoded data back to original format in  file
                img_file = open('image.jpeg', 'wb')
                img_file.write(image_data)
                img_file.close()

        # Create a new PDF document
        output_pdf_path = f'{BASE_DIR}/pdf/{owner}.pdf'
        c = canvas.Canvas(output_pdf_path, pagesize=letter)
        c.drawString(50, 750, "Authorize", c.setFont("Helvetica", 14))
        c.drawString(50, 720, attorney_name, c.setFont("Helvetica", 10))
        c.line(x1=50, y1=715, x2=550, y2=715)
        c.drawString(50, 700, "The Undersigned Owner", c.setFont("Helvetica", 14))
        c.drawString(50, 670, owner, c.setFont("Helvetica", 10))
        c.line(x1=50, y1=665, x2=550, y2=665)
        c.drawString(50, 650, "The Appartment in the Floor Community", c.setFont("Helvetica", 14))
        c.drawString(50, 620, appartment_name, c.setFont("Helvetica", 10))
        c.line(x1=50, y1=615, x2=550, y2=615)
        c.drawString(50, 600, "Authorizes here by", c.setFont("Helvetica", 14))
        c.drawString(50, 570, attorney_name, c.setFont("Helvetica", 10))
        c.line(x1=50, y1=565, x2=550, y2=565)
        x=200
        y=400
        img = f'{BASE_DIR}/{img_file.name}'
        c.drawImage(img, x, y, width=150, height=70, mask=None)
        c.showPage()  # Move to the next page for the next order
        c.save()
        instance = MeetingParticipant.objects.get(participant_email=email,meeting=meetid)
        instance.power_of_attroney= True
        instance.attroney_attchment =output_pdf_path
        instance.power_of_attroney_name =attorney_name
        instance.apartment = appartment_name
        instance.save()
        return Response("sucessfully saved data") 

# Create your views here.
class MeetingParticipantAgendaViewSet(viewsets.ModelViewSet):
    queryset = MeetingParticipantAgenda.objects.all()
    serializer_class = MeetingParticipantAgendaSerializer

    @action(detail=False, methods=['post'], name='submit_agenda',url_path='submit_agenda/(?P<email>[^/.@]+@[^/.@]+\.[^/.@]+)/(?P<meetid>[^/.]+)')    
    def submit_agenda(self, request,email,meetid):
        participant_id= MeetingParticipant.objects.get(participant_email=email,meeting=meetid)
        if participant_id:
            print("participant_id",participant_id)
            params ={}
            params['email']=email
            params['meetid']=meetid
            serializer = MeetingParticipantAgendaSerializer(data=request.data, context={'request': params})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
    

