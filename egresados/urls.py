from django.urls import path, include
from egresados.views import home, settings, empleos, empleo, crearEmpleo, crear_empresa

urlpatterns = [
    path('settings/',settings, name='settings'),
    path('empleos/',empleos, name='empleos'),
    path('empleo/<str:pk>/', empleo, name='empleo'),
    path('crear_empleo/<str:pk>/', crearEmpleo, name='crear_empleo'),
    #path('crear_empresa/', crearEmpresa, name='crear_empresa'),
    path('crear_empresa/', crear_empresa,name='crear_empresa'),
    path('', home, name="home"),
]
