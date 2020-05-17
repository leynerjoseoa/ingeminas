from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

# Create your views here.
from egresados.forms import EgresadoForm
from egresados.models import Egresado


def home(request):
    return render(request, 'administrador/main.html')


def registrar_egresado(request):
    if request.method == 'GET':
        form = EgresadoForm()
    elif request.method == 'POST':
        try:
            user = User(
                username=request.POST.get('name'),
                email=request.POST.get('email')
            )
            user.set_password(request.POST.get('clave'))
            user.save()
            egresado = Egresado.objects.create(
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
