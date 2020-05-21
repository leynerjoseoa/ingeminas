from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                if request.user.empresausuario:
                    return redirect('empresas:presentacion', pk_empresa=request.user.empresausuario.id)
            except:
                pass
            try:
                if request.user.egresado:
                    return redirect('egresados:home')
            except:
                pass
            try:
                if request.user.administrador:
                    return redirect('administrador:home')
            except:
                return HttpResponse('Ya iniciaste sesion')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

