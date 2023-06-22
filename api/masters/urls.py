from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = "api.master"

router = routers.DefaultRouter()

router.register(r'properties', RealestatepropertyViewSet,basename="properties")
router.register(r'objects', RealestateobjectsViewSet,basename="objects")
router.register(r'agents', RealestateagentsViewSet,basename="agents")
router.register(r'messages', MessagesViewSet,basename="messages")
router.register(r'comments', MessagecommentsViewSet,basename="comments")
router.register(r'tickets', TicketsViewSet,basename="tickets")
router.register(r'offers', TicketoffersViewSet,basename="offers")
router.register(r'service-providers', RealestateserviceprovidersViewSet,basename="service-providers")
router.register(r'feedbacks', FeedbacksViewSet,basename="feedbacks")
router.register(r'owner', RealestatepersonsViewSet,basename="persons")
router.register(r'tenant', RealestatepropertytenantViewSet,basename='property')
router.register(r'meeting-template', MessagetemplateViewSet,basename="meeting-template")
router.register(r'agendas', AgendaViewSet,basename="agendas")
router.register(r'quroums', QuroumsViewSet,basename="quroums")
router.register(r'objectdetail', RealestateobjectsdetailViewSet,basename='properties'),
router.register(r'objectdetailitem', RealestateObjectDetailItemsViewSet,basename='properties'),
router.register(r'subgroup', SubgroupViewSet,basename="subgroup"),
router.register(r'keys', RealestatekeysViewSet,basename="properties"),
router.register(r'meters', RealestatemetersViewSet,basename="properties"),
router.register(r'property-management', PropertyManagementViewSet,basename="property-management")

urlpatterns = [

]
urlpatterns += router.urls
