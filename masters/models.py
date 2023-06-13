from django.db import models
from django_countries.fields import CountryField

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    createdby = models.CharField(max_length=36, blank=True, null=True)
    lastmodifiedby = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True

class Realestateagents(BaseModel):
    prefix = models.CharField(max_length=5)  # Field name made lowercase.
    name = models.CharField(max_length=50)  # Field name made lowercase.
    contactname = models.CharField(max_length=100)  # Field name made lowercase.
    email = models.CharField(max_length=320, blank=True, null=True)  # Field name made lowercase.
    website = models.TextField(blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(max_length=100)  # Field name made lowercase.
    zip = models.CharField(max_length=10, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    country = CountryField( blank=True, null=True)  # Field name made lowercase.    isactive = models.BooleanField(default=False)  # Field name made lowercase.
    


class Realestatepropertyowner(BaseModel):
    userid = models.CharField( max_length=36, blank=True, null=True)  # Field name made lowercase.
    #realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING, db_column='RealEstateAgentId')  # Field name made lowercase.
    # realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING)  # Field name made lowercase.
    realestatepersontypeid = models.IntegerField()  # Field name made lowercase.
    name = models.CharField(max_length=50)  # Field name made lowercase.
    surname = models.CharField(max_length=100)  # Field name made lowercase.
    email = models.CharField(max_length=320, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(max_length=100)  # Field name made lowercase.
    zip = models.CharField(max_length=10, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    country = CountryField( blank=True, null=True)  # Field name made lowercase.    isactive = models.BooleanField(default=False)  # Field name made lowercase.
    languageid = models.IntegerField()  # Field name made lowercase.
    isnotificationnewtickets = models.BooleanField(default=False)  # Field name made lowercase.
    isnotificationnewupdates = models.BooleanField(default=False)  # Field name made lowercase.
    isnotificationticketdeadline = models.BooleanField(default=False)  # Field name made lowercase.
    isactive = models.BooleanField(default=False)  # Field name made lowercase.
    lastlogindate = models.DateTimeField(null=True, blank=True)  # Field name made lowercase.
    attachment = models.TextField(blank=True, null=True)  # Field name made lowercase.
    attachments = models.TextField(blank=True, null=True)  # Field name made lowercase.

class Messages(models.Model):
    realestateagentid = models.ForeignKey('Realestateagents', models.DO_NOTHING)  # Field name made lowercase.
    subject = models.CharField(max_length=150)  # Field name made lowercase.
    body = models.CharField(max_length=2500)  # Field name made lowercase.
    isemailnotification = models.BooleanField(default=False)  # Field name made lowercase.
    isimportant = models.BooleanField(default=False)  # Field name made lowercase.
    isallowcomment = models.BooleanField(default=False)  # Field name made lowercase.
    issendimmediately = models.BooleanField(default=False)  # Field name made lowercase.
    senddate = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    createdrealestapersonid = models.ForeignKey('Realestatepropertyowner', models.DO_NOTHING)  # Field name made lowercase.
    isdeleted = models.BooleanField(default=False)  # Field name made lowercase.
    attachments = models.TextField(blank=True, null=True)  # Field name made lowercase.

class Messagecomments(models.Model):
    messageid = models.ForeignKey('Messages', models.DO_NOTHING)  # Field name made lowercase.
    realestapersonid = models.ForeignKey('Realestatepropertyowner', models.DO_NOTHING)  # Field name made lowercase.
    comment = models.CharField(max_length=500)  # Field name made lowercase.
    created = models.DateTimeField(null=True, blank=True)  # Field name made lowercase.


class Messagerecipients(models.Model):
    messageid = models.ForeignKey('Messages', models.DO_NOTHING)  # Field name made lowercase.
    realestapersonid = models.OneToOneField('Realestatepropertyowner', models.DO_NOTHING, primary_key=True)  # Field name made lowercase. The composite primary key (RealEstaPersonId, MessageId) found, that is not supported. The first column is selected.
    isread = models.BooleanField(default=True)  # Field name made lowercase.
    readdate = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'MessageRecipients'
    #     unique_together = (('realestapersonid', 'messageid'),)

class Realestateobjectpersons(models.Model):
    realestateobjectid = models.OneToOneField('Realestateobjects', models.DO_NOTHING, primary_key=True)  # Field name made lowercase. The composite primary key (RealEstateObjectId, RealEstatePersonId) found, that is not supported. The first column is selected.
    realestatepersonid = models.ForeignKey('Realestatepropertyowner', models.DO_NOTHING)  # Field name made lowercase.
    isactive = models.BooleanField(default=True)  # Field name made lowercase.



class Realestateproperties(BaseModel):
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING)  # Field name made lowercase.
    name = models.CharField(max_length=50)  # Field name made lowercase.
    street = models.CharField(max_length=100)  # Field name made lowercase.
    zip = models.CharField(max_length=10)  # Field name made lowercase.
    city = models.CharField(max_length=50)  # Field name made lowercase.
    country = CountryField( blank=True, null=True)  # Field name made lowercase.    isactive = models.BooleanField(default=False)  # Field name made lowercase.
    isactive = models.BooleanField(default=False)  # Field name made lowercase.
    attachments = models.TextField(blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f" {self.name}"

class Feedbacks(BaseModel):
    comment = models.CharField(db_column='Comment', max_length=500,   )  # Field name made lowercase.
    class Meta:
        db_table = 'Feedbacks'


class Languages(BaseModel):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50,   )  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', unique=True, max_length=2,   )  # Field name made lowercase.
    displayorder = models.IntegerField(db_column='DisplayOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Languages'


class Localestringresources(BaseModel):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name',   )  # Field name made lowercase.
    value = models.TextField(db_column='Value',   )  # Field name made lowercase.
    languageid = models.ForeignKey(Languages, models.DO_NOTHING, db_column='LanguageId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocaleStringResources'


class Localizedproperties(BaseModel):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entityid = models.CharField(db_column='EntityId', max_length=36)  # Field name made lowercase.
    languageid = models.ForeignKey(Languages, models.DO_NOTHING, db_column='LanguageId')  # Field name made lowercase.
    entityname = models.CharField(db_column='EntityName', max_length=100,   )  # Field name made lowercase.
    propertyname = models.CharField(db_column='PropertyName', max_length=100,   )  # Field name made lowercase.
    localevalue = models.TextField(db_column='LocaleValue',   )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocalizedProperties'

#model created for subgroup details in meeting 
class Realestatepropertiessubgroup(BaseModel):
    property = models.ForeignKey(Realestateproperties,on_delete=models.CASCADE,verbose_name=("property"))
    name =  models.CharField(max_length=100,null=True, blank=True, verbose_name=("name"))
    Description = models.TextField(null=True, blank=True, verbose_name=("Description"))
    area =  models.CharField(max_length=100,null=True, blank=True, verbose_name=("area"))
    amenities = models.CharField(max_length=100,null=True, blank=True, verbose_name=("amenities"))

    class Meta:
        managed = False
        db_table = 'Realestatepropertiessubgroup'

class Realestateobjects(BaseModel):
    realestatepropertyid = models.ForeignKey('Realestateproperties', models.DO_NOTHING)  # Field name made lowercase.
    objectusagetypeid = models.IntegerField()  # Field name made lowercase.
    name = models.CharField(max_length=50)  # Field name made lowercase.
    description = models.CharField(max_length=100)  # Field name made lowercase.
    location = models.CharField(max_length=100)  # Field name made lowercase.
    floor = models.CharField(max_length=20)  # Field name made lowercase.
    rooms = models.CharField(max_length=20, blank=True, null=True)  # Field name made lowercase.
    surfacearea = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(default=False)  # Field name made lowercase.
    attachments = models.TextField(blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f" {self.name}"

    class Meta:
        db_table = 'RealEstateObjects'

#object detail model
class RealEstateObjectsDetails(models.Model):
    object_code = models.CharField(max_length=100,null=True,blank=True)
    related_object = models.ForeignKey(Realestateobjects, on_delete=models.CASCADE,null=True,blank=True)
    objectName = models.TextField()
    related_detail = models.ForeignKey('RealEstateObjectsDetails', on_delete=models.CASCADE, null=True, blank=True)
    new = models.BooleanField(blank=True,null=True)
    inorder = models.BooleanField(blank=True,null=True)
    normal_wear = models.BooleanField(blank=True,null=True)
    notes = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='object_images_master/')
    

    def __str__(self):
        return f"Details for {self.objectName}"


class Realestatepropertymanagement(BaseModel):
    realestatepropertyid = models.OneToOneField(Realestateproperties, models.DO_NOTHING, primary_key=True)  
    realestateownerid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING)  
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING) 
    realestateobjectid = models.ForeignKey(Realestateobjects, models.DO_NOTHING)
    care_taker = models.CharField(max_length=10, choices=(('owner', 'Owner'), ('agent', 'Agent')))
    care_taker_id = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        db_table = 'Realestatepropertymanagement'

    def save(self, *args, **kwargs):
        if self.take_care == 'agent':
            self.care_taker_id = self.realestateagentid_id
            self.realestateownerid_id = None
        elif self.take_care == 'owner':
            self.care_taker_id = self.realestateownerid_id
            self.realestateagentid_id = None
        super().save(*args, **kwargs)

class Realestateserviceproviders(BaseModel):
    # id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING)  # Field name made lowercase.
    name = models.CharField(max_length=50)  # Field name made lowercase.
    field = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    languageid = models.IntegerField()  # Field name made lowercase.
    contactname = models.TextField(blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(max_length=30)  # Field name made lowercase.
    email = models.CharField(max_length=320)  # Field name made lowercase.
    street = models.CharField(max_length=100)  # Field name made lowercase.
    zip = models.CharField(max_length=10)  # Field name made lowercase.
    city = models.CharField(max_length=50)  # Field name made lowercase.
    country = CountryField( blank=True, null=True)  # Field name made lowercase.    isactive = models.BooleanField(default=False)  # Field name made lowercase.
    isactive = models.BooleanField(default=False)  # Field name made lowercase.
   
class Ticketmessages(models.Model):
    ticketid = models.ForeignKey('Tickets', models.DO_NOTHING)  # Field name made lowercase.
    realestapersonid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING)  # Field name made lowercase.
    message = models.CharField(max_length=2500)  # Field name made lowercase.
    created = models.DateTimeField(null=True, blank=True)  # Field name made lowercase.
    attachments = models.TextField(blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'TicketMessages'


class Ticketoffers(BaseModel):
    # id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    offertypeid = models.IntegerField()  # Field name made lowercase.
    ticketid = models.ForeignKey('Tickets', models.DO_NOTHING)  # Field name made lowercase.
    realestateserviceproviderid = models.ForeignKey(Realestateserviceproviders, models.DO_NOTHING)  # Field name made lowercase.
    requestnote = models.CharField(max_length=1000, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=1000, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricelimit = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    deadline = models.DateField(blank=True, null=True)  # Field name made lowercase.
    appointmentdate = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    serviceproviderratingbytenant = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    serviceprovidercommentbytenant = models.CharField(max_length=1000, blank=True, null=True)  # Field name made lowercase.
    serviceproviderratingbymanager = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    serviceprovidercommentbymanager = models.CharField(max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ourrating = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    problemcomment = models.CharField(max_length=1000, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField()  # Field name made lowercase.
    noteattachments = models.TextField(blank=True, null=True)  # Field name made lowercase.
    requestnoteattachments = models.TextField(blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'TicketOffers'
    #     unique_together = (('ticketid', 'realestateserviceproviderid', 'status'),)


class Ticketsequences(models.Model):
    realestateagentid = models.CharField(primary_key=True, max_length=36)  # Field name made lowercase.
    sequence = models.IntegerField()  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'TicketSequences'


class Tickets(BaseModel):
    # id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    tickettypeid = models.IntegerField()  # Field name made lowercase.
    slug = models.CharField(max_length=15)  # Field name made lowercase.
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING)  # Field name made lowercase.
    realestatepropertyid = models.ForeignKey(Realestateproperties, models.DO_NOTHING)  # Field name made lowercase.
    realestateobjectid = models.ForeignKey(Realestateobjects, models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.
    realestatetenantid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING)  # Field name made lowercase.
    responsibleuserid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING,related_name='tickets_responsibleuserid_set')  # Field name lowercase.
    title = models.CharField(max_length=150)  # Field name made lowercase.
    message = models.CharField(max_length=2500, blank=True, null=True)  # Field name made lowercase.
    reportingtext = models.CharField(max_length=500, blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField()  # Field name made lowercase.
    contactname = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    contactphone = models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    contactemail = models.CharField(max_length=320, blank=True, null=True)  # Field name made lowercase.
    attachments = models.TextField(blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'Tickets'


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(primary_key=True, max_length=150)  # Field name made lowercase.
    productversion = models.CharField(max_length=32)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = '__EFMigrationsHistory'



class Sysdiagrams(BaseModel):
    name = models.CharField(max_length=128,   )
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'sysdiagrams'
    #     unique_together = (('principal_id', 'name'),)

class Agenda(BaseModel):
    topic=models.CharField(max_length=100, blank=False, null=False)
    class Meta:
        managed = False
        db_table = 'Agenda'

class AgendaDetails(BaseModel):
    agenda = models.ForeignKey(Agenda,related_name="agenda_detail",on_delete=models.CASCADE)
    topic_details=models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'Agenda'

class Quorums(BaseModel):
    types = (
        ("head", ("Head Votes")),
        ("object", ("Object Votes")),
        ("value", ("Value Votes")),
    )
    voting_type=models.CharField(
        max_length=20, choices=types)
    present_votes=models.IntegerField(blank=False, null=False)
    condition = models.CharField(max_length=20, blank=False, null=False)
    class Meta:
        managed = False
        db_table = 'Quorums'

class Votes(BaseModel):
    types = (
        ("head", ("Head Votes")),
        ("object", ("Object Votes")),
        ("value", ("Value Votes")),
    )
    voting_type=models.CharField(max_length=20, choices=types)
    majority=models.IntegerField(blank=False, null=False)
    condition = models.CharField(max_length=20, blank=False, null=False)
    basic_set=models.CharField(max_length=20, blank=False, null=False)
    tie_case= models.CharField(max_length=20, blank=False, null=False)
    class Meta:
        managed = False
        db_table = 'Votes'