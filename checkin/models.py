from django.db import models
from foundation.models import BaseModel, User
from masters.models import Realestateobjects,Realestateobjectsdetail,Realestatepropertytenant,Realestateproperties,Realestatekeyhandover,Realestatemeterhandover
import uuid

# checkin model
class CheckInOut(BaseModel):
    user = models.ForeignKey(Realestatepropertytenant, on_delete=models.CASCADE)
    service_ticket_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    object_check_in = models.ForeignKey(Realestateobjects, on_delete=models.CASCADE, null=True, blank=True)
    check_in_date = models.DateField(null=True, blank=True)
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
    inspection_date_time = models.DateTimeField(null=True, blank=True)
    # object_details = models.ManyToManyField(Realestateobjectsdetail)
    object_detail_list = models.ForeignKey('ObjectListInspection', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.name} checked into {self.object_check_in}"

class GeneralInspection(BaseModel):
    #  fk service id link with check in&out, 
    service_id = models.ForeignKey(CheckInOut, on_delete=models.CASCADE, null=True, blank=True)
    real_estate_object = models.ForeignKey(Realestateobjects, on_delete=models.CASCADE, null=True, blank=True,related_name='inspections')
    inspection_report = models.TextField()
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='inspection_images/')

    def __str__(self):
        return f"Inspection for {self.real_estate_object}"


#  object list inspection by tenant

class ObjectListInspection(BaseModel):
    #  fk service id link with check in&out, 
    service_id = models.ForeignKey(CheckInOut, on_delete=models.CASCADE, null=True, blank=True)
    object_detail_list = models.ForeignKey(Realestateobjectsdetail, on_delete=models.CASCADE,null=True,blank=True,related_name='inspections')
    new = models.BooleanField(default=False,null=True,blank=True)
    inorder = models.BooleanField(default=False,null=True,blank=True)
    normal_wear = models.BooleanField(blank=True,null=True)
    notes = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='object_images_teenant/',null=True,blank=True)   
    def __str__(self):
        return f'Object {self.id}'

class Realestatekey(BaseModel):
    checkin = models.ForeignKey(CheckInOut,on_delete=models.CASCADE, null=True, blank=True) 
    obj = models.ForeignKey(Realestatekeyhandover,on_delete=models.CASCADE, null=True, blank=True) 
    photos = models.ImageField(upload_to='key_photos/',null=True,blank=True)
    count = models.IntegerField(default=0)
    description = models.TextField(null=True,blank=True)
    name = models.CharField(max_length=300,null=True, blank=True)

    class Meta:
        db_table = 'Realestatekey'
        ordering = ['-id']

    def __str__(self):
        return str(self.name)
    
class Realestatemeter(BaseModel):
    checkin = models.ForeignKey(CheckInOut,on_delete=models.CASCADE, null=True, blank=True) 
    # obj = models.ForeignKey(Realestatemeterhandover,on_delete=models.CASCADE, null=True, blank=True) 
    photos = models.ImageField(upload_to='meter_photos/',null=True,blank=True)
    count = models.IntegerField(default=0)
    description = models.TextField()
    name = models.CharField(max_length=300,null=True, blank=True)

    class Meta:
        db_table = 'Realestatemeter'
        ordering = ['-id']

    def __str__(self):
        return str(self.name)

class PDFReport(models.Model):
    pdf_file = models.FileField(upload_to='pdf_reports/')

    def __str__(self):
        return self.pdf_file.name
    
class FurnitureInspection(models.Model):

    
    CLEANING_TYPES = [
        ('General Cleaning', 'General Cleaning'),
        ('Sheer Cleaning', 'Sheer Cleaning'),
        ('Linen Cleaning', 'Linen Cleaning'),
    ]
    checkin = models.ForeignKey(CheckInOut, models.DO_NOTHING,null=True,blank=True)   
    cleaning_type = models.CharField(max_length=50, choices=CLEANING_TYPES)
    photos = models.ImageField(upload_to='inspection_photos/',null=True,blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.cleaning_type} - {self.pk}"
    
class Checkincomments(BaseModel):
    checkin = models.ForeignKey(CheckInOut, models.DO_NOTHING)   
    tenantcomment = models.CharField(max_length=500,null=True,blank=True)   
    comment = models.CharField(max_length=500,null=True,blank=True)   

    class Meta:
        db_table = "Checkincomments" 
        ordering = ['-created_at']

class RentalDeduction(models.Model):
    DEDUCTION_TYPES = [
    ('lump_sum', 'Lump Sum'),
    ('tenant_expense', 'At the Tenant Expense'),
    ('invoice_payment', 'Payment by Invoice'),
    ('to_be_defined', 'To Be Defined'),
    ]
    title = models.CharField(max_length=50)
    deduction_type = models.CharField(max_length=50, choices=DEDUCTION_TYPES)
    photo = models.ImageField(upload_to='rental_deductions/')
    description = models.TextField()
    deadline = models.DateTimeField(auto_now_add=True)
    checkinout = models.ForeignKey(CheckInOut, on_delete=models.CASCADE)
    period = models.CharField(max_length=100,null=True,blank=True)   

    def __str__(self):
        return f"{self.title} - {self.pk}"