from django.db import models
from django_countries.fields import CountryField
from foundation.models import BaseModel
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

class Realestateagents(BaseModel):
    prefix = models.CharField(max_length=5,verbose_name=("Prefix")) 
    name = models.CharField(max_length=50,verbose_name=("Name")) 
    email = models.CharField(max_length=320, blank=True, null=True,verbose_name=("Email"))  
    website = models.TextField(blank=True, null=True,verbose_name=("Website"))  
    phonenumber = models.CharField(max_length=30, blank=True, null=True,verbose_name=("Phone Number")) 
    street = models.CharField(max_length=100,blank=True, null=True,verbose_name=("Street")) 
    zip = models.CharField(max_length=10, blank=True, null=True,verbose_name=("Zip"))  
    city = models.CharField(max_length=50, blank=True, null=True,verbose_name=("City"))  
    country = CountryField( blank=True, null=True,verbose_name=("Country")) 

    class Meta:
        db_table = "Realestateagents"
        verbose_name = "Agents"
        ordering = ['-id']
    def __str__(self):
        return str(self.name)

class Realestatepropertyowner(BaseModel):
    name = models.CharField(max_length=50,verbose_name=("Name"))   
    surname = models.CharField(max_length=100,verbose_name=("Surname"))   
    email = models.CharField(max_length=320, blank=True, null=True,verbose_name=("Email"))   
    phonenumber = models.CharField(max_length=30, blank=True, null=True,verbose_name=("Phone Number"))   
    street = models.CharField(max_length=100,blank=True, null=True,verbose_name=("Street"))   
    zip = models.CharField(max_length=10, blank=True, null=True,verbose_name=("Zip"))   
    city = models.CharField(max_length=50, blank=True, null=True,verbose_name=("City"))   
    country = CountryField( blank=True, null=True,verbose_name=("Country"))    
    owner_representative = models.CharField( max_length=50, blank=True, null=True,verbose_name=("Owner Representative")) 
    isnotificationnewtickets = models.BooleanField(default=False,verbose_name=("Is Notification New Tickets"))   
    isnotificationnewupdates = models.BooleanField(default=False,verbose_name=("Is Notification New Updates"))   
    isnotificationticketdeadline = models.BooleanField(default=False,verbose_name=("Is Notification Ticket Deadline"))   
    isactive = models.BooleanField(default=False,verbose_name=("Is Active"))   
    lastlogindate = models.DateTimeField(null=True, blank=True,verbose_name=("Last Logindate"))   
    attachment = models.FileField(upload_to='attachement/',blank=True, null=True,verbose_name=("Attachment")) 

    class Meta:
        db_table = "Realestatepropertyowner"
        verbose_name = "Owners"
        ordering = ['-id']

    def __str__(self):
        return str(self.name)
    
class Realestatepropertytenant(BaseModel):
    STATUS_CHOICES = [
        ('ENQUIRER', 'Enquirer'),
        ('REGISTER', 'Register'),
        ('OCCUPIED', 'Occupied'),
        ('VACATOR', 'Vacator'),
    ]
    
    userid = models.CharField( max_length=36, blank=True, null=True,verbose_name=("User Id"))  
    realestatepersontypeid = models.IntegerField(null=True,blank=True,verbose_name=("Person Type Id"))  
    name = models.CharField(max_length=50,null=True,blank=True,verbose_name=("Name"))  
    surname = models.CharField(max_length=100,null=True,blank=True,verbose_name=("Surname"))  
    email = models.CharField(max_length=320, blank=True, null=True,verbose_name=("Email"))  
    phonenumber = models.CharField(max_length=30, blank=True, null=True,verbose_name=("Phone Number"))  
    country = CountryField( blank=True, null=True,verbose_name=("Country"))    
    state = models.CharField(max_length=100,null=True,blank=True,verbose_name=("State"))  
    street = models.CharField(max_length=100,null=True,blank=True,verbose_name=("Street"))  
    zip = models.CharField(max_length=10, blank=True, null=True,verbose_name=("Zip"))  
    city = models.CharField(max_length=50, blank=True, null=True,verbose_name=("City"))  
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='ENQUIRER',null=True,blank=True,verbose_name=("Status"))

    state = models.CharField(max_length=100,null=True,blank=True,verbose_name=("State"))  
    class Meta:
        db_table = "Realestatepropertytenant"
        verbose_name = "Tenants"
        ordering = ['-id']
      
    def __str__(self):
        return str(self.name)

