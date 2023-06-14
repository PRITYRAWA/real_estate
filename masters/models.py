from django.db import models
from django_countries.fields import CountryField
from foundation.models import BaseModel


class Realestateagents(BaseModel):
    prefix = models.CharField(max_length=5) 
    name = models.CharField(max_length=50) 
    contactname = models.CharField(max_length=100) 
    email = models.CharField(max_length=320, blank=True, null=True)  
    website = models.TextField(blank=True, null=True)  
    phonenumber = models.CharField(max_length=30, blank=True, null=True) 
    street = models.CharField(max_length=100) 
    zip = models.CharField(max_length=10, blank=True, null=True)  
    city = models.CharField(max_length=50, blank=True, null=True)  
    country = CountryField( blank=True, null=True) 

    class Meta:
        db_table = "Realestateagents"


class Realestatepropertyowner(BaseModel):
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
    languageid = models.IntegerField()   
    owner_representative = models.CharField( max_length=50, blank=True, null=True) 
    isnotificationnewtickets = models.BooleanField(default=False)   
    isnotificationnewupdates = models.BooleanField(default=False)   
    isnotificationticketdeadline = models.BooleanField(default=False)   
    isactive = models.BooleanField(default=False)   
    lastlogindate = models.DateTimeField(null=True, blank=True)   
    attachment = models.TextField(blank=True, null=True)   
    attachments = models.TextField(blank=True, null=True)   

    class Meta:
        db_table = "Realestatepropertyowner"

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
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING)   
    name = models.CharField(max_length=50)   
    street = models.CharField(max_length=100)   
    zip = models.CharField(max_length=10)   
    city = models.CharField(max_length=50)   
    country = CountryField( blank=True, null=True)     
    isactive = models.BooleanField(default=False)   
    attachments = models.TextField(blank=True, null=True)   

    class Meta:
        db_table = "Realestateproperties" 
        ordering = ['-id']

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
    property = models.ForeignKey(Realestateproperties,on_delete=models.CASCADE,verbose_name=("property"))
    name =  models.CharField(max_length=100,null=True, blank=True, verbose_name=("name"))
    Description = models.TextField(null=True, blank=True, verbose_name=("Description"))
    area =  models.CharField(max_length=100,null=True, blank=True, verbose_name=("area"))
    amenities = models.CharField(max_length=100,null=True, blank=True, verbose_name=("amenities"))

    class Meta:
        db_table = 'Realestatepropertiessubgroup'

class Realestateobjects(BaseModel):
    realestatepropertyid = models.ForeignKey('Realestateproperties', models.DO_NOTHING)   
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

#object detail model
class RealEstateObjectsDetails(BaseModel):
    object_code = models.CharField(max_length=100,null=True,blank=True)
    related_object = models.ForeignKey(Realestateobjects, on_delete=models.CASCADE,null=True,blank=True)
    objectName = models.TextField()
    related_detail = models.ForeignKey('RealEstateObjectsDetails', on_delete=models.CASCADE, null=True, blank=True)
    new = models.BooleanField(blank=True,null=True)
    inorder = models.BooleanField(blank=True,null=True)
    normal_wear = models.BooleanField(blank=True,null=True)
    notes = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='object_images_master/')
    
    class Meta:
        db_table = 'RealEstateObjectsDetails'

    def __str__(self):
        return f"Details for {self.objectName}"


class Realestatepropertymanagement(BaseModel):
    realestatepropertyid = models.OneToOneField(Realestateproperties, models.DO_NOTHING, primary_key=True)  
    realestatepersonid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING)  
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING) 
    realestateobjectid = models.ForeignKey(Realestateobjects, models.DO_NOTHING)


    class Meta:
        db_table = 'Realestatepropertymanagement'

class Realestateserviceproviders(BaseModel):
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING)   
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

    class Meta:
        db_table = 'Realestateserviceproviders'
   
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
    topic=models.CharField(max_length=100, blank=False, null=False)
    status=models.CharField(max_length=20, choices= status )
    
    class Meta:
        db_table = 'Agenda'

class AgendaDetails(BaseModel):
    agenda = models.ForeignKey(Agenda,related_name="agenda_detail",on_delete=models.CASCADE)
    topic_details=models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'AgendaDetails'

class Quorums(BaseModel):
    types = (
        ("head", ("Head Votes")),
        ("object", ("Object Votes")),
        ("value", ("Value Votes")),
    )
    voting_type=models.CharField(max_length=20, choices=types)
    present_votes=models.IntegerField(blank=False, null=False)
    condition = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        db_table = 'Quorums'

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
    quorums = models.ForeignKey(Quorums,related_name="votes_detail",on_delete=models.CASCADE)
    tabs = models.CharField(max_length=30, choices=tabs, default='qualified')
    voting_type=models.CharField(max_length=30, choices=types)
    majority=models.IntegerField(blank=False, null=False)
    condition = models.CharField(max_length=30, blank=False, null=False)
    basic_set=models.CharField(max_length=30, choices=cases)
    tie_case= models.CharField(max_length=30, choices=cases)
    
    class Meta:
        db_table = 'Votes'

class MessageTemplate(BaseModel):
    title = models.CharField(max_length=100, blank=False, null=False)
    venue = models.TextField(blank=True, null=True)
    property = models.ForeignKey(Realestateproperties,related_name="property",on_delete=models.CASCADE)
    subgroup = models.ForeignKey(Realestatepropertiessubgroup,related_name="subgroup",on_delete=models.CASCADE)
    chairman = models.ForeignKey(Realestatepropertyowner,related_name="chairman",on_delete=models.CASCADE)
    mintue_taker = models.ForeignKey(Realestatepropertyowner,related_name="mintue_taker",on_delete=models.CASCADE)
    meeting_date = models.DateField(auto_now_add=True)
    meeting_time=models.TimeField(auto_now_add=True)
    date_defined =models.BooleanField(default=False)
    visible_to_ownership_app=models.BooleanField(default=False)
    submission_deadline =models.BooleanField(default=False)
    dispatch_invitaion=models.BooleanField(default=False)
    online_voting = models.BooleanField(default=False)
    attendence_in_person= models.BooleanField(default=False)
    allow_power_of_attorney=models.BooleanField(default=False)
    days_before_the_metting=models.CharField(max_length=20, blank=True, null=True)
    cover_picture_for_presenation=models.FileField(upload_to="images", null=True, blank=True)
    association_information=models.TextField(null=True, blank=True)
    information_for_current_meeting=models.TextField(null=True, blank=True)
    quorum = models.ForeignKey(Quorums,related_name="quorum",on_delete=models.CASCADE)
    votes= models.ForeignKey(Votes,related_name="votes",on_delete=models.CASCADE)

    class Meta:
        db_table = 'MessageTemplate'

