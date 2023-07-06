from django.conf import settings
from rest_framework import serializers
from tasks.models import *
from masters.models import *

class TicketAttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketAttachments
        fields = '__all__'  # Include all fields or specify the required fields

class TicketsSerializer(serializers.ModelSerializer):
    manageby_id = serializers.CharField(read_only=True, source='manageby_id.manager_name')
    property_id = serializers.CharField(read_only=True, source='property_id.name')
    object_id = serializers.CharField(read_only=True, source='object_id.object_name')  
    tenant_id = serializers.CharField(read_only=True, source='tenant_id.name')  
    responsible_user_id = serializers.CharField(read_only=True, source='responsible_user_id.name')
    attachments = TicketAttachmentsSerializer(many=True)

    class Meta:
        model = Tickets
        exclude = ('created_at', 'updated_at')


class TicketofferSerializer(serializers.ModelSerializer):
    realestate_service_provider_id = serializers.CharField(read_only=True, source='Realestateserviceproviders.name')   
    class Meta:
        model = Ticketoffers
        exclude = ('created_at', 'updated_at')

    def to_representation(self, instance):
        request = self.context.get('request')
        base_url = request.build_absolute_uri('/')+ settings.MEDIA_URL
        representation = super().to_representation(instance)
        queryset = Tickets.objects.get(id=representation['ticket'])
        representation.pop('ticket')
        representation['ticket'] = {}
        representation['ticket']['title'] = queryset.title
        representation['ticket']['tickettype'] = queryset.tickettype_id
        if queryset.manageby_id:
            representation['ticket']['manageby'] = queryset.manageby_id.manageby
        if queryset.property_id:
            representation['ticket']['property_name'] = queryset.property_id.name
        if queryset.object_id:
            representation['ticket']['object'] = queryset.object_id.object_name
        if queryset.tenant_id:
            representation['ticket']['tenant'] = queryset.tenant_id.name
        if queryset.responsible_user_id:
            representation['ticket']['responsible_user'] = queryset.responsible_user_id.name
        representation['ticket']['message'] = queryset.message
        representation['ticket']['reporting_text'] = queryset.reporting_text
        representation['ticket']['due_date'] = queryset.due_date
        representation['ticket']['status'] = queryset.status
        representation['ticket']['contact_name'] = queryset.contact_name
        representation['ticket']['contact_phone'] = queryset.contact_phone
        representation['ticket']['contact_email'] = queryset.contact_email
        representation['ticket']['contact_time'] = queryset.contact_time
        representation['ticket']['info'] = queryset.info
        representation['ticket']['created_date'] = queryset.created_date
        attachments = queryset.attachments.all()
        attachment_list = []
        for i in attachments:
            attachment_dict= {}
            if i.image:
                attachment_dict['image'] = base_url + str(i.image)
            if i.attachment:
                attachment_dict['attachment'] = base_url + str(i.attachment)
            attachment_list.append(attachment_dict)
        representation['ticket']['attachments'] = attachment_list

        return representation
    
class TkDamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TKDamageReport
        exclude = ('created_at', 'updated_at')
    
    def to_representation(self, instance):
        request = self.context.get('request')
        base_url = request.build_absolute_uri('/')+ settings.MEDIA_URL
        representation = super().to_representation(instance)
        queryset = Tickets.objects.get(id=representation['ticket'])
        representation.pop('ticket')
        representation['ticket'] = {}
        representation['ticket']['title'] = queryset.title
        representation['ticket']['tickettype'] = queryset.tickettype_id
        if queryset.manageby_id:
            representation['ticket']['manageby'] = queryset.manageby_id.manageby
        if queryset.property_id:
            representation['ticket']['property_name'] = queryset.property_id.name
        if queryset.object_id:
            representation['ticket']['object'] = queryset.object_id.object_name
        if queryset.tenant_id:
            representation['ticket']['tenant'] = queryset.tenant_id.name
        if queryset.responsible_user_id:
            representation['ticket']['responsible_user'] = queryset.responsible_user_id.name
        representation['ticket']['message'] = queryset.message
        representation['ticket']['reporting_text'] = queryset.reporting_text
        representation['ticket']['due_date'] = queryset.due_date
        representation['ticket']['status'] = queryset.status
        representation['ticket']['contact_name'] = queryset.contact_name
        representation['ticket']['contact_phone'] = queryset.contact_phone
        representation['ticket']['contact_email'] = queryset.contact_email
        representation['ticket']['contact_time'] = queryset.contact_time
        representation['ticket']['info'] = queryset.info
        representation['ticket']['created_date'] = queryset.created_date
        attachments = queryset.attachments.all()
        attachment_list = []
        for i in attachments:
            attachment_dict= {}
            if i.image:
                attachment_dict['image'] = base_url + str(i.image)
            if i.attachment:
                attachment_dict['attachment'] = base_url + str(i.attachment)
            attachment_list.append(attachment_dict)
        representation['ticket']['attachments'] = attachment_list

        return representation


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
