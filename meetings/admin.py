from django.contrib import admin
from meetings.models import *


# creating parent child model for agenda
class MeetingAgendasInline(admin.TabularInline):
    model = MeetingAgenda
    extra = 1

class MeetingParticipantsInline(admin.TabularInline):
    model = MeetingParticipant
    extra = 1

@admin.register(MeetingSchedule)
class CustomAgenda(admin.ModelAdmin):
    
    inlines = [
        MeetingAgendasInline,MeetingParticipantsInline
    ]

