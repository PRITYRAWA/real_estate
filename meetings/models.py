from django.db import models
from foundation.models import BaseModel
from masters.models import *


class MeetingSchedule(BaseModel):
    status = (
        ("finished", ("Finished")),
        ("pending", ("Pending")),
        ("live", ("Live")),
    )
    title = models.CharField(max_length=50, blank=False, null=False)
    venue = models.CharField(max_length=100, blank=True, null=True)
    property = models.ForeignKey(
        Realestateproperties, related_name="properties", on_delete=models.PROTECT
    )
    object = models.ForeignKey(
        Realestateobjects, related_name="property_objects", on_delete=models.PROTECT,null=True,blank=True
    )
    subgroup = models.ForeignKey(
        Realestateproperties,
        related_name="subgroups",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )
    chairman = models.ForeignKey(
        Realestatepropertymanagement, related_name="chairmans", on_delete=models.PROTECT
    )
    minute_taker = models.ForeignKey(
        Realestatepropertymanagement,
        related_name="mintue_takers",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    meeting_date = models.DateField(auto_now_add=True)
    meeting_time=models.TimeField(auto_now_add=False,null=True,blank=True)
    date_defined =models.BooleanField(default=False)
    visible_to_ownership_app=models.BooleanField(default=False)
    submission_deadline =models.DateField(auto_now_add=False, null=True,blank=True)
    dispatch_invitation=models.DateField(auto_now_add=False, null=True,blank=True)
    online_voting = models.BooleanField(default=False)
    attendance_in_person= models.BooleanField(default=False)
    allow_power_of_attorney=models.BooleanField(default=False)
    days_before_the_metting=models.CharField(max_length=20, blank=True, null=True)
    cover_picture_for_presenation=models.FileField(upload_to="images", null=True, blank=True)
    association_information=models.TextField(null=True, blank=True)
    information_for_current_meeting=models.TextField(null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    status = models.TextField(max_length=50,choices= status,default='pending')
    subassociation= models.CharField(max_length=100, blank=True, null=True)
    meet_start_time=models.TimeField(auto_now_add=False,null=True,blank=True)
    meet_end_time=models.TimeField(auto_now_add=False,null=True,blank=True)
    meeting_protocol=models.FileField(upload_to="images", null=True, blank=True)

    class Meta:
        db_table = "MeetingSchedule"

    def __str__(self):
        return str(self.title)


class MeetingAgenda(BaseModel):
    status = (
        ("draft", ("Draft")),
        ("definitive", ("Definitive")),
    )
    meeting = models.ForeignKey(
        MeetingSchedule, related_name="meeting_agendas", on_delete=models.CASCADE
    )
    topic = models.CharField(max_length=100, blank=False, null=False)
    status = models.TextField(max_length=20, choices=status, default="draft")

    class Meta:
        db_table = "MeetingAgenda"
        constraints = [
            models.UniqueConstraint(fields=["meeting", "topic"], name="meetingtopic")
        ]

    def __str__(self):
        return str(self.topic)


class MeetingSubAgendaDetails(BaseModel):
    meeting_agenda = models.ForeignKey(
        MeetingAgenda,
        blank=True,
        null=True,
        related_name="meetingagenda_detail",
        on_delete=models.CASCADE,
        verbose_name=("Meeting Agenda"),
    )
    sub_item = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=("Sub Agenda")
    )
    description = models.TextField(blank=True, null=True, verbose_name=("Description"))
    notes_to_mintue = models.TextField(
        blank=True, null=True, verbose_name=("Notes To mintue")
    )
    submitter = models.ForeignKey(
        Realestatepropertymanagement,
        related_name="submitter",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=("Submitter"),
    )

    class Meta:
        db_table = "MeetingAgendaDetails"
        verbose_name = "MeetingAgenda Details"
        ordering = ["-id"]
        constraints = [
            models.UniqueConstraint(
                fields=["meeting_agenda", "sub_item"], name="agendasubitem"
            )
        ]


class MeetingVotingCircle(BaseModel):
    types = (
        ("main", ("Main")),
        ("subassociation", ("Sub Association")),
    )

    meeting = models.ForeignKey(
        MeetingSchedule, related_name="meeting_votingcircles", on_delete=models.CASCADE
    )
    participant_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    manageby = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="Manage By"
    )
    manageby_id = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="Manager Id"
    )
    object_count = models.IntegerField(default=1, verbose_name=("Object Count"))
    asset_value = models.FloatField(
        default=0.0, null=True, blank=True, verbose_name=("Asset Value")
    )
    category = models.CharField(
        max_length=20, choices=types, default="main", verbose_name=("Category")
    )

    class Meta:
        db_table = "MeetingVotingCircle"
        constraints = [
            models.UniqueConstraint(fields=["meeting", "email"], name="votingemail")
        ]

    def __str__(self):
        return str(self.participant_name)


