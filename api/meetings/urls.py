from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = "api.meetings"

router = routers.DefaultRouter()

router.register(r"meetings", MeetingScheduleViewSet,basename="meetings")
urlpatterns = []

urlpatterns += router.urls