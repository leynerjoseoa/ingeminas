from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from accounts.decorators import unauthenticated_user
from accounts.forms import CreateUserForm


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
                if user.empresa:
                    return redirect('empresas:home')
            except:
                pass
            try:
                if user.egresado:
                    print('e')
                    return redirect('egresados:home')
            except:
                pass
            try:
                if user.administrador:
                    return redirect('administrador_home')
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
