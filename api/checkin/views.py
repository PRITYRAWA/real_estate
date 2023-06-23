from rest_framework import viewsets
from .serializers import *
from checkin.models import *
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from django.http import HttpRequest
from django.conf import settings
from django.http import HttpResponse

class CheckInOutListCreateView(viewsets.ModelViewSet):
    queryset = CheckInOut.objects.all()
    serializer_class = CheckInOutSerializer

class ObjectListInspectionView(viewsets.ModelViewSet):
    queryset = ObjectListInspection.objects.all()
    serializer_class = CheckInOutSerializer


class KeysViewSet(viewsets.ModelViewSet):
    queryset = Realestatekey.objects.all()
    serializer_class = KeysSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        checkin_id = self.request.query_params.get('checkin')
        if checkin_id:
            queryset = Realestatekey.objects.filter(checkin=checkin_id)
        else:
            queryset = super().get_queryset() 

        return queryset

class MetersViewSet(viewsets.ModelViewSet):
    queryset = Realestatemeter.objects.all()
    serializer_class = MetersSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        checkin_id = self.request.query_params.get('checkin')
        if checkin_id:
            queryset = Realestatemeter.objects.filter(checkin=checkin_id)
        else:
            queryset = super().get_queryset() 

        return queryset


def generate_pdf_report(request: HttpRequest) -> HttpResponse:
    # Get the data from the serializer
    serializer = CheckInOutSerializer(instance=CheckInOut.objects.all(), many=True)
    serialized_data = serializer.data

    # Define the folder path to save the PDF file
    folder_path = os.path.join(settings.MEDIA_ROOT, 'pdf')
    os.makedirs(folder_path, exist_ok=True)

    # Define the file path for the PDF
    file_path = os.path.join(folder_path, 'report.pdf')

    # Create the PDF document
    c = canvas.Canvas(file_path, pagesize=letter)

    # Define the styles for the report
    title_style = 'Helvetica-Bold'
    content_style = 'Helvetica'

    # Write the report title
    c.setFont(title_style, 16)
    c.drawString(50, 750, 'Check-In/Check-Out Report')

    # Write the report content
    c.setFont(content_style, 12)
    y = 700

    for data in serialized_data:
        # Extract relevant fields from the serialized data
        user_name = data['user_name']
        service_ticket_number = data['service_ticket_number']
        check_in_date = data['check_in_date']
        check_out_date = data['check_out_date']

        # Write the data to the PDF
        c.drawString(50, y, f"User Name: {user_name}")
        c.drawString(50, y - 20, f"Service Ticket Number: {service_ticket_number}")
        c.drawString(50, y - 40, f"Check-In Date: {check_in_date}")
        c.drawString(50, y - 60, f"Check-Out Date: {check_out_date}")
        c.drawString(50, y - 80, "-" * 50)

        y -= 100
 
    # Save the PDF and close the canvas
    c.save()

    # Get the relative path of the PDF file within the media folder
    relative_path = os.path.join('pdf', 'report.pdf')

    # Construct the URL to access the PDF
    report_url = request.build_absolute_uri(f"{settings.MEDIA_URL}{relative_path}")

    return HttpResponse(report_url)

class FurnitureInspectionViewSet(viewsets.ModelViewSet):
    queryset = FurnitureInspection.objects.all()
    serializer_class = FurnitureInspectionSerializer
    lookup_field = 'checkin'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    # def retrieve(self, request, *args, **kwargs):
    #     self.lookup_field = 'checkin'
    #     return super().retrieve(request, *args, **kwargs)

class RentaldeductionViewSet(viewsets.ModelViewSet):
    queryset = FurnitureInspection.objects.all()
    serializer_class = RentaldeductionSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


def generate_pdf(request, pk):
    inspection = FurnitureInspection.objects.get(pk=pk)
    serializer = FurnitureInspectionSerializer(inspection)
    pdf_path = serializer.generate_pdf(serializer.data)

    with open(pdf_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=furniture_inspection_{pk}.pdf'
        return response