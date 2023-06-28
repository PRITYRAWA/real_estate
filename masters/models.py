from django.db import models
from django_countries.fields import CountryField
from foundation.models import BaseModel
from django.utils.translation import gettext_lazy as _



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
    street = models.CharField(max_length=100,null=True,blank=True,verbose_name=("Street"))  
    zip = models.CharField(max_length=10, blank=True, null=True,verbose_name=("Zip"))  
    city = models.CharField(max_length=50, blank=True, null=True,verbose_name=("City"))  
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='ENQUIRER',null=True,blank=True,verbose_name=("Status"))

    class Meta:
        db_table = "Realestatepropertytenant"
        ordering = ['-id']
      
    def __str__(self):
        return str(self.name)

class Messages(BaseModel):
    realestateagentid = models.ForeignKey('Realestateagents', models.DO_NOTHING)   
    subject = models.CharField(max_length=150)   
    body = models.CharField(max_length=2500)   
    isemailnotification = models.BooleanField(default=False)   
    isimportant = models.BooleanField(default=False)   
    isallowcomment = models.BooleanField(default=False)   
    issendimmediately = models.BooleanField(default=False)   
    senddate = models.DateTimeField(blank=True, null=True)   
    created = models.DateTimeField(blank=True, null=True)   
    createdrealestateownerid = models.ForeignKey('Realestatepropertyowner', models.DO_NOTHING)   
    isdeleted = models.BooleanField(default=False)   
    attachments = models.TextField(blank=True, null=True)   

    class Meta:
        db_table = "Messages"  
        ordering = ['-id']

class Messagecomments(BaseModel):
    messageid = models.ForeignKey('Messages', models.DO_NOTHING,null=True,blank=True)   
    realestateownerid = models.ForeignKey('Realestatepropertyowner', models.DO_NOTHING)   
    tenantcomment = models.CharField(max_length=500,null=True,blank=True)   
    comment = models.CharField(max_length=500,null=True,blank=True)   

    class Meta:
        db_table = "Messagecomments" 
        ordering = ['-created_at']


class Messagerecipients(BaseModel):
    messageid = models.ForeignKey('Messages', models.DO_NOTHING)   
    realestateownerid = models.OneToOneField('Realestatepropertyowner', models.DO_NOTHING, primary_key=True) 
    isread = models.BooleanField(default=True)   
    readdate = models.DateTimeField(blank=True, null=True)   

    class Meta:
        db_table = "Messagerecipients" 
        ordering = ['-created_at']
    

class Realestateproperties(BaseModel):
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING,verbose_name=("Agent Id"),null=True,blank=True)   
    name = models.CharField(max_length=50,verbose_name=("Name"))   
    street = models.CharField(max_length=100,verbose_name=("Street"))   
    zip = models.CharField(max_length=10,verbose_name=("Zip"))   
    city = models.CharField(max_length=50,verbose_name=("City"))   
    country = CountryField( blank=True, null=True,verbose_name=("Country"))     
    isactive = models.BooleanField(default=False,verbose_name=("Is Active"))   
    attachment = models.FileField(upload_to='attachement/',blank=True, null=True,verbose_name=("Attachment")) 
   

    class Meta:
        db_table = "Realestateproperties" 
        ordering = ['-id']

    def __str__(self):
        return str(self.name)
    
class Feedbacks(BaseModel):
    comment = models.CharField(db_column='Comment', max_length=500,   )   
    class Meta:
        db_table = 'Feedbacks'
        ordering = ['-id']


class Languages(BaseModel):
    id = models.AutoField(db_column='Id', primary_key=True)   
    name = models.CharField(db_column='Name', max_length=50,   )   
    languagecode = models.CharField(db_column='LanguageCode', unique=True, max_length=2,   )   
    displayorder = models.IntegerField(db_column='DisplayOrder')   

    class Meta:
        db_table = 'Languages'
        ordering = ['-id']
    

class Localestringresources(BaseModel):
    id = models.AutoField(db_column='Id', primary_key=True)   
    name = models.TextField(db_column='Name',   )   
    value = models.TextField(db_column='Value',   )   
    languageid = models.ForeignKey(Languages, models.DO_NOTHING, db_column='LanguageId')   

    class Meta:
        db_table = 'LocaleStringResources'
        ordering = ['-id']

