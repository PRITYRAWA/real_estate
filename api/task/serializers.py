from django.conf import settings
from rest_framework import serializers
from tasks.models import *
from masters.models import *
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django_countries.serializer_fields import CountryField


class TicketAttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketAttachments
        fields = "__all__"  # Include all fields or specify the required fields


class TicketsSerializer(WritableNestedModelSerializer):
    ticketattachments_set = TicketAttachmentsSerializer(many=True, required=False)

    class Meta:
        model = Tickets
        exclude = (
            "created_at",
            "updated_at",
        )


class TicketofferSerializer(serializers.ModelSerializer):
    realestate_service_provider = serializers.CharField(
        read_only=True, source="Realestateserviceproviders.name"
    )

    class Meta:
        model = Ticketoffers
        exclude = ("created_at", "updated_at")

    def to_representation(self, instance):
        request = self.context.get("request")
        base_url = request.build_absolute_uri("/") + settings.MEDIA_URL
        representation = super().to_representation(instance)
        queryset = Tickets.objects.get(id=representation["ticket"])
        representation.pop("ticket")
        representation["ticket"] = {}
        representation["ticket"]["title"] = queryset.title
        representation["ticket"]["tickettype"] = queryset.tickettype_id
        if queryset.manageby_id:
            representation["ticket"]["manageby"] = queryset.manageby_id.manageby
        if queryset.property_id:
            representation["ticket"]["property_name"] = queryset.property_id.name
        if queryset.object_id:
            representation["ticket"]["object"] = queryset.object_id.object_name
        if queryset.tenant_id:
            representation["ticket"]["tenant"] = queryset.tenant_id.name
        if queryset.responsible_user_id:
            representation["ticket"][
                "responsible_user"
            ] = queryset.responsible_user_id.name
        representation["ticket"]["message"] = queryset.message
        representation["ticket"]["reporting_text"] = queryset.reporting_text
        representation["ticket"]["due_date"] = queryset.due_date
        representation["ticket"]["status"] = queryset.status
        representation["ticket"]["contact_name"] = queryset.contact_name
        representation["ticket"]["contact_phone"] = queryset.contact_phone
        representation["ticket"]["contact_email"] = queryset.contact_email
        representation["ticket"]["contact_time"] = queryset.contact_time
        representation["ticket"]["info"] = queryset.info

        return representation


class TkDamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TKDamageReport
        exclude = ("created_at", "updated_at")

    def to_representation(self, instance):
        request = self.context.get("request")
        base_url = request.build_absolute_uri("/") + settings.MEDIA_URL
        representation = super().to_representation(instance)
        queryset = Tickets.objects.get(id=representation["ticket"])
        representation.pop("ticket")
        representation["ticket"] = {}
        representation["ticket"]["title"] = queryset.title
        representation["ticket"]["tickettype"] = queryset.tickettype_id
        if queryset.manageby_id:
            representation["ticket"]["manageby"] = queryset.manageby_id.manageby
        if queryset.property_id:
            representation["ticket"]["property_name"] = queryset.property_id.name
        if queryset.object_id:
            representation["ticket"]["object"] = queryset.object_id.object_name
        if queryset.tenant_id:
            representation["ticket"]["tenant"] = queryset.tenant_id.name
        if queryset.responsible_user_id:
            representation["ticket"][
                "responsible_user"
            ] = queryset.responsible_user_id.name
        representation["ticket"]["message"] = queryset.message
        representation["ticket"]["reporting_text"] = queryset.reporting_text
        representation["ticket"]["due_date"] = queryset.due_date
        representation["ticket"]["status"] = queryset.status
        representation["ticket"]["contact_name"] = queryset.contact_name
        representation["ticket"]["contact_phone"] = queryset.contact_phone
        representation["ticket"]["contact_email"] = queryset.contact_email
        representation["ticket"]["contact_time"] = queryset.contact_time
        representation["ticket"]["info"] = queryset.info

        return representation


class TkEnquiriesSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source="ticket.title")

    class Meta:
        model = TkGeneralEnquiries
        exclude = ("created_at", "updated_at")


class TkInvoiceSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source="ticket.title")

    class Meta:
        model = TkInvoiceQuestion
        exclude = ("created_at", "updated_at")


class TkPetSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source="ticket.title")

    class Meta:
        model = TkPetRequest
        exclude = ("created_at", "updated_at")


class TkOrderKeySerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source="ticket.title")

    class Meta:
        model = TkOrderKey
        exclude = ("created_at", "updated_at")


class TkPaymentSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source="ticket.title")

    class Meta:
        model = TkPaymentSlips
        exclude = ("created_at", "updated_at")


class TkBankSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source="ticket.title")

    class Meta:
        model = TkBankDetails
        exclude = ("created_at", "updated_at")


class TkOrderSerializer(serializers.ModelSerializer):
    ticket = serializers.CharField(read_only=True, source="ticket.title")

    class Meta:
        model = TkOrderBadge
        exclude = ("created_at", "updated_at")


class RealestatepropertiesSerializer(serializers.ModelSerializer):
    country = CountryField(country_dict=True)

    class Meta:
        model = Realestateproperties
        fields = "__all__"


class TicketReadSerializer(serializers.ModelSerializer):
    property_id = RealestatepropertiesSerializer()
    ticketattachments_set = TicketAttachmentsSerializer(many=True)
    ticketoffers_set = TicketofferSerializer(many=True)
    tkdamagereport_set = TkDamageSerializer(many=True)
    tkgeneralenquiries_set = TkEnquiriesSerializer(many=True)
    tkinvoicequestion_set = TkInvoiceSerializer(many=True)
    tkpetrequest_set = TkPetSerializer(many=True)
    tkorderkey_set = TkOrderKeySerializer(many=True)
    tkpaymentslips_set = TkPaymentSerializer(many=True)
    tkbankdetails_set = TkBankSerializer(many=True)
    tkorderbadge_set = TkOrderSerializer(many=True)

    class Meta:
        model = Tickets
        fields = (
            "id",
            "tickettype_id",
            "manageby_id",
            "property_id",
            "object_id",
            "tenant_id",
            "responsible_user_id",
            "title",
            "message",
            "reporting_text",
            "due_date",
            "status",
            "contact_name",
            "contact_phone",
            "contact_email",
            "contact_time",
            "info",
            "created_at",
            "updated_at",
            "ticketattachments_set",
            "ticketoffers_set",
            "tkdamagereport_set",
            "tkgeneralenquiries_set",
            "tkinvoicequestion_set",
            "tkpetrequest_set",
            "tkorderkey_set",
            "tkpaymentslips_set",
            "tkbankdetails_set",
            "tkorderbadge_set",
        )
        depth = 1
