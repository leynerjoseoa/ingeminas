from django.shortcuts import render

# Create your views here.
from egresados.forms import GraduadoForm
from empleo.models import Empleo


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
    context = {'empleos':empleos}
    return render(request, 'egresados/empleos.html', context)