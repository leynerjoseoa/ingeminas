from django.urls import path

from empresas.views import home, settings

urlpatterns = [
    path('settings/', settings, name='settings'),
    path('', home, name='home'),
]