class Messages(BaseModel):
    realestateagentid = models.ForeignKey('Realestateagents', on_delete=models.PROTECT)   
    subject = models.CharField(max_length=150)   
    body = models.CharField(max_length=2500)   
    isemailnotification = models.BooleanField(default=False)   
    isimportant = models.BooleanField(default=False)   
    isallowcomment = models.BooleanField(default=False)   
    issendimmediately = models.BooleanField(default=False)   
    senddate = models.DateTimeField(blank=True, null=True)   
    created = models.DateTimeField(blank=True, null=True)   
    createdrealestateownerid = models.ForeignKey('Realestatepropertyowner', on_delete=models.PROTECT)   
    isdeleted = models.BooleanField(default=False)   
    attachments = models.TextField(blank=True, null=True)   

    class Meta:
        db_table = "Messages"  
        verbose_name = "not required"
        ordering = ['-id']

class Messagecomments(BaseModel):
    messageid = models.ForeignKey('Messages', on_delete=models.PROTECT ,null=True,blank=True)   
    realestateownerid = models.ForeignKey('Realestatepropertyowner', on_delete=models.PROTECT)   
    tenantcomment = models.CharField(max_length=500,null=True,blank=True)   
    comment = models.CharField(max_length=500,null=True,blank=True)   

    class Meta:
        db_table = "Messagecomments" 
        verbose_name = "not required"
        ordering = ['-created_at']


class Messagerecipients(BaseModel):
    messageid = models.ForeignKey('Messages', on_delete=models.PROTECT)   
    realestateownerid = models.OneToOneField('Realestatepropertyowner', on_delete=models.PROTECT, primary_key=True) 
    isread = models.BooleanField(default=True)   
    readdate = models.DateTimeField(blank=True, null=True)   

    class Meta:
        db_table = "Messagerecipients" 
        verbose_name = "not required"
        ordering = ['-created_at']
    

class Realestateproperties(BaseModel):
    realestateagentid = models.ForeignKey(Realestateagents, on_delete=models.PROTECT,verbose_name=("Agent Id"),null=True,blank=True) 
    realted_property = models.ForeignKey('Realestateproperties',null=True, blank=True,on_delete=models.PROTECT,related_name="sub_group",verbose_name=("Realted Property"))  
    name = models.CharField(max_length=50,verbose_name=("Name"))   
    street = models.CharField(max_length=100,verbose_name=("Street"))   
    zip = models.CharField(max_length=10,verbose_name=("Zip"))   
    city = models.CharField(max_length=50,verbose_name=("City"))   
    country = CountryField( blank=True, null=True,verbose_name=("Country"))     
    isactive = models.BooleanField(default=False,verbose_name=("Is Active"))   
    attachment = models.FileField(upload_to='attachement/',blank=True, null=True,verbose_name=("Attachment")) 


    class Meta:
        db_table = "Realestateproperties" 
        verbose_name = "Properties"
        ordering = ['-id']

    def __str__(self):
        return str(self.name)

    
class Feedbacks(BaseModel):
    comment = models.CharField(db_column='Comment', max_length=500,   )   
    class Meta:
        db_table = 'Feedbacks'
        verbose_name = "not required"
        ordering = ['-id']


class Languages(BaseModel):
    id = models.AutoField(db_column='Id', primary_key=True)   
    name = models.CharField(db_column='Name', max_length=50,   )   
    languagecode = models.CharField(db_column='LanguageCode', unique=True, max_length=2,   )   
    displayorder = models.IntegerField(db_column='DisplayOrder')   

    class Meta:
        db_table = 'Languages'
        verbose_name = "not required"
        ordering = ['-id']
    

