from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'properties', RealestatepropertyViewSet,basename='property')
router.register(r'objects', RealestateobjectsViewSet,basename='property')
router.register(r'agents', RealestateagentsViewSet)
router.register(r'messages', MessagesViewSet)

router.register(r'comments', MessagecommentsViewSet)
router.register(r'tickets', TicketsViewSet)
router.register(r'offers', TicketoffersViewSet)
router.register(r'service-providers', RealestateserviceprovidersViewSet)
router.register(r'feedbacks', FeedbacksViewSet)
router.register(r'owner', RealestatepersonsViewSet,basename='property')

urlpatterns = [
    path('real-estate/',include(router.urls))
]