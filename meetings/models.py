from django.db import models
from foundation.models import BaseModel
from masters.models import *

class MeetingSchedule(BaseModel):
    status = (
        ("finished", ("Finished")),
        ("pending", ("Pending")),
        ("live", ("Live")),
      
    )
    title = models.CharField(max_length=100, blank=False, null=False)
    venue = models.TextField(blank=True, null=True)
    property = models.ForeignKey(Realestateproperties,related_name="properties",on_delete=models.PROTECT)
    object = models.ForeignKey(Realestateobjects,related_name="property_objects",on_delete=models.PROTECT)
    subgroup = models.ForeignKey(Realestatepropertiessubgroup,related_name="subgroups",on_delete=models.PROTECT)
    chairman = models.ForeignKey(Realestatepropertyowner,related_name="chairmans",on_delete=models.PROTECT)
    minute_taker = models.ForeignKey(Realestateagents,related_name="mintue_takers",on_delete=models.PROTECT)
    meeting_date = models.DateField(auto_now_add=True)
    meeting_time=models.TimeField(auto_now_add=True)
    date_defined =models.BooleanField(default=False)
    visible_to_ownership_app=models.BooleanField(default=False)
    submission_deadline =models.BooleanField(default=False)
    dispatch_invitation=models.BooleanField(default=False)
    online_voting = models.BooleanField(default=False)
    attendance_in_person= models.BooleanField(default=False)
    allow_power_of_attorney=models.BooleanField(default=False)
    days_before_the_metting=models.CharField(max_length=20, blank=True, null=True)
    cover_picture_for_presenation=models.FileField(upload_to="images", null=True, blank=True)
    association_information=models.TextField(null=True, blank=True)
    information_for_current_meeting=models.TextField(null=True, blank=True)
    quorum = models.ForeignKey(Quorums,related_name="quorums",on_delete=models.PROTECT)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    status = models.TextField(max_length=50,choices= status,default='pending')
    subassociation= models.CharField(max_length=100, blank=True, null=True)
    #voting_circle = models.ForeignKey(Realestatepropertyowner,related_name="voting_circles",on_delete=models.CASCADE)

    class Meta:
        db_table = 'MeetingSchedule'
    
    def __str__(self):
        return str(self.title)

class MeetingAgenda(BaseModel):
    status = (
        ("draft", ("Draft")),
        ("definitive", ("Definitive")),
      
    )
    meeting = models.ForeignKey(MeetingSchedule,related_name="meeting_agendas",on_delete=models.PROTECT)
    topic = models.CharField(max_length=100, blank=False, null=False)
    status = models.TextField(max_length=20,choices= status,default='draft')
    
    class Meta:
        db_table = 'MeetingAgenda'
    
    def __str__(self):
        return str(self.topic)

class MeetingVotingCircle(BaseModel):

    meeting = models.ForeignKey(MeetingSchedule,related_name="meeting_votingcircles",on_delete=models.PROTECT)
    participant_name=models.CharField(max_length=100, blank=False, null=False)
    email=models.CharField(max_length=100, blank=False, null=False)
    manageby = models.CharField(max_length=30,null=True,blank=True,verbose_name="Manage By")
    manageby_id = models.CharField(max_length=30,null=True,blank=True,verbose_name="Manager Id")

    class Meta:
        db_table = 'MeetingVotingCircle'
    
    def __str__(self):
        return str(self.participant_name)

        
class MeetingParticipant(BaseModel):
    meeting = models.ForeignKey(MeetingSchedule,related_name="meeting_participants",on_delete=models.PROTECT)
    participant=models.ForeignKey(MeetingVotingCircle,related_name="participants",on_delete=models.PROTECT)
    attendence_in_person= models.BooleanField(default=False)
    online_voting= models.BooleanField(default=False)
    meeting_attendence= models.BooleanField(default=False)
    voting_attendence= models.BooleanField(default=False)
    power_of_attroney= models.BooleanField(default=False)
    attroney_attchment = models.FileField(upload_to="attachment", null=True, blank=True)
    verified_attroney= models.BooleanField(default=False)


    class Meta:
        db_table = 'MeetingParticipant'
    
    def __str__(self):
        return str(self.participant.participant_name)
