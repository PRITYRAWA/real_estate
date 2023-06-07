from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import RealestatepropertySerializer, RealestateobjectSerializer, RealestateagentSerializer, MessageSerializer, MessagecommentSerializer, TicketSerializer, TicketofferSerializer, RealestateserviceproviderSerializer
from .models import Realestateproperties, Realestateobjects, Realestateagents, Messages, Messagecomments, Tickets, Ticketoffers, Realestateserviceproviders

# Create your views here.

class RealestatepropertyViewSet(viewsets.ModelViewSet):
    # end point to access RealEstateProperty Model.
    queryset = Realestateproperties.objects.all()
    serializer_class = RealestatepropertySerializer

class RealestateobjectsViewSet(viewsets.ModelViewSet):
    # end point to access RealEstateObjects Model.
    queryset = Realestateobjects.objects.all()
    serializer_class = RealestateobjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
            'realestatepropertyid': ['exact']
    }

class RealestateagentsViewSet(viewsets.ModelViewSet):
    # end point to access Realestateagents Model.
    queryset = Realestateagents.objects.all()
    serializer_class = RealestateagentSerializer

class MessagesViewSet(viewsets.ModelViewSet):
    # end point to access Messages Model.
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer

class MessagecommentsViewSet(viewsets.ModelViewSet):
    # end point to access Messagecomments Model.
    queryset = Messagecomments.objects.all()
    serializer_class = MessagecommentSerializer

class TicketsViewSet(viewsets.ModelViewSet):
    # end point to access Tickets Model.
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializer

class TicketoffersViewSet(viewsets.ModelViewSet):
    # end point to access Ticketoffers Model.
    queryset = Ticketoffers.objects.all()
    serializer_class = TicketofferSerializer

class RealestateserviceprovidersViewSet(viewsets.ModelViewSet):
    # end point to access Realestateserviceproviders Model.
    queryset = Realestateserviceproviders.objects.all()
    serializer_class = RealestateserviceproviderSerializer