from django.shortcuts import render
from .serializers import *
from meetings.models import *
from rest_framework import viewsets
from PIL import Image
from pyzbar import pyzbar
from rest_framework.decorators import action
from rest_framework.response import Response
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,inch
from property.settings import BASE_DIR,MEDIA_ROOT
import base64
import os
from django.utils import timezone
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
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
    
    def partial_update(self, request, pk=None):
        instance = MeetingSchedule.objects.get(pk=pk)
        serializer = MeetingScheduleSerializer(instance,data=request.data,partial=True, context={'request': request})
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


    @action(detail=False, methods=['get'], name='votes_result',url_path='votes_result/(?P<meetid>[^/.]+)/(?P<agid>[^/.]+)')
    def votes_result(self,request,meetid,agid):
        #participants = MeetingParticipant.objects.filter(meeting=meetid)
        result_dict={}
        agendas = MeetingAgenda.objects.get(meeting=meetid,id=agid)
        meet_participants =ParticipantAgenda.objects.filter(agenda=agid)
        pers_participant=MeetingParticipant.objects.filter(meeting=meetid,attendance_in_person=True).count()
        adv_participant=MeetingParticipant.objects.filter(meeting=meetid,online_voting=True).count()
        print("meet",meet_participants)
        result_dict['participation_in_person']=pers_participant
        result_dict['participation_in_advance']=adv_participant
        participants_count = meet_participants.count()
        votes_participants=[]
        vote_yes= meet_participants.filter(agenda_vote=True)
        for rec in vote_yes:
            votes_yes={}
            votes_yes['email']=rec.participant.participant_email
            votes_yes['name']=rec.participant.participant.participant_name
            votes_participants.append(votes_yes)
        result_dict['votes_yes']=votes_participants
        vote_yes_count= vote_yes.count()
        votes_participants_no=[]
        vote_no= meet_participants.filter(agenda_vote=False)
        vote_no_count= vote_no.count()
        for rec in vote_no:
            votes_no={}
            votes_no['email']=rec.participant.participant_email
            votes_no['name']=rec.participant.participant.participant_name
            votes_participants_no.append(votes_no)
        result_dict['votes_no']=votes_participants_no
        result_dict['votes_no_count']=vote_no_count
        result_dict['votes_yes_count']=vote_yes_count
        result_dict['participants_count']=participants_count
        vote_type= MeetingVotes.objects.filter(meeting=meetid).values_list('voting_type','tie_case','tabs','condition')
        yes_votes_averge_percent =vote_yes_count/participants_count
        yes_result = round(yes_votes_averge_percent,1)
        result_dict['yes_averge']=yes_result
        no_votes_averge_percent =vote_no_count/participants_count
        no_result = round(no_votes_averge_percent,1)
        result_dict['no_averge']=no_result
        valuess = []
        for item in vote_type[0]:
            split_items = item.split(',')
            valuess.extend(split_items)
        result_dict['tab']=valuess[2]  
        result_dict['condition']=valuess[3]   
        if valuess[0] == 'head':
            result_dict['vote_type']='head'
            if yes_result > no_result:
                result_dict['final_result']="Accepted"
                result_dict['tie_case']='No'
            elif yes_result < no_result:
                result_dict['final_result']="Rejected"
                result_dict['tie_case']='No'
            else:
                result_dict['tie_case']='Yes'
                result_dict['final_result']=valuess[1]
        if valuess[0] == 'object':
            result_dict['vote_type']='object'
            yes_object_count=0
            for rec in vote_yes:
                yes_object_count= yes_object_count + rec.participant.object_count
            no_object_count=0
            for rec in vote_no:
                no_object_count= no_object_count + rec.participant.object_count
            if yes_object_count > no_object_count:
                result_dict['final_result']="Accepted"
                result_dict['tie_case']='No'
            elif no_object_count < no_object_count:
                result_dict['final_result']="Rejected"
                result_dict['tie_case']='No'
            else:
                result_dict['tie_case']='Yes'
                result_dict['final_result']=valuess[1]
        if valuess[0] == 'value':
            result_dict['vote_type']='value'
            yes_object_count=0
            for rec in vote_yes:
                yes_value = yes_object_count + rec.participant.asset_value
            no_object_count=0
            for rec in vote_no:
                no_value= no_object_count + rec.participant.asset_value
            if yes_value > no_value:
                result_dict['final_result']="Accepted"
                result_dict['tie_case']='No'
            elif no_value < no_value:
                result_dict['final_result']="Rejected"
                result_dict['tie_case']='No'
            else:
                result_dict['tie_case']='Yes'
                result_dict['final_result']=valuess[1]

        return Response(result_dict)

    @action(detail=False, methods=['post'], name='scan_qr_code',url_path='scan_qr_code/(?P<email>[^/]+[@._][^/]+)/(?P<meetid>[^/.]+)')
    def scan_qr_code(self,request,email,meetid):
        meeting_id = MeetingSchedule.objects.get(id=meetid)
        attendence = MeetingParticipant.objects.get(meeting=meetid,participant_email=email)
        attendence.meeting_attendance= True
        attendence.attendance_in_person = True
        attendence.save()
        serializer = MeetingParticipantSerializer(attendence)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], name='present_participants',url_path='present_participants/(?P<email>[^/]+[@._][^/]+)/(?P<meetid>[^/.]+)')
    def present_participants(self,request,email,meetid):
        attendence = MeetingParticipant.objects.filter(meeting=meetid,meeting_attendance=True)
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
                return Response(meeting_list)
        except Exception as e:
            return Response(str(e))

    @action(detail=False, methods=['patch'], name='update_time',url_path='update_time/(?P<meetid>[^/.]+)')
    def update_time(self,request,meetid):
        try:
            flag = request.data.get('flag')
            current_time = timezone.now().time()
            meeting = MeetingSchedule.objects.get(id=meetid)
            if flag == 0:
                meeting.meet_start_time=current_time
                meeting.status='live'
            if flag ==1:
                meeting.meet_start_time=current_time
                meeting.status='finished'
            meeting.save()
            serializer = MeetingScheduleSerializer(meeting)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e))
        
    @action(detail=False, methods=['get'], name='download_pdf',url_path='download_pdf/(?P<meetid>[^/.]+)')
    def download_pdf(self,request,meetid):
        meet_details= MeetingSchedule.objects.get(id=meetid)
        pers_participant=MeetingParticipant.objects.filter(meeting=meetid,voting_attendance=True).count()
        adv_participant=MeetingParticipant.objects.filter(meeting=meetid,online_voting=True).count()
        agenda_items=MeetingAgenda.objects.filter(meeting=meetid)
        participant=MeetingParticipant.objects.filter(meeting=meetid)

        output_pdf_path = f'{MEDIA_ROOT}/pdf/{meet_details.title}.pdf'
        c = canvas.Canvas(output_pdf_path, pagesize=letter)
        c.drawString(50, 700, meet_details.title, c.setFont("Helvetica", 14))
        c.line(x1=50, y1=650, x2=550, y2=650)
        width = 400
        height = 100
        data = [
            ["Location:",meet_details.venue],
            ["Date | Time:", meet_details.meeting_date],
            ["Chairperson:", meet_details.chairman.manager_name],
            ["Minute-taker:", meet_details.minute_taker.manager_name],
            ["Present:",pers_participant],
            ["Guest:","--"]
        ]
        style = TableStyle([
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Table body background color
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Table grid color
            ('FONTSIZE', (0, 1), (-1, -1), 10),  # Table body font size
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Table body font
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical alignment for all cells
        ])
        # Increase the padding of the second cell in the first row
        style.add('RIGHTPADDING', (1, 0), (1, 0), 415)  # Increase the right padding

        table = Table(data)
        table.setStyle(style)

        table.wrapOn(c, 50, 400)
        table.drawOn(c, 50, 525) 

        c.line(x1=50, y1=515, x2=550, y2=515)
        c.drawString(50, 485, "Agenda items", c.setFont("Helvetica", 12))
        c.line(x1=50, y1=482, x2=125, y2=482)
        xData = 465
        count = 1
        for rec in agenda_items:
            c.drawString(50, xData, rec.topic, c.setFont("Helvetica", 10))
            count = count + 1
            xData = xData - 15
        c.drawString(50, 370, "Further remarks:", c.setFont("Helvetica", 10))
        c.drawString(50, 365, "__", c.setFont("Helvetica", 10))
        c.drawString(50, 350, "End of the meeting : "+str(meet_details.meet_end_time), c.setFont("Helvetica", 10))
        c.drawString(50, 330, "LEATUS AG", c.setFont("Helvetica", 10))
        c.drawString(50, 300, meet_details.chairman.manager_name, c.setFont("Helvetica", 10))
        c.drawString(350, 300, meet_details.minute_taker.manager_name, c.setFont("Helvetica", 10))
        c.drawString(50, 290, "Chairperson", c.setFont("Helvetica", 10))
        c.drawString(350, 290, "Minute-taker", c.setFont("Helvetica", 10))
        c.drawString(50, 270, "Attendance list", c.setFont("Helvetica", 10))
        
        data = [
            ["Name","Participation","Value quotas", "Head votes", "Object votes"]
        ]
       
        style = TableStyle([
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Table body background color
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Table grid color
            ('FONTSIZE', (0, 1), (-1, -1), 10),  # Table body font size
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Table body font
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical alignment for all cells
        ])
        column_widths = [6 * cm, 4 * cm] + [None] * 4 
        table = Table(data, colWidths=column_widths)
        table.setStyle(style)

        table.wrapOn(c, 50, 170)
        table.drawOn(c, 50, 250)
        c.showPage()  # Move to the next page for the next order
        c.save()
        pdf_path = f'pdf/{meet_details.title}.pdf'
        meet_details.meeting_protocol=pdf_path
        meet_details.save()
        serializer = MeetingScheduleSerializer(meet_details)
        return Response(serializer.data['meeting_protocol'])


        
