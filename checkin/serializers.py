# serializers.py
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

# class UserSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = CustomUser
#         fields = ['id','email', 'password', 'confirm_password']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }

#     def validate(self, attrs):
#         if attrs['password'] != attrs['confirm_password']:
#             raise serializers.ValidationError({'confirm_password': 'Passwords do not match.'})

#         try:
#             validate_password(attrs['password'], self.instance)
#         except ValidationError as e:
#             raise serializers.ValidationError({'password': e.messages})

#         return attrs

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user

# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(write_only=True, required=True)

#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')

#         if email and password:
#             user = authenticate(email=email, password=password)
#             if user:
#                 if not user.is_active:
#                     raise serializers.ValidationError('User account is disabled.')
#                 attrs['user'] = user
#             else:
#                 raise serializers.ValidationError('Unable to login with provided credentials.')
#         else:
#             raise serializers.ValidationError('Must include "email" and "password".')
        
#         return attrs


class GeneralInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInspection
        fields = '__all__'

class ObjectListInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectListInspection
        fields = '__all__'

class CheckInOutSerializer(serializers.ModelSerializer):
    general_inspection = GeneralInspectionSerializer()
    object_list_inspection = ObjectListInspectionSerializer()

    class Meta:
        model = CheckInOut
        fields = ('id', 'user', 'service_ticket_number', 'object_check_in', 'check_in_date', 'check_in_time',
                  'check_out_date', 'check_out_time', 'inspection_date_time', 'object_details', 'object_detail_list','general_inspection','object_list_inspection')

    def create(self, validated_data):
        general_inspection_data = validated_data.pop('general_inspection', None)
        object_list_inspection_data = validated_data.pop('object_list_inspection', None)

        checkinout = CheckInOut.objects.create(**validated_data)

        if general_inspection_data:
            GeneralInspection.objects.create(service_id=checkinout, **general_inspection_data)

        if object_list_inspection_data:
            ObjectListInspection.objects.create(service_id=checkinout, **object_list_inspection_data)

        return checkinout
