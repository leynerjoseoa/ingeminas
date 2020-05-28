from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from accounts.decorators import unauthenticated_user

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