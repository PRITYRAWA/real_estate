from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = "api.meetings"

router = routers.DefaultRouter()

router.register(r"meetings", MeetingScheduleViewSet,basename="meetings")
router.register(r"meeting_participants", MeetingParticipantViewSet,basename="meeting_participants")
urlpatterns = []

urlpatterns += router.urls