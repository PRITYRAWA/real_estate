from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register([CheckInOut,GeneralInspection,ObjectListInspection,FurnitureInspection,Realestatekey,Checkincomments,Appendicestransaction,RentalDeduction,Personmovein])