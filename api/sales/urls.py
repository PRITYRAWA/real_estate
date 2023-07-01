from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = "api.sales"

router = routers.DefaultRouter()

router.register(r'person-visit', PersonmoveinViewSet,basename="Personmovein")
router.register(r'tenders', TenderViewSet,basename="tender")
router.register(r'vacant', VacantPropertiesViewSet,basename="property-management")


urlpatterns = []

urlpatterns += router.urls