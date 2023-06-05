from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from . manager import *

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

# object(flat) model
class RealEstateObjects(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    floor = models.CharField(max_length=100)
    surface_area = models.IntegerField(null=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

#object detail model
class RealEstateObjectsDetails(models.Model):
    related_object = models.OneToOneField(RealEstateObjects, on_delete=models.CASCADE)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Details for {self.object}"



# checkin model
class CheckIn(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    object_check_in = models.ForeignKey(RealEstateObjects, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_in_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    inspection = models.ForeignKey('Inspection', on_delete=models.SET_NULL, null=True, blank=True)
    object_details = models.ManyToManyField(RealEstateObjectsDetails)

    def __str__(self):
        return f"{self.user.full_name} checked into {self.object_check_in}"


# inspection model  

class Inspection(models.Model):
    object = models.ForeignKey(RealEstateObjects, on_delete=models.CASCADE)
    inspection_report = models.TextField()

    def __str__(self):
        return f"Inspection for {self.object}"
    
# inspection of keys
class InspectionOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class InspectionImage(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE, related_name='images')
    option = models.ForeignKey(InspectionOption, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='inspection_images/')

    def __str__(self):
        return f"Image for {self.option.name} in {self.inspection}"


class CheckOut(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    object_check_out = models.ForeignKey(RealEstateObjects, on_delete=models.CASCADE)
    check_out_date = models.DateField()
    check_out_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.full_name} checked out from {self.object_check_out}"

    def perform_inspections(self):
        for detail in self.object_check_out.object_details.all():
            inspection = Inspection.objects.create(object=self.object_check_out)
            inspection.inspection_report = f"Inspection report for {detail}"
            inspection.save()




