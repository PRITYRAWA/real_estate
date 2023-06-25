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

class GeneralInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInspection
        fields = '__all__'

class ObjectListInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectListInspection
        fields = '__all__'

class CheckInOutSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Realestatepropertytenant.objects.all())
    user_name = serializers.SerializerMethodField()
    object_check_in = serializers.PrimaryKeyRelatedField(queryset=Realestateobjects.objects.all())
    property_check_in = serializers.SerializerMethodField()
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
        return check_in_out

class KeysSerializer(serializers.ModelSerializer):

    class Meta:
        model = Realestatekey
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

class MetersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestatemeter
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')    


class FurnitureInspectionSerializer(serializers.ModelSerializer):
    checkin = serializers.PrimaryKeyRelatedField(queryset=CheckInOut.objects.all())

    class Meta:
        model = FurnitureInspection
        fields = ('id', 'cleaning_type', 'photos', 'description', 'checkin')

    def generate_pdf(self, data):
        pdf_filename = f'furniture_inspection_{data["id"]}.pdf'
        pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)

        # Create the PDF document
        c = canvas.Canvas(pdf_path)
        c.drawString(100, 750, 'Furniture Inspection Details')
        c.drawString(100, 700, f'ID: {data["id"]}')
        c.drawString(100, 650, f'Cleaning Type: {data["cleaning_type"]}')
        # Add more fields as needed

        c.showPage()
        c.save()

        return pdf_path

class RentaldeductionSerializer(serializers.ModelSerializer):
    checkin_id = serializers.PrimaryKeyRelatedField(queryset=CheckInOut.objects.all(), source='checkin', write_only=True)

    class Meta:
        model = RentalDeduction
        fields = '__all__'
