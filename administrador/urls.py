from django.urls import path, include
from administrador.views import home,registrar_egresado
urlpatterns = [
        path('registrar_egresado', registrar_egresado, name="registrar_egresado"),
        path('', home, name="home"),
]
