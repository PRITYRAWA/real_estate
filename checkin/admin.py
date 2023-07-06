from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register([CheckInOut,GeneralInspection,ObjectListInspection,FurnitureInspection,Realestatekey,Realestatemeter,Checkincomments,Appendicestransaction,RentalDeduction,CheckinContacts,CheckinImage])

