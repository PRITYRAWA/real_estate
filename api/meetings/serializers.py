from rest_framework import serializers
from meetings.models import *

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
    #meeting_participants = MeetingParticipantSerializer(many=True)
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
            #"meeting_participants",
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

        # participant_list = []
        # for participant in participants_detail:
        #     participant.pop("meeting", None)
        #     participant_list.append(MeetingParticipant(meeting=instance, **participant))

        # bulk_participants_details = MeetingParticipant.objects.bulk_create(participant_list)
        # print("bulk_participants_details ", bulk_participants_details)

        voting_list = []
        for voting in votingcircle_detail:
            voting.pop("meeting", None)
            voting_list.append(MeetingVotingCircle(meeting=instance, **voting))

        bulk_voting_details = MeetingVotingCircle.objects.bulk_create(voting_list)
        print("bulk_voting_details ", bulk_voting_details)

        instance.save()
        return instance