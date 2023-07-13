from django.db import models
from django_countries.fields import CountryField
from foundation.models import BaseModel
from django.utils.translation import gettext_lazy as _
from masters.models import *


class Tickets(BaseModel):
    ticket_choice = (
        ("TicketDamage", "TicketDamage"),
        ("GeneralEnquiries", "GeneralEnquiries"),
        ("InvoiceQuestion", "InvoiceQuestion"),
        ("PetRequest", "PetRequest"),
        ("OrderKey", "OrderKey"),
        ("PaymentSlips", "PaymentSlips"),
        ("BankDetails", "BankDetails"),
        ("OrderBadge", "OrderBadge"),
        ("Messages", "Messages"),
    )
    status_choice = (
        ("pending", ("Pending")),
        ("inprogress", ("In Progress")),
        ("completed", ("Completed")),
        ("cancelled", ("Cancelled")),
    )
    tickettype_id = models.CharField(
        max_length=20,
        choices=ticket_choice,
        default="draft",
        verbose_name=("ticket choice"),
    )
    manageby_id = models.ForeignKey(
        Realestatepropertymanagement,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("Manage By"),
    )
    property_id = models.ForeignKey(
        Realestateproperties,
        on_delete=models.PROTECT,
        verbose_name=_("Property"),
        null=True,
        blank=True,
    )
    object_id = models.ForeignKey(
        Realestateobjects,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name=_("Object"),
    )
    tenant_id = models.ForeignKey(
        Realestatepropertytenant,
        on_delete=models.PROTECT,
        verbose_name=_("Tenant"),
        null=True,
        blank=True,
    )
    responsible_user_id = models.ForeignKey(
        Realestatepropertyowner,
        on_delete=models.PROTECT,
        related_name="tickets_responsibleuserid_set",
        verbose_name=("Responsible User"),
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=("title")
    )
    message = models.CharField(
        max_length=250, blank=True, null=True, verbose_name=("Message")
    )
    reporting_text = models.TextField(
        blank=True, null=True, verbose_name=("Reporting Text")
    )
    due_date = models.DateTimeField(blank=True, null=True, verbose_name=("Due-Date"))
    status = models.CharField(
        null=True,
        blank=True,
        choices=status_choice,
        max_length=20,
        verbose_name=("Status"),
    )
    contact_name = models.CharField(
        max_length=30, blank=True, null=True, verbose_name=("Contact Name")
    )
    contact_phone = models.CharField(
        max_length=30, blank=True, null=True, verbose_name=("Contact Phone")
    )
    contact_email = models.EmailField(
        blank=True, null=True, verbose_name=("Contact Email")
    )
    contact_time = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=("Contact Time")
    )
    info = models.TextField(blank=True, null=True, verbose_name=("Information"))

    class Meta:
        db_table = "Tickets"
        verbose_name = "Tickets"
        ordering = ["-id"]

    def __str__(self):
        return str(self.title)


class TicketAttachments(models.Model):
    ticket = models.ForeignKey(
        Tickets, on_delete=models.CASCADE, verbose_name=("Ticket")
    )
    attachment = models.FileField(
        upload_to="ticket/attachements/", null=True, blank=True
    )
    image = models.ImageField(upload_to="ticket/images/", null=True, blank=True)


