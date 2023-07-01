from django.shortcuts import render
from .serializers import *
from tasks.models import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class TicketsViewSet(viewsets.ModelViewSet):
    # end point to access Tickets Model.
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


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