# Create your views here.
class MeetingParticipantViewSet(viewsets.ModelViewSet):
    queryset = MeetingParticipant.objects.all()
    serializer_class = MeetingParticipantSerializer

    @action(detail=False, methods=['put'], name='update_users',url_path='update_users/(?P<email>[^/]+[@._][^/]+)/(?P<meetid>[^/.]+)')
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

    @action(detail=False, methods=['post'], name='attorney_data',url_path='attorney_data/(?P<email>[^/]+[@._][^/]+)/(?P<meetid>[^/.]+)')
    def attorney_data(self, request, email, meetid):
        getData = request.data
        base64_image = request.POST.get('signature')
        prefix = "data:image/png;base64,"
        if base64_image.startswith(prefix):
            base64_string = base64_image[len(prefix):]
        #padded_string = base64_image + '=' * (4 - (len(base64_image) % 4))
        #print(base64_image)
        # Decode the base64 image data)
        image_data = base64.b64decode(base64_string)
        print("flow is here")
        attorney_name = getData.get('power_of_attorney_name')
        appartment_name = getData.get('appartment_name')
        owner = getData.get('owner_name')
        print(attorney_name,appartment_name,owner)
        if image_data:
            #write the decoded data back to original format in  file
            file_path = os.path.join(BASE_DIR, 'image.jpeg')
            with open(file_path, 'wb') as img_file:
                img_file.write(image_data)
                img_file.close()

        # Create a new PDF document
        output_pdf_path = f'{MEDIA_ROOT}/pdf/{owner}.pdf'
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
        img =file_path #f'{BASE_DIR}/{img_file.name}'
        c.drawImage(img, x, y, width=150, height=70, mask=None)
        c.showPage()  # Move to the next page for the next order
        c.save()
        pdf_path = f'pdf/{owner}.pdf'
        instance = MeetingParticipant.objects.get(participant_email=email,meeting=meetid)
        instance.power_of_attroney= True
        instance.attroney_attchment =pdf_path
        instance.power_of_attroney_name =attorney_name
        instance.apartment = appartment_name
        instance.save()
        serializer=MeetingParticipantSerializer(instance)
        return Response(serializer.data) 
    
    

# Create your views here.
class MeetingParticipantAgendaViewSet(viewsets.ModelViewSet):
    queryset = MeetingParticipantAgenda.objects.all()
    serializer_class = MeetingParticipantAgendaSerializer

    @action(detail=False, methods=['post'], name='submit_agenda',url_path='submit_agenda/(?P<email>[^/]+[@._][^/]+)/(?P<meetid>[^/.]+)')    
    def submit_agenda(self, request,email,meetid):
        participant_id= MeetingParticipant.objects.get(participant_email=email,meeting=meetid)
        if participant_id:
            request.email = email
            request.meetid = meetid
            serializer = MeetingParticipantAgendaSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
    
class ParticipantAgendaViewSet(viewsets.ModelViewSet):
    queryset = ParticipantAgenda.objects.all()
    serializer_class = ParticipantAgendaSerializer
