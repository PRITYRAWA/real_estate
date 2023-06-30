from django.db import models
from django_countries.fields import CountryField
from foundation.models import BaseModel
from django.utils.translation import gettext_lazy as _
from masters.models import *

class Tickets(BaseModel):
    ticket_choice = (
        ('TicketDamage','TicketDamage'),
        ('GeneralEnquiries','GeneralEnquiries'),
        ('InvoiceQuestion','InvoiceQuestion'),
        ('PetRequest','PetRequest'),
        ('OrderKey','OrderKey'),
        ('PaymentSlips','PaymentSlips'),
        ('BankDetails','BankDetails'),
        ('OrderBadge','OrderBadge'),
        ('Messages','Messages')
    )
    tickettypeid=models.CharField(max_length=20, choices= ticket_choice ,default='draft',verbose_name=("ticket choice") )
    manageby_id = models.CharField(max_length=100,null=True,blank=True,verbose_name=_("Manager Id"))
    realestatepropertyid = models.ForeignKey(Realestateproperties, models.DO_NOTHING)   
    realestateobjectid = models.ForeignKey(Realestateobjects, models.DO_NOTHING, blank=True, null=True)   
    realestatetenantid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING)   
    responsibleuserid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING,related_name='tickets_responsibleuserid_set')
    title = models.CharField(max_length=150)   
    message = models.CharField(max_length=2500, blank=True, null=True)   
    reportingtext = models.CharField(max_length=500, blank=True, null=True)   
    duedate = models.DateTimeField(blank=True, null=True)   
    status = models.IntegerField()   
    contactname = models.CharField(max_length=100, blank=True, null=True)   
    contactphone = models.CharField(max_length=30, blank=True, null=True)   
    contactemail = models.CharField(max_length=320, blank=True, null=True)   
    attachments = models.TextField(blank=True, null=True)   
    info = models.TextField(blank=True, null=True)   

    class Meta:
        db_table = 'Tickets' 
        ordering = ['-id']

class Ticketoffers(BaseModel):
    ticket_choice = (
        ('TicketDamage','TicketDamage'),
        ('GeneralEnquiries','GeneralEnquiries'),
        ('InvoiceQuestion','InvoiceQuestion'),
        ('PetRequest','PetRequest'),
        ('OrderKey','OrderKey'),
        ('PaymentSlips','PaymentSlips'),
        ('BankDetails','BankDetails'),
        ('OrderBadge','OrderBadge'),
        ('Messages','Messages')
    )
    tickettypeid=models.CharField(max_length=20, choices= ticket_choice ,default='draft',verbose_name=("ticket choice") ) 
    ticket = models.ForeignKey(Tickets,on_delete=models.PROTECT)   
    realestateserviceproviderid = models.ForeignKey(Realestateserviceproviders, models.PROTECT)   
    requestnote = models.CharField(max_length=1000, blank=True, null=True)   
    note = models.CharField(max_length=1000, blank=True, null=True)   
    price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)   
    pricelimit = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)   
    deadline = models.DateField(blank=True, null=True)   
    appointmentdate = models.DateTimeField(blank=True, null=True)   
    serviceproviderratingbytenant = models.IntegerField(blank=True, null=True)   
    serviceprovidercommentbytenant = models.CharField(max_length=1000, blank=True, null=True)   
    serviceproviderratingbymanager = models.IntegerField(blank=True, null=True)   
    serviceprovidercommentbymanager = models.CharField(max_length=1000, blank=True, null=True)   
    ourrating = models.IntegerField(blank=True, null=True)   
    problemcomment = models.CharField(max_length=1000, blank=True, null=True)   
    status = models.IntegerField()   
    noteattachments = models.TextField(blank=True, null=True)   
    requestnoteattachments = models.TextField(blank=True, null=True)   

    class Meta:
        db_table = 'Ticketoffers' 
        ordering = ['-id']
   



