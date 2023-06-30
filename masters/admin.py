from django.contrib import admin
from masters.models import *

# Register your models here.
admin.site.register([
                     Feedbacks,  Realestateagents,
                     Messages, Messagecomments,Messagerecipients,
                     Realestateserviceproviders, Ticketmessages, Ticketoffers, Ticketsequences, Tickets,
                     Efmigrationshistory,Languages,Realestatepropertytenant,Sysdiagrams,Realestatepropertiessubgroup,Realestatepropertyowner,Localestringresources,Localizedproperties,Realestatekeyhandover,Realestatemeterhandover,Appendicesmaster,Tender])




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

@admin.register(Realestatepropertymanagement)
class PropertyManagement(admin.ModelAdmin):
   
    def save_model(self, request, obj, form, change):
        manage_by=obj.manageby
        if not change:
            print("id",obj.id)
            if manage_by == 'owner':
                owner = obj.realestateownerid
                record = Realestatepropertyowner.objects.get(id=owner)
                print(record.email)
                print("owner",owner)
            if manage_by == 'agent':
                agent = obj.realestateownerid
                print("agent",agent)
            if not change:  # Only populate the value if it's a new object
                obj.some_field = "Value based on ID: {}".format(obj.id)
        super().save_model(request, obj, form, change)