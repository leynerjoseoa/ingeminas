from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from convocatorias.forms import ConvocatoriaForm
from convocatorias.models import Convocatoria
from egresados.models import Egresado
from empresas.models import EmpresaUsuario


def crear(request):
    if request.method == 'GET':
        form = ConvocatoriaForm()
    elif request.method == 'POST':
        form = ConvocatoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Convocatoria creada correctamente')
        else:
            print('[',form.errors,' ] Estos son los errores')
            messages.error(request, 'No se ha creado correctamente la convocatoria', extra_tags='danger')
    context = {'form': form}
    return render(request, 'convocatorias/crear.html', context)


def editar(request, pk_convocatoria):
    if request.method == 'GET':
        convocatoria = Convocatoria.objects.get(id=pk_convocatoria)
        form = ConvocatoriaForm(instance=convocatoria)
    elif request.method == 'POST':
        convocatoria = Convocatoria.objects.get(id=pk_convocatoria)
        form = ConvocatoriaForm(request.POST,instance=convocatoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Convocatoria modificada correctamente')
        else:
            messages.error(request, 'No se ha modificado correctamente la convocatoria', extra_tags='danger')
    context = {'form': form}
    return render(request, 'convocatorias/editar.html', context)


def eliminar(request, pk_convocatoria):
    convocatoria = Convocatoria.objects.get(id=pk_convocatoria)
    if request.method == 'GET':
        context = {
            'convocatoria': convocatoria,
            'empresa_id':request.user.empresausuario.id
        }
    if request.method == 'POST':
        convocatoria.delete()
        messages.success(request, 'Convocatoria eliminada correctamente')
        return redirect('convocatorias:convocatorias_empresas',request.user.empresausuario.id)
    return render(request, 'convocatorias/eliminar.html', context)


def ver(request, pk_convocatoria):
    convocatoria = Convocatoria.objects.get(id=pk_convocatoria)
    context = {'convocatoria': convocatoria}
    return render(request, 'convocatorias/ver.html', context)


def convocatorias_egresado(request, pk_egresado):
    egresado = Egresado.objects.get(id=pk_egresado)
    convocatorias = Convocatoria.objects.filter(egresados=egresado)
    context = {'convocatorias': convocatorias}
    return render(request, 'egresados/convocatorias.html', context)


def convocatorias_empresa(request, pk_empresa):
    empresa1 = EmpresaUsuario.objects.get(id=pk_empresa)
    convocatorias = Convocatoria.objects.filter(empresa=empresa1)
    context = {'convocatorias': convocatorias}
    return render(request, 'empresas/convocatorias.html', context)