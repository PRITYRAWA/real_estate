from rest_framework import serializers
from masters.models import *

class RealestateobjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateobjects
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')


class RealestatepropertySerializer(serializers.ModelSerializer):
    objects_detail=RealestateobjectSerializer(many=True,read_only=True)
    
    class Meta:
        model = Realestateproperties
        fields = (
            "id",
            "name",
            "street",
            "zip",
            "city",
            "country",
            "isactive",
            "attachment",
            "objects_detail",
            
        )

    def create(self, validated_data):
        realestatepropertyobjects_detail = validated_data.pop('objects_detail', None)
        realestateproperty = Realestateproperties.objects.create(**validated_data)

        if realestatepropertyobjects_detail:
            Realestateobjects.objects.create(realestatepropertyid=realestateproperty, **realestatepropertyobjects_detail[0])

        return realestateproperty

class RealestateagentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateagents
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

class MessagecommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messagecomments
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

class TicketofferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticketoffers
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

class RealestateserviceproviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateserviceproviders
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

class RealestatepersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestatepropertyowner
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')



class RealestatetenantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Realestatepropertytenant
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

class AgendaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaDetails
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

class Agendaserializer(serializers.ModelSerializer):
    agenda_detail = AgendaDetailSerializer(many=True)
    class Meta:
        model = Agenda
        fields = (
            "id",
            "topic",
            "status",
            "agenda_detail",
            
        )

class Votesserializer(serializers.ModelSerializer):
    class Meta:
        model = Votes
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')       

class Quorumsserializer(serializers.ModelSerializer):
    votes_detail = Votesserializer(many=True)
    class Meta:
        model = Quorums
        fields = (
            "id",
            "voting_type",
            "present_votes",
            "condition",
            "votes_detail",
        )
       

class Mettingtemplateserializer(serializers.ModelSerializer):
    class Meta:
        model = Mettingtemplate
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

class Subgroupserializer(serializers.ModelSerializer):
    class Meta:
        model = Realestatepropertiessubgroup
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

# class RealEstateObjectsDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Realestateobjectsdetail
#         exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')
    
class RealEstateKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestatekeyhandover
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')    

class Propertymanagementserializer(serializers.ModelSerializer):
    class Meta:
        model = Realestatepropertymanagement
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')
class RealEstateMeterssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestatemeterhandover
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

class RealestateobjectsdetailSerializer(serializers.ModelSerializer):
    child_details = serializers.SerializerMethodField()

    class Meta:
        model = Realestateobjectsdetail
        fields = '__all__'

    def get_child_details(self, obj):
        if self.context.get('exclude_child_details'):
            return []
        child_details = obj.child_details.all()
        serialized_child_details = self.__class__(child_details, many=True, context={'exclude_child_details': True}).data
        return serialized_child_details

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('child_details')  # Remove child_details from the main representation
        representation['child_details'] = self.get_child_details(instance)
        return representation

class RealEstateObjectsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateobjectsdetail
        fields = '__all__' 
    

class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')
