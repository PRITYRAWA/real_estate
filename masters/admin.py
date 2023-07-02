from django.contrib import admin
from masters.models import *

# Register your models here.
admin.site.register([
                     # Feedbacks,  
                     # Messages, Messagecomments,Messagerecipients, Languages,
                     Realestateagents,
                     Realestateserviceproviders,Realestatepropertytenant,Realestatepropertiessubgroup,
                     Realestatepropertyowner,Localestringresources,Localizedproperties,
                     Realestatekeyhandover,Realestatemeterhandover,FurnitureInspectionMaster,
                     Appendicesmaster])




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
            if manage_by == 'owner':
                obj.manageby_id = obj.realestateownerid.id
                obj.manager_name = obj.realestateownerid.name
                obj.manager_email = obj.realestateownerid.email
                obj.manager_Phone = obj.realestateownerid.phonenumber
            if manage_by == 'agent':
                obj.manageby_id = obj.realestateagentid.id
                obj.manager_name = obj.realestateagentid.name
                obj.manager_email = obj.realestateagentid.email
                obj.manager_Phone = obj.realestateagentid.phonenumber
            obj.save()
        super().save_model(request, obj, form, change)