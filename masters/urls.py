from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'real-estate-property', RealestatepropertyViewSet)
router.register(r'objects', RealestateobjectsViewSet)
router.register(r'agents', RealestateagentsViewSet)
router.register(r'message', MessagesViewSet)
router.register(r'comments', MessagecommentsViewSet)
router.register(r'tickets', TicketsViewSet)
router.register(r'offers', TicketoffersViewSet)
router.register(r'service-providers', RealestateserviceprovidersViewSet)

urlpatterns = [
    path('',include(router.urls))
]