class Localestringresources(BaseModel):
    id = models.AutoField(db_column='Id', primary_key=True)   
    name = models.TextField(db_column='Name',   )   
    value = models.TextField(db_column='Value',   )   
    languageid = models.ForeignKey(Languages, on_delete=models.PROTECT, db_column='LanguageId')   

    class Meta:
        db_table = 'LocaleStringResources'
        verbose_name = "not required"
        ordering = ['-id']

class Localizedproperties(BaseModel):
    id = models.AutoField(db_column='Id', primary_key=True)   
    entityid = models.CharField(db_column='EntityId', max_length=36)   
    languageid = models.ForeignKey(Languages, on_delete=models.PROTECT, db_column='LanguageId')   
    entityname = models.CharField(db_column='EntityName', max_length=100,   )   
    propertyname = models.CharField(db_column='PropertyName', max_length=100,   )   
    localevalue = models.TextField(db_column='LocaleValue',   )   

    class Meta:
        db_table = 'LocalizedProperties'
        verbose_name = "not required"
        ordering = ['-id']

#model created for subgroup details in meeting 
class Realestatepropertiessubgroup(BaseModel):
    property = models.ForeignKey(Realestateproperties,on_delete=models.PROTECT,verbose_name=("Property"))
    name =  models.CharField(max_length=100,null=True, blank=True, verbose_name=("Name"))
    Description = models.TextField(null=True, blank=True, verbose_name=("Description"))
    area =  models.CharField(max_length=100,null=True, blank=True, verbose_name=("Area"))
    amenities = models.CharField(max_length=100,null=True, blank=True, verbose_name=("Amenities"))

    class Meta:
        db_table = 'Realestatepropertiessubgroup'
        verbose_name = "not required"
        ordering = ['-id']
    
    def __str__(self):
        return str(self.name)

class Realestateobjects(BaseModel):
    STATUS_CHOICES = [
        ('OCCUPIED', 'Occupied'),
        ('VACANT', 'vacant'),
    ]
    USAGE_CHOICE = [
        ('COMMERCIAL','commercial'),
        ('RESIDENCE','residence'),
        ('private','private'),
        ('PUBLIC','public'),
        ('OTHERS','others'),
    ]
    realestatepropertyid = models.ForeignKey(Realestateproperties,related_name="objects_detail",on_delete=models.PROTECT,null=True,blank=True, verbose_name=("Property Id"))
    objectusagetypeid = models.CharField(max_length=10,choices=USAGE_CHOICE,null=True,blank=True,verbose_name=("Usage Type id"))
    object_name = models.CharField(max_length=50,verbose_name=("Object Name"))   
    object_description = models.CharField(max_length=100,verbose_name="Object Description")   
    location = models.CharField(max_length=100,verbose_name="Location")   
    floor = models.CharField(max_length=20,blank=True, null=True,verbose_name=("Floor"))   
    rooms = models.CharField(max_length=20, blank=True, null=True,verbose_name=("Rooms"))
    value = models.FloatField(default=0.0,  null=True, blank=True,verbose_name=("Value")) 
    surfacearea = models.IntegerField(blank=True, null=True,verbose_name=("Surface Area"))   
    isactive = models.BooleanField(default=False,verbose_name=("Is Active"))   
    attachments = models.FileField(upload_to='attachement/',blank=True, null=True,verbose_name=("Attachments"))   
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='VACANT',null=True,blank=True,verbose_name=("Status"))

    class Meta:
        db_table = 'Realestateobjects'
        verbose_name = "Objects"
        ordering = ['-id']

    def __str__(self):
        return str(self.object_name)
    
