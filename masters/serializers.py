from rest_framework import serializers
from .models import *

class RealestatepropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateproperties
        fields = '__all__'

class RealestateobjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateobjects
        fields = '__all__'

class RealestateagentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateagents
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'

class MessagecommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messagecomments
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'

class TicketofferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticketoffers
        fields = '__all__'

class RealestateserviceproviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestateserviceproviders
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = '__all__'

class Realestateowner(serializers.ModelSerializer):
    class Meta:
        model = Realestatepropertyowner
        fields = '__all__'
