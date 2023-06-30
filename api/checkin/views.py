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
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors
from django.shortcuts import get_object_or_404
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO



class CheckInOutListCreateView(viewsets.ModelViewSet):
    queryset = CheckInOut.objects.all()
    serializer_class = CheckInOutSerializer

class ObjectListInspectionViewSet(viewsets.ModelViewSet):
    queryset = ObjectListInspection.objects.all()
    serializer_class = ObjectListInspectionSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(related_detail=None)  # Exclude self-related items
        return queryset
    
class ChildObjectListInspectionViewSet(viewsets.ModelViewSet):
    queryset = ObjectListInspection.objects.all()
    serializer_class = ChildDetailSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']



class KeysViewSet(viewsets.ModelViewSet):
    queryset = Realestatekey.objects.all()
    serializer_class = KeysSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        checkin_id = self.request.query_params.get('checkin')
        obj_id = self.request.query_params.get('obj')
        queryset = Realestatekey.objects.all()

        if checkin_id and obj_id:
            queryset = queryset.filter(Q(checkin=checkin_id) & Q(obj=obj_id))
        elif checkin_id:
            queryset = queryset.filter(checkin=checkin_id)
        elif obj_id:
            queryset = queryset.filter(obj=obj_id)
        return queryset

class MetersViewSet(viewsets.ModelViewSet):
    queryset = Realestatemeter.objects.all()
    serializer_class = MetersSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        checkin_id = self.request.query_params.get('checkin')
        obj_id = self.request.query_params.get('obj')
        queryset = Realestatemeter.objects.all()

        if checkin_id and obj_id:
            queryset = queryset.filter(Q(checkin=checkin_id) & Q(obj=obj_id))
        elif checkin_id:
            queryset = queryset.filter(checkin=checkin_id)
        elif obj_id:
            queryset = queryset.filter(obj=obj_id)
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
        print(data)
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
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
    def get_queryset(self):
        checkin_id = self.request.query_params.get('checkin')
        if checkin_id:
            queryset = FurnitureInspection.objects.filter(checkin=checkin_id)
        else:
            queryset = super().get_queryset() 

        return queryset


class RentaldeductionViewSet(viewsets.ModelViewSet):
    queryset = RentalDeduction.objects.all()
    serializer_class = RentaldeductionSerializer
    # http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        checkin_id = self.request.query_params.get('checkin')
        obj_id = self.request.query_params.get('obj')
        queryset = RentalDeduction.objects.all()

        if checkin_id and obj_id:
            queryset = queryset.filter(Q(checkin=checkin_id) & Q(obj=obj_id))
        elif checkin_id:
            queryset = queryset.filter(checkin=checkin_id)
        elif obj_id:
            queryset = queryset.filter(obj=obj_id)
        return queryset
    
class AppendTransViewSet(viewsets.ModelViewSet):
    queryset = Appendicestransaction.objects.all()
    serializer_class = AppendicesTransSerializer

    def get_queryset(self):
        checkin_id = self.request.query_params.get('checkin')
        obj_id = self.request.query_params.get('obj')
        queryset = Appendicestransaction.objects.all()

        if checkin_id and obj_id:
            queryset = queryset.filter(Q(checkin=checkin_id) & Q(obj=obj_id))
        elif checkin_id:
            queryset = queryset.filter(checkin=checkin_id)
        elif obj_id:
            queryset = queryset.filter(obj=obj_id)
        return queryset
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Checkincomments.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Checkincomments.objects.all()
        checkin_id = self.request.query_params.get('checkin')
        if checkin_id:
            queryset = Checkincomments.objects.filter(checkin=checkin_id)
        else:
            queryset = super().get_queryset() 
        return queryset
        
class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer

class PersonmoveinViewSet(viewsets.ModelViewSet):
    queryset = Personmovein.objects.all()
    serializer_class = PersonmoveinSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if Realestatepropertytenant.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists in Realestatepropertytenant.'},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


