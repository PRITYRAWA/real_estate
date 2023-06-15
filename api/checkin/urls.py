from django.urls import path
from .views import *
from rest_framework import routers


app_name = "api.checkin"

router = routers.DefaultRouter()
router.register(r"checkinouts", CheckInOutListCreateView,basename="checkinouts")
urlpatterns = []

urlpatterns += router.urls