class TicketCommonFields(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    ticket = models.ForeignKey(Tickets,on_delete=models.PROTECT)   
    property = models.ForeignKey(Realestateproperties, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    Ticket_responsible = models.CharField(max_length=50, null=True, blank=True)
    Current_process_step = models.CharField(max_length=100,null=True,blank=True)
    object = models.ForeignKey(Realestateobjects,on_delete=models.CASCADE, max_length=100, null=True, blank=True)
    tenant = models.ForeignKey(Realestatepropertytenant,on_delete=models.CASCADE, max_length=100, null=True, blank=True)
    duedate = models.DateField(verbose_name="due_date",null=True,blank=True)
    descriptions = models.TextField(null=True,blank=True)
    # attachments = models.FileField(upload_to='manager', null=True, blank=True)

    class Meta:
        abstract = True


class ExtendedBaseModel(BaseModel, TicketCommonFields):
    class Meta:
        abstract = True


class TicketDamage(ExtendedBaseModel):
    TIME_CHOICES = (
    ('MORNING', 'Morning (8 to 12)'),
    ('AFTERNOON', 'Afternoon (13 to 17)'),
    ('FULL_DAY', 'Full day (8 to 17)'),
    )
    CONTACT_PERSON_CHOICES = (
    ('SITE_CONTACT', 'Contact person on site'),
    ('LETTER_BOX_CARETAKER', 'Letter box caretaker'),
    ('NEIGHBOR_DEPOSIT', 'At the neighbour\'s/deposit'),
    )
    ticket = models.ForeignKey(Tickets,on_delete=models.PROTECT)   
    date = models.DateField()
    time_range = models.CharField(max_length=20, choices=TIME_CHOICES)
    contact_person = models.CharField(max_length=30, choices=CONTACT_PERSON_CHOICES)
    KeyLocation = models.CharField(max_length=250,null=True,blank=True)

    class Meta:
        db_table = 'Reportdamage'
        ordering = ['-id']



class TkGeneralEnquiries(ExtendedBaseModel):
    ticket = models.ForeignKey(Tickets,on_delete=models.PROTECT)   
    attachments = models.FileField(upload_to='manager_enquiries',null=True,blank=True)

    class Meta:
        db_table = 'Generalenquiries'
        ordering = ['-id']

class TkInvoiceQuestion(ExtendedBaseModel):
    ticket = models.ForeignKey(Tickets,on_delete=models.PROTECT)   
    refrence_number = models.CharField(max_length=100,null=True,blank=True)
    invoice_amount = models.CharField(max_length=100,null=True,blank=True)
    question = models.TextField(null=True,blank=True)
    attachments = models.FileField(upload_to='manager_invoice',null=True,blank=True)

    class Meta:
        db_table = 'Invoicequestion'
        ordering = ['-id']

class TkPetRequest(ExtendedBaseModel):
    PET_CHOICES = (
    ('cat_inside', 'Cat (inside)'),
    ('cat_in_out', 'Cat (inside and outside)'),
    ('dog', 'Dog'),
    ('fish', 'Fish (aquarium)'),
    ('reptiles', 'Reptiles (terrarium)'),
    ('birds', 'Birds'),
    ('other_pets', 'Other pets'),
    )
    ticket = models.ForeignKey(Tickets,on_delete=models.PROTECT)   
    pet_type = models.CharField(max_length=20, choices=PET_CHOICES)
    quantity = models.CharField(max_length=100,null=True,blank=True)
    attachments = models.FileField(upload_to='pet_request',null=True,blank=True)

    class Meta:
        db_table = 'Petrequest'
        ordering = ['-id']

class TkOrderKey(BaseModel):
    KEY_CHOICES = (
    ('house_apartment', 'House and apartment/property door'),
    ('front_door', 'Front door'),
    ('object_door', 'Object door'),
    ('mailbox', 'Mailbox'),
    ('garage', 'Garage'),
    ('other', 'Other'),
    )
    REASON_CHOICES = (
    ('loss', 'Loss (can no longer be found)'),
    ('defective', 'Defective (key present but defective)'),
    ('additional_key', 'Additional Key'),
    ('other', 'Other (enter reason in remarks)'),
    )
    ticket = models.ForeignKey(Tickets,on_delete=models.PROTECT)   
    key_type = models.CharField(max_length=20, choices=KEY_CHOICES)
    quantity = models.CharField(max_length=100,null=True,blank=True)
    locking_system = models.CharField(max_length=100,null=True,blank=True)
    serial_number = models.CharField(max_length=100,null=True,blank=True)
    order_reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    attachments = models.FileField(upload_to='order-key',null=True,blank=True)

    class Meta:
        db_table = 'Orderkey'
        ordering = ['-id']

class TkPaymentSlips(BaseModel):
    MONTH_CHOICES = (
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    )

    YEAR_CHOICES = (
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
        # Add more years as needed
    )
    PAYMENT_SLIP_DELIVERY_CHOICES = (
        ('app', 'Via app'),
        ('email', 'By e-mail'),
        ('mail', 'By mail'),
    )
    ticket = models.ForeignKey(Tickets,on_delete=models.PROTECT)   
    from_month = models.CharField(max_length=50,choices=MONTH_CHOICES,null=True,blank=True)
    from_year = models.CharField(max_length=50,choices=YEAR_CHOICES,null=True,blank=True)
    to_month = models.CharField(max_length=50,choices=MONTH_CHOICES,null=True,blank=True)
    to_year =  models.CharField(max_length=50,choices=YEAR_CHOICES,null=True,blank=True)
    payment_slip_delivery = models.CharField(max_length=10, choices=PAYMENT_SLIP_DELIVERY_CHOICES)
    attachments = models.FileField(upload_to='payment-slip',null=True,blank=True)

    class Meta:
        db_table = 'Paymentslips'
        ordering = ['-id']

class TkBankDetails(ExtendedBaseModel):
    ticket = models.ForeignKey(Tickets,on_delete=models.PROTECT)   
    valid = models.DateField()
    account_name = models.CharField(max_length=200)
    zip = models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    iban = models.CharField(max_length=200)
    swift = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=150)
    place = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'Bankdetails'
        ordering = ['-id']

class TkOrderBadge(ExtendedBaseModel):
    ORDER_CHOICES = [
        ('complete_set', 'I would like a complete set of new badges with the inscription.'),
        ('replacement', 'I wish only the replacement of the sign at certain locations.'),
    ]
    VALID_FROM_CHOICES = [
        ('assembly', 'Valid From (assembly)'),
        ('asap', 'As Soon As Possible'),
        ('date', 'Valid From Date'),
    ]
    ticket = models.ForeignKey(Tickets,on_delete=models.PROTECT)   
    order_type = models.CharField(
        max_length=20,
        choices=ORDER_CHOICES,
        default='complete_set',
        verbose_name='Order Type',
    )
    valid_from = models.CharField(
        max_length=20,
        choices=VALID_FROM_CHOICES,
        default='assembly',
        verbose_name='Valid From'
    )
    labeling = models.CharField(max_length=300)
