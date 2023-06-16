from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from masters.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
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

class RealestatepropertytenantViewSet(viewsets.ModelViewSet):
    serializer_class = RealestatetenantSerializer

    def get_queryset(self):
        queryset = Realestatepropertytenant.objects.filter(status="Occupied")
        return queryset


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

class SubgroupViewSet(viewsets.ModelViewSet):
    # end point to access Realestatepersons Model.
    queryset = Realestatepropertiessubgroup.objects.all()
    serializer_class = Subgroupserializer

class RealestateObjectDetailItemsViewSet(viewsets.ModelViewSet):
    serializer_class = RealEstateObjectsDetailsSerializer
    queryset = Realestateobjectsdetail.objects.all()
    lookup_field = 'id'  # Specify the lookup field for detail view

    def get_queryset(self):
        prop_id = self.request.query_params.get('propid')
        obj_id = self.request.query_params.get('objectid')
        obj_detail_id = self.request.query_params.get('objdetailid')
        
        try:
            queryset = Realestateobjectsdetail.objects.filter(related_property_id=prop_id, related_object=obj_id, related_detail=obj_detail_id)
            return queryset
        except Realestateobjectsdetail.DoesNotExist:
            return Realestateobjectsdetail.objects.none()
