from django.contrib import admin
from masters.models import *
from django.db.models import Sum
from django.db.models import Count

# Register your models here.
admin.site.register([
                     # Feedbacks,  
                     # Messages, Messagecomments,Messagerecipients, Languages,
                     Realestateagents,
                     Realestateserviceproviders,Realestatepropertytenant,Realestatepropertiessubgroup,
                     Realestatepropertyowner,Localestringresources,Localizedproperties,
                     Realestatekeyhandover,Realestatemeterhandover,FurnitureInspectionMaster,
                     Appendicesmaster,Quorums,Votes])




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
        object=obj.realestateobjectid
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
            if object:
                asset_value= Realestateobjects.objects.get(id=object.id)
                obj.asset_value=asset_value.value
                obj.object_count= 1
            else:
                asset_value=Realestateobjects.objects.filter(realestatepropertyid=obj.realestatepropertyid.id).aggregate(total=Sum('value'))
                object_count = Realestateobjects.objects.filter(realestatepropertyid=obj.realestatepropertyid.id).count()
                
                sum_value = asset_value['total']
                print("object",object_count,"sum",sum_value)
                if object_count == 0:
                    obj.asset_value=0.00
                    obj.object_count=1
                else:
                    obj.asset_value=sum_value
                    obj.object_count=object_count
            obj.save()
        super().save_model(request, obj, form, change)