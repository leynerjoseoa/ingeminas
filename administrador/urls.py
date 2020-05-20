from django.urls import path, include
from administrador.views import home,registrar_egresado,registrar_empresa,listado_egresados_pdf
urlpatterns = [
        path('registrar_egresado/', registrar_egresado, name="registrar_egresado"),
        path('registrar_empresa/', registrar_empresa, name="registrar_empresa"),
        path('listado_egresados_pdf/', listado_egresados_pdf, name="listado_egresados_pdf"),
        path('', home, name="home"),
]
