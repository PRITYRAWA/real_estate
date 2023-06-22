from rest_framework import serializers
from meetings.models import *
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
       
        )

class MeetingScheduleSerializer(serializers.ModelSerializer):
    meeting_agendas = MeetingAgendaSerializer(many=True)
    meeting_participants = MeetingParticipantSerializer(many=True,read_only=True)
    meeting_votingcircles = VotingCircleSerializer(many=True)

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
            "mintue_taker",
            "meeting_date",
            "meeting_time",
            "date_defined",
            "visible_to_ownership_app",
            "submission_deadline",
            "dispatch_invitaion",
            "online_voting",
            "attendence_in_person",
            "allow_power_of_attorney",
            "days_before_the_metting",
            "cover_picture_for_presenation",
            "association_information",
            "cover_picture_for_presenation",
            "information_for_current_meeting",
            "quorum",
            "meeting_agendas",
            "qr_code",
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
                participant_list.append(MeetingParticipant(meeting=instance,participant=votes))
            bulk_participants_details = MeetingParticipant.objects.bulk_create(participant_list)
        print("bulk_voting_details ", bulk_voting_details)
        print("bulk_participants_details ", bulk_participants_details)

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
        instance.save()
        return instance