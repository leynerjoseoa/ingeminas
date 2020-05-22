from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from gunicorn import app

from egresados.forms import EgresadoForm
from egresados.models import Egresado
from empleo.forms import EmpleoForm, EmpresaForm
from empleo.models import Empleo, Entidad
from convocatorias.models import Convocatoria

def home(request):
    pk_egresado = request.user.egresado.id
    egresado1=Egresado.objects.get(id=pk_egresado)
    convocatorias=Convocatoria.objects.filter(egresados=egresado1)
    context={
            'id_egresado':request.user.egresado.id,
            'convocatorias':convocatorias
            }
    return render(request, 'egresados/main.html',context)

def settings(request):
    egresado = request.user.egresado
    form = EgresadoForm(instance=egresado)
    if request.method == 'POST':
        form = EgresadoForm(request.POST, request.FILES, instance=egresado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos modificados correctamente!')
        else:
            messages.error(request, 'No se han modificado los datos correctamente!', extra_tags='danger')
    context = {'form': form}
    return render(request, 'egresados/settings.html', context)


def empleos(request):
    print('llevando empleos')
    empleos = Empleo.objects.filter(egresado=request.user.egresado)
    print('empleos del egresado {0}'.format(empleos.count()))
    context = {'empleos': empleos}
    return render(request, 'egresados/empleos.html', context)


def empleo(request, pk):
    print('pk del egresado{0}'.format(pk))
    empleo = Empleo.objects.get(id=pk)
    form = EmpleoForm(instance=empleo)
    if request.method == 'POST':
        form = EmpleoForm(request.POST, instance=empleo)
        if form.is_valid():
            form.save()
            return redirect('egresados:empleos')  # aqui lo cambieredirect('egresados:empleos')
    context = {'empleo': empleo, 'form': form}
    return render(request, 'egresados/empleo.html', context)


# def eliminarEmpleo(request,pk_empleo):
#     empleo1 = Empleo.objects.get(pk=pk_empleo)
#     empleo1.delete()
#     return redirect('egresados:empleos')
# def eliminarEmpleo(request,pk_empleo):
#     empleo1 = Empleo.objects.get(pk=pk_empleo)
#     if request.method == 'POST':
#         empleo1.delete()
#         return redirect('egresados:empleos')
#     context={'item':empleo1}
#     return render(request, 'egresados/eliminar_empleo.html', context)
# @csrf_exempt
def eliminarEmpleo(request, pk_empleo):
    print('#DELETE#', pk_empleo, ']')
    print('#DELETE#', request.POST.get('c_sesion'), ']')
    template_name = 'egresados/eliminar_empleo.html'
    empleo1 = Empleo.objects.get(pk=pk_empleo)
    if request.method == 'POST':
        print('va a eliminar')
        empleo1.delete()
        messages.success(request, 'Empleo eliminado correctamente')
        return redirect('egresados:empleos')
    context = {'item': empleo1}
    if request.method == 'GET':
        context = {'item': empleo1}
    return render(request, template_name, context)

    ##########################  FIN DELETE ############################


def editarEmpleo(request, pk_empleo):
    empleo1 = Empleo.objects.get(pk=pk_empleo)
    if request.method == 'POST':
        form = EmpleoForm(request.POST, instance=empleo1)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleo modificado correctamente')
            return redirect('egresados:editar_empleo', pk_empleo=empleo1.pk)
        else:
            messages.error(request, 'No se ha modificado el empleo', extra_tags='danger')
            return redirect('egresados:editar_empleo', pk_empleo=empleo1.pk)
    else:
        form = EmpleoForm(instance=empleo1)
    context = {'form': form, 'empleo': empleo1}
    # return render(request, 'egresados/modal_editar_empleo.html', context)
    return render(request, 'egresados/editar_empleo.html', context)


def crearEmpleo(request):
    form = EmpleoForm()
    if request.method == 'POST':
        form = EmpleoForm(request.POST)
        if form.is_valid():
            test = form.save()
            print(test, 'ñ')
            messages.success(request, 'Empleo creado correctamente')
            return redirect('egresados:editar_empleo', test.pk)
        else:
            messages.error(request, 'No se ha creado el empleo', extra_tags='danger')
            return redirect('egresados:crear_empleo', pk=request.user.egresado.id)

    print('va bien')
    context = {'form': form}
    return render(request, 'egresados/crear_empleo.html', context)


# def crearEmpleo(request, pk):
#     empresas = Entidad.objects.all()
#     print('va bien')
#     #request.POST += Egresado.objects.get(pk=request.user.egresado.pk)
#     print(request.POST)
#     egresado = Egresado.objects.get(id=pk)
#     # EmpleoFormSet = inlineformset_factory(Egresado, Order, fields=('product', 'status'), extra=5)
#     form = EmpleoForm()
#     if request.method == 'POST':
#         #empresa = Entidad.objects.get(pk=request.POST.get('entidad'))
#         #print(empresa.nombre)
#         request.POST
#         form = EmpleoForm(request.POST)
#         print(form)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Empleo creado correctamente')
#             redirect('egresados:empleos')
#         else:
#             messages.error(request, 'No se ha creado el empleo', extra_tags='danger')
#             redirect('egresados:empleos')
#     context = {'form':form,'empresas':empresas}
#     return render(request, 'egresados/crear_empleo.html', context)

def crear_empresa(request):
    if Entidad.objects.filter(pk=request.POST.get('nit')).exists():
        # acciones cuando la entidad ya existe
        print('si existe entidad')
        if request.method == 'POST':
            print(' => post')
            empresa = Entidad.objects.get(pk=request.POST.get('nit'))
            form = EmpresaForm(request.POST, instance=empresa)
            if form.is_valid():
                form.save()
                messages.success(request, 'Empresa modificada correctamente')
                redirect('egresados:crear_empleo')
            else:
                messages.error(request, 'Ya esta registrada esta Empresa', extra_tags='danger')
                redirect('egresados:crear_empleo')
        else:
            print(' => get')
    else:
        # acciones cuando la entidad noexiste
        print('no existe entidad')
        form = EmpresaForm()
        if request.method == 'POST':
            print(' => post')
            form = EmpresaForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Empresa creada correctamente')
                redirect('egresados:crear_empleo')
            else:
                messages.error(request, 'Ya esta registrada esta Empresa', extra_tags='danger')
                redirect('egresados:crear_empleo')
        else:
            print(' => get')

    context = {'form': form, 'empresas': Entidad.objects.all()}
    return render(request, 'egresados/crear_empresa.html', context)

def egresados(request):
    graduates = Egresado.objects.filter(estado=request.GET.get('estado'))
    return JsonResponse(list(graduates.values()), safe=False)


def egresados(request):
    graduates = Egresado.objects.all()
    print(graduates)
    return JsonResponse(list(graduates.values()), safe=False)
