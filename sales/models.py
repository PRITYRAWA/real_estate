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
    reason_for_moving =models.CharField(max_length=256,null=True,blank=True ,verbose_name=("Reason for Moving"))
    company_name =models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Company name"))
    legal_form =models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Legal form"))
    industry =models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Industry"))
    purpose =models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Purpose"))
    website =models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Website"))
    company_headquarters =models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Company headquarters"))
    founding_year =models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Founding year"))
    correspondence_address =models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Correspondence address"))
    company_registered =models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Company Registered"))
    liability_insurance =models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Liability Insurance"))
    annual_turnover =models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Annual turnover"))
    parking =models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Parking"))
    moving_date =models.DateField(auto_now=True,null=True,blank=True ,verbose_name=("Moving Date"))
    commercial_register =models.FileField(upload_to="images", null=True, blank=True,verbose_name=("Commercial Register"))
    debt_extract =models.FileField(upload_to="images", null=True, blank=True,verbose_name=("Debt Extract"))
    remarks=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Remarks"))
    attachment =models.FileField(upload_to="images", null=True, blank=True,verbose_name=("Attachment"))
    gender=models.CharField(max_length=20,null=True,blank=True ,verbose_name=("Gender"))
    residence_permit=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Residence Permit"))
    address=models.CharField(max_length=265,null=True,blank=True ,verbose_name=("Address"))
    zipcode=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Zipcode"))
    current_landlord_name=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Current landlord's name"))
    landlord_reference_person=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Landlord reference person"))
    landlord_reference_person_phone=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Landlord reference person's phone"))
    landlord_reference_person_email=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Landlord reference person's email"))
    rent_address=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Rent Address"))
    previous_rent=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Previous Rent"))
    employment_status=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Employment status"))
    profession=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Profession"))
    gross_salary_per_year=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Gross salary per year (CHF)"))
    pay_slip =models.FileField(upload_to="images", null=True, blank=True,verbose_name=("Pay Slip"))
    employer=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Employer"))
    employed_since=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Employed since"))
    employer_reference_person=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Employer reference person"))
    employer_reference_person_phn=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Employer reference person's phone"))
    employer_reference_person_email=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Employer reference person's email"))
    employment_contract=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Employment Contract"))
    debt_collection=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("Debt Collection"))
    id_card=models.CharField(max_length=100,null=True,blank=True ,verbose_name=("ID Card"))
    deb_extract=models.FileField(upload_to="images", null=True, blank=True,verbose_name=("Deb Extract"))
    
    class Meta:
        db_table = 'PersonVisit'
        ordering = ['-id']
    
    def __str__(self):
        return str(self.first_name)+' '+str(self.last_name)

class Tender(BaseModel):
    property = models.ForeignKey(Realestateproperties,on_delete=models.PROTECT, null=True, blank=True,verbose_name=("Property")) 
    object = models.ForeignKey(Realestateobjects,on_delete=models.PROTECT, null=True, blank=True,verbose_name=("Object")) 
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
    rent_charges = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    reference = models.CharField(max_length=100, null=True,blank=True)
    number_room = models.CharField(max_length=100, null=True,blank=True)
    floor = models.CharField(max_length=100, null=True,blank=True)
    livingspace = models.CharField(max_length=100, null=True,blank=True)
    construction_year = models.CharField(max_length=100, null=True,blank=True)
    renovation_year = models.CharField(max_length=100, null=True,blank=True)
    available = models.CharField(max_length=100, null=True,blank=True)
    online_debt_extract = models.CharField(max_length=100, null=True,blank=True)
    surroundings = models.CharField(max_length=256, null=True,blank=True)
    description = models.CharField(max_length=256, null=True,blank=True)

    class Meta:
        db_table = 'Tender'
        ordering = ['-id']

    def __str__(self):
        return str(self.role_of_property)
    
    def save(self, *args, **kwargs):
        if not self.link:  # Generate link only if it is not already set
            self.link = f"/tenders/{self.pk}/"
        super().save(*args, **kwargs)