class Ticketoffers(BaseModel):
    offer_choices = (
        ("pending", ("Pending")),
        ("received", ("Received")),
        ("selected", ("Selected")),
        ("rejected", ("Rejected")),
    )
    invoice_choices = (
        ("pending", ("Pending")),
        ("invoiced", ("Invoiced")),
        ("paid", ("Paid")),
        ("dispute", ("Dispute")),
    )
    ticket = models.ForeignKey(
        Tickets, on_delete=models.PROTECT, verbose_name=("Ticket")
    )
    realestate_service_provider_id = models.ForeignKey(
        Realestateserviceproviders,
        on_delete=models.PROTECT,
        verbose_name=("Service Provider"),
        null=True,
        blank=True,
    )
    request_note = models.CharField(
        max_length=150, blank=True, null=True, verbose_name=("Request Note")
    )
    offer_note = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=("Note")
    )
    price = models.DecimalField(
        max_digits=18, decimal_places=2, blank=True, null=True, verbose_name=("Price")
    )
    price_limit = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name=("Price Limit"),
    )
    dead_line = models.DateField(blank=True, null=True, verbose_name=("Last date"))
    appointment_date = models.DateTimeField(
        blank=True, null=True, verbose_name=("Appointment Date")
    )
    service_provider_rating_by_tenant = models.IntegerField(
        blank=True, null=True, verbose_name=("Service Provider Rating by Tenant")
    )
    service_provider_comment_by_tenant = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=("Service Provider Comment by Tenant"),
    )
    service_provider_rating_by_manager = models.IntegerField(
        blank=True, null=True, verbose_name=("Service Provider Rating by Manager")
    )
    service_provider_comment_by_manager = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name=("Service Provider Comment by Manager"),
    )
    our_rating = models.IntegerField(blank=True, null=True, verbose_name=("Our Rating"))
    problem_comment = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=("Problem Comment")
    )
    offer_status = models.CharField(
        choices=offer_choices,
        max_length=20,
        null=True,
        blank=True,
        verbose_name=("Offer Status"),
    )
    offer_note_attachements = models.TextField(
        blank=True, null=True, verbose_name=("Offer Note Attachments")
    )
    request_note_attachments = models.TextField(
        blank=True, null=True, verbose_name=("Request Note Attachments")
    )
    invoice_status = models.CharField(
        choices=invoice_choices,
        max_length=20,
        null=True,
        blank=True,
        verbose_name=("Invoice Status"),
    )

    class Meta:
        db_table = "Ticketoffers"
        verbose_name = "Ticket_offers"
        ordering = ["-id"]

    def __str__(self):
        return str(self.ticket.title)


class TKDamageReport(BaseModel):
    TIME_CHOICES = (
        ("MORNING", "Morning (8 to 12)"),
        ("AFTERNOON", "Afternoon (13 to 17)"),
        ("FULL_DAY", "Full day (8 to 17)"),
    )
    CONTACT_PERSON_CHOICES = (
        ("SITE_CONTACT", "Contact person on site"),
        ("LETTER_BOX_CARETAKER", "Letter box caretaker"),
        ("NEIGHBOR_DEPOSIT", "At the neighbour's/deposit"),
    )
    ticket = models.ForeignKey(Tickets, on_delete=models.PROTECT)
    damagr_date = models.DateField(null=True, blank=True)
    time_range = models.CharField(
        max_length=20, choices=TIME_CHOICES, null=True, blank=True
    )
    contact_person = models.CharField(
        max_length=30, choices=CONTACT_PERSON_CHOICES, null=True, blank=True
    )
    KeyLocation = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = "TKDamageReport"
        ordering = ["-id"]

    def __str__(self):
        return str(self.ticket.title)


class TkGeneralEnquiries(BaseModel):
    ticket = models.ForeignKey(Tickets, on_delete=models.PROTECT)

    class Meta:
        db_table = "Generalenquiries"
        ordering = ["-id"]

    def __str__(self):
        return str(self.ticket.title)


class TkInvoiceQuestion(BaseModel):
    ticket = models.ForeignKey(Tickets, on_delete=models.PROTECT)
    refrence_number = models.CharField(max_length=100, null=True, blank=True)
    invoice_amount = models.CharField(max_length=100, null=True, blank=True)
    question = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "Invoicequestion"
        ordering = ["-id"]

    def __str__(self):
        return str(self.ticket.title)


class TkPetRequest(BaseModel):
    PET_CHOICES = (
        ("cat_inside", "Cat (inside)"),
        ("cat_in_out", "Cat (inside and outside)"),
        ("dog", "Dog"),
        ("fish", "Fish (aquarium)"),
        ("reptiles", "Reptiles (terrarium)"),
        ("birds", "Birds"),
        ("other_pets", "Other pets"),
    )
    ticket = models.ForeignKey(Tickets, on_delete=models.PROTECT)
    pet_type = models.CharField(
        max_length=20, choices=PET_CHOICES, null=True, blank=True
    )
    quantity = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "Petrequest"
        ordering = ["-id"]

    def __str__(self):
        return str(self.ticket.title)