class MeetingParticipant(BaseModel):
    meeting = models.ForeignKey(
        MeetingSchedule, related_name="meeting_participants", on_delete=models.CASCADE
    )
    participant = models.ForeignKey(
        MeetingVotingCircle, related_name="participants", on_delete=models.CASCADE
    )
    participant_email = models.EmailField(blank=True, null=True)
    object_count = models.IntegerField(default=1, verbose_name=("Object Count"))
    asset_value = models.FloatField(
        default=0.0, null=True, blank=True, verbose_name=("Asset Value")
    )
    attendance_in_person = models.BooleanField(default=False)
    online_voting = models.BooleanField(default=False)
    meeting_attendance = models.BooleanField(default=False)
    voting_attendance = models.BooleanField(default=False)
    power_of_attroney = models.BooleanField(default=False)
    attroney_attchment = models.FileField(upload_to="attachment", null=True, blank=True)
    verified_attroney = models.BooleanField(default=False)
    power_of_attroney_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=("Power of attroney Name")
    )
    apartment = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=("Apartment")
    )

    class Meta:
        db_table = "MeetingParticipant"

    def __str__(self):
        return str(self.participant.participant_name)


class ParticipantAgenda(BaseModel):
    participant = models.ForeignKey(
        MeetingParticipant, related_name="meet_participants", on_delete=models.CASCADE
    )
    agenda = models.ForeignKey(
        MeetingAgenda,
        related_name="meet_agendas",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    agenda_vote = models.BooleanField(null=True)


class MeetingParticipantAgenda(BaseModel):
    meeting_participant = models.ForeignKey(
        MeetingParticipant, related_name="meeting_participant", on_delete=models.CASCADE
    )
    participant_email = models.EmailField(blank=True, null=True)
    owner_name = models.CharField(
        max_length=30, blank=True, null=True, verbose_name=("Owner Name")
    )
    apartment_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=("Apartment Name")
    )
    title = models.CharField(max_length=100, blank=False, null=False)
    voting_ques = models.CharField(max_length=100, blank=False, null=False)
    explaination = models.CharField(max_length=100, blank=True, null=True)
    attachment = models.FileField(upload_to="attachement", null=True, blank=True)

    class Meta:
        db_table = "MeetingParticipantAgenda"
        verbose_name = "MeetingParticipant Agenda"
        ordering = ["-id"]


class MeetingQuorums(BaseModel):
    types = (
        ("head", ("Head Votes")),
        ("object", ("Object Votes")),
        ("value", ("Value Votes")),
    )
    condition = (
        ("greater than or equals to", (">=")),
        ("greater than", (">")),
    )
    meeting = models.ForeignKey(
        MeetingSchedule, related_name="meeting_quorums", on_delete=models.CASCADE
    )
    voting_type = models.CharField(
        max_length=20, choices=types, verbose_name=("Voting Type")
    )
    present_votes = models.IntegerField(
        blank=False, null=False, verbose_name=("Present Votes")
    )
    condition = models.CharField(
        max_length=30,
        choices=condition,
        blank=False,
        null=False,
        verbose_name=("Condition"),
    )

    class Meta:
        db_table = "MeetingQuorums"
        verbose_name = "Meeting Quorums"
        ordering = ["-id"]

        constraints = [
            models.UniqueConstraint(
                fields=["meeting", "voting_type"], name="meetingquorom"
            )
        ]


class MeetingVotes(BaseModel):
    types = (
        ("head", ("Head Votes")),
        ("object", ("Object Votes")),
        ("value", ("Value Votes")),
    )
    cases = (
        ("rejected", ("Rejected")),
        ("accepted", ("Accepted")),
    )
    sets = (
        ("representatives_owners", ("Presence/representatives Owner")),
        ("total_owner", ("Total owners")),
        (
            "voting_owners_without_abstentions",
            ("Only voting owners without abstentions"),
        ),
    )
    tabs = (
        ("simple", ("Simple Majority")),
        ("qualified", ("qualified Majority")),
        ("unanimous", ("Unanimous Vote Tab")),
    )
    condition = (
        ("greater than or equals to", (">=")),
        ("greater than", (">")),
    )
    meeting = models.ForeignKey(
        MeetingSchedule, related_name="meeting_votingcretriea", on_delete=models.CASCADE
    )
    # meeting_quorums = models.ForeignKey(MeetingQuorums,related_name="meeting_votes",on_delete=models.CASCADE,verbose_name=("Meeting Quorums"))
    tabs = models.CharField(
        max_length=50, choices=tabs, default="qualified", verbose_name=("Tabs")
    )
    voting_type = models.CharField(
        max_length=50, choices=types, verbose_name=("Voting Type")
    )
    majority = models.IntegerField(blank=False, null=False, verbose_name=("Majority"))
    condition = models.CharField(
        max_length=30,
        choices=condition,
        blank=False,
        null=False,
        verbose_name=("Condition"),
    )
    basic_set = models.CharField(
        max_length=50, choices=sets, verbose_name=("Basic Set")
    )
    tie_case = models.CharField(max_length=50, choices=cases, verbose_name=("Tie Case"))

    class Meta:
        db_table = "MeetingVotes"
        verbose_name = "Meeting Votes"
        ordering = ["-id"]
