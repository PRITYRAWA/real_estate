from rest_framework import serializers
from meetings.models import *
from masters.models import *
import qrcode
from PIL import Image
from django.conf import settings

class MeetingAgendaSerializer(serializers.ModelSerializer):
    meeting = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = MeetingAgenda
        fields = (
            "id",
            "meeting",
            "topic",
            "status",
       
        )
    
class MeetingParticipantSerializer(serializers.ModelSerializer):
    meeting = serializers.PrimaryKeyRelatedField(read_only=True)
    participant = serializers.CharField(source='participant.participant_name', read_only=True)
    class Meta:
        model = MeetingParticipant
        fields = (
            "id",
            "meeting",
            "participant",
            "attendence_in_person",
            "online_voting",
            "meeting_attendence"
       
        )

class VotingCircleSerializer(serializers.ModelSerializer):
    meeting = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = MeetingVotingCircle
        fields = (
            "id",
            "meeting",
            "participant_name",
            "email",
            "manageby",
            "manageby_id"
       
        )
#create custom serializer for meeting.
class MeetingScheduleSerializer(serializers.ModelSerializer):
    meeting_agendas = MeetingAgendaSerializer(many=True)
    meeting_participants = MeetingParticipantSerializer(many=True,read_only=True)
    meeting_votingcircles = VotingCircleSerializer(many=True)
    property = serializers.CharField(source='property.name', read_only=True)
    object = serializers.CharField(source='object.object_name', read_only=True)
    subgroup = serializers.CharField(source='subgroup.name', read_only=True)
    chairman = serializers.CharField(source='chairman.name', read_only=True)
    minute_taker = serializers.CharField(source='minute_taker.name', read_only=True)
    quorum = serializers.CharField(source='quorum.condition', read_only=True)

    class Meta:
        model = MeetingSchedule
        fields = (
            "id",
            "title",
            "venue",
            "property",
            "object",
            "subgroup",
            "chairman",
            "minute_taker",
            "meeting_date",
            "meeting_time",
            "date_defined",
            "visible_to_ownership_app",
            "submission_deadline",
            "dispatch_invitation",
            "online_voting",
            "attendance_in_person",
            "allow_power_of_attorney",
            "days_before_the_metting",
            "cover_picture_for_presenation",
            "association_information",
            "cover_picture_for_presenation",
            "information_for_current_meeting",
            "quorum",
            "meeting_agendas",
            "qr_code",
            "status",
            "meeting_participants",
           "meeting_votingcircles"
        )
    
    def create(self, data):
        print("validated_data",data)
        model = self.Meta.model
        agenda_details = data.pop('meeting_agendas', None)
        #participants_detail = data.pop('meeting_participants', None)
        votingcircle_detail = data.pop('meeting_votingcircles', None)
        print("validateddata",data)
        dates = self.context.get('request').data
        meeting_date = dates.pop('meeting_date',None)
        instance = model.objects.create(**data)

        agenda_list = []
        for agenda in agenda_details:
            agenda.pop("meeting", None)
            agenda_list.append(MeetingAgenda(meeting=instance, **agenda))

        bulk_agendas_details = MeetingAgenda.objects.bulk_create(agenda_list)
        print("bulk_agendas_details ", bulk_agendas_details)

        voting_list = []
        for voting in votingcircle_detail:
            voting.pop("meeting", None)
            voting_list.append(MeetingVotingCircle(meeting=instance, **voting))

        bulk_voting_details = MeetingVotingCircle.objects.bulk_create(voting_list)
        participant_list=[]
        if bulk_voting_details:
            for votes in bulk_voting_details:
                votes.save()
                participant_list.append(MeetingParticipant(meeting=instance,participant=votes))
            bulk_participants_details = MeetingParticipant.objects.bulk_create(participant_list)
        print("bulk_voting_details ", bulk_voting_details)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(instance.id)
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image_path = f'qr_code/{instance.id}.png'
        qr_image.save(settings.MEDIA_ROOT / qr_image_path)

        instance.qr_code = qr_image_path
        instance.meeting_date = meeting_date
        instance.save()
        return instance
    
    def update(self, instance,validated_data):
        model = self.Meta.model
        data = self.context.get('request').data

        agenda_details = data.pop('meeting_agendas', None)
        votingcircle_detail = data.pop('meeting_votingcircles', None)
        agenda_detailss = validated_data.pop('meeting_agendas', None)
        votingcircle_details = validated_data.pop('meeting_votingcircles', None)
        meeting_date = data.pop('meeting_date',None)
        # update the parent model.
        super(self.__class__, self).update(instance, validated_data)
        # update the related child model.
        agenda_list=[]
        for agenda in agenda_details:
            print("agenda",agenda)
            if "id" in agenda.keys():
                agenda_id = agenda["id"]
                agenda_obj = MeetingAgenda.objects.filter(id=agenda_id)
                print("agenda_obj",agenda_obj)
                if agenda_obj.exists():
                    agenda_data = agenda_obj.update(**agenda)
                    agenda_list.append(agenda_id)
                else:
                    continue
            else:
                print("flow is in else condition")
                agenda.pop("meeting", None)
                agenda_data = MeetingAgenda.objects.create(**agenda, meeting=instance)
                agenda_list.append(agenda_data.id)
        print("flow is here correctly")
        for agenda in instance.meeting_agendas.all():
                if agenda.id not in agenda_list:
                    agenda.delete()

        voting_list = []
        for voting in votingcircle_detail:
            if "id" in voting.keys():
                voting_id=voting["id"]
                voting_obj = MeetingVotingCircle.objects.filter(id=voting_id)
                if voting_obj.exists():
                    voting_data = voting_obj.update(**voting)
                    voting_list.append(voting_id)
                else:
                    continue
            else:
                voting.pop("meeting", None)
                voting_data = MeetingVotingCircle.objects.create(**voting, meeting=instance)
                voting_list.append(voting_data.id)

        for voting in instance.meeting_votingcircles.all():
                if voting.id not in voting_list:
                    voting.delete()
		 
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(instance.id)
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image_path = f'qr_code/{instance.id}.png'
        qr_image.save(settings.MEDIA_ROOT / qr_image_path)

        instance.qr_code = qr_image_path
        instance.meeting_date = meeting_date
        instance.save()
        return instance
