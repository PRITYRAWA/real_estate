from django.shortcuts import render
from .serializers import *
from tasks.models import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer

    def get_queryset(self):
        ticket_type = self.request.query_params.get('ticket_type', None)
        if ticket_type:
            return self.queryset.filter(tickettype_id=ticket_type)
        return self.queryset

    def create(self, request, *args, **kwargs):
        getData = request.data
        haveImg = False
        haveAtt = False
        result = []
        if 'image' in getData:
            imgs = getData.pop('image')
            haveImg = True
        if 'attachment' in getData:
            atts = getData.pop('attachment')
            haveAtt = True
        newRec = TicketsSerializer(data=getData, context={'request':request})
        if newRec.is_valid(raise_exception=True):
            newRec.save()
            recDetails = Tickets.objects.get(id=newRec.data.get('id'))
            length = max(len(imgs), len(atts))
            if haveImg or haveAtt:
                for i in range(length):
                    img, att = None, None
                    if i < len(imgs):
                        img = imgs[i]
                    if i < len(atts):
                        att = atts[i]
                    new_image = TicketAttachments.objects.create(image=img, attachment=att)
                    recDetails.attachments.add(new_image)
        result = TicketsSerializer(recDetails, context={'request':request})
        return Response(result.data)

    def update(self, request, *args, **kwargs):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",request.data)
        m = {}
        data = request.data
        if 'tickettype_id' in data:
            m['tickettype_id'] = data['tickettype_id']
        if 'title' in data:
            m['title'] = data['title']
        if 'message' in data:
            m['message'] = data['message']
        if 'reporting_text' in data:
            m['reporting_text'] = data['reporting_text']
        if 'due_date' in data:
            m['due_date'] = data['due_date']
        if 'status' in data:
            m['status'] = data['status']
        if 'contact_name' in data:
            m['contact_name'] = data['contact_name']
        if 'contact_phone' in data:
            m['contact_phone'] = data['contact_phone']
        if 'contact_email' in data:
            m['contact_email'] = data['contact_email']
        if 'contact_time' in data:
            m['contact_time'] = data['contact_time']
        if 'info' in data:
            m['info'] = data['info']
        if 'created_date' in data:
            m['created_date'] = data['created_date']
        if 'manageby_id' in data:
            m['manageby_id'] = data['manageby_id']
        if 'property_id' in data:
            m['property_id'] = data['property_id']
        if 'object_id' in data:
            m['object_id'] = data['object_id']
        if 'tenant_id' in data:
            m['tenant_id'] = data['tenant_id']
        if 'responsible_user_id' in data:
            m['responsible_user_id'] = data['responsible_user_id']
        instance = self.get_object()
        getData = data  # Create a mutable copy of the QueryDict
        haveImg = False
        haveAtt = False
        imgs, atts = [], []
        if 'image' in getData:
            imgs = getData.pop('image')
            haveImg = True
        if 'attachment' in getData:
            atts = getData.pop('attachment')
            haveAtt = True


        serializer = TicketAttachmentsSerializer(instance, data=m, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        gettickets = Tickets.objects.get(id=instance.id)
        # Update associated images
        length = max(len(imgs), len(atts))
        if haveImg or haveAtt:
            for i in range(length):
                img, att = None, None
                if i < len(imgs):
                    img = imgs[i]
                if i < len(atts):
                    att = atts[i]
                new_attachment = TicketAttachments.objects.create(image=img, attachment=att)
                gettickets.attachments.add(new_attachment)
        result = TicketsSerializer(instance, context={'request': request})
        return Response(result.data)


class TicketoffersViewSet(viewsets.ModelViewSet):
    # end point to access Ticketoffers Model.
    queryset = Ticketoffers.objects.all()
    serializer_class = TicketofferSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class TkDamageViewSet(viewsets.ModelViewSet):
    queryset = TKDamageReport.objects.all()
    serializer_class = TkDamageSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class TkEnquiriesViewSet(viewsets.ModelViewSet):
    queryset = TkGeneralEnquiries.objects.all()
    serializer_class = TkEnquiriesSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class TkInvoiceViewSet(viewsets.ModelViewSet):
    queryset = TkInvoiceQuestion.objects.all()
    serializer_class = TkInvoiceSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class TkPetViewSet(viewsets.ModelViewSet):
    queryset = TkPetRequest.objects.all()
    serializer_class = TkPetSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class TkOrderKeyViewSet(viewsets.ModelViewSet):
    queryset = TkOrderKey.objects.all()
    serializer_class = TkOrderKeySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class TkPaymentSlipViewSet(viewsets.ModelViewSet):
    queryset = TkPaymentSlips.objects.all()
    serializer_class = TkPaymentSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class TkBankDetailViewSet(viewsets.ModelViewSet):
    queryset = TkBankDetails.objects.all()
    serializer_class = TkBankSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class TkOrderBadgeViewSet(viewsets.ModelViewSet):
    queryset = TkOrderBadge.objects.all()
    serializer_class = TkOrderSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
