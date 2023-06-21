from django.urls import path
from .views import *
from rest_framework import routers


app_name = "api.checkin"

router = routers.DefaultRouter()
router.register(r"checkinouts", CheckInOutListCreateView,basename="checkinouts")
router.register(r'key', keysViewSet,basename="properties"),

urlpatterns = [
        path('generate-report/', generate_pdf_report, name='generate_report'),

]

urlpatterns += router.urls