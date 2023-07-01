from rest_framework import serializers
from sales.models import *

class PersonmoveinSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PersonVisit
        exclude = ('created_at', 'updated_at')

class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        exclude = ('created_at', 'updated_at')