class Localizedproperties(BaseModel):
    id = models.AutoField(db_column='Id', primary_key=True)   
    entityid = models.CharField(db_column='EntityId', max_length=36)   
    languageid = models.ForeignKey(Languages, models.DO_NOTHING, db_column='LanguageId')   
    entityname = models.CharField(db_column='EntityName', max_length=100,   )   
    propertyname = models.CharField(db_column='PropertyName', max_length=100,   )   
    localevalue = models.TextField(db_column='LocaleValue',   )   

    class Meta:
        db_table = 'LocalizedProperties'
        ordering = ['-id']

#model created for subgroup details in meeting 
class Realestatepropertiessubgroup(BaseModel):
    property = models.ForeignKey(Realestateproperties,on_delete=models.CASCADE,verbose_name=("Property"))
    name =  models.CharField(max_length=100,null=True, blank=True, verbose_name=("Name"))
    Description = models.TextField(null=True, blank=True, verbose_name=("Description"))
    area =  models.CharField(max_length=100,null=True, blank=True, verbose_name=("Area"))
    amenities = models.CharField(max_length=100,null=True, blank=True, verbose_name=("Amenities"))

    class Meta:
        db_table = 'Realestatepropertiessubgroup'
        ordering = ['-id']

class Realestateobjects(BaseModel):
    STATUS_CHOICES = [
        ('OCCUPIED', 'Occupied'),
        ('VACATOR', 'Vacator'),
    ]
    USAGE_CHOICE = [
        ('COMMERCIAL','commercial'),
        ('RESIDENCE','residence'),
        ('private','private'),
        ('PUBLIC','public'),
        ('OTHERS','others'),
    ]
    realestatepropertyid = models.ForeignKey(Realestateproperties,related_name="objects_detail",on_delete=models.CASCADE,null=True,blank=True, verbose_name=("Property Id"))
    objectusagetypeid = models.CharField(max_length=10,choices=USAGE_CHOICE,null=True,blank=True,verbose_name=("Usage Type id"))
    object_name = models.CharField(max_length=50,verbose_name=("Object Name"))   
    object_description = models.CharField(max_length=100,verbose_name="Object Description")   
    location = models.CharField(max_length=100,verbose_name="Location")   
    floor = models.CharField(max_length=20,blank=True, null=True,verbose_name=("Floor"))   
    rooms = models.CharField(max_length=20, blank=True, null=True,verbose_name=("Rooms"))   
    surfacearea = models.IntegerField(blank=True, null=True,verbose_name=("Surface Area"))   
    isactive = models.BooleanField(default=False,verbose_name=("Is Active"))   
    attachments = models.TextField(blank=True, null=True,verbose_name=("Attachments"))   
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='VACATOR',null=True,blank=True,verbose_name=("Status"))

    class Meta:
        db_table = 'Realestateobjects'
        ordering = ['-id']
    def __str__(self):
        return str(self.object_name)
    
#object detail model
class Realestateobjectsdetail(BaseModel):
    object_code = models.CharField(max_length=100,null=True,blank=True,verbose_name=("Object Code"))
    category = models.CharField(max_length=100,null=True,blank=True,verbose_name=("Category"))
    related_object = models.ForeignKey(Realestateobjects, on_delete=models.CASCADE,null=True,blank=True,verbose_name=("Related Object"))
    related_property = models.ForeignKey(Realestateproperties, on_delete=models.CASCADE,null=True,blank=True,verbose_name=("Related Property"))
    objectName = models.TextField(verbose_name=("Object Name"))
    related_detail = models.ForeignKey('Realestateobjectsdetail', on_delete=models.CASCADE, null=True, blank=True,verbose_name=("Related Detail"),related_name='child_details')
    new = models.BooleanField(blank=True,null=True,verbose_name=("New"))
    inorder = models.BooleanField(blank=True,null=True,verbose_name=("In Order"),default=False)
    normal_wear = models.BooleanField(blank=True,null=True,verbose_name=("Normal Wear"),default=False)
    notes = models.TextField(blank=True, null=True,verbose_name=("Notes"))
    image = models.ImageField(upload_to='object_images_master/',verbose_name=("Image"))
    
    class Meta:
        db_table = 'Realestateobjectsdetail'
        ordering = ['-id']

    def __str__(self):
        return str(self.objectName)

