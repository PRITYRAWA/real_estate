from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from checkin.models import *
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from django.http import HttpRequest
from django.urls import reverse

from django.http import HttpResponse
class CheckInOutListCreateView(viewsets.ModelViewSet):
    queryset = CheckInOut.objects.all()
    serializer_class = CheckInOutSerializer



class keysViewSet(viewsets.ModelViewSet):
    queryset = Realestatekey.objects.all()
    serializer_class = KeysSerializer
    lookup_field = 'obj'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def perform_create(self, serializer):
        print(self.request.data)
        photos_string = self.request.data.get('photos')
        photos = json.loads(photos_string) if photos_string else []
        serializer.save(photos=photos)



def generate_pdf_report(request):
    # Get the data from the serializer
    serializer = CheckInOutSerializer(instance=CheckInOut.objects.all(), many=True)
    serialized_data = serializer.data

    # Define the folder path to save the PDF file
    folder_path = os.path.join(os.getcwd(), 'pdf')
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

    # Construct the URL manually
    protocol = 'http://' if not request.is_secure() else 'https://'
    host = request.get_host()
    report_url = f"{protocol}{host}/pdf/report.pdf"

    return HttpResponse(report_url)