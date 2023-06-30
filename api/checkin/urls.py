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
router.register(r'appendices', AppendTransViewSet,basename="properties"),
router.register(r'room', ObjectListInspectionViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'room-detail', ChildObjectListInspectionViewSet, basename='child-objectlistinspection')
router.register(r'tenders', TenderViewSet,basename="tender")
router.register(r'person-movein', PersonmoveinViewSet,basename="Personmovein")
urlpatterns = [
        path('generate-report/', generate_pdf_report, name='generate_report'),
        path('generate-report-furniture/', generate_pdf_report_furniture, name='generate_report-furniture'),
        path('inspection/<int:id>', generate_checkin_report, name='generate_pdf'),

]

urlpatterns += router.urls