#object detail model
class Realestateobjectsdetail(BaseModel):
    CATEGORY_CHOICES = [
        ('furniture_inspection', 'Furniture inspection'),
        ('property_inspection', 'Property inspection'),
    ]
    object_code = models.CharField(max_length=15,null=True,blank=True,verbose_name=("Object Code"))
    category_type = models.CharField(max_length=30, null=True, blank=True, choices=CATEGORY_CHOICES, verbose_name=("Category_Type"))
    category = models.CharField(max_length=50, null=True, blank=True, verbose_name=("Category"))
    related_object = models.ForeignKey(Realestateobjects, on_delete=models.PROTECT,null=True,blank=True,related_name='object_detail',verbose_name=("Related Object"))
    related_property = models.ForeignKey(Realestateproperties, on_delete=models.PROTECT,null=True,blank=True,verbose_name=("Related Property"))
    object_name = models.CharField(max_length=100,verbose_name=("Object Name"))
    object_description = models.CharField(max_length=100,null=True,blank=True,verbose_name="Object Description")   
    related_detail = models.ForeignKey('Realestateobjectsdetail', on_delete=models.PROTECT, null=True, blank=True,verbose_name=("Related Detail"),related_name='child_details')
    new = models.BooleanField(blank=True,null=True,verbose_name=("New"))
    inorder = models.BooleanField(blank=True,null=True,verbose_name=("In Order"),default=False)
    normal_wear = models.BooleanField(blank=True,null=True,verbose_name=("Normal Wear"),default=False)
    notes = models.TextField(blank=True, null=True,verbose_name=("Notes"))
    image = models.ImageField(upload_to='object_images_master/',null=True,blank=True,verbose_name=("Image"))
    count = models.IntegerField(default=0,verbose_name=("Count"),null=True,blank=True)

    class Meta:
        db_table = 'Realestateobjectsdetail'
        verbose_name = "Object Details"
        ordering = ['-id']

    def __str__(self):
        return str(self.object_name)

class Realestatekeyhandover(BaseModel):
    STATE_CHOICES = (
        ('1_missing', '1 Missing'),
        ('2_missing', '2 Missing'),
        ('3_missing', '3 Missing'),
    )
    DETERIORATION_CHOICES = (
        ('1_damaged', '1 Damaged'),
        ('2_damaged', '2 Damaged'),
        ('3_damaged', '3 Damaged'),
    )
    state = MultiSelectField(choices=STATE_CHOICES, max_length=30,null=True, blank=True, verbose_name="State")
    deterioration = MultiSelectField(choices=DETERIORATION_CHOICES,max_length=30, null=True, blank=True, verbose_name="Deterioration")
    others = models.CharField(max_length=50,null=True,blank=True)
    property = models.ForeignKey(Realestateproperties, null=True, blank=True,verbose_name=("Property"), on_delete=models.PROTECT) 
    object = models.ForeignKey(Realestateobjects,on_delete=models.PROTECT, null=True, blank=True,verbose_name=("Object")) 
    photo = models.ImageField(upload_to='master_key_photos/',null=True, blank=True,verbose_name=("Photo"))
    count = models.IntegerField(default=0,verbose_name=("Count"), null=True, blank=True)
    description = models.TextField(null=True, blank=True,verbose_name=("Description"))
    name = models.CharField(max_length=300,null=True, blank=True,verbose_name=("Name"))
   
    class Meta:
        db_table = 'Realestatekeyhandover'
        verbose_name = "Keys"
        ordering = ['-id']

    def __str__(self):
        return str(self.name)