class TkOrderKey(BaseModel):
    KEY_CHOICES = (
        ("house_apartment", "House and apartment/property door"),
        ("front_door", "Front door"),
        ("object_door", "Object door"),
        ("mailbox", "Mailbox"),
        ("garage", "Garage"),
        ("other", "Other"),
    )
    REASON_CHOICES = (
        ("loss", "Loss (can no longer be found)"),
        ("defective", "Defective (key present but defective)"),
        ("additional_key", "Additional Key"),
        ("other", "Other (enter reason in remarks)"),
    )
    ticket = models.ForeignKey(Tickets, on_delete=models.PROTECT)
    key_type = models.CharField(
        max_length=20, choices=KEY_CHOICES, null=True, blank=True
    )
    quantity = models.CharField(max_length=100, null=True, blank=True)
    locking_system = models.CharField(max_length=100, null=True, blank=True)
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    order_reason = models.CharField(
        max_length=20, choices=REASON_CHOICES, null=True, blank=True
    )

    class Meta:
        db_table = "Orderkey"
        ordering = ["-id"]

    def __str__(self):
        return str(self.ticket.title)


class TkPaymentSlips(BaseModel):
    MONTH_CHOICES = (
        ("1", "January"),
        ("2", "February"),
        ("3", "March"),
        ("4", "April"),
        ("5", "May"),
        ("6", "June"),
        ("7", "July"),
        ("8", "August"),
        ("9", "September"),
        ("10", "October"),
        ("11", "November"),
        ("12", "December"),
    )

    YEAR_CHOICES = (
        ("2022", "2022"),
        ("2023", "2023"),
        ("2024", "2024"),
        ("2025", "2025"),
        ("2026", "2026"),
        ("2027", "2027"),
        ("2028", "2028"),
        ("2029", "2029"),
        ("2030", "2030"),
        # Add more years as needed
    )
    PAYMENT_SLIP_DELIVERY_CHOICES = (
        ("app", "Via app"),
        ("email", "By e-mail"),
        ("mail", "By mail"),
    )
    ticket = models.ForeignKey(Tickets, on_delete=models.PROTECT)
    from_month = models.CharField(
        max_length=50, choices=MONTH_CHOICES, null=True, blank=True
    )
    from_year = models.CharField(
        max_length=50, choices=YEAR_CHOICES, null=True, blank=True
    )
    to_month = models.CharField(
        max_length=50, choices=MONTH_CHOICES, null=True, blank=True
    )
    to_year = models.CharField(
        max_length=50, choices=YEAR_CHOICES, null=True, blank=True
    )
    payment_slip_delivery = models.CharField(
        max_length=10, choices=PAYMENT_SLIP_DELIVERY_CHOICES, null=True, blank=True
    )

    class Meta:
        db_table = "Paymentslips"
        ordering = ["-id"]

    def __str__(self):
        return str(self.ticket.title)


class TkBankDetails(BaseModel):
    ticket = models.ForeignKey(Tickets, on_delete=models.PROTECT)
    valid = models.DateField(null=True, blank=True)
    account_name = models.CharField(max_length=200)
    zip = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    iban = models.CharField(max_length=200, null=True, blank=True)
    swift = models.CharField(max_length=200, null=True, blank=True)
    bank_name = models.CharField(max_length=150)
    place = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "Bankdetails"
        ordering = ["-id"]

    def __str__(self):
        return str(self.ticket.title)


class TkOrderBadge(BaseModel):
    ORDER_CHOICES = [
        (
            "complete_set",
            "I would like a complete set of new badges with the inscription.",
        ),
        (
            "replacement",
            "I wish only the replacement of the sign at certain locations.",
        ),
    ]
    VALID_FROM_CHOICES = [
        ("assembly", "Valid From (assembly)"),
        ("asap", "As Soon As Possible"),
        ("date", "Valid From Date"),
    ]
    ticket = models.ForeignKey(Tickets, on_delete=models.PROTECT)
    order_type = models.CharField(
        max_length=20,
        choices=ORDER_CHOICES,
        default="complete_set",
        verbose_name="Order Type",
        null=True,
        blank=True,
    )
    valid_from = models.CharField(
        max_length=20,
        choices=VALID_FROM_CHOICES,
        default="assembly",
        verbose_name="Valid From",
        null=True,
        blank=True,
    )
    labeling = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        db_table = "Order badge"
        ordering = ["-id"]

    def __str__(self):
        return str(self.ticket.title)
