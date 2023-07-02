from rest_framework import serializers
from tasks.models import *


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        exclude = ('created_at', 'updated_at')

class TicketofferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticketoffers
        exclude = ('created_at', 'updated_at')

class TkDamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TKDamageReport
        exclude = ('created_at', 'updated_at')

class TkEnquiriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TkGeneralEnquiries
        exclude = ('created_at', 'updated_at')

class TkInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TkInvoiceQuestion
        exclude = ('created_at', 'updated_at')

class TkPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TkPetRequest
        exclude = ('created_at', 'updated_at')

class TkOrderKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = TkOrderKey
        exclude = ('created_at', 'updated_at')

class TkPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TkPaymentSlips
        exclude = ('created_at', 'updated_at')

class TkBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = TkBankDetails
        exclude = ('created_at', 'updated_at')

class TkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TkOrderBadge
        exclude = ('created_at', 'updated_at')
