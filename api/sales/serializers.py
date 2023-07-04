from rest_framework import serializers
from sales.models import *
from masters.models import *

class PersonmoveinSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PersonVisit
        exclude = ('created_at', 'updated_at')

class TenderSerializer(serializers.ModelSerializer):
    property = serializers.CharField(read_only=True, source='property.name')
    object = serializers.CharField(read_only=True, source='object.object_name')
    class Meta:
        model = Tender
        exclude = ('created_at', 'updated_at')
