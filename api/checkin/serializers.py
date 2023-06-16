# serializers.py
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from checkin.models import *
from django.contrib.auth import authenticate


class GeneralInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInspection
        fields = '__all__'

class ObjectListInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectListInspection
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('full_name',)

class CheckInOutSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = CheckInOut
        fields = ('id', 'user', 'service_ticket_number', 'object_check_in', 'check_in_date', 'check_in_time',
                  'check_out_date', 'check_out_time', 'inspection_date_time')

