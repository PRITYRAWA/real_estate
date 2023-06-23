from django.urls import path
from .views import *
from rest_framework import routers


app_name = "api.checkin"

router = routers.DefaultRouter()
router.register(r"checkinouts", CheckInOutListCreateView,basename="checkinouts")
router.register(r'key', KeysViewSet,basename="properties"),
router.register(r'meter', MetersViewSet,basename="properties"),
router.register(r'furniture/cleaning', FurnitureInspectionViewSet,basename="properties"),
router.register(r'deduction', RentaldeductionViewSet,basename="properties"),
router.register(r'room', ObjectListInspectionView,basename="properties"),

urlpatterns = [
        path('generate-report/', generate_pdf_report, name='generate_report'),
        path('furniture-inspection/<int:pk>/pdf/', generate_pdf, name='generate_pdf'),

]

urlpatterns += router.urls


