from rest_framework import serializers
from tasks.models import *
from masters.models import *

class TicketSerializer(serializers.ModelSerializer):
    manageby_id = serializers.CharField(read_only=True, source='manageby_id.manager_name')
    property_id = serializers.CharField(read_only=True, source='property_id.name')
    object_id = serializers.CharField(read_only=True, source='object_id.object_name')  
    tenant_id = serializers.CharField(read_only=True, source='tenant_id.name')  
    responsible_user_id = serializers.CharField(read_only=True, source='responsible_user_id.name')

    class Meta:
        model = Tickets
        exclude = ('created_at', 'updated_at')

class TicketofferSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source='ticket.title') 
    realestate_service_provider_id = serializers.CharField(read_only=True, source='Realestateserviceproviders.name')   
    class Meta:
        model = Ticketoffers
        exclude = ('created_at', 'updated_at')

class TkDamageSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source='ticket.title') 
    class Meta:
        model = TKDamageReport
        exclude = ('created_at', 'updated_at')

class TkEnquiriesSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source='ticket.title') 
    class Meta:
        model = TkGeneralEnquiries
        exclude = ('created_at', 'updated_at')

class TkInvoiceSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source='ticket.title') 
    class Meta:
        model = TkInvoiceQuestion
        exclude = ('created_at', 'updated_at')

class TkPetSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source='ticket.title') 
    class Meta:
        model = TkPetRequest
        exclude = ('created_at', 'updated_at')

class TkOrderKeySerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source='ticket.title') 
    class Meta:
        model = TkOrderKey
        exclude = ('created_at', 'updated_at')

class TkPaymentSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source='ticket.title') 
    class Meta:
        model = TkPaymentSlips
        exclude = ('created_at', 'updated_at')

class TkBankSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source='ticket.title') 
    class Meta:
        model = TkBankDetails
        exclude = ('created_at', 'updated_at')

class TkOrderSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source='ticket.title') 
    class Meta:
        model = TkOrderBadge
        exclude = ('created_at', 'updated_at')
