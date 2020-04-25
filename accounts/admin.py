from django.contrib import admin

# Register your models here.
from accounts.models import Egresado, Administrador

admin.site.register(Egresado)
admin.site.register(Administrador)

