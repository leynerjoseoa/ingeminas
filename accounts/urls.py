from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import home, egresado, loginPage, logoutUser

urlpatterns = [
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),

    path('egresado/', egresado, name='egresado'),
    path('', loginPage),
]
