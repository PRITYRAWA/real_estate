from django.contrib import admin
from masters.models import *

# Register your models here.
admin.site.register([
                     Feedbacks,  Realestateagents,
                     Messages, Messagecomments,Messagerecipients,
                     Realestateserviceproviders, Ticketmessages, Ticketoffers, Ticketsequences, Tickets,
                     Efmigrationshistory,Languages,Realestatepropertytenant,Sysdiagrams,Realestatepropertiessubgroup,Realestatepropertymanagement,Realestatepropertyowner,Localestringresources,Localizedproperties,Realestatekeyhandover,Realestatemeterhandover,Appendicesmaster,Tender])




# creating parent child model for agenda
class AgendaDetailsInline(admin.TabularInline):
    model = AgendaDetails
    extra = 1

@admin.register(Agenda)
class CustomAgenda(admin.ModelAdmin):
    exclude = ("createdby","lastmodifiedby")
    inlines = [
        AgendaDetailsInline,
    ]

# creating parent child model for quroms   
class VotesInline(admin.TabularInline):
    model = Votes
    extra = 1


@admin.register(Quorums)
class CustomQuorums(admin.ModelAdmin):
    exclude = ("createdby","lastmodifiedby")
    inlines = [
        VotesInline,
    ]


class ObjectsInline(admin.TabularInline):
    model = Realestateobjects
    extra = 1


@admin.register(Realestateproperties)
class CustomProperties(admin.ModelAdmin):
    exclude = ("createdby","lastmodifiedby")
    inlines = [
        ObjectsInline,
    ]

class ObjectsdetailInline(admin.TabularInline):
    model = Realestateobjectsdetail
    extra = 1

@admin.register(Realestateobjects)
class CustomProperties(admin.ModelAdmin):
    exclude = ("createdby","lastmodifiedby")
    inlines = [
        ObjectsdetailInline,
    ]
