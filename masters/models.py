from django.db import models
from django_countries.fields import CountryField

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# class Aspnetroles(BaseModel):
#     id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=256,   blank=True, null=True)  # Field name made lowercase.
#     normalizedname = models.CharField(db_column='NormalizedName', unique=True, max_length=256,   blank=True, null=True)  # Field name made lowercase.
#     concurrencystamp = models.TextField(db_column='ConcurrencyStamp',   blank=True, null=True)  # Field name made lowercase.
#     discriminator = models.TextField(db_column='Discriminator',   )  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'AspNetRoles'

# class Aspnetroleclaims(BaseModel):
#     roleid = models.ForeignKey('Aspnetroles', models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.
#     claimtype = models.TextField(db_column='ClaimType',   blank=True, null=True)  # Field name made lowercase.
#     claimvalue = models.TextField(db_column='ClaimValue',   blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'AspNetRoleClaims'

# class Countries(models.Model):
#     id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=60,   )  # Field name made lowercase.
#     twoletterisocode = models.CharField(db_column='TwoLetterIsoCode', max_length=2,   )  # Field name made lowercase.
#     threeletterisocode = models.CharField(db_column='ThreeLetterIsoCode', max_length=3,   )  # Field name made lowercase.
#     numericisocode = models.IntegerField(db_column='NumericIsoCode')  # Field name made lowercase.
#     displayorder = models.IntegerField(db_column='DisplayOrder')  # Field name made lowercase.
#     created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
#     createdby = models.CharField(db_column='CreatedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
#     lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.CharField(db_column='LastModifiedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Countries'

# class Aspnetusers(models.Model):
#     id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=50,   )  # Field name made lowercase.
#     surname = models.CharField(db_column='Surname', max_length=100,   )  # Field name made lowercase.
#     street = models.CharField(db_column='Street', max_length=100,   blank=True, null=True)  # Field name made lowercase.
#     zip = models.CharField(db_column='Zip', max_length=10,   blank=True, null=True)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=50,   blank=True, null=True)  # Field name made lowercase.
#     countryid = models.ForeignKey('Countries', models.DO_NOTHING, db_column='CountryId', blank=True, null=True)  # Field name made lowercase.
#     languageid = models.IntegerField(db_column='LanguageId')  # Field name made lowercase.
#     isnotificationnewtickets = models.BooleanField(db_column='IsNotificationNewTickets')  # Field name made lowercase.
#     isnotificationnewupdates = models.BooleanField(db_column='IsNotificationNewUpdates')  # Field name made lowercase.
#     isnotificationticketdeadline = models.BooleanField(db_column='IsNotificationTicketDeadline')  # Field name made lowercase.
#     imagepath = models.TextField(db_column='ImagePath',   blank=True, null=True)  # Field name made lowercase.
#     lastlogindate = models.DateTimeField(db_column='LastLoginDate')  # Field name made lowercase.
#     username = models.CharField(db_column='UserName', max_length=256,   blank=True, null=True)  # Field name made lowercase.
#     normalizedusername = models.CharField(db_column='NormalizedUserName', unique=True, max_length=256,   blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', max_length=256,   blank=True, null=True)  # Field name made lowercase.
#     normalizedemail = models.CharField(db_column='NormalizedEmail', max_length=256,   blank=True, null=True)  # Field name made lowercase.
#     emailconfirmed = models.BooleanField(db_column='EmailConfirmed')  # Field name made lowercase.
#     passwordhash = models.TextField(db_column='PasswordHash',   blank=True, null=True)  # Field name made lowercase.
#     securitystamp = models.TextField(db_column='SecurityStamp',   blank=True, null=True)  # Field name made lowercase.
#     concurrencystamp = models.TextField(db_column='ConcurrencyStamp',   blank=True, null=True)  # Field name made lowercase.
#     phonenumber = models.CharField(db_column='PhoneNumber', max_length=30,   blank=True, null=True)  # Field name made lowercase.
#     phonenumberconfirmed = models.BooleanField(db_column='PhoneNumberConfirmed')  # Field name made lowercase.
#     twofactorenabled = models.BooleanField(db_column='TwoFactorEnabled')  # Field name made lowercase.
#     lockoutend = models.DateTimeField(db_column='LockoutEnd', blank=True, null=True)  # Field name made lowercase.
#     lockoutenabled = models.BooleanField(db_column='LockoutEnabled')  # Field name made lowercase.
#     accessfailedcount = models.IntegerField(db_column='AccessFailedCount')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'AspNetUsers'