class Realestatemeterhandover(BaseModel):
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
    STATE_CHOICES = [
        ('new', 'New'),
        ('no_longer_works', 'No Longer Works'),
        ('inaccessible', 'Inaccessible'),
    ]
    CLEANING_CHOICES = [
        ('incomplete', 'Incomplete Cleaning'),
    ]
    DETERIORATION_CHOICES = [
        ('leak', 'Leak'),
        ('broken_glass', 'Broken Glass'),
        ('damaged_items', 'Damaged Items'),
        ('partially_erased', 'Partially Erased'),
        ('erased', 'Erased'),
    ]
    ACCESSORIES_CHOICES = [
        ('missing_accessories', 'Missing Accessories'),
    ]
    name = models.CharField(max_length=300,null=True, blank=True,verbose_name=("Name"))
    property = models.ForeignKey(Realestateproperties,on_delete=models.PROTECT, null=True, blank=True,verbose_name=("Property")) 
    object = models.ForeignKey(Realestateobjects,on_delete=models.PROTECT, null=True, blank=True,verbose_name=("Object")) 
    meterno = models.CharField(max_length=200,null=True,blank=True,verbose_name=("Meter Number"))
    reading = models.CharField(max_length=200,null=True,blank=True,verbose_name=("Reading"))
    photos = models.ImageField(upload_to='master_meter_photos/',null=True,blank=True,verbose_name=("Photo"))
    count = models.IntegerField(default=0,verbose_name=("Count"),null=True,blank=True)
    unit = models.CharField(max_length=10,choices=UNIT_CHOICES,null=True,blank=True,verbose_name=("Unit"))
    whochange = models.CharField(max_length=200,choices=WHO_CHANGES,null=True,blank=True,verbose_name=("Who Change"))
    company = models.CharField(max_length=100,choices=COMPANY_CHOICES,null=True,blank=True,verbose_name=("Company "))
    description = models.TextField(null=True,blank=True,verbose_name=("Description"))
    state = MultiSelectField(choices=STATE_CHOICES, max_length=30,null=True, blank=True, verbose_name=("State"))
    cleaning = MultiSelectField(choices=CLEANING_CHOICES, max_length=30,null=True, blank=True, verbose_name=("Cleaning"))
    deterioration = MultiSelectField(choices=DETERIORATION_CHOICES, max_length=30,null=True, blank=True, verbose_name=("Deterioration"))
    accessories = MultiSelectField(choices=ACCESSORIES_CHOICES, max_length=30,null=True, blank=True, verbose_name=("Accessories"))
    others = models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        db_table = 'Realestatemeterhandover'
        verbose_name = "Meters"
        ordering = ['-id']

    def __str__(self):
        return str(self.name)

class FurnitureInspectionMaster(BaseModel):
    CLEANING_TYPES = [
        ('General Cleaning', 'General Cleaning'),
        ('Sheer Cleaning', 'Sheer Cleaning'),
        ('Linen Cleaning', 'Linen Cleaning'),
    ]
    property = models.ForeignKey(Realestateproperties,on_delete=models.PROTECT, null=True, blank=True,verbose_name=("Property")) 
    object = models.ForeignKey(Realestateobjects,on_delete=models.PROTECT, null=True, blank=True,verbose_name=("Object"))    
    cleaning_type = models.CharField(max_length=50, choices=CLEANING_TYPES,verbose_name=("Cleaning Type"))
    photos = models.ImageField(upload_to='master_inspection_photos/',null=True,blank=True,verbose_name=("Photos"))
    description = models.TextField()

    def __str__(self):
        return f"{self.cleaning_type} - {self.pk}"
    
    class Meta:
        db_table = 'FurnitureInspectionMaster'
        verbose_name = "Furniture Inspection Master"
        ordering = ['-id']
    
class Realestatepropertymanagement(BaseModel):
    realestatepropertyid = models.ForeignKey(Realestateproperties, on_delete=models.PROTECT,verbose_name=_("Property") ) 
    realestateownerid = models.ForeignKey(Realestatepropertyowner, on_delete=models.PROTECT,verbose_name=_("Property Owner"))  
    realestateagentid = models.ForeignKey(Realestateagents, on_delete=models.PROTECT,null=True,blank=True,verbose_name=_("Property Agent")) 
    realestateobjectid = models.ForeignKey(Realestateobjects, on_delete=models.PROTECT,null=True,blank=True,verbose_name=_("Property Object"))
    manageby = models.CharField(max_length=10, choices=(('owner', 'Owner'), ('agent', 'Agent')),verbose_name=_("Manage By"))
    manageby_id = models.CharField(max_length=100,null=True,blank=True,verbose_name=_("Manager Id"))
    manager_name = models.CharField(max_length=100,null=True,blank=True,verbose_name=_("Manager Name"))
    manager_email = models.CharField(max_length=100,null=True,blank=True,verbose_name=_("Manager Email"))
    manager_Phone = models.CharField(max_length=100,null=True,blank=True,verbose_name=_("Manager Phone"))
    object_count= models.IntegerField(default=1,verbose_name=("Object Count")) 
    asset_value=models.FloatField(default=0.0,  null=True, blank=True,verbose_name=("Asset Value"))

    class Meta:
        db_table = 'Realestatepropertymanagement'
        verbose_name = "Property Managers"
        ordering = ['-id']
   
    def __str__(self):
        return str(self.manager_name)