class Realestatekeyhandover(BaseModel):
    property = models.ForeignKey(Realestateproperties,on_delete=models.CASCADE, null=True, blank=True,verbose_name=("Property")) 
    object = models.ForeignKey(Realestateobjects,on_delete=models.CASCADE, null=True, blank=True,verbose_name=("Object")) 
    photo = models.ImageField(upload_to='master_key_photos/',null=True, blank=True,verbose_name=("Photo"))
    count = models.IntegerField(default=0,verbose_name=("Count"))
    description = models.TextField(null=True, blank=True,verbose_name=("Description"))
    name = models.CharField(max_length=300,null=True, blank=True,verbose_name=("Name"))

    class Meta:
        db_table = 'Realestatekeyhandover'
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
    name = models.CharField(max_length=300,null=True, blank=True,verbose_name=("Name"))
    property = models.ForeignKey(Realestateproperties,on_delete=models.CASCADE, null=True, blank=True,verbose_name=("Property")) 
    object = models.ForeignKey(Realestateobjects,on_delete=models.CASCADE, null=True, blank=True,verbose_name=("Object")) 
    meterno = models.CharField(max_length=200,null=True,blank=True,verbose_name=("Meter Number"))
    reading = models.CharField(max_length=200,null=True,blank=True,verbose_name=("Reading"))
    photos = models.ImageField(upload_to='master_meter_photos/',null=True,blank=True,verbose_name=("Photo"))
    count = models.IntegerField(default=0,verbose_name=("Count"))
    unit = models.CharField(max_length=10,choices=UNIT_CHOICES,null=True,blank=True,verbose_name=("Unit"))
    whochange = models.CharField(max_length=200,choices=WHO_CHANGES,null=True,blank=True,verbose_name=("Who Change"))
    company = models.CharField(max_length=100,choices=COMPANY_CHOICES,null=True,blank=True,verbose_name=("Company "))
    description = models.TextField(null=True,blank=True,verbose_name=("Description"))

    class Meta:
        db_table = 'Realestatemeterhandover'
        ordering = ['-id']

    def __str__(self):
        return str(self.name)

class FurnitureInspectionMaster(models.Model):
    CLEANING_TYPES = [
        ('General Cleaning', 'General Cleaning'),
        ('Sheer Cleaning', 'Sheer Cleaning'),
        ('Linen Cleaning', 'Linen Cleaning'),
    ]
    property = models.ForeignKey(Realestateproperties,on_delete=models.CASCADE, null=True, blank=True,verbose_name=("Property")) 
    object = models.ForeignKey(Realestateobjects,on_delete=models.CASCADE, null=True, blank=True,verbose_name=("Object"))    
    cleaning_type = models.CharField(max_length=50, choices=CLEANING_TYPES,verbose_name=("Cleaning Type"))
    photos = models.ImageField(upload_to='master_inspection_photos/',null=True,blank=True,verbose_name=("Photos"))
    description = models.TextField()

    def __str__(self):
        return f"{self.cleaning_type} - {self.pk}"
    
class Realestatepropertymanagement(BaseModel):
    realestatepropertyid = models.OneToOneField(Realestateproperties, models.DO_NOTHING,verbose_name=_("Property") ) 
    realestateownerid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING,verbose_name=_("Property Owner"))  
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING,verbose_name=_("Property Agent")) 
    realestateobjectid = models.ForeignKey(Realestateobjects, models.DO_NOTHING,verbose_name=_("Property Object"))
    manageby = models.CharField(max_length=10, choices=(('owner', 'Owner'), ('agent', 'Agent')),verbose_name=_("Manage By"))
    manageby_id = models.CharField(max_length=100,null=True,blank=True,verbose_name=_("Manager Id"))

    class Meta:
        db_table = 'Realestatepropertymanagement'
        ordering = ['-id']
   

class Realestateserviceproviders(BaseModel):
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING,null=True,blank=True,verbose_name=("Realestate Agent Id"))   
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
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING,verbose_name=("Agent Id"))   
    name = models.CharField(max_length=50,verbose_name=("Name"))   
    field = models.CharField(max_length=50, blank=True, null=True,verbose_name=("Field")) 
    contactname = models.TextField(blank=True, null=True,verbose_name=("Contact Name"))   
    phonenumber = models.CharField(max_length=30,verbose_name=("Phone Number"))   
    email = models.CharField(max_length=320,verbose_name=("Email"))   
    street = models.CharField(max_length=100,verbose_name=("Street"))   
    zip = models.CharField(max_length=10,verbose_name=("Zip"))   
    city = models.CharField(max_length=50,verbose_name=("City"))   
    country = CountryField( blank=True, null=True,verbose_name=("Country"))  
    isactive = models.BooleanField(default=False,verbose_name=("Is Active"))   

    class Meta:
        db_table = 'Realestateserviceproviders'
        ordering = ['-id']

