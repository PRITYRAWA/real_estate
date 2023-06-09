from django.contrib import admin
from masters.models import *

# Register your models here.
admin.site.register([
                     Feedbacks,  Realestateagents,
                     Messages, Messagecomments,Messagerecipients, Realestateobjectpersons, Realestateproperties, Realestateobjects,
                     Realestateserviceproviders, Ticketmessages, Ticketoffers, Ticketsequences, Tickets,
                     Efmigrationshistory, Sysdiagrams])