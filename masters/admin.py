from django.contrib import admin
from masters.models import *

# Register your models here.
admin.site.register([Aspnetroles, Aspnetroleclaims, Countries, Aspnetusers, Aspnetuserclaims, Aspnetuserlogins, Aspnetuserroles, Aspnetusertokens,
                     Feedbacks, Languages, Localestringresources, Localizedproperties, Realestateagents, Realestatepersons,
                     Messages, Messagecomments,Messagerecipients, Realestateobjectpersons, Realestateproperties, Realestateobjects,
                     Realestatepropertypersons, Realestateserviceproviders, Ticketmessages, Ticketoffers, Ticketsequences, Tickets,
                     Efmigrationshistory, Sysdiagrams])