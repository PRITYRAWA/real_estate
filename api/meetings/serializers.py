from rest_framework import serializers
from meetings.models import *

class MeetingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingSchedule
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')
