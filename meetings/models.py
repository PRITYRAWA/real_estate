from django.db import models
from foundation.models import BaseModel
from masters.models import *

class MeetingSchedule(BaseModel):
    title = models.CharField(max_length=100, blank=False, null=False)
    venue = models.TextField(blank=True, null=True)
    property = models.ForeignKey(Realestateproperties,related_name="properties",on_delete=models.CASCADE)
    object = models.ForeignKey(Realestateobjects,related_name="property_objects",on_delete=models.CASCADE)
    subgroup = models.ForeignKey(Realestatepropertiessubgroup,related_name="subgroups",on_delete=models.CASCADE)
    chairman = models.ForeignKey(Realestatepropertyowner,related_name="chairmans",on_delete=models.CASCADE)
    mintue_taker = models.ForeignKey(Realestateagents,related_name="mintue_takers",on_delete=models.CASCADE)
    meeting_date = models.DateField(auto_now_add=True)
    meeting_time=models.TimeField(auto_now_add=True)
    date_defined =models.BooleanField(default=False)
    visible_to_ownership_app=models.BooleanField(default=False)
    submission_deadline =models.BooleanField(default=False)
    dispatch_invitaion=models.BooleanField(default=False)
    online_voting = models.BooleanField(default=False)
    attendence_in_person= models.BooleanField(default=False)
    allow_power_of_attorney=models.BooleanField(default=False)
    days_before_the_metting=models.CharField(max_length=20, blank=True, null=True)
    cover_picture_for_presenation=models.FileField(upload_to="images", null=True, blank=True)
    association_information=models.TextField(null=True, blank=True)
    information_for_current_meeting=models.TextField(null=True, blank=True)
    quorum = models.ForeignKey(Quorums,related_name="quorums",on_delete=models.CASCADE)
    #voting_circle = models.ForeignKey(Realestatepropertyowner,related_name="voting_circles",on_delete=models.CASCADE)

    class Meta:
        db_table = 'MeetingSchedule'

class MeetingAgenda(BaseModel):
    status = (
        ("draft", ("Draft")),
        ("definitive", ("Definitive")),
      
    )
    meeting = models.ForeignKey(MeetingSchedule,related_name="meeting_agendas",on_delete=models.CASCADE)
    topic = models.CharField(max_length=100, blank=False, null=False)
    status = models.TextField(max_length=20,choices= status,default='draft')
    
    class Meta:
        db_table = 'MeetingAgenda'

class MeetingVotingCircle(BaseModel):

    meeting = models.ForeignKey(MeetingSchedule,related_name="meeting_votingcircles",on_delete=models.CASCADE)
    participant_name=models.CharField(max_length=100, blank=False, null=False)
    email=models.CharField(max_length=100, blank=False, null=False)
    class Meta:
        db_table = 'MeetingVotingCircle'

        
class MeetingParticipant(BaseModel):

    meeting = models.ForeignKey(MeetingSchedule,related_name="meeting_participants",on_delete=models.CASCADE)
    participant=models.ForeignKey(MeetingVotingCircle,related_name="participants",on_delete=models.CASCADE)
    attendence_in_person= models.BooleanField(default=False)
    online_voting= models.BooleanField(default=False)

    class Meta:
        db_table = 'MeetingParticipant'
