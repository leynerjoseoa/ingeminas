from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from empresas.forms import EmpresaForm
from empresas.models import EmpresaUsuario


def home(request, pk_empresa):
    """devuelve un objeto(Empresa) con la informacion de la misma, si no existe devuelve el objeto vacio
    requiere recivir por parametro el id de la empresa"""
    try:
        empresa = EmpresaUsuario.objects.get(id=pk_empresa)
    except EmpresaUsuario.DoesNotExist:
        empresa = None
        messages.error(request, 'No existe la Empresa', extra_tags='danger')
    context = {'empresa': empresa}
    return render(request, 'empresas/presentacion.html',  context)

def presentacion_empresa_egresado(request, pk_empresa):
    """devuelve un objeto(Empresa) con la informacion de la misma, si no existe devuelve el objeto vacio
    requiere recivir por parametro el id de la empresa"""
    try:
        empresa = EmpresaUsuario.objects.get(id=pk_empresa)
    except EmpresaUsuario.DoesNotExist:
        empresa = None
        messages.error(request, 'No existe la Empresa', extra_tags='danger')
    context = {'empresa': empresa}
    return render(request, 'egresados/presentacion_empresa.html',  context)


def settings(request):
    empresa = request.user.empresausuario
    form = EmpresaForm(instance=empresa)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa modificada correctamente')
        else:
            messages.error(request, 'No se ha modificado la Empresa', extra_tags='danger')
    context = {'form': form}
    return render(request, 'empresas/settings.html', context)