class Realestateserviceproviders(BaseModel):
    jobs = (
        ("manager", ("Manager")),
        ("others", ("Others")),
    )
    realestatepropertyid = models.ForeignKey(Realestateproperties, on_delete=models.PROTECT,null=True,blank=True,verbose_name=("Realestate Property"))   
    name = models.CharField(max_length=50,verbose_name=("Name"))   
    field = models.CharField(max_length=50, blank=True, null=True,verbose_name=("Field"))   
    languageid = models.IntegerField(null=True,blank=True,verbose_name=("Language Id"))   
    contactname = models.TextField(blank=True, null=True,verbose_name=("Contact Name"))   
    phonenumber = models.CharField(max_length=30,verbose_name=("Phone Number"))   
    email = models.CharField(max_length=320,verbose_name=("Email"))   
    street = models.CharField(max_length=100,verbose_name=("Street"))   
    zip = models.CharField(max_length=10,verbose_name=("Zip"))   
    city = models.CharField(max_length=50,verbose_name=("City")) 
    country = CountryField( blank=True, null=True)  
    isactive = models.BooleanField(default=False,verbose_name=("Is Active"))
    job = models.CharField(max_length=20, choices= jobs ,default='others',verbose_name=("Job") )  

    class Meta:
        db_table = 'Realestateserviceproviders'
        verbose_name = "Service Providers"
        ordering = ['-id']

    def __str__(self):
        return str(self.name)

class Agenda(BaseModel):
    status = (
        ("draft", ("Draft")),
        ("definitive", ("Definitive")),
    )
    topic=models.CharField(max_length=100, blank=False, null=False,verbose_name=("Topic"))
    status=models.CharField(max_length=20, choices= status ,default='draft',verbose_name=("Status") )
    
    class Meta:
        db_table = 'Agenda'
        verbose_name = "Agenda Template"
        ordering = ['-id']
    
    def __str__(self):
        return str(self.topic)

class AgendaDetails(BaseModel):
    agenda = models.ForeignKey(Agenda,related_name="agenda_detail",on_delete=models.PROTECT,verbose_name=("Agenda"))
    topic_details=models.CharField(max_length=100, blank=True, null=True,verbose_name=("Topic Details"))

    class Meta:
        db_table = 'AgendaDetails'
        verbose_name = "Agenda Details"
        ordering = ['-id']
    
    def __str__(self):
        return str(self.agenda.topic)

class Quorums(BaseModel):
    types = (
        ("head", ("Head Votes")),
        ("object", ("Object Votes")),
        ("value", ("Value Votes")),
    )
    condition=(
        ("greater than or equals to",(">=")),
        ("greater than",(">")),
    )
    voting_type=models.CharField(max_length=20, choices=types,verbose_name=("Voting Type"))
    present_votes=models.IntegerField(blank=False, null=False,verbose_name=("Present Votes"))
    condition = models.CharField(max_length=30,choices=condition, blank=False, null=False,verbose_name=("Condition"))

    class Meta:
        db_table = 'Quorums'
        verbose_name = "Quorums"
        ordering = ['-id']
    
    def __str__(self):
        return str(self.voting_type)

