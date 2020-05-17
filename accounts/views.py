from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from accounts.decorators import unauthenticated_user
from accounts.forms import CreateUserForm
from egresados.models import Egresado


def crear_egresado(request):
    #me = User.objects.create(username='monica',email='monica@gmail.com',password='0Clave0001',is_active=True)
    try:
        me = User(username='albertao', email='alberto@gmail.com', is_active=True)
        me.set_password('0Clave0001')

        me.save()
        egresado = Egresado.objects.create(
            # user=models.OneToOneField(User, on_delete=models.CASCADE)
            user=me,
            name='alberto',
            email='alberto@gmail.com',
            descripcion='estu',

            estado='desempleado'
        )
        return HttpResponse('ready!')
    except IntegrityError:
        return HttpResponse('Integrity Error!')

    return HttpResponse('Failed!')


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # group = Group.objects.get(name='customer')
            # user.groups.add(group)
            # Customer.objects.create(
            #     user=user,
            #     name=user.username,
            # )
            messages.success(request, 'Account was created for ' + username)
            return redirect('home')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@login_required(login_url='login')
@permission_required('accounts.view_egresado', raise_exception=True)
def home(request):
    context = {}
    return render(request, 'accounts/dashboard.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                if user.empresausuario:
                    return redirect('empresas:presentacion', pk_empresa=request.user.empresausuario.id)
            except:
                pass
            try:
                if user.egresado:
                    return redirect('egresados:home')
            except:
                pass
            try:
                if user.administrador:
                    return redirect('administrador:home')
            except:
                pass

            print('ninguno')
        else:
            messages.info(request, 'Usuario o clave incorrecta')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def egresado(request):
    context = {}
    return render(request, 'accounts/egresado.html', context)

# def graduadoSettings(request):
#     egresado = request.user.egresado
#     form = GraduadoForm(instance=egresado)
#     if request.method == 'POST':
#         form = GraduadoForm(request.POST, request.FILES, instance=egresado)
#         if form.is_valid():
#             form.save()
#     context = {'form': form}
#     return render(request, 'egresado/settings.html', context)
