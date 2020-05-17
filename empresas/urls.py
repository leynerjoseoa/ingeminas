from django.urls import path

from empresas.views import home, settings, presentacion_empresa_egresado
presentacion_empresa_egresado
urlpatterns = [
    path('settings/', settings, name='settings'),
    path('presentacion/<str:pk_empresa>/', presentacion_empresa_egresado, name='presentacion_empresa'),
    path('pre/<str:pk_empresa>/', home, name='presentacion'),
]