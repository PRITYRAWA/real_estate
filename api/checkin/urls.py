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
#router.register(r'appendices-checkbox', AppendicescheckboxViewSet,basename="properties"),
router.register(r'room', ObjectListInspectionViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'room-detail', ChildObjectListInspectionViewSet, basename='child-objectlistinspection')

router.register(r'checkin-contacts', CheckinContactsViewSet, basename='checkin-contacts')
router.register(r'checks', ChecksViewSet)

urlpatterns = [
        path('generate-report/', generate_pdf_report, name='generate_report'),
        path('generate-report-furniture/', generate_pdf_report_furniture, name='generate_report-furniture'),
        path('inspection/<int:id>', generate_checkin_report, name='generate_pdf'),
        path('key-get/<int:realestatekey_id>/', realestatekey_images, name='key-get'),
        path('key-post/<int:realestatekey_id>/', update_realestatekey_image, name='key-post'),
        path('key-delete/<int:realestatekey_id>/', delete_realestatekey_images, name='key-delete'),
        path('meter-get/<int:realestatemeter_id>/', realestatemeter_images, name='key-get'),
        path('meter-post/<int:realestatemeter_id>/', update_realestatemeter_image, name='key-post'),
        path('meter-delete/<int:realestatemeter_id>/', delete_realestatemeter_images, name='key-delete'),
]
urlpatterns += router.urls

