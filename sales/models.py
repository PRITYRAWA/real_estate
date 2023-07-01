from django.db import models
from foundation.models import BaseModel
from masters.models import *
# Create your models here.

class PersonVisit(BaseModel):
    first_name = models.CharField(max_length=100, verbose_name=("First Name"))
    last_name = models.CharField(max_length=100, verbose_name=("Last Name"))
    email = models.EmailField(verbose_name=("Email"))
    phone_number = models.CharField(max_length=20, verbose_name=("Phone Number"))
    birthday = models.DateField(verbose_name=("Birthday"))
    marital_status = models.CharField(max_length=20, verbose_name=("Marital Status"))
    nationality = models.CharField(max_length=100, verbose_name=("Nationality"))
    further_details = models.TextField(verbose_name=("Further Details"))
    desired_move_in_date = models.DateField(verbose_name=("Move-in Date"))
    has_pet = models.BooleanField(verbose_name=("Pet?"))
    plays_instrument = models.BooleanField(verbose_name=("Play instruments?"))
    parking_service = models.BooleanField(verbose_name=("Parking service?"))
    has_done_visit = models.BooleanField(verbose_name=("Have you done a visit?"))
    description = models.TextField(verbose_name=("Description"))

    class Meta:
        db_table = 'PersonVisit'
        ordering = ['-id']

class Tender(BaseModel):
    property = models.ForeignKey(Realestateproperties,on_delete=models.CASCADE, null=True, blank=True,verbose_name=("Property")) 
    object = models.ForeignKey(Realestateobjects,on_delete=models.CASCADE, null=True, blank=True,verbose_name=("Object")) 
    net_rent_total_per_month = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    net_rent_total_per_year = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    incidental_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    gross_rent_total_per_month = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    gross_rent_total_per_year = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    move_in_date = models.DateField(null=True)
    display_rent_per_month = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    furnished = models.BooleanField(default=False)
    unfurnished = models.BooleanField(default=False)
    role_of_property = models.CharField(max_length=100, blank=True)
    assigned_manager = models.CharField(max_length=100, blank=True)
    contact_person = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    link = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'Tender'
        ordering = ['-id']

    def __str__(self):
        return str(self.role_of_property)
    
    def save(self, *args, **kwargs):
        if not self.link:  # Generate link only if it is not already set
            self.link = f"/tenders/{self.pk}/"
        super().save(*args, **kwargs)