from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = "api.task"

router = routers.DefaultRouter()

router.register(r'tickets', TicketsViewSet,basename="tickets")
router.register(r'ticket-offers', TicketoffersViewSet,basename="offers")
router.register(r'ticket-damage', TkDamageViewSet,basename="task")
router.register(r'ticket-enquiry', TkEnquiriesViewSet,basename="task")
router.register(r'ticket-invoice', TkInvoiceViewSet,basename="task")
router.register(r'ticket-pet', TkPetViewSet,basename="task")
router.register(r'ticket-orderkey', TkOrderKeyViewSet,basename="task")
router.register(r'ticket-paymentslip', TkPaymentSlipViewSet,basename="task")
router.register(r'ticket-bankdetail', TkBankDetailViewSet,basename="task")
router.register(r'tickets-orderbadge', TkOrderBadgeViewSet,basename="task")
urlpatterns = []

urlpatterns += router.urls