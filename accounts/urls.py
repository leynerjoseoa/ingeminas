from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import home, egresado, registerPage, loginPage, logoutUser, graduadoSettings

urlpatterns = [
    path('register/', registerPage, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),

    path('account/', graduadoSettings, name="graduado_settings"),
    # path('login/', loginPage, name="login"),
    # path('logout/', logoutUser, name="logout"),


    path('egresado/', egresado, name='egresado'),
    path('', home, name='home'),
]
