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

class CheckInOutSerializer(serializers.ModelSerializer):
    # general_inspection = GeneralInspectionSerializer()
    # general_inspection = GeneralInspectionSerializer()
    object_list_inspection = ObjectListInspectionSerializer()

    class Meta:
        model = CheckInOut
        fields = ('id', 'user', 'service_ticket_number', 'object_check_in', 'check_in_date', 'check_in_time',
                  'check_out_date', 'check_out_time', 'inspection_date_time', 'object_list_inspection','object_details','object_detail_list')

    def create(self, validated_data):
        # general_inspection_data = validated_data.pop('general_inspection', None)
        object_list_inspection_data = validated_data.pop('object_detail_list', None)
        # general_inspection_data = validated_data.pop('general_inspection', None)
        # object_list_inspection_data = validated_data.pop('object_detail_list', None)

        checkinout = CheckInOut.objects.create(**validated_data)

        # if general_inspection_data:
        #     GeneralInspection.objects.create(service_id=checkinout, **general_inspection_data)
        # if general_inspection_data:
        #     GeneralInspection.objects.create(service_id=checkinout, **general_inspection_data)

        if object_list_inspection_data:
            ObjectListInspection.objects.create(service_id=checkinout, **object_list_inspection_data)

        return checkinout
