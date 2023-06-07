from rest_framework import serializers
from .models import Realestateproperties, Realestateobjects, Realestateagents, Messages, Messagecomments, Tickets, Ticketoffers, Realestateserviceproviders


class RealestatepropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateproperties
        exclude = ('created', 'createdby', 'lastmodified', 'lastmodifiedby')

class RealestateobjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateobjects
        exclude = ('created', 'createdby', 'lastmodified', 'lastmodifiedby')

class RealestateagentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateagents
        exclude = ('created', 'createdby', 'lastmodified', 'lastmodifiedby')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        exclude = ('created', 'createdby', 'lastmodified', 'lastmodifiedby')

class MessagecommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messagecomments
        exclude = ('created',)

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        exclude = ('created',)

class TicketofferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticketoffers
        exclude = ('created',)

class RealestateserviceproviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateserviceproviders
        exclude = ('created',)