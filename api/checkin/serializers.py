# serializers.py
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from checkin.models import *
from django.contrib.auth import authenticate
from api.masters.serializers import *
from reportlab.pdfgen import canvas
from django.conf import settings
import os
from masters.models import *

class GeneralInspectionSerializer(serializers.ModelSerializer):
    service_id = serializers.CharField(source = 'service_id.service_ticket_number', read_only=True)
    real_estate_object = serializers.CharField(source = 'real_estate_object.object_name', read_only=True)
    class Meta:
        model = GeneralInspection
        exclude = ('created_at', 'updated_at')

# class ChildDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Realestateobjectsdetail
#         fields = '__all__'
    # def get_child_details(self, obj):
    #     if self.context.get('exclude_child_details'):
    #         return []
    #     child_details = obj.child_details.all()
    #     serialized_child_details = self.__class__(child_details, many=True, context={'exclude_child_details': True}).data
    #     return serialized_child_details

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation.pop('child_details')  # Remove child_details from the main representation
    #     representation['child_details'] = self.get_child_details(instance)
    #     return representation

class ChildDetailSerializer(serializers.ModelSerializer):
    child_details = serializers.SerializerMethodField()
    checkin = serializers.CharField(source = 'checkin.object_name', read_only=True)
    object_detail_list = serializers.CharField(source = 'object_detail_list.object_name', read_only=True)
    related_object = serializers.CharField(source = 'related_object.object_name', read_only=True)
    related_detail = serializers.CharField(source = 'related_detail.object_name', read_only=True)
    

    class Meta:
        model = ObjectListInspection
        exclude = ('created_at', 'updated_at')

    def get_child_details(self, obj):
        if self.context.get('exclude_child_details'):
            return []
        child_details = obj.child_details.all()
        serialized_child_details = self.__class__(child_details, many=True, context={'exclude_child_details': True}).data
        return serialized_child_details
    
class ObjectListInspectionSerializer(serializers.ModelSerializer):
    child_details = ChildDetailSerializer(many=True, required=False)
    checkin = serializers.CharField(source='checkin.user.name', read_only=True)
    object_detail_list = serializers.CharField(source = 'object_detail_list.object_name', read_only=True)
    related_object = serializers.CharField(source = 'related_object.object_name', read_only=True)
    related_detail = serializers.CharField(source = 'related_detail.object_name', read_only=True)

    class Meta:
        model = ObjectListInspection
        exclude = ('created_at', 'updated_at')

    def create(self, validated_data):
        child_details_data = validated_data.pop('child_details', [])
        inspection = ObjectListInspection.objects.create(**validated_data)

        for child_detail_data in child_details_data:
            child_detail_data['related_detail'] = inspection
            ChildDetailSerializer().create(child_detail_data)

        return inspection
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation.pop('child_details')  # Remove child_details from the main representation
    #     representation['child_details'] = self.get_child_details(instance)
    #     return representation


    # def create(self, validated_data):
    #     object_id = self.context.get('object_id')
    #     if object_id is not None:
    #         validated_data['related_detail'] = object_id  
    #         inspection = ObjectListInspection.objects.create(**validated_data)
    #         return inspection
    #     else:
    #         raise serializers.ValidationError('object_id is missing.')
        
class CheckInOutSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Realestatepropertytenant.objects.all())
    user_name = serializers.SerializerMethodField()
    object_check_in = serializers.PrimaryKeyRelatedField(queryset=Realestateobjects.objects.all())
    property_check_in = serializers.SerializerMethodField()
    object_detail_list = serializers.CharField(source='object_detail_list.object_detail_list.object_name', read_only=True)
    # furniture_check_in = serializers.PrimaryKeyRelatedField(queryset=Realestateobjects.objects.all())

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

        # Update property status to 'OCCUPIED'
        property_check_in = validated_data.get('object_check_in', None)
        if property_check_in:
            property_id = property_check_in.id
            if property_id:
                property_instance = Realestateobjects.objects.get(id=property_id)
                property_instance.status = 'OCCUPIED'
                property_instance.save()

        return check_in_out
    
class KeysSerializer(serializers.ModelSerializer):
    checkin = serializers.CharField(source='checkin.user.name', read_only=True)
    obj = serializers.CharField(source='obj.name', read_only=True)
    class Meta:
        model = Realestatekey
        exclude = ('created_at', 'updated_at')

class MetersSerializer(serializers.ModelSerializer):
    checkin = serializers.CharField(source='checkin.user.name', read_only=True)
    obj = serializers.CharField(source='obj.object_name', read_only=True)
    class Meta:
        model = Realestatemeter
        exclude = ('created_at', 'updated_at')


class FurnitureInspectionSerializer(serializers.ModelSerializer):
    checkin = serializers.PrimaryKeyRelatedField(queryset=CheckInOut.objects.all())

    class Meta:
        model = FurnitureInspection
        exclude = ('created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    realestatemanageid = serializers.CharField(source='realestatemanageid.manager_name', read_only=True)
    checkin = serializers.CharField(source='checkin.user.name', read_only=True)
    class Meta:
        model = Checkincomments
        exclude = ('created_at', 'updated_at')

    # def generate_pdf(self, data):
    #     pdf_filename = f'furniture_inspection_{data["id"]}.pdf'
    #     pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)

    #     # Create the PDF document
    #     c = canvas.Canvas(pdf_path)
    #     c.drawString(100, 750, 'Furniture Inspection Details')
    #     c.drawString(100, 700, f'ID: {data["id"]}')
    #     c.drawString(100, 650, f'Cleaning Type: {data["cleaning_type"]}')
    #     # Add more fields as needed

    #     c.showPage()
    #     c.save()

    #     return pdf_path

class RentaldeductionSerializer(serializers.ModelSerializer):
    checkin = serializers.CharField(source='checkin.user.name', read_only=True)
    class Meta:
        model = RentalDeduction
        exclude = ('created_at', 'updated_at')

class AppendicesTransSerializer(serializers.ModelSerializer):
    checkin = serializers.CharField(source='checkin.user.name', read_only=True)
    obj = serializers.CharField(source='obj.name', read_only=True)
    class Meta:
        model = Appendicestransaction
        exclude = ('created_at', 'updated_at')

class CheckinContactsSerializer(serializers.ModelSerializer):
    checkin = serializers.CharField(source='checkin.user.name', read_only=True)
    class Meta:
        model = CheckinContacts
        fields = '__all__'