# class Aspnetuserclaims(models.Model):
#     id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
#     userid = models.ForeignKey('Aspnetusers', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
#     claimtype = models.TextField(db_column='ClaimType',   blank=True, null=True)  # Field name made lowercase.
#     claimvalue = models.TextField(db_column='ClaimValue',   blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'AspNetUserClaims'


# class Aspnetuserlogins(models.Model):
#     loginprovider = models.CharField(db_column='LoginProvider', primary_key=True, max_length=450,   )  # Field name made lowercase. The composite primary key (LoginProvider, ProviderKey) found, that is not supported. The first column is selected.
#     providerkey = models.CharField(db_column='ProviderKey', max_length=450,   )  # Field name made lowercase.
#     providerdisplayname = models.TextField(db_column='ProviderDisplayName',   blank=True, null=True)  # Field name made lowercase.
#     userid = models.ForeignKey('Aspnetusers', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'AspNetUserLogins'
#         unique_together = (('loginprovider', 'providerkey'),)


# class Aspnetuserroles(models.Model):
#     userid = models.OneToOneField('Aspnetusers', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase. The composite primary key (UserId, RoleId) found, that is not supported. The first column is selected.
#     roleid = models.ForeignKey(Aspnetroles, models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'AspNetUserRoles'
#         unique_together = (('userid', 'roleid'),)


# class Aspnetusertokens(models.Model):
#     userid = models.OneToOneField('Aspnetusers', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase. The composite primary key (UserId, LoginProvider, Name) found, that is not supported. The first column is selected.
#     loginprovider = models.CharField(db_column='LoginProvider', max_length=450,   )  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=450,   )  # Field name made lowercase.
#     value = models.TextField(db_column='Value',   blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'AspNetUserTokens'
#         unique_together = (('userid', 'loginprovider', 'name'),)

