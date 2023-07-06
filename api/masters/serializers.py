from rest_framework import serializers
from masters.models import *
from tasks.models import *

class RealestateobjectSerializer(serializers.ModelSerializer):
    realestatepropertyid = serializers.CharField(read_only=True, source='realestatepropertyid.name')
    class Meta:
        model = Realestateobjects
        exclude = ('created_at', 'updated_at')


class RealestatepropertySerializer(serializers.ModelSerializer):
    objects_detail=RealestateobjectSerializer(many=True,read_only=True)
    realted_property=serializers.CharField(read_only=True, source='realted_property.name')
    realestateagentid=serializers.CharField(read_only=True, source='realestateagentid.name')
    
    class Meta:
        model = Realestateproperties
        fields = (
            "id",
            "realestateagentid",
            'objects_detail',
            "realted_property",
            "name",
            "street",
            "zip",
            "city",
            "country",
            "isactive",
            "attachment",
            
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
        exclude = ('created_at', 'updated_at')

class MessageSerializer(serializers.ModelSerializer):
    realestateagentid = serializers.CharField(read_only=True, source='realestateagentid.name')
    createdrealestateownerid = serializers.CharField(read_only=True, source='createdrealestateownerid.name')
    class Meta:
        model = Messages
        exclude = ('created_at', 'updated_at')

class MessagecommentSerializer(serializers.ModelSerializer):
    messageid = serializers.CharField(read_only=True, source='messageid.subject')
    realestateownerid = serializers.CharField(read_only=True, source='realestateownerid.name')
    class Meta:
        model = Messagecomments
        exclude = ('created_at', 'updated_at')

class RealestateserviceproviderSerializer(serializers.ModelSerializer):
    realestateproperty = serializers.CharField(read_only=True, source='realestatepropertyid.name')
    class Meta:
        model = Realestateserviceproviders
        exclude = ('created_at', 'updated_at')

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        exclude = ('created_at', 'updated_at')

class RealestatepersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realestatepropertyowner
        exclude = ('created_at', 'updated_at')



class RealestatetenantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Realestatepropertytenant
        exclude = ('created_at', 'updated_at')

class AgendaDetailSerializer(serializers.ModelSerializer):
    agenda = serializers.CharField(source='agenda.topic', read_only=True)
    class Meta:
        model = AgendaDetails
        exclude = ('created_at', 'updated_at')

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
    quorums = serializers.CharField(read_only=True)
    class Meta:
        model = Votes
        exclude = ('created_at', 'updated_at')

class Quorumsserializer(serializers.ModelSerializer):
    meeting_votes = Votesserializer(many=True)
    class Meta:
        model = Quorums
        fields = (
            "id",
            "voting_type",
            "present_votes",
            "condition",
            "meeting_votes",
        )
       

class Mettingtemplateserializer(serializers.ModelSerializer):
    quorum = serializers.CharField(source='quorum.condition', read_only=True)
    agenda = serializers.CharField(source='agenda.topic', read_only=True)
    voting_circle = serializers.CharField(source='voting_circle.manager_name', read_only=True)

    class Meta:
        model = Mettingtemplate
        exclude = ('created_at', 'updated_at')

class Subgroupserializer(serializers.ModelSerializer):
    property = serializers.CharField(read_only=True, source='property.name')
    class Meta:
        model = Realestatepropertiessubgroup
        exclude = ('created_at', 'updated_at')

# class RealEstateObjectsDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Realestateobjectsdetail
#         exclude = ('created_at', 'updated_at', 'createdby', 'lastmodifiedby')
    
class RealEstateKeysSerializer(serializers.ModelSerializer):
    property = serializers.CharField(read_only=True, source="property.name")
    object = serializers.CharField(read_only=True, source="object.object_name")
    class Meta:
        model = Realestatekeyhandover
        exclude = ('created_at', 'updated_at')

class GetPropertymanagementserializer(serializers.ModelSerializer):
    property_name = serializers.CharField(read_only=True, source="realestatepropertyid.name")
    owner_name = serializers.CharField(read_only=True, source="realestateownerid.name")
    agent_name = serializers.CharField(read_only=True, source="realestateagentid.name")
    object_name = serializers.CharField(read_only=True, source="realestateobjectid.name")
    

    class Meta:
        model = Realestatepropertymanagement
        fields = (
            "id",
            "property_name",
            "owner_name",
            "agent_name",
            "object_name",
            "manageby",
            "manageby_id",
            "manager_name",
            "manager_email",
            "manager_Phone"

        )

class Propertymanagementserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Realestatepropertymanagement
        exclude = ('created_at', 'updated_at')

class CreatePropertymanagementserializer(serializers.ModelSerializer):

    def create(self, validated_data):
        data = self.context.get('request').data
        model = self.Meta.model
        instance = model.objects.create(**validated_data)
        if instance.manageby == 'owner':
                instance.manageby_id = instance.realestateownerid.id
                instance.manager_name = instance.realestateownerid.name
                instance.manager_email = instance.realestateownerid.email
                instance.manager_Phone = instance.realestateownerid.phonenumber
        if instance.manageby == 'agent':
            instance.manageby_id = instance.realestateagentid.id
            instance.manager_name = instance.realestateagentid.name
            instance.manager_email = instance.realestateagentid.email
            instance.manager_Phone = instance.realestateagentid.phonenumber
        instance.save()

        return instance

    
    class Meta:
        model = Realestatepropertymanagement
        exclude = ('created_at', 'updated_at')

class RealEstateMeterssSerializer(serializers.ModelSerializer):
    property = serializers.CharField(read_only=True, source='property.name')
    object = serializers.CharField(read_only=True, source='object.object_name')
    class Meta:
        model = Realestatemeterhandover
        exclude = ('created_at', 'updated_at')

class RealestateobjectsdetailSerializer(serializers.ModelSerializer):
    child_details = serializers.SerializerMethodField()
    related_object = serializers.CharField(read_only=True, source='related_object.object_name')
    related_property = serializers.CharField(read_only=True, source='related_property.name')
    related_detail = serializers.CharField(read_only=True, source='related_detail.object_name')
    
    class Meta:
        model = Realestateobjectsdetail
        exclude = ('created_at', 'updated_at')

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
        exclude = ('created_at', 'updated_at')

class FurnitureInspectionMasterSerializer(serializers.ModelSerializer):
    property = serializers.CharField(read_only=True, source='property.name')
    object = serializers.CharField(read_only=True, source='object.object_name')
    class Meta:
        model = FurnitureInspectionMaster
        exclude = ('created_at', 'updated_at') 


class AppendicesMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appendicesmaster
        exclude = ('created_at', 'updated_at')



class PropertyContactSerializer(serializers.ModelSerializer):
    property_id = serializers.SerializerMethodField('get_alternate_id')
    property_name = serializers.SerializerMethodField('get_alternate_name')

    def get_alternate_name(self, obj):
        return obj.name
    
    def get_alternate_id(self, obj):
        return obj.id
    
    def to_representation(self, instance): 
        property_id = self.context['view'].kwargs['property_id']
        object_id = self.context['view'].kwargs.get('object_id')

        representation = super().to_representation(instance)
        if object_id:
            queryset = Realestatepropertymanagement.objects.filter(realestatepropertyid = property_id, realestateobjectid = object_id).first()
            representation['object_id'] = object_id
            representation['object_name'] = Realestateobjects.objects.get(id=object_id).object_name
        else:
            queryset = Realestatepropertymanagement.objects.filter(realestatepropertyid = property_id).first()
            
        representation['manager'] = {}
        representation['owner'] = {}
        representation['manager']['email'] = queryset.manager_email
        representation['manager']['name'] = queryset.manager_name
        representation['manager']['phone'] = queryset.manager_Phone
        representation['owner']['name'] = queryset.realestateownerid.name
        representation['owner']['email'] = queryset.realestateownerid.email
        representation['owner']['phone'] = queryset.realestateownerid.phonenumber
       
        queryset2 = Realestateserviceproviders.objects.filter(realestatepropertyid = property_id, job='manager').first()
        if queryset2:
            representation['serviceprovider'] = {}
            representation['serviceprovider']['name'] = queryset2.name
            representation['serviceprovider']['email'] = queryset2.email
            representation['serviceprovider']['phone'] = queryset2.phonenumber
           
        return representation
    
    class Meta:
        model = Realestateproperties
        exclude = ("id","created_at", "updated_at", "name", "street","zip", "city",
        "country", "isactive", "attachment", "realestateagentid")