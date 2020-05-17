from django.urls import path, include
from administrador.views import home,registrar_egresado,registrar_empresa
urlpatterns = [
        path('registrar_egresado/', registrar_egresado, name="registrar_egresado"),
path('registrar_empresa/', registrar_empresa, name="registrar_empresa"),
        path('', home, name="home"),
]
