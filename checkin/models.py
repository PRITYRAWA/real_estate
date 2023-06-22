from django.db import models
from masters.models import Realestateobjects,Realestateobjectsdetail,Realestatepropertytenant,Realestateproperties,Realestatekeyhandover,Realestatemeterhandover
from foundation.models import BaseModel,CustomUser
import uuid
from django.contrib.postgres.fields import ArrayField
import json
# # user registration model
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     full_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['full_name']

#     def __str__(self):
#         return self.email
    

# inspection model  

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
class StringArrayField(models.TextField):
    def from_db_value(self, value, expression, connection):
        if value is None:
            return []
        return json.loads(value)

    def to_python(self, value):
        if isinstance(value, list):
            return value
        if value is None:
            return []
        return json.loads(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        return json.dumps(value)

class Realestatekey(BaseModel):
    checkin = models.ForeignKey(CheckInOut,on_delete=models.CASCADE, null=True, blank=True) 
    obj = models.ForeignKey(Realestatekeyhandover,on_delete=models.CASCADE, null=True, blank=True) 
    photos = StringArrayField(null=True, blank=True)
    count = models.IntegerField(default=0)
    description = models.TextField()
    name = models.CharField(max_length=300,null=True, blank=True)

    class Meta:
        db_table = 'Realestatekey'
        ordering = ['-id']

    def __str__(self):
        return str(self.name)
    
# class Realestatemeter(BaseModel):
#     checkin = models.ForeignKey(CheckInOut,on_delete=models.CASCADE, null=True, blank=True) 
#     obj = models.ForeignKey(Realestatemeterhandover,on_delete=models.CASCADE, null=True, blank=True) 
#     photo = models.FileField(upload_to='keys_photos/',null=True,blank=True)
#     count = models.IntegerField(default=0)
#     description = models.TextField()
#     name = models.CharField(max_length=300,null=True, blank=True)

#     class Meta:
#         db_table = 'Realestatemeter'
#         ordering = ['-id']

#     def __str__(self):
#         return str(self.name)

class PDFReport(models.Model):
    pdf_file = models.FileField(upload_to='pdf_reports/')

    def __str__(self):
        return self.pdf_file.name