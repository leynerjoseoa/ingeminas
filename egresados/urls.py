from django.urls import path, include
from egresados.views import home, settings, empleos, empleo, crearEmpleo, crear_empresa, editarEmpleo, eliminarEmpleo

urlpatterns = [

    #  path('empleo/<str:pk>/', empleo, name='empleo'),

    path('editar_empleo/<str:pk_empleo>/', editarEmpleo, name='editar_empleo'),
    path('eliminar_empleo/<str:pk_empleo>/', eliminarEmpleo, name='eliminar_empleo'),
    # path('crear_empresa/', crearEmpresa, name='crear_empresa'),

    path('crear_empresa/', crear_empresa, name='crear_empresa'),
    path('editar_empleo/<str:pk_empleo>/', editarEmpleo, name='editar_empleo'),
    path('crear_empleo/', crearEmpleo, name='crear_empleo'),
    path('settings/', settings, name='settings'),
    path('empleos/', empleos, name='empleos'),
    path('', home, name="home"),
]
# path('settings/', settings, name='settings'),
#     path('empleos/', empleos, name='empleos'),
#     #  path('empleo/<str:pk>/', empleo, name='empleo'),
#     path('crear_empleo/<str:pk>/', crearEmpleo, name='crear_empleo'),
#     path('editar_empleo/<str:pk_empleo>/', editarEmpleo, name='editar_empleo'),
#     path('eliminar_empleo/<str:pk_empleo>/', eliminarEmpleo, name='eliminar_empleo'),
#     # path('crear_empresa/', crearEmpresa, name='crear_empresa'),
#     path('crear_empresa/', crear_empresa, name='crear_empresa'),
#
#     path('', home, name="home"),
