from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from . manager import *
from masters.models import Realestateobjects, ObjectDetailList,RealEstateObjectsDetails
import uuid
# user registration model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email
    

# inspection model  

# checkin model
class CheckInOut(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service_ticket_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    object_check_in = models.ForeignKey(Realestateobjects, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_in_time = models.TimeField()
    check_out_date = models.DateField()
    check_out_time = models.TimeField()
    inspection_date_time = models.DateTimeField()
    object_details = models.ManyToManyField(RealEstateObjectsDetails)
    object_detail_list = models.ForeignKey('ObjectListInspection', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.full_name} checked into {self.object_check_in}"

class GeneralInspection(models.Model):
    #  fk service id link with check in&out, 
    service_id = models.ForeignKey(CheckInOut, on_delete=models.CASCADE, null=True, blank=True)
    real_estate_object = models.ForeignKey(Realestateobjects, on_delete=models.CASCADE,related_name='inspections')
    inspection_report = models.TextField()
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='inspection_images/')

    def __str__(self):
        return f"Inspection for {self.real_estate_object}"


#  object list inspection by tenant

class ObjectListInspection(models.Model):
    #  fk service id link with check in&out, 
    service_id = models.ForeignKey(CheckInOut, on_delete=models.CASCADE, null=True, blank=True)
    object_detail_list = models.ForeignKey(RealEstateObjectsDetails, on_delete=models.CASCADE,related_name='inspections')
    new = models.BooleanField(default=False)
    inorder = models.BooleanField(default=False)
    normal_wear = models.BooleanField(blank=True,null=True)
    notes = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='object_images_teenant/')   
    def __str__(self):
        return f'Object {self.id}'






