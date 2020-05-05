from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from gunicorn import app

from egresados.forms import GraduadoForm
from egresados.models import Egresado
from empleo.forms import EmpleoForm, EmpresaForm
from empleo.models import Empleo, Entidad


def home(request):
    return render(request, 'egresados/main.html')


def settings(request):
    egresado = request.user.egresado
    form = GraduadoForm(instance=egresado)
    if request.method == 'POST':
        form = GraduadoForm(request.POST, request.FILES, instance=egresado)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'egresados/settings.html', context)


def empleos(request):
    empleos = Empleo.objects.filter(egresado=request.user.egresado)
    context = {'empleos': empleos}
    return render(request, 'egresados/empleos.html', context)


def empleo(request, pk):
    empleo = Empleo.objects.get(id=pk)
    form = EmpleoForm(instance=empleo)
    if request.method == 'POST':
        form = EmpleoForm(request.POST, instance=empleo)
        if form.is_valid():
            form.save()
            redirect('egresados:empleos')
    context = {'empleo': empleo, 'form': form}
    return render(request, 'egresados/empleo.html', context)


def crearEmpleo(request, pk):
    empresas = Entidad.objects.all()
    egresado = Egresado.objects.get(id=pk)
    # entidad = Entidad.objects.cre
    # EmpleoFormSet = inlineformset_factory(Egresado, Order, fields=('product', 'status'), extra=5)
    form = EmpleoForm()
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleo creado correctamente')
            redirect('egresados:empleos')
        else:
            messages.error(request, 'No se ha creado el empleo', extra_tags='danger')
            redirect('egresados:empleos')
    context = {'form':form,'empresas':empresas}
    return render(request, 'egresados/crear_empleo.html', context)

def crear_empresa(request):

    if Entidad.objects.filter(pk=request.POST.get('nit')).exists():
        #acciones cuando la entidad ya existe
        print('si existe entidad')
        if request.method == 'POST':
            print(' => post')
            empresa = Entidad.objects.get(pk=request.POST.get('nit'))
            form = EmpresaForm(request.POST, instance=empresa)
            if form.is_valid():
                form.save()
                messages.success(request, 'Empresa modificada correctamente')
                redirect('egresados:crear_empleo', pk=request.user.egresado.id)
            else:
                messages.error(request, 'Ya esta registrada esta Empresa', extra_tags='danger')
                redirect('egresados:crear_empleo', pk=request.user.egresado.id)
        else:
            print(' => get')
    else:
        #acciones cuando la entidad noexiste
        print('no existe entidad')
        form = EmpresaForm()
        if request.method == 'POST':
            print(' => post')
            form = EmpresaForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Empresa creada correctamente')
                redirect('egresados:crear_empleo', pk=request.user.egresado.id)
            else:
                messages.error(request, 'Ya esta registrada esta Empresa', extra_tags='danger')
                redirect('egresados:crear_empleo', pk=request.user.egresado.id)
        else:
            print(' => get')
    # form=EmpresaForm()
    #
    # if request.method == 'POST':
    #     empresa = Entidad.objects.get(pk=request.POST.get('nit'))
    #     print('#')
    #     if empresa is None:
    #         print('es vacio')
    #     print(empresa)
    #     print('#')
    #     form = EmpresaForm(request.POST, instance=empresa)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Empresa creada correctamente')
    #         redirect('egresados:crear_empleo',pk=request.user.egresado.id)
    #     else:
    #         messages.error(request, 'Ya esta registrada esta Empresa', extra_tags='danger')
    #         redirect('egresados:crear_empleo', pk=request.user.egresado.id)
    context = {'form':form,'empresas':Entidad.objects.all()}
    return render(request, 'egresados/crear_empresa.html', context)
# from datetime import date
# Empleo.objects.create(cargo="doctor",fechaIngreso=date(2020,2,2),fechaSalida=date(2020,3,7))


# def crearEmpresa(request):
#     print('test')
#     print(request)
#     print(request.POST)
#     nombre = request.POST.get('nombre_empresa')
#     descripcion = request.POST.get('descripcion_empresa')
#     # empresa = Entidad.objects.create(nombre=nombre,descripicion=descripcion,estado=True)
#     # form_empresa = EmpresaForm(instance=empresa)
#     if request.method == 'POST':
#         form = EmpresaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             redirect('egresados:empleos')
#     context = {}
#     # return redirect('egresados:empleos')
#     return render(request, 'egresados/crear_empleo.html', context)

