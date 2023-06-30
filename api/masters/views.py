from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from masters.models import *
from checkin.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import datetime
from masters.utils import render_to_pdf #created in step 4

# Create your views here.

class RealestatepropertyViewSet(viewsets.ModelViewSet):
    # end point to access RealEstateProperty Model.
    queryset = Realestateproperties.objects.all()
    serializer_class = RealestatepropertySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class RealestateobjectsViewSet(viewsets.ModelViewSet):
    # end point to access RealEstateObjects Model.
    queryset = Realestateobjects.objects.all()
    serializer_class = RealestateobjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
            'realestatepropertyid': ['exact']
    }
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class RealestateagentsViewSet(viewsets.ModelViewSet):
    # end point to access Realestateagents Model.
    queryset = Realestateagents.objects.all()
    serializer_class = RealestateagentSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

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
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class FeedbacksViewSet(viewsets.ModelViewSet):
    # end point to access Feedbacks Model.
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbackSerializer

class RealestatepersonsViewSet(viewsets.ModelViewSet):
    # end point to access Realestatepersons Model.
    queryset = Realestatepropertyowner.objects.all()
    serializer_class = RealestatepersonSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class RealestatepropertytenantViewSet(viewsets.ModelViewSet):
    serializer_class = RealestatetenantSerializer
    queryset = Realestatepropertytenant.objects.all()

    # def get_queryset(self):
    #     queryset = Realestatepropertytenant.objects.filter(status="OCCUPIED")
    #     return queryset

    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

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

# class RealestateObjectDetailViewSet(viewsets.ModelViewSet):
#     serializer_class = RealestateobjectsdetailSerializer
#     queryset = Realestateobjectsdetail.objects.all()
#     lookup_field = 'id'  # Specify the lookup field for detail view

#     def get_queryset(self):
#         prop_id = self.request.query_params.get('propid')
#         obj_id = self.request.query_params.get('objectid')
#         obj_detail_id = self.request.query_params.get('objdetailid')
        
#         try:
#             queryset = Realestateobjectsdetail.objects.filter(related_property_id=prop_id, related_object=obj_id, related_detail=obj_detail_id)
#             return queryset
#         except Realestateobjectsdetail.DoesNotExist:
#             return Realestateobjectsdetail.objects.none()
        
class RealestatekeysViewSet(viewsets.ModelViewSet):
    # end point to access RealEstateProperty Model.
    queryset = Realestatekeyhandover.objects.all()
    serializer_class = RealEstateKeysSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class RealestatemetersViewSet(viewsets.ModelViewSet):
    # end point to access RealEstateProperty Model.
    queryset = Realestatemeterhandover.objects.all()
    serializer_class = RealEstateMeterssSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class RealestateobjectsdetailViewSet(viewsets.ModelViewSet):
    queryset = Realestateobjectsdetail.objects.all()
    serializer_class = RealestateobjectsdetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(related_detail=None)  # Exclude self-related items
        return queryset

class PropertyManagementViewSet(viewsets.ModelViewSet):
    # end point to access Realestatepersons Model.
    queryset = Realestatepropertymanagement.objects.all()
    serializer_class = Propertymanagementserializer
    
class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer
    
class AppendMasterViewSet(viewsets.ModelViewSet):
    queryset = Appendicesmaster.objects.all()
    serializer_class = AppendicesMasterSerializer


class RealestateObjectDetailItemsViewSet(viewsets.ModelViewSet):
    serializer_class = RealEstateObjectsDetailsSerializer
    queryset = Realestateobjectsdetail.objects.all()
    lookup_field = 'id'  # Specify the lookup field for detail view

    def get_queryset(self):
        # prop_id = self.request.query_params.get('propid')
        obj_id = self.request.query_params.get('roomid')
        obj_detail_id = self.request.query_params.get('childid')
        
        try:
            queryset = Realestateobjectsdetail.objects.get( related_object=obj_id, related_detail=obj_detail_id)
            print(queryset)
            return queryset
        except Realestateobjectsdetail.DoesNotExist:
            return Realestateobjectsdetail.objects.none()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