class Ticketmessages(BaseModel):
    ticketid = models.ForeignKey('Tickets', models.DO_NOTHING,verbose_name=("Ticket Id"))   
    realestapersonid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING,verbose_name=("Owner Id"))   
    message = models.CharField(max_length=2500,verbose_name=("Message"))   
    created = models.DateTimeField(null=True, blank=True,verbose_name=("Created"))   
    attachments = models.TextField(blank=True, null=True,verbose_name=("Attachment"))  

    class Meta:
        db_table = 'Ticketmessages' 
        ordering = ['-id']


class Ticketoffers(BaseModel):
    offertypeid = models.IntegerField()   
    ticketid = models.ForeignKey('Tickets', models.DO_NOTHING)   
    realestateserviceproviderid = models.ForeignKey(Realestateserviceproviders, models.DO_NOTHING)   
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
   

class Ticketsequences(BaseModel):
    realestateagentid = models.CharField(primary_key=True, max_length=36)   
    sequence = models.IntegerField()   

    class Meta:
        db_table = 'Ticketsequences' 
        ordering = ['-created_at']


class Tickets(BaseModel):
    # id = models.CharField(db_column='Id', primary_key=True, max_length=36)   
    tickettypeid = models.IntegerField()   
    slug = models.CharField(max_length=15)   
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING)   
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


class Efmigrationshistory(BaseModel):
    migrationid = models.CharField(primary_key=True, max_length=150)   
    productversion = models.CharField(max_length=32)   

    class Meta:
        db_table = 'Efmigrationshistory' 
        ordering = ['-created_at']

class Sysdiagrams(BaseModel):
    name = models.CharField(max_length=128,   )
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table = 'Sysdiagrams' 

class Agenda(BaseModel):
    status = (
        ("draft", ("Draft")),
        ("definitive", ("Definitive")),
    )
    topic=models.CharField(max_length=100, blank=False, null=False,verbose_name=("Topic"))
    status=models.CharField(max_length=20, choices= status ,default='draft',verbose_name=("Status") )
    
    class Meta:
        db_table = 'Agenda'
        ordering = ['-id']
class AgendaDetails(BaseModel):
    agenda = models.ForeignKey(Agenda,related_name="agenda_detail",on_delete=models.CASCADE,verbose_name=("Agenda"))
    topic_details=models.CharField(max_length=100, blank=True, null=True,verbose_name=("Topic Details"))

    class Meta:
        db_table = 'AgendaDetails'
        ordering = ['-id']
class Quorums(BaseModel):
    types = (
        ("head", ("Head Votes")),
        ("object", ("Object Votes")),
        ("value", ("Value Votes")),
    )
    voting_type=models.CharField(max_length=20, choices=types,verbose_name=("Voting Type"))
    present_votes=models.IntegerField(blank=False, null=False,verbose_name=("Present Votes"))
    condition = models.CharField(max_length=20, blank=False, null=False,verbose_name=("Condition"))

    class Meta:
        db_table = 'Quorums'
        ordering = ['-id']

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
    quorums = models.ForeignKey(Quorums,related_name="votes_detail",on_delete=models.CASCADE,verbose_name=("Quorums"))
    tabs = models.CharField(max_length=50, choices=tabs, default='qualified',verbose_name=("Tabs"))
    voting_type=models.CharField(max_length=50, choices=types,verbose_name=("Voting Type"))
    majority=models.IntegerField(blank=False, null=False,verbose_name=("Majority"))
    condition = models.CharField(max_length=50, blank=False, null=False,verbose_name=("Condition"))
    basic_set=models.CharField(max_length=50, choices=sets,verbose_name=("Basic Set"))
    tie_case= models.CharField(max_length=50, choices=cases,verbose_name=("Tie Case"))
    
    class Meta:
        db_table = 'Votes'
        ordering = ['-id']

class Mettingtemplate(BaseModel):
    quorum = models.ForeignKey(Quorums,related_name="quorum",on_delete=models.CASCADE,verbose_name=("Quorums"))
    agenda = models.ForeignKey(Agenda,related_name="agenda",on_delete=models.CASCADE,verbose_name=("Agenda"))
    voting_circle = models.ForeignKey(Realestatepropertymanagement,related_name="voting_circle",on_delete=models.CASCADE,verbose_name=("Voting Circle"))
    
    class Meta:
        db_table = 'Mettingtemplate'
        ordering = ['-id']

