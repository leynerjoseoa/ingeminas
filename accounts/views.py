from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from accounts.decorators import unauthenticated_user
from accounts.forms import CreateUserForm, GraduadoForm
from accounts.models import Egresado
from accounts.templatetags.has_group import register


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            #group = Group.objects.get(name='customer')
            #user.groups.add(group)
            # Customer.objects.create(
            #     user=user,
            #     name=user.username,
            # )
            messages.success(request, 'Account was created for ' + username)
            return redirect('home')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@login_required(login_url='login')
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
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def egresado(request):
    context = {}
    return render(request, 'accounts/egresado.html', context)

def graduadoSettings(request):
    egresado = request.user.egresado
    form = GraduadoForm(instance=egresado)
    if request.method == 'POST':
        form = GraduadoForm(request.POST, request.FILES, instance=egresado)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'egresado/settings.html', context)
