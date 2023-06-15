from rest_framework import serializers
from meetings.models import *

class MeetingAgendaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeetingAgenda
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')


class MeetingScheduleSerializer(serializers.ModelSerializer):
    meeting_agendas = MeetingAgendaSerializer(many=True)
    class Meta:
        model = MeetingSchedule
        fields = (
            "id",
            "title",
            "venue",
            "property",
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
            "voting_circle",
            "meeting_agendas",
        )