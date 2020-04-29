from django.urls import path, include
from egresados.views import home, settings
urlpatterns = [
    path('settings/',settings, name='settings'),
    path('', home, name="home"),
]
