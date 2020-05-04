from django.urls import path, include
from egresados.views import home, settings, empleos
urlpatterns = [
    path('settings/',settings, name='settings'),
    path('empleos/',empleos, name='empleos'),

    path('', home, name="home"),
]
