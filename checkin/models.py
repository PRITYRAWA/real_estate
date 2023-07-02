from django.db import models
from masters.models import Realestateobjects,Realestateobjectsdetail,Realestatepropertytenant,Realestateproperties,Realestatekeyhandover,Realestatemeterhandover,Realestatepropertyowner,Appendicesmaster,FurnitureInspectionMaster
from foundation.models import BaseModel
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
    photos = models.ImageField(upload_to='inspection_images/')

    def __str__(self):
        return f"Inspection for {self.real_estate_object}"


#  object list inspection by tenant

class ObjectListInspection(BaseModel):
    #  fk service id link with check in&out, 
    checkin = models.ForeignKey(CheckInOut, on_delete=models.CASCADE, null=True, blank=True)
    object_detail_list = models.ForeignKey(Realestateobjectsdetail, on_delete=models.CASCADE,null=True,blank=True,related_name='object_inspections')
    object_code = models.CharField(max_length=100,null=True,blank=True,verbose_name=("Object Code"))
    category = models.CharField(max_length=100,null=True,blank=True,verbose_name=("Category"))
    related_object = models.ForeignKey(Realestateobjects, on_delete=models.CASCADE,null=True,blank=True,verbose_name=("Related Object"))
    object_name = models.TextField(verbose_name=("Object Name"))
    object_description = models.CharField(max_length=100,null=True,blank=True,verbose_name="Object Description")   
    related_detail = models.ForeignKey('ObjectListInspection', on_delete=models.CASCADE, null=True, blank=True,verbose_name=("Related Detail"),related_name='child_details')
    new = models.BooleanField(blank=True,null=True,verbose_name=("New"))
    inorder = models.BooleanField(blank=True,null=True,verbose_name=("In Order"),default=False)
    normal_wear = models.BooleanField(blank=True,null=True,verbose_name=("Normal Wear"),default=False)
    notes = models.TextField(blank=True, null=True,verbose_name=("Notes"))
    photos = models.ImageField(upload_to='object_images_transaction/',blank=True, null=True,verbose_name=("Image"))
    count = models.IntegerField(default=0,verbose_name=("Count"),null=True,blank=True)

    class Meta:
        db_table = 'Object transaction'
        ordering = ['-id']

    def __str__(self):
        return f'Object {self.object_name}'

class Realestatekey(BaseModel):
    checkin = models.ForeignKey(CheckInOut,on_delete=models.CASCADE, null=True, blank=True) 
    obj = models.ForeignKey(Realestatekeyhandover,on_delete=models.CASCADE, null=True, blank=True) 
    photos = models.ImageField(upload_to='key_photos/',null=True,blank=True)
    count = models.IntegerField(default=0,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    name = models.CharField(max_length=300,null=True, blank=True)

    class Meta:
        db_table = 'Realestatekey'
        ordering = ['-id']

    def __str__(self):
        return str(self.name)
    
class Realestatemeter(BaseModel):
    checkin = models.ForeignKey(CheckInOut,on_delete=models.CASCADE, null=True, blank=True) 
    obj = models.ForeignKey(Realestatemeterhandover,on_delete=models.CASCADE, null=True, blank=True) 
    UNIT_CHOICES = [
        ('Kwh', 'Kwh'),
        ('m3', 'm3'),
        ('litres', 'litres'),
        ('units', 'units'),
        ('steres', 'steres'),
    ]
    COMPANY_CHOICES = [
        ('company1','company1'),
        ('company2','company2'),
        ('company3','company3'),
    ]
    WHO_CHANGES = [
        ('user','user'),
        ('admin','admin'),
    ]
    name = models.CharField(max_length=300,null=True, blank=True,verbose_name=("Name"))
    meterno = models.CharField(max_length=200,null=True,blank=True,verbose_name=("Meter Number"))
    reading = models.CharField(max_length=200,null=True,blank=True,verbose_name=("Reading"))
    photos = models.ImageField(upload_to='meter_photos/',null=True,blank=True,verbose_name=("Photo"))
    count = models.IntegerField(default=0,null=True,blank=True,verbose_name=("Count"))
    unit = models.CharField(max_length=10,choices=UNIT_CHOICES,default='Kwh',null=True,blank=True,verbose_name=("Unit"))
    whochange = models.CharField(max_length=200,choices=WHO_CHANGES,null=True,blank=True,verbose_name=("Who Change"))
    company = models.CharField(max_length=100,choices=COMPANY_CHOICES,null=True,blank=True,verbose_name=("Company "))
    description = models.TextField(null=True,blank=True,verbose_name=("Description"))

    class Meta:
        db_table = 'Realestatemeter'
        ordering = ['-id']

    def __str__(self):
        return str(self.name)

class PDFReport(models.Model):
    pdf_file = models.FileField(upload_to='pdf_reports/')

    def __str__(self):
        return self.pdf_file.name
    
class FurnitureInspection(BaseModel):

    
    CLEANING_TYPES = [
        ('General Cleaning', 'General Cleaning'),
        ('Sheer Cleaning', 'Sheer Cleaning'),
        ('Linen Cleaning', 'Linen Cleaning'),
    ]
    checkin = models.ForeignKey(CheckInOut, models.DO_NOTHING,null=True,blank=True)   
    # obj = models.ForeignKey(FurnitureInspectionMaster,on_delete=models.CASCADE, null=True, blank=True) 
    cleaning_type = models.CharField(max_length=50, choices=CLEANING_TYPES)
    photos = models.ImageField(upload_to='inspection_photos/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.cleaning_type} - {self.pk}"
    

class RentalDeduction(BaseModel):
    DEDUCTION_TYPES = [
    ('lum-sum', 'Lump Sum'),
    ('tenant_expense', 'At Tenant Expense'),
    ('invoice_payment', 'Payment by Invoice'),
    ('to_be_defined', 'To Be Defined'),
    ]
    title = models.CharField(max_length=50)
    deduction_type = models.CharField(max_length=50, choices=DEDUCTION_TYPES)
    photos = models.ImageField(upload_to='rental_deductions/',null=True,blank=True)
    description = models.TextField()
    deadline = models.DateTimeField(auto_now_add=True)
    checkin = models.ForeignKey(CheckInOut, on_delete=models.CASCADE)
    period = models.CharField(max_length=100,null=True,blank=True)   

    class Meta:
        db_table = 'Rental_deduction'
        ordering = ['-id']

    def __str__(self):
        return str(self.title)  

class Appendicestransaction(BaseModel):
    checkin = models.ForeignKey(CheckInOut, models.DO_NOTHING,null=True,blank=True)   
    obj = models.ForeignKey(Appendicesmaster,on_delete=models.CASCADE, null=True, blank=True) 
    photos = models.ImageField(upload_to='master_key_photos/',null=True, blank=True,verbose_name=("Photos"))
    count = models.IntegerField(default=0,verbose_name=("Count"),null=True,blank=True)
    description = models.TextField(null=True, blank=True,verbose_name=("Description"))
    name = models.CharField(max_length=300,null=True, blank=True,verbose_name=("Name"))

    class Meta:
        db_table = 'Appendices_transaction'
        ordering = ['-id']

    def __str__(self):
        return str(self.name)  

class Checkincomments(BaseModel):
    realestateownerid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING)  
    checkin = models.ForeignKey(CheckInOut, models.DO_NOTHING,null=True,blank=True)   
    tenantcomment = models.CharField(max_length=500,null=True,blank=True)   
    comment = models.CharField(max_length=500,null=True,blank=True)   

    class Meta:
        db_table = "Checkincomments" 
        ordering = ['-created_at']
