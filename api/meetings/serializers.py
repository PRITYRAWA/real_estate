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

class GetMeetingSubAgendasSerializer(serializers.ModelSerializer):

    meeting_agenda = serializers.CharField(read_only=True, source="meeting_agenda.topic")
    submitter = serializers.CharField(read_only=True, source="submitter.manager_name")

    class Meta:
        model = MeetingSubAgendaDetails
        fields = (
            "id",
            "meeting_agenda",
            "sub_item",
            "description",
            "notes_to_mintue",
            "submitter"
        )

class GetMeetingAgendaSerializer(serializers.ModelSerializer):
    meeting = serializers.PrimaryKeyRelatedField(read_only=True, source="meeting.title")
    meetingagenda_detail = GetMeetingSubAgendasSerializer(many=True)

    class Meta:
        model = MeetingAgenda
        fields = (
            "id",
            "meeting",
            "topic",
            "status",
            "meetingagenda_detail"
       
        )
    
class MeetingParticipantSerializer(serializers.ModelSerializer):
    meeting = serializers.PrimaryKeyRelatedField(read_only=True,source="meeting.title")
    class Meta:
        model = MeetingParticipant
        fields = (
            "id",
            "meeting",
            "participant",
            "participant_email",
            "attendence_in_person",
            "online_voting",
            "meeting_attendence",
            "voting_attendence",
            "power_of_attroney",
            "attroney_attchment",
            "verified_attroney",
            "power_of_attroney_name",
            "apartment"
       
        )


class MeetingParticipantAgendaSerializer(serializers.ModelSerializer):
    meeting_participant = serializers.PrimaryKeyRelatedField(read_only=True,source="meeting_participant.meeting.title")
    
    class Meta:
        model = MeetingParticipantAgenda
        fields = (
            "id",
            "meeting_participant",
            "participant_email",
            "owner_name",
            "apartment_name",
            "title",
            "voting_ques",
            "explaination",
            "attachment"
        )

    def create(self, data):
        params=self.context.get('request')
        email =params['email']
        meetid=params['meetid']
        user_obj= MeetingParticipant.objects.get(meeting=meetid,participant_email=email)
        instance = MeetingParticipantAgenda.objects.create(meeting_participant=user_obj,**data)
        instance.save()
        return instance

class GetMeetingParticipantSerializer(serializers.ModelSerializer):
    meeting = serializers.PrimaryKeyRelatedField(read_only=True,source="meeting.title")
    participant = serializers.PrimaryKeyRelatedField(read_only=True,source="participant.participant_name")
    class Meta:
        model = MeetingParticipant
        fields = (
            "id",
            "meeting",
            "participant",
            "participant_email",
            "attendence_in_person",
            "online_voting",
            "meeting_attendence",
            "voting_attendence",
            "power_of_attroney",
            "attroney_attchment",
            "verified_attroney",
            "power_of_attroney_name",
            "apartment"
       
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
            "manageby_id",
            "category"
       
        )

class GetVotingCircleSerializer(serializers.ModelSerializer):
    meeting = serializers.PrimaryKeyRelatedField(read_only=True,source="meeting.title")
    
    class Meta:
        model = MeetingVotingCircle
        fields = (
            "id",
            "meeting",
            "participant_name",
            "email",
            "manageby",
            "manageby_id",
            "category"
       
        )

class MeetingVotesSerializer(serializers.ModelSerializer):
    meeting_quorums = serializers.SerializerMethodField()

    def get_meeting_quorums(self, obj):
        result = MeetingQuorums.objects.filter(id=obj.id)
        return result.data
    
    class Meta:
        model = MeetingVotes
        fields = (
            "id",
            "meeting_quorums",
            "tabs",
            "voting_type",
            "majority",
            "condition",
            "basic_set",
            "tie_case"
        )


class GetMeetingVotesSerializer(serializers.ModelSerializer):
    meeting_quorums = serializers.CharField(read_only=True, source="meeting_quorums.meeting.title")
    
    class Meta:
        model = MeetingVotes
        fields = (
            "id",
            "tabs",
            "voting_type",
            "meeting_quorums",
            "majority",
            "condition",
            "basic_set",
            "tie_case"
        )

class GetMeetingQuorumsSerializer(serializers.ModelSerializer):
    meeting = serializers.CharField(read_only=True, source="meeting.title")
    # meeting_votes = serializers.SerializerMethodField()
    meeting_votes = GetMeetingVotesSerializer(many=True)

    # def get_meeting_votes(self, obj):
    #     result = MeetingVotesSerializer(MeetingVotes.objects.filter(meeting_quorums=obj.id), many=True)
    #     return result.data
    
    class Meta:
        model = MeetingQuorums
        fields = (
            "id",
            "meeting",
            "voting_type",
            "present_votes",
            "condition",
            "meeting_votes"
       
        )

