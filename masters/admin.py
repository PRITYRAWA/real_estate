from django.contrib import admin
from masters.models import *

# Register your models here.
admin.site.register([
                     Feedbacks,  Realestateagents,
                     Messages, Messagecomments,Messagerecipients,
                     Realestateserviceproviders, Ticketmessages, Ticketoffers, Ticketsequences, Tickets,
                     Efmigrationshistory, Sysdiagrams])

# creating parent child model for agenda
class AgendaDetailsInline(admin.TabularInline):
    model = AgendaDetails
    extra = 1

@admin.register(Agenda)
class CustomAgenda(admin.ModelAdmin):
    
    inlines = [
        AgendaDetailsInline,
    ]

# creating parent child model for quroms   
class VotesInline(admin.TabularInline):
    model = Votes
    extra = 1


@admin.register(Quorums)
class CustomQuorums(admin.ModelAdmin):
    
    inlines = [
        VotesInline,
    ]


class ObjectsInline(admin.TabularInline):
    model = Realestateobjects
    extra = 1


@admin.register(Realestateproperties)
class CustomProperties(admin.ModelAdmin):
    
    inlines = [
        ObjectsInline,
    ]