from django.urls import path, include
from administrador.views import home
urlpatterns = [
        path('', home, name="administrador_home"),
]
