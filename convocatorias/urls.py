from django.urls import path, include
from convocatorias.views import crear, convocatorias_egresado, ver, convocatorias_empresa, editar, eliminar

urlpatterns = [
    path('ver/<str:pk_convocatoria>/', ver, name="ver"),
    path('convocatorias/<str:pk_egresado>/', convocatorias_egresado, name="convocatorias_egresado"),
    path('convocatorias_empresa/<str:pk_empresa>/', convocatorias_empresa, name="convocatorias_empresas"),
    path('editar/<str:pk_convocatoria>/', editar, name="editar"),
    path('eliminar/<str:pk_convocatoria>/', eliminar, name="eliminar"),
    path('crear/', crear, name="crear"),
]