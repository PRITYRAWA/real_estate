from django.urls import path
from .views import *


urlpatterns = [
    path('signup/',SignupView.as_view()),
    path('login/',LoginView.as_view()),
    path('checkinouts/', CheckInOutListCreateView.as_view(), name='checkinout-list-create'),
    path('checkinouts/<int:pk>/', CheckInOutRetrieveUpdateDestroyView.as_view(), name='checkinout-retrieve-update-destroy'),

]