def generate_pdf(request, pk):
    inspection = FurnitureInspection.objects.get(pk=pk)
    serializer = FurnitureInspectionSerializer(inspection)
    pdf_path = serializer.generate_pdf(serializer.data)

    with open(pdf_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=furniture_inspection_{pk}.pdf'
        return response
    


def generate_pdf_report_furniture(request: HttpRequest) -> HttpResponse:
    # Get the data from the serializer
    serializer = FurnitureInspectionSerializer(instance=FurnitureInspection.objects.all(), many=True)
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
    c.drawString(50, 750, 'Check-In/furniture Report')

    # Write the report content
    c.setFont(content_style, 12)
    y = 700

    for data in serialized_data:
        # Extract relevant fields from the serialized data
        # user_name = data['user_name']
        cleaning_type = data['cleaning_type']
        description = data['description']
        # check_out_date = data['check_out_date']

        # Write the data to the PDF
        # c.drawString(50, y, f"User Name: {user_name}")
        c.drawString(50, y - 20, f"cleaning type: {cleaning_type}")
        c.drawString(50, y - 40, f"description: {description}")
        # c.drawString(50, y - 60, f"Check-Out Date: {check_out_date}")
        c.drawString(50, y - 80, "-" * 50)

        y -= 100
 
    # Save the PDF and close the canvas
    c.save()

    # Get the relative path of the PDF file within the media folder
    relative_path = os.path.join('pdf', 'report.pdf')

    # Construct the URL to access the PDF
    report_url = request.build_absolute_uri(f"{settings.MEDIA_URL}{relative_path}")

    return HttpResponse(report_url)




def generate_checkin_report(request, id):
    checkin = get_object_or_404(CheckInOut, id=id)
    furniture_inspections = FurnitureInspection.objects.filter(checkin=checkin)
    rental_deductions = RentalDeduction.objects.filter(checkin=checkin)
    appendices_transactions = Appendicestransaction.objects.filter(checkin=checkin)
    checkin_comments = Checkincomments.objects.filter(checkin=checkin)

    doc = SimpleDocTemplate("checkin_report.pdf", pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    buffer = BytesIO()

    title = Paragraph("<b>Check-In Report</b>", styles["Title"])
    elements.append(title)

    # Add check-in details
    user = checkin.user
    object_check_in = checkin.object_check_in
    agent = object_check_in.realestatepropertyid.realestateagentid
    property_name = object_check_in.realestatepropertyid.name
    object_name = object_check_in.object_name

    details_data = [
        ["User", user.name],
        ["Agent", agent.name],
        ["Property Name", property_name],
        ["Object Name", object_name],
    ]

    details_table = Table(details_data, colWidths=100, rowHeights=30)
    details_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(details_table)

    # Add object details
    object_details = object_check_in.object_detail.all()

    if object_details:
        elements.append(Paragraph("<b>Object Details</b>", styles["Heading2"]))

        object_data = [["Object Detail", "Property Name"]]

        for detail in object_details:
            object_data.append([detail.object_name, detail.related_property.name])

        object_table = Table(object_data, colWidths=[200, 200], rowHeights=30)
        object_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 12),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(object_table)

    # Add furniture inspections table
    if furniture_inspections:
        elements.append(Paragraph("<b>Furniture Inspections</b>", styles["Heading2"]))

        furniture_data = [["Cleaning Type", "Photos", "Description"]]

        for inspection in furniture_inspections:
            cleaning_type = inspection.cleaning_type
            photos = inspection.photos.url if inspection.photos else ""
            description = inspection.description

            furniture_data.append([cleaning_type, photos, description])

        furniture_table = Table(furniture_data, colWidths=[100, 150, 200], rowHeights=30)
        furniture_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 12),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(furniture_table)

    # Add rental deductions table
    if rental_deductions:
        elements.append(Paragraph("<b>Rental Deductions</b>", styles["Heading2"]))

        rental_deductions_data = [["Title", "Deduction Type", "Photos", "Description", "Deadline", "Period"]]

        for deduction in rental_deductions:
            title = deduction.title
            deduction_type = deduction.deduction_type
            photos = deduction.photos.url if deduction.photos else ""
            description = deduction.description
            deadline = deduction.deadline.strftime("%Y-%m-%d %H:%M:%S")
            period = deduction.period

            rental_deductions_data.append([title, deduction_type, photos, description, deadline, period])

        rental_deductions_table = Table(rental_deductions_data, colWidths=[100, 100, 150, 200, 100, 100], rowHeights=30)
        rental_deductions_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 12),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(rental_deductions_table)

    # Add appendices transactions table
    if appendices_transactions:
        elements.append(Paragraph("<b>Appendices Transactions</b>", styles["Heading2"]))

        appendices_transactions_data = [["Object", "Photos", "Count", "Description", "Name"]]

        for transaction in appendices_transactions:
            obj = transaction.obj
            photos = transaction.photos.url if transaction.photos else ""
            count = transaction.count
            description = transaction.description
            name = transaction.name

            appendices_transactions_data.append([obj, photos, count, description, name])

        appendices_transactions_table = Table(appendices_transactions_data, colWidths=[150, 150, 50, 200, 100], rowHeights=30)
        appendices_transactions_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 12),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(appendices_transactions_table)

    # Add check-in comments table
    if checkin_comments:
        elements.append(Paragraph("<b>Check-In Comments</b>", styles["Heading2"]))

        checkin_comments_data = [["Real Estate Owner", "Tenant Comment", "Comment"]]

        for comment in checkin_comments:
            real_estate_owner = comment.realestateownerid
            tenant_comment = comment.tenantcomment
            comment_text = comment.comment

            checkin_comments_data.append([real_estate_owner, tenant_comment, comment_text])

        checkin_comments_table = Table(checkin_comments_data, colWidths=[150, 150, 200], rowHeights=30)
        checkin_comments_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 12),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(checkin_comments_table)

    # Build the PDF document
    doc.build(elements)

    # Get the PDF content from the buffer
    pdf = buffer.getvalue()

    # Close the buffer
    buffer.close()

    # Create a PDF response
    pdf_response = HttpResponse(content_type='application/pdf')
    pdf_response['Content-Disposition'] = 'attachment; filename="checkin_report.pdf"'
    pdf_response.write(pdf)

    return pdf_response