from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from masters.models import *

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

class FeedbacksViewSet(viewsets.ModelViewSet):
    # end point to access Feedbacks Model.
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbackSerializer

class RealestatepersonsViewSet(viewsets.ModelViewSet):
    # end point to access Realestatepersons Model.
    queryset = Realestatepropertyowner.objects.all()
    serializer_class = RealestatepersonSerializer


class AgendaViewSet(viewsets.ModelViewSet):
    # end point to access Realestateserviceproviders Model.
    queryset = Agenda.objects.all()
    serializer_class = Agendaserializer

class QuroumsViewSet(viewsets.ModelViewSet):
    # end point to access Feedbacks Model.
    queryset = Quorums.objects.all()
    serializer_class = Quorumsserializer

class MessagetemplateViewSet(viewsets.ModelViewSet):
    # end point to access Realestatepersons Model.
    queryset = Mettingtemplate.objects.all()
    serializer_class = Mettingtemplateserializer