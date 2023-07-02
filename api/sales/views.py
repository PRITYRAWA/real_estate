from django.shortcuts import render
from .serializers import *
from api.masters.serializers import RealestateobjectSerializer
from sales.models import *
from masters.models import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class PersonmoveinViewSet(viewsets.ModelViewSet):
    queryset = PersonVisit.objects.all()
    serializer_class = PersonmoveinSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if Realestatepropertytenant.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists in Realestatepropertytenant.'},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer

class VacantPropertiesViewSet(viewsets.ModelViewSet):
    serializer_class = RealestateobjectSerializer

    def get_queryset(self):
            return Realestateobjects.objects.filter(status='VACANT')


