from django.urls import path, include
from empleo.views import home
urlpatterns = [
    path('', home, name="home"),
]