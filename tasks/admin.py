from django.contrib import admin
from .models import *

# Register your models here.


class TicketAttachmentsInline(admin.TabularInline):
    model = TicketAttachments
    extra = 1


@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    inlines = [TicketAttachmentsInline]


admin.site.register(
    [
        Ticketoffers,
        TKDamageReport,
        TkGeneralEnquiries,
        TkInvoiceQuestion,
        TkPetRequest,
        TkOrderKey,
        TkPaymentSlips,
        TkBankDetails,
        TkOrderBadge,
    ]
)
