from rest_framework import serializers
from sales.models import *
from masters.models import *

class PersonmoveinSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PersonVisit
        exclude = ('created_at', 'updated_at')

class TenderSerializer(serializers.ModelSerializer):
    property = serializers.CharField(source='property.name')
    object = serializers.CharField(source='object.object_name')

    class Meta:
        model = Tender
        exclude = ('created_at', 'updated_at')
    
    def create(self, validated_data):
        property_data = validated_data.pop('property', None)
        object_data = validated_data.pop('object', None)

        tender = Tender.objects.create(**validated_data)

        if property_data:
            property_instance, _ = Realestateproperties.objects.get_or_create(name=property_data['name'])
            tender.property = property_instance

        if object_data:
            object_instance, _ = Realestateobjects.objects.get_or_create(object_name=object_data['object_name'])
            tender.object = object_instance

        tender.save()
        return tender