class Votes(BaseModel):
    
    types = (
        ("head", ("Head Votes")),
        ("object", ("Object Votes")),
        ("value", ("Value Votes")),
    )
    cases = (
        ("rejected", ("Rejected")),
        ("accepted", ("Accepted")),
      
    )
    sets=(
        ("representatives_owners",("Presence/representatives Owner")),
        ("total_owner",("Total owners")),
        ("voting_owners_without_abstentions",("Only voting owners without abstentions")),
    )
    tabs =(
        ("simple",("Simple Majority")),
        ("qualified",("qualified Majority")),
        ("unanimous",("Unanimous Vote Tab")),
    )
    condition=(
        ("greater than or equals to",(">=")),
        ("greater than",(">")),
    )
    #quorums = models.ForeignKey(Quorums,related_name="meeting_votes",on_delete=models.PROTECT,verbose_name=("Quorums"))
    tabs = models.CharField(max_length=50, choices=tabs, default='qualified',verbose_name=("Tabs"))
    voting_type=models.CharField(max_length=50, choices=types,verbose_name=("Voting Type"))
    majority=models.IntegerField(blank=False, null=False,verbose_name=("Majority"))
    condition = models.CharField(max_length=30,choices=condition, blank=False, null=False,verbose_name=("Condition"))
    basic_set=models.CharField(max_length=50, choices=sets,verbose_name=("Basic Set"))
    tie_case= models.CharField(max_length=50, choices=cases,verbose_name=("Tie Case"))
    
    class Meta:
        db_table = 'Votes'
        verbose_name = "Votes"
        ordering = ['-id']
    
    def __str__(self):
        return str(self.voting_type)

class Mettingtemplate(BaseModel):
    quorum = models.ForeignKey(Quorums,related_name="quorum",on_delete=models.PROTECT,verbose_name=("Quorums"))
    votes = models.ForeignKey(Votes,related_name="votes",on_delete=models.PROTECT,verbose_name=("Votes"))
    agenda = models.ForeignKey(Agenda,related_name="agenda",on_delete=models.PROTECT,verbose_name=("Agenda"))
    voting_circle = models.ForeignKey(Realestatepropertymanagement,related_name="voting_circle",on_delete=models.PROTECT,verbose_name=("Voting Circle"))
    
    class Meta:
        db_table = 'Mettingtemplate'
        verbose_name = "Meeting Template"
        ordering = ['-id']

    def __str__(self):
        return str(self.agenda.topic)

class Appendicesmaster(BaseModel):
    STATE_CHOICES = [
        ('satisfactory', 'Satisfactory'),
        ('very_satisfactory', 'Very Satisfactory'),
        ('good_enough', 'Good Enough'),
        ('short', 'Short'),
        ('to_repeat', 'To Repeat'),
    ]
    CLEANING_CHOICES = [
        ('neat', 'Neat'),
        ('well_maintained', 'Well Maintained'),
        ('incomplete_cleaning', 'Incomplete Cleaning'),
        ('mold', 'Mold'),
        ('poorly_maintained', 'Poorly Maintained'),
        ('very_poorly_maintained', 'Very Poorly Maintained'),
        ('average_state_of_maintenance', 'Average State of Maintenance'),
        ('trace_of_humidity', 'Trace of Humidity'),
    ]
    photos = models.ImageField(upload_to='master_key_photos/',null=True, blank=True,verbose_name=("Photos"))
    count = models.IntegerField(default=0,verbose_name=("Count"),null=True,blank=True)
    description = models.TextField(null=True, blank=True,verbose_name=("Description"))
    name = models.CharField(max_length=300,null=True, blank=True,verbose_name=("Name"))
    state = MultiSelectField(choices=STATE_CHOICES, max_length=30,null=True, blank=True, verbose_name=("State"))
    cleaning = MultiSelectField(choices=CLEANING_CHOICES, max_length=30,null=True, blank=True, verbose_name=("Cleaning"))
    others = models.CharField(max_length=50,null=True,blank=True)
    is_done = models.BooleanField(default=False, verbose_name=("Is Done"),null=True,blank=True)
    is_todo = models.BooleanField(default=False, verbose_name=("Is Todo"),null=True,blank=True)

    class Meta:
        db_table = 'Appendices_Master'
        verbose_name = "Appendices"
        ordering = ['-id']

    def __str__(self):
        return str(self.name)  
    

