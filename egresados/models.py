from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime

"""se usa el parámetro blank=True en campos tipo Texto o null=True para campos tipo Fecha o Numéricos."""


class Egresado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    foto = models.ImageField(default='education.png', null=True, upload_to='', blank=True)
    email = models.EmailField(blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    fechaNacimiento = models.DateField(editable=True, blank=True, null=True)
    fechaGrado = models.DateField(editable=True, blank=True, null=True)

    def __str__(self):
        return self.name
