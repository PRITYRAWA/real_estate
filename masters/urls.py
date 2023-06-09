from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()


router.register(r'properties', RealestatepropertyViewSet)
router.register(r'objects', RealestateobjectsViewSet)
router.register(r'agents', RealestateagentsViewSet)
router.register(r'messages', MessagesViewSet)

router.register(r'comments', MessagecommentsViewSet)
router.register(r'tickets', TicketsViewSet)
router.register(r'offers', TicketoffersViewSet)
router.register(r'service-providers', RealestateserviceprovidersViewSet)
router.register(r'feedbacks', FeedbacksViewSet)
router.register(r'persons', RealestatepersonsViewSet)

urlpatterns = [
    path('real-estate/',include(router.urls))
]