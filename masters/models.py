from django.db import models
from django_countries.fields import CountryField
from foundation.models import BaseModel
from django.utils.translation import gettext_lazy as _

class Realestateagents(BaseModel):
    prefix = models.CharField(max_length=5,verbose_name=("Prefix")) 
    name = models.CharField(max_length=50,verbose_name=("Name")) 
    contactname = models.CharField(max_length=100,verbose_name=("Contact Name")) 
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
        return self.name

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
        return self.name
class Realestatepropertytenant(BaseModel):
    STATUS_CHOICES = [
        ('ENQUIRER', 'Enquirer'),
        ('REGISTER', 'Register'),
        ('OCCUPIED', 'Occupied'),
        ('VACATOR', 'Vacator'),
    ]
    userid = models.CharField( max_length=36, blank=True, null=True)  
    realestatepersontypeid = models.IntegerField()  
    name = models.CharField(max_length=50)  
    surname = models.CharField(max_length=100)  
    email = models.CharField(max_length=320, blank=True, null=True)  
    phonenumber = models.CharField(max_length=30, blank=True, null=True)  
    street = models.CharField(max_length=100)  
    zip = models.CharField(max_length=10, blank=True, null=True)  
    city = models.CharField(max_length=50, blank=True, null=True)  
    country = CountryField( blank=True, null=True)  
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='ENQUIRER')

    class Meta:
        db_table = "Realestatepropertytenant"
        
    def __str__(self):
        return self.name

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

class Messagecomments(BaseModel):
    messageid = models.ForeignKey('Messages', models.DO_NOTHING)   
    realestateownerid = models.ForeignKey('Realestatepropertyowner', models.DO_NOTHING)   
    comment = models.CharField(max_length=500)   

    class Meta:
        db_table = "Messagecomments" 


class Messagerecipients(BaseModel):
    messageid = models.ForeignKey('Messages', models.DO_NOTHING)   
    realestateownerid = models.OneToOneField('Realestatepropertyowner', models.DO_NOTHING, primary_key=True) 
    isread = models.BooleanField(default=True)   
    readdate = models.DateTimeField(blank=True, null=True)   

    class Meta:
        db_table = "Messagerecipients" 
    
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
        return self.name
    
class Feedbacks(BaseModel):
    comment = models.CharField(db_column='Comment', max_length=500,   )   
    class Meta:
        db_table = 'Feedbacks'


class Languages(BaseModel):
    id = models.AutoField(db_column='Id', primary_key=True)   
    name = models.CharField(db_column='Name', max_length=50,   )   
    languagecode = models.CharField(db_column='LanguageCode', unique=True, max_length=2,   )   
    displayorder = models.IntegerField(db_column='DisplayOrder')   

    class Meta:
        db_table = 'Languages'
    
class Localestringresources(BaseModel):
    id = models.AutoField(db_column='Id', primary_key=True)   
    name = models.TextField(db_column='Name',   )   
    value = models.TextField(db_column='Value',   )   
    languageid = models.ForeignKey(Languages, models.DO_NOTHING, db_column='LanguageId')   

    class Meta:
        db_table = 'LocaleStringResources'

class Localizedproperties(BaseModel):
    id = models.AutoField(db_column='Id', primary_key=True)   
    entityid = models.CharField(db_column='EntityId', max_length=36)   
    languageid = models.ForeignKey(Languages, models.DO_NOTHING, db_column='LanguageId')   
    entityname = models.CharField(db_column='EntityName', max_length=100,   )   
    propertyname = models.CharField(db_column='PropertyName', max_length=100,   )   
    localevalue = models.TextField(db_column='LocaleValue',   )   

    class Meta:
        db_table = 'LocalizedProperties'

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
    realestatepropertyid = models.ForeignKey(Realestateproperties,related_name="objects_detail",on_delete=models.CASCADE,null=True,blank=True)
    objectusagetypeid = models.IntegerField()   
    name = models.CharField(max_length=50)   
    description = models.CharField(max_length=100)   
    location = models.CharField(max_length=100)   
    floor = models.CharField(max_length=20)   
    rooms = models.CharField(max_length=20, blank=True, null=True)   
    surfacearea = models.IntegerField(blank=True, null=True)   
    isactive = models.BooleanField(default=False)   
    attachments = models.TextField(blank=True, null=True)   

    class Meta:
        db_table = 'Realestateobjects'
        ordering = ['-id']
    def __str__(self):
        return self.name
    