class CommonFields(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
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


class ExtendedBaseModel(BaseModel, CommonFields):
    class Meta:
        abstract = True


class Reportdamage(ExtendedBaseModel):
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
    date = models.DateField()
    time_range = models.CharField(max_length=20, choices=TIME_CHOICES)
    contact_person = models.CharField(max_length=30, choices=CONTACT_PERSON_CHOICES)
    KeyLocation = models.CharField(max_length=250,null=True,blank=True)

    class Meta:
        db_table = 'Reportdamage'
        ordering = ['-id']



class Generalenquiries(ExtendedBaseModel):
    attachments = models.FileField(upload_to='manager_enquiries',null=True,blank=True)

    class Meta:
        db_table = 'Generalenquiries'
        ordering = ['-id']

class Invoicequestion(ExtendedBaseModel):
    refrence_number = models.CharField(max_length=100,null=True,blank=True)
    invoice_amount = models.CharField(max_length=100,null=True,blank=True)
    question = models.TextField(null=True,blank=True)
    attachments = models.FileField(upload_to='manager_invoice',null=True,blank=True)

    class Meta:
        db_table = 'Invoicequestion'
        ordering = ['-id']

class Petrequest(ExtendedBaseModel):
    PET_CHOICES = (
    ('cat_inside', 'Cat (inside)'),
    ('cat_in_out', 'Cat (inside and outside)'),
    ('dog', 'Dog'),
    ('fish', 'Fish (aquarium)'),
    ('reptiles', 'Reptiles (terrarium)'),
    ('birds', 'Birds'),
    ('other_pets', 'Other pets'),
    )
    pet_type = models.CharField(max_length=20, choices=PET_CHOICES)
    quantity = models.CharField(max_length=100,null=True,blank=True)
    attachments = models.FileField(upload_to='pet_request',null=True,blank=True)

    class Meta:
        db_table = 'Petrequest'
        ordering = ['-id']

class Orderkey(BaseModel):
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

  
    key_type = models.CharField(max_length=20, choices=KEY_CHOICES)
    quantity = models.CharField(max_length=100,null=True,blank=True)
    locking_system = models.CharField(max_length=100,null=True,blank=True)
    serial_number = models.CharField(max_length=100,null=True,blank=True)
    order_reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    attachments = models.FileField(upload_to='order-key',null=True,blank=True)

    class Meta:
        db_table = 'Orderkey'
        ordering = ['-id']

class Paymentslips(BaseModel):
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

    from_month = models.CharField(max_length=50,choices=MONTH_CHOICES,null=True,blank=True)
    from_year = models.CharField(max_length=50,choices=YEAR_CHOICES,null=True,blank=True)
    to_month = models.CharField(max_length=50,choices=MONTH_CHOICES,null=True,blank=True)
    to_year =  models.CharField(max_length=50,choices=YEAR_CHOICES,null=True,blank=True)
    payment_slip_delivery = models.CharField(max_length=10, choices=PAYMENT_SLIP_DELIVERY_CHOICES)
    attachments = models.FileField(upload_to='payment-slip',null=True,blank=True)

    class Meta:
        db_table = 'Paymentslips'
        ordering = ['-id']

class Bankdetails(ExtendedBaseModel):
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

class Orderbadge(ExtendedBaseModel):
    ORDER_CHOICES = [
        ('complete_set', 'I would like a complete set of new badges with the inscription.'),
        ('replacement', 'I wish only the replacement of the sign at certain locations.'),
    ]
    VALID_FROM_CHOICES = [
        ('assembly', 'Valid From (assembly)'),
        ('asap', 'As Soon As Possible'),
        ('date', 'Valid From Date'),
    ]
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

class Appendicesmaster(BaseModel):
    photos = models.ImageField(upload_to='master_key_photos/',null=True, blank=True,verbose_name=("Photos"))
    count = models.IntegerField(default=0,verbose_name=("Count"))
    description = models.TextField(null=True, blank=True,verbose_name=("Description"))
    name = models.CharField(max_length=300,null=True, blank=True,verbose_name=("Name"))

    class Meta:
        db_table = 'Appendices_Master'
        ordering = ['-id']

    def __str__(self):
        return str(self.name)  
