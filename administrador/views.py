from io import BytesIO

from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
# Create your views here.
from reportlab.platypus import Paragraph, Table, TableStyle

from egresados.forms import EgresadoForm
from egresados.models import Egresado
from empresas.forms import EmpresaForm
from empresas.models import EmpresaUsuario


def home(request):
    return render(request, 'administrador/main.html')

def listado_egresados_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment: filename=reporte_egresados.pdf'
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    c.setLineWidth(.3)
    c.setFont('Courier',8)
    c.setFillColorRGB(0,0,255)
    c.drawString(30, 5, 'www.nodeweb.com')
    c.setFillColorRGB(0,0,0)
    c.setFont('Helvetica', 24)
    c.drawString(30,750,'MINAS')
    c.setFont('Helvetica', 12)
    c.drawString(30,730,'Report')
    c.setFont('Helvetica', 8)
    c.drawString(480,750,str(datetime.now()))
    c.line(480,747,590,747)
    egresados = Egresado.objects.all()

    #table header
    styles =getSampleStyleSheet()
    styleBH=styles['Normal']
    styleBH.alignment=TA_CENTER
    styleBH.fontSize=10

    numero = Paragraph('''#''',styleBH)
    alumno = Paragraph('''Egresado''',styleBH)
    b1=Paragraph('''BIM1''',styleBH)
    b2 = Paragraph('''BIM1''', styleBH)
    b3 = Paragraph('''BIM1''', styleBH)
    total = Paragraph('''Promedio''', styleBH)
    data=[]
    data.append([numero,alumno,b1,b2,b3,total])

    #tabla
    styleN =styles['BodyText']
    styleN.alignment=TA_CENTER
    styleN.fontSize=7
    high=650
    for e in egresados:
        data_aux=[e.id,e.name,e.email,e.estado,5,6]
        data.append(data_aux)
        high=high-18

    #tablesize
    width,height=A4
    table=Table(data,colWidths=[1*cm,2*cm,4*cm,3*cm,1.9*cm,2*cm,])
    table.setStyle(TableStyle([
        ('INNERGRID',(0,0),(-1,-1),0.25,colors.black),
        ('BOX',(0,0),(-1,-1),0.25,colors.black)
    ]))
    table.wrapOn(c,width,height)
    table.drawOn(c,30,high)
    c.showPage()
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


def registrar_egresado(request):
    if request.method == 'GET':
        form = EgresadoForm(request.POST)
    elif request.method == 'POST':
        try:
            user = User(
                username=request.POST.get('name'),
                email=request.POST.get('email')
            )
            user.set_password(request.POST.get('clave'))
            user.save()
            Egresado.objects.create(
                user=user,
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                estado='desempleado'
            )
            print(user.id, '[ id del usuario egresado]')
            messages.success(request, 'Egresado registrado correctamente.')
            return redirect('administrador:registrar_egresado')
        except IntegrityError:
            messages.error(request, 'Es posible que este usuario ya se encuentre registrado', extra_tags='danger')
    return render(request, 'administrador/registrar_egresado.html', context={'form': form})

def registrar_empresa(request):
    if request.method == 'GET':
        form = EmpresaForm(request.POST)
    elif request.method == 'POST':
        try:
            user = User(
                username=request.POST.get('name'),
                email=request.POST.get('email')
            )
            user.set_password(request.POST.get('clave'))
            user.save()
            EmpresaUsuario.objects.create(
                user=user,
                name=request.POST.get('name'),
                email=request.POST.get('email'),
            )
            messages.success(request, 'Empresa registrada correctamente.')
            return redirect('administrador:registrar_empresa')
        except IntegrityError:
            messages.error(request, 'Es posible que la empresa ya se encuentre registrado', extra_tags='danger')
    return render(request, 'administrador/registrar_empresa.html', context={'form': form})


