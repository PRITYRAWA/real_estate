# serializers.py
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from checkin.models import *
from django.contrib.auth import authenticate
from api.masters.serializers import *

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
    user = serializers.PrimaryKeyRelatedField(queryset=Realestatepropertytenant.objects.all())
    user_name = serializers.SerializerMethodField()
    object_check_in = serializers.PrimaryKeyRelatedField(queryset=Realestateobjects.objects.all())
    property_check_in = serializers.SerializerMethodField()

    class Meta:
        model = CheckInOut
        fields = ('id', 'user', 'user_name', 'service_ticket_number', 'object_check_in',
                  'check_in_date', 'check_in_time', 'check_out_date', 'check_out_time', 'inspection_date_time','property_check_in')

    def get_user_name(self, obj):
        return obj.user.name

    def get_object_check_in(self, obj):
        return obj.object_check_in


    def get_property_check_in(self, obj):
        if obj.object_check_in and obj.object_check_in.realestatepropertyid:
            return obj.object_check_in.realestatepropertyid.id
        return None

    def create(self, validated_data):
        user = validated_data.pop('user')
        check_in_out = CheckInOut.objects.create(user=user, **validated_data)
        return check_in_out

class KeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestatekey
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')    