class Feedbacks(BaseModel):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500,   )  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.CharField(db_column='LastModifiedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
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

class Realestateagents(BaseModel):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    prefix = models.CharField(db_column='Prefix', max_length=5)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50,   )  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=100,   )  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=320,   blank=True, null=True)  # Field name made lowercase.
    website = models.TextField(db_column='WebSite',   blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=30,   blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=100,   )  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=10,   blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50,   blank=True, null=True)  # Field name made lowercase.
    country = CountryField( blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.CharField(db_column='LastModifiedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RealEstateAgents'

class Realestatepropertyowner(BaseModel):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    #realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING, db_column='RealEstateAgentId')  # Field name made lowercase.
    realestatepersontypeid = models.IntegerField(db_column='RealEstatePersonTypeId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50,   )  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=100,   )  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=320,   blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=30,   blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=100,   )  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=10,   blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50,   blank=True, null=True)  # Field name made lowercase.
    country = CountryField( blank=True, null=True) # Field name made lowercase.
    languageid = models.IntegerField(db_column='LanguageId')  # Field name made lowercase.
    isnotificationnewtickets = models.BooleanField(db_column='IsNotificationNewTickets')  # Field name made lowercase.
    isnotificationnewupdates = models.BooleanField(db_column='IsNotificationNewUpdates')  # Field name made lowercase.
    isnotificationticketdeadline = models.BooleanField(db_column='IsNotificationTicketDeadline')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    lastlogindate = models.DateTimeField(db_column='LastLoginDate')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.CharField(db_column='LastModifiedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    attachment = models.TextField(db_column='Attachment',   blank=True, null=True)  # Field name made lowercase.
    attachments = models.TextField(db_column='Attachments',   blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Realestatepropertyowner'


class Messages(BaseModel):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    realestateagentid = models.ForeignKey('Realestateagents', models.DO_NOTHING, db_column='RealEstateAgentId')  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=150,   )  # Field name made lowercase.
    body = models.CharField(db_column='Body', max_length=2500,   )  # Field name made lowercase.
    isemailnotification = models.BooleanField(db_column='IsEmailNotification')  # Field name made lowercase.
    isimportant = models.BooleanField(db_column='IsImportant')  # Field name made lowercase.
    isallowcomment = models.BooleanField(db_column='IsAllowComment')  # Field name made lowercase.
    issendimmediately = models.BooleanField(db_column='IsSendImmediately')  # Field name made lowercase.
    senddate = models.DateTimeField(db_column='SendDate', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    createdrealestapersonid = models.ForeignKey('Realestatepropertyowner', models.DO_NOTHING, db_column='CreatedRealEstaPersonId')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    attachments = models.TextField(db_column='Attachments',   blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Messages'

class Messagecomments(BaseModel):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    messageid = models.ForeignKey('Messages', models.DO_NOTHING, db_column='MessageId')  # Field name made lowercase.
    realestapersonid = models.ForeignKey('Realestatepropertyowner', models.DO_NOTHING, db_column='RealEstaPersonId')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500,   )  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MessageComments'


class Messagerecipients(BaseModel):
    messageid = models.ForeignKey('Messages', models.DO_NOTHING, db_column='MessageId')  # Field name made lowercase.
    realestapersonid = models.OneToOneField('Realestatepropertyowner', models.DO_NOTHING, db_column='RealEstaPersonId', primary_key=True)  # Field name made lowercase. The composite primary key (RealEstaPersonId, MessageId) found, that is not supported. The first column is selected.
    isread = models.BooleanField(db_column='IsRead')  # Field name made lowercase.
    readdate = models.DateTimeField(db_column='ReadDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MessageRecipients'
        unique_together = (('realestapersonid', 'messageid'),)

class Realestateobjectpersons(BaseModel):
    realestateobjectid = models.OneToOneField('Realestateobjects', models.DO_NOTHING, db_column='RealEstateObjectId', primary_key=True)  # Field name made lowercase. The composite primary key (RealEstateObjectId, RealEstatePersonId) found, that is not supported. The first column is selected.
    realestatepersonid = models.ForeignKey('Realestatepropertyowner', models.DO_NOTHING, db_column='RealEstatePersonId')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RealEstateObjectPersons'
        unique_together = (('realestateobjectid', 'realestatepersonid'),)

class Realestateproperties(BaseModel):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING, db_column='RealEstateAgentId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50,   )  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=100,   )  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=10,   )  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50,   )  # Field name made lowercase.
    country = CountryField( blank=True, null=True) # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.CharField(db_column='LastModifiedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    attachments = models.TextField(db_column='Attachments',   blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RealEstateProperties'

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
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    realestatepropertyid = models.ForeignKey('Realestateproperties', models.DO_NOTHING, db_column='RealEstatePropertyId')  # Field name made lowercase.
    objectusagetypeid = models.IntegerField(db_column='ObjectUsageTypeId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50,   )  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100,   )  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100,   )  # Field name made lowercase.
    floor = models.CharField(db_column='Floor', max_length=20,   )  # Field name made lowercase.
    rooms = models.CharField(db_column='Rooms', max_length=20,   blank=True, null=True)  # Field name made lowercase.
    surfacearea = models.IntegerField(db_column='SurfaceArea', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.CharField(db_column='LastModifiedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    attachments = models.TextField(db_column='Attachments',   blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RealEstateObjects'


class Realestatepropertymanagement(BaseModel):
    realestatepropertyid = models.OneToOneField(Realestateproperties, models.DO_NOTHING, db_column='RealEstatePropertyId', primary_key=True)  
    realestatepersonid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING, db_column='RealEstatePersonId')  
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING, db_column='RealEstateAgentId') 
    realestateobjectid = models.ForeignKey(Realestateobjects, models.DO_NOTHING, db_column='Realestateobjectid')

    class Meta:
        managed = False
        db_table = 'Realestatepropertymanagement'
        #unique_together = (('realestatepropertyid', 'realestatepersonid'),)


class Realestateserviceproviders(BaseModel):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING, db_column='RealEstateAgentId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50,   )  # Field name made lowercase.
    field = models.CharField(db_column='Field', max_length=50,   blank=True, null=True)  # Field name made lowercase.
    languageid = models.IntegerField(db_column='LanguageId')  # Field name made lowercase.
    contactname = models.TextField(db_column='ContactName',   blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=30,   )  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=320,   )  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=100,   )  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=10,   )  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50,   )  # Field name made lowercase.
    country = CountryField( blank=True, null=True)
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.CharField(db_column='LastModifiedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RealEstateServiceProviders'


class Ticketmessages(BaseModel):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    ticketid = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='TicketId')  # Field name made lowercase.
    realestapersonid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING, db_column='RealEstaPersonId')  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=2500,   )  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    attachments = models.TextField(db_column='Attachments',   blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TicketMessages'


class Ticketoffers(BaseModel):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    offertypeid = models.IntegerField(db_column='OfferTypeId')  # Field name made lowercase.
    ticketid = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='TicketId')  # Field name made lowercase.
    realestateserviceproviderid = models.ForeignKey(Realestateserviceproviders, models.DO_NOTHING, db_column='RealEstateServiceProviderId')  # Field name made lowercase.
    requestnote = models.CharField(db_column='RequestNote', max_length=1000,   blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=1000,   blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pricelimit = models.DecimalField(db_column='PriceLimit', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    deadline = models.DateField(db_column='Deadline', blank=True, null=True)  # Field name made lowercase.
    appointmentdate = models.DateTimeField(db_column='AppointmentDate', blank=True, null=True)  # Field name made lowercase.
    serviceproviderratingbytenant = models.IntegerField(db_column='ServiceProviderRatingByTenant', blank=True, null=True)  # Field name made lowercase.
    serviceprovidercommentbytenant = models.CharField(db_column='ServiceProviderCommentByTenant', max_length=1000,   blank=True, null=True)  # Field name made lowercase.
    serviceproviderratingbymanager = models.IntegerField(db_column='ServiceProviderRatingByManager', blank=True, null=True)  # Field name made lowercase.
    serviceprovidercommentbymanager = models.CharField(db_column='ServiceProviderCommentByManager', max_length=1000,   blank=True, null=True)  # Field name made lowercase.
    ourrating = models.IntegerField(db_column='OurRating', blank=True, null=True)  # Field name made lowercase.
    problemcomment = models.CharField(db_column='ProblemComment', max_length=1000,   blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.CharField(db_column='LastModifiedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    noteattachments = models.TextField(db_column='NoteAttachments',   blank=True, null=True)  # Field name made lowercase.
    requestnoteattachments = models.TextField(db_column='RequestNoteAttachments',   blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TicketOffers'
        unique_together = (('ticketid', 'realestateserviceproviderid', 'status'),)


class Ticketsequences(BaseModel):
    realestateagentid = models.CharField(db_column='RealEstateAgentId', primary_key=True, max_length=36)  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TicketSequences'


class Tickets(BaseModel):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.
    slug = models.CharField(db_column='Slug', max_length=15,   )  # Field name made lowercase.
    realestateagentid = models.ForeignKey(Realestateagents, models.DO_NOTHING, db_column='RealEstateAgentId')  # Field name made lowercase.
    realestatepropertyid = models.ForeignKey(Realestateproperties, models.DO_NOTHING, db_column='RealEstatePropertyId')  # Field name made lowercase.
    realestateobjectid = models.ForeignKey(Realestateobjects, models.DO_NOTHING, db_column='RealEstateObjectId', blank=True, null=True)  # Field name made lowercase.
    realestatetenantid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING, db_column='RealEstateTenantId')  # Field name made lowercase.
    responsibleuserid = models.ForeignKey(Realestatepropertyowner, models.DO_NOTHING, db_column='ResponsibleUserId', related_name='tickets_responsibleuserid_set')  # Field name lowercase.
    title = models.CharField(db_column='Title', max_length=150,   )  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=2500,   blank=True, null=True)  # Field name made lowercase.
    reportingtext = models.CharField(db_column='ReportingText', max_length=500,   blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=100,   blank=True, null=True)  # Field name made lowercase.
    contactphone = models.CharField(db_column='ContactPhone', max_length=30,   blank=True, null=True)  # Field name made lowercase.
    contactemail = models.CharField(db_column='ContactEmail', max_length=320,   blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.CharField(db_column='LastModifiedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.
    attachments = models.TextField(db_column='Attachments',   blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(db_column='Info',   blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tickets'


class Efmigrationshistory(BaseModel):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150,   )  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32,   )  # Field name made lowercase.
    class Meta:

        managed = False
        db_table = '__EFMigrationsHistory'

class Sysdiagrams(BaseModel):
    name = models.CharField(max_length=128,   )
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)

# New tables for meetings 
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