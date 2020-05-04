from django.contrib import admin

# Register your models here.
from empleo.models import Entidad, Empleo

admin.site.register(Entidad)
admin.site.register(Empleo)