from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register([Tickets,Ticketoffers,TKDamageReport,TkGeneralEnquiries,TkInvoiceQuestion,TkPetRequest,TkOrderKey,TkPaymentSlips,TkBankDetails,TkOrderBadge])