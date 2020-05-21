from django.urls import path, include
from egresados.views import *

urlpatterns = [


    path('editar_empleo/<str:pk_empleo>/', editarEmpleo, name='editar_empleo'),
    path('eliminar_empleo/<str:pk_empleo>/', eliminarEmpleo, name='eliminar_empleo'),

    path('crear_empresa/', crear_empresa, name='crear_empresa'),
    path('editar_empleo/<str:pk_empleo>/', editarEmpleo, name='editar_empleo'),
    path('crear_empleo/', crearEmpleo, name='crear_empleo'),
    path('settings/', settings, name='settings'),
    path('empleos/', empleos, name='empleos'),
    path('', home, name="home"),


    path('egresados/', egresados, name="egresados"),
]