class CreateMeetingVotesSerializer(serializers.ModelSerializer):
    meeting_quorums = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = MeetingVotes
        fields = (
            "id",
            "meeting_quorums",
            "tabs",
            "voting_type",
            "majority",
            "condition",
            "basic_set",
            "tie_case"
        )

class CreateMeetingSubAgendaSerializer(serializers.ModelSerializer):
    meeting_agenda = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = MeetingSubAgendaDetails
        fields = (
            "id",
            "meeting_agenda",
            "sub_item",
            "description",
            "notes_to_mintue",
            "submitter"
        )

class CreateMeetingQuorumsSerializer(serializers.ModelSerializer):
    meeting_votes = CreateMeetingVotesSerializer(many=True)
    meeting = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = MeetingQuorums
        fields = (
            "id",
            "meeting",
            "voting_type",
            "present_votes",
            "condition",
            "meeting_votes"
        )

class CreateMeetingAgendaSerializer(serializers.ModelSerializer):
    meetingagenda_detail = CreateMeetingSubAgendaSerializer(many=True)
    meeting = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = MeetingAgenda
        fields = (
            "id",
            "meeting",
            "topic",
            "status",
            "meetingagenda_detail"
       
        )
#create custom serializer for meeting.
class MeetingScheduleSerializer(serializers.ModelSerializer):
    meeting_agendas = CreateMeetingAgendaSerializer(many=True)
    meeting_participants = MeetingParticipantSerializer(many=True,read_only=True)
    meeting_votingcircles = VotingCircleSerializer(many=True)
    meeting_quorums = CreateMeetingQuorumsSerializer(many=True)

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
            "meeting_agendas",
            "qr_code",
            "status",
            "meeting_participants",
           "meeting_votingcircles",
           "meeting_quorums"
        )
    
    def create(self, data):
        model = self.Meta.model
        agenda_details = data.pop('meeting_agendas', None)
        votingcircle_detail = data.pop('meeting_votingcircles', None)
        meeting_quorums = data.pop('meeting_quorums', None)
        meeting_votes = data.pop('meeting_votes', None)
        dates = self.context.get('request').data
        meeting_date = dates.pop('meeting_date',None)
        meeting_time = dates.pop('meeting_time',None)
        instance = model.objects.create(**data)

        agenda_list = []
        for agenda in agenda_details:
            #agenda.pop("meeting", None)
            sub_agendas= agenda.pop("meetingagenda_detail", None)
            agenda_list.append(MeetingAgenda(meeting=instance, **agenda))

        bulk_agendas_details = MeetingAgenda.objects.bulk_create(agenda_list)
        print("bulk_agendas_details ", bulk_agendas_details)
        subagendas_list=[]
        if bulk_agendas_details:
            for subagenda in bulk_agendas_details:
                subagenda.save()
                for aub_agenda in sub_agendas:
                    subagendas_list.append(MeetingSubAgendaDetails(meeting_agenda=subagenda, **aub_agenda))    
                bulk_subagendas_details = MeetingSubAgendaDetails.objects.bulk_create(subagendas_list)    

        voting_list = []
        for voting in votingcircle_detail:
            voting.pop("meeting", None)
            voting_list.append(MeetingVotingCircle(meeting=instance, **voting))

        bulk_voting_details = MeetingVotingCircle.objects.bulk_create(voting_list)
        participant_list=[]
        if bulk_voting_details:
            for votes in bulk_voting_details:
                votes.save()
                participant_list.append(MeetingParticipant(meeting=instance,participant=votes,participant_email=votes.email))
            bulk_participants_details = MeetingParticipant.objects.bulk_create(participant_list)
        print("bulk_voting_details ", bulk_voting_details)
        quorums_list=[]
        if meeting_quorums:
            for quorums in meeting_quorums:
                print("quorms",quorums)
                meeting_votes= quorums.pop("meeting_votes", None)
                quorums_list.append(MeetingQuorums(meeting=instance, **quorums))    
            bulk_quorums_details = MeetingQuorums.objects.bulk_create(quorums_list)
            meeting_votes_list=[]
            if bulk_quorums_details:
                for quorums in bulk_quorums_details:
                    quorums.save()
                    for quorum_votes in meeting_votes:
                        meeting_votes_list.append(MeetingVotes(meeting_quorums=quorums, **quorum_votes))    
                    bulk_votes_details = MeetingVotes.objects.bulk_create(meeting_votes_list)       


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
        instance.meeting_time = meeting_time
        instance.save()
        return instance
    
    def update(self, instance,validated_data):
        model = self.Meta.model
        data = self.context.get('request').data
        agenda_details = data.pop('meeting_agendas', None)
        votingcircle_detail = data.pop('meeting_votingcircles', None)
        quorums_detail = data.pop('meeting_quorums', None)
        agenda_detailss = validated_data.pop('meeting_agendas', None)
        votingcircle_details = validated_data.pop('meeting_votingcircles', None)
        quorums_details = validated_data.pop('meeting_quorums', None)
        meeting_date = data.pop('meeting_date',None)
        meeting_time = data.pop('meeting_time',None)
        # update the parent model.
        print("update method before")
        super(self.__class__, self).update(instance, validated_data)
        print("update method after")
       
        # update the related meeting agendas and sub agendas model.
        agenda_list=[]
        detail_list=[]
        for agenda in agenda_details:
            print("agenda",agenda)
            magenda_details= agenda.pop('meetingagenda_detail',None)
            if "id" in agenda.keys():
                agenda_id = agenda["id"]
                agenda_obj = MeetingAgenda.objects.filter(id=agenda_id)
                print("agenda_obj",agenda_obj)
                if agenda_obj.exists():
                    agenda_data = agenda_obj.update(**agenda)
                    agenda_list.append(agenda_id)
                else:
                    continue
                for detail in magenda_details:
                    if "id" in detail.keys():
                        detail_id = detail["id"]
                        detail_obj = MeetingSubAgendaDetails.objects.filter(id=detail_id)
                        print("detail_obj",detail_obj)
                        if detail_obj.exists():
                            detail_data = detail_obj.update(**detail)
                            detail_list.append(detail_id)
                        else:
                            continue
                    else:
                        print("flow is in else agendacondition")
                        agenda_id = MeetingAgenda.objects.get(id=agenda_id)
                        submitter = detail.pop('submitter',None)
                        submiiter_id= Realestatepropertymanagement.objects.get(id=submitter)
                        detail_data = MeetingSubAgendaDetails.objects.create(**detail,submitter=submiiter_id, meeting_agenda=agenda_id)
                        detail_list.append(detail_data.id)
                for mdetails in instance.meeting_agendas.all():
                    for meet_details in mdetails.meetingagenda_detail.all():
                        if meet_details.id not in detail_list:
                            print("delete floe")
                            meet_details.delete()
            else:
                print("flow is in else condition")
                agenda_data = MeetingAgenda.objects.create(**agenda, meeting=instance)
                agenda_list.append(agenda_data.id)
        print("flow is here correctly")
        for agenda in instance.meeting_agendas.all():
                if agenda.id not in agenda_list:
                    agenda.delete()

        # update the related meeting quroms and their voting model.
        quoroms_list=[]
        meetingvotes_list=[]
        for quorums in quorums_detail:
            print("quorums",quorums)
            votes_details= quorums.pop('meeting_votes',None)
            if "id" in quorums.keys():
                quorums_id = quorums["id"]
                quorums_obj = MeetingQuorums.objects.filter(id=quorums_id)
                print("quorums_obj",quorums_obj)
                if quorums_obj.exists():
                    quorums_data = quorums_obj.update(**quorums)
                    quoroms_list.append(quorums_id)
                else:
                    continue
                for vdetail in votes_details:
                    if "id" in vdetail.keys():
                        vdetail_id = vdetail["id"]
                        vdetail_obj = MeetingVotes.objects.filter(id=vdetail_id)
                        print("vdetail_obj",vdetail_obj)
                        if vdetail_obj.exists():
                            vdetail_data = vdetail_obj.update(**vdetail)
                            meetingvotes_list.append(vdetail_id)
                        else:
                            continue
                    else:
                        print("flow is in else quromscondition")
                        quorom_id = MeetingQuorums.objects.get(id=quorums_id)
                        vdetail_data = MeetingVotes.objects.create(**vdetail,meeting_quorums=quorom_id)
                        meetingvotes_list.append(vdetail_data.id)
                for mvdetails in instance.meeting_quorums.all():
                    for vmmeet_details in mvdetails.meeting_votes.all():
                        if vmmeet_details.id not in meetingvotes_list:
                            print("delete floe quorums")
                            vmmeet_details.delete()
            else:
                continue
        print("flow is here correctly")
        for mquorms in instance.meeting_quorums.all():
                if mquorms.id not in quoroms_list:
                    mquorms.delete()

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
        instance.meeting_time = meeting_time
        instance.save()
        return instance


#create custom serializer for meeting.
class GetMeetingScheduleSerializer(serializers.ModelSerializer):
    meeting_agendas = GetMeetingAgendaSerializer(many=True)
    meeting_participants = GetMeetingParticipantSerializer(many=True)
    meeting_votingcircles = GetVotingCircleSerializer(many=True)
    meeting_quorums = GetMeetingQuorumsSerializer(many=True)
    property = serializers.CharField(read_only=True, source="property.name")
    chairman = serializers.CharField(read_only=True, source="chairman.name")
    minute_taker = serializers.CharField(read_only=True, source="minute_taker.name")
    object = serializers.CharField(read_only=True, source="object.name")
    subgroup = serializers.CharField(read_only=True, source="subgroup.name")

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
            "meeting_agendas",
            "qr_code",
            "status",
            "meeting_participants",
           "meeting_votingcircles",
           "meeting_quorums"
        )
    
    
    
    