#object detail model
class Realestateobjectsdetail(BaseModel):
    object_code = models.CharField(max_length=100,null=True,blank=True,verbose_name=("Object Code"))
    category = models.CharField(max_length=100,null=True,blank=True,verbose_name=("Category"))
    related_object = models.ForeignKey(Realestateobjects, on_delete=models.CASCADE,null=True,blank=True,verbose_name=("Related Object"))
    related_property = models.ForeignKey(Realestateproperties, on_delete=models.CASCADE,null=True,blank=True,verbose_name=("Related Property"))
    objectName = models.TextField(verbose_name=("Object Name"))
    related_detail = models.ForeignKey('Realestateobjectsdetail', on_delete=models.CASCADE, null=True, blank=True,verbose_name=("Related Detail"),related_name='child_details')
    new = models.BooleanField(blank=True,null=True,verbose_name=("New"))
    inorder = models.BooleanField(blank=True,null=True,verbose_name=("In Order"))
    normal_wear = models.BooleanField(blank=True,null=True,verbose_name=("Normal Wear"))
    notes = models.TextField(blank=True, null=True,verbose_name=("Notes"))
    image = models.ImageField(upload_to='object_images_master/',verbose_name=("Image"))
    
    class Meta:
        db_table = 'RealEstateObjectsDetails'
        ordering = ['-id']
    def __str__(self):
        return self.objectName

class Realestatekeyhandover(BaseModel):
    property = models.ForeignKey(Realestateproperties,on_delete=models.CASCADE, null=True, blank=True) 
    object = models.ForeignKey(Realestateobjects,on_delete=models.CASCADE, null=True, blank=True) 
    photo = models.FileField(upload_to='key_photos/')
    count = models.IntegerField(default=0)
    description = models.TextField()
    name = models.CharField(max_length=300,null=True, blank=True)

    class Meta:
        db_table = 'Keys'

    def __str__(self):
        return self.name

class Realestatemeterhandover(BaseModel):
    UNIT_CHOICES = [
        ('Kwh', 'Kwh'),
        ('m3', 'm3'),
        ('litres', 'litres'),
        ('units', 'units'),
        ('steres', 'steres'),
    ]
    COMPANY_CHOICES = [
        ('abc','abc')
    ]
    name = models.CharField(max_length=300,null=True, blank=True)
    property = models.ForeignKey(Realestateproperties,on_delete=models.CASCADE, null=True, blank=True) 
    object = models.ForeignKey(Realestateobjects,on_delete=models.CASCADE, null=True, blank=True) 
    meterno = models.CharField(max_length=200,null=True,blank=True)
    reading = models.CharField(max_length=200,null=True,blank=True)
    unit = models.CharField(max_length=10,choices=UNIT_CHOICES,default='Kwh',null=True,blank=True)
    whochange = models.CharField(max_length=200,null=True,blank=True)
    company = models.CharField(max_length=100,choices=COMPANY_CHOICES,null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    class Meta:
        db_table = 'meters'

    def __str__(self):
        return self.name


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
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING,null=True,blank=True)   
    name = models.CharField(max_length=50)   
    field = models.CharField(max_length=50, blank=True, null=True)   
    languageid = models.IntegerField()   
    contactname = models.TextField(blank=True, null=True)   
    phonenumber = models.CharField(max_length=30)   
    email = models.CharField(max_length=320)   
    street = models.CharField(max_length=100)   
    zip = models.CharField(max_length=10)   
    city = models.CharField(max_length=50)   
    country = CountryField( blank=True, null=True)  
    isactive = models.BooleanField(default=False)   
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
    ticketid = models.ForeignKey('Tickets', models.DO_NOTHING)   
    realestapersonid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING)   
    message = models.CharField(max_length=2500)   
    created = models.DateTimeField(null=True, blank=True)   
    attachments = models.TextField(blank=True, null=True)  

    class Meta:
        db_table = 'Ticketmessages' 


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
   

class Ticketsequences(BaseModel):
    realestateagentid = models.CharField(primary_key=True, max_length=36)   
    sequence = models.IntegerField()   

    class Meta:
        db_table = 'Ticketsequences' 

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


class Efmigrationshistory(BaseModel):
    migrationid = models.CharField(primary_key=True, max_length=150)   
    productversion = models.CharField(max_length=32)   

    class Meta:
        db_table = 'Efmigrationshistory' 

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