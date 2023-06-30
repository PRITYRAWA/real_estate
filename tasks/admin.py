from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register([TicketDamage,TkGeneralEnquiries,TkInvoiceQuestion,TkPetRequest,TkOrderKey,TkPaymentSlips,TkBankDetails,TkOrderBadge])