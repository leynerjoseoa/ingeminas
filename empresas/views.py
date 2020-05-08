from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from empresas.forms import EmpresaForm
from empresas.models import EmpresaUsuario


def home(request):
    return render(request,'empresas/dashboard.html')


def settings(request):
    empresa = request.user.empresa
    form = EmpresaForm(instance=empresa)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'empresas/settings.html', context)