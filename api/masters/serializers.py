from rest_framework import serializers
from masters.models import *

class RealestateobjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateobjects
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')

class RealestatepropertySerializer(serializers.ModelSerializer):
    objects_detail=RealestateobjectSerializer(many=True)

    class Meta:
        model = Realestateproperties
        fields = (
            "id",
            "realestateagentid",
            "name",
            "street",
            "zip",
            "city",
            "country",
            "isactive",
            "attachment",
            "objects_detail",
            
        )

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

class RealEstateObjectsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateobjectsdetail
        fields = '__all__'  

class Propertymanagementserializer(serializers.ModelSerializer):
    class Meta:
        model = Realestatepropertymanagement
        exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')