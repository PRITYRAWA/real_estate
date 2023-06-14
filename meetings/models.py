from django.db import models
from foundation.models import BaseModel

class MeetingSchedule(BaseModel):
    title = models.CharField(max_length=100, blank=False, null=False)
    venue = models.TextField(blank=True, null=True)
    # property = models.ForeignKey(Realestateproperties,related_name="property",on_delete=models.CASCADE)
    # subgroup = models.ForeignKey(Realestatepropertiessubgroup,related_name="subgroup",on_delete=models.CASCADE)
    # chairman = models.ForeignKey(Realestatepropertyowner,related_name="chairman",on_delete=models.CASCADE)
    # mintue_taker = models.ForeignKey(Realestatepropertyowner,related_name="mintue_taker",on_delete=models.CASCADE)
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
    # quorum = models.ForeignKey(Quorums,related_name="quorum",on_delete=models.CASCADE)
    # votes= models.ForeignKey(Votes,related_name="votes",on_delete=models.CASCADE)

    class Meta:
        db_table = 'MeetingSchedule'
