from django.db import models

# Create your models here.
from egresados.models import Egresado


class Entidad(models.Model):
    nombre = models.CharField(max_length=200,blank=False,null=False)
    nit = models.CharField(max_length=50, primary_key=True,blank=True)
    descripicion = models.CharField(max_length=200, blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Empleo(models.Model):
    cargo = models.CharField(max_length=200, blank=True, null=True)
    fechaIngreso = models.DateField(editable=True, null=True)
    fechaSalida = models.DateField(editable=True, null=True)

    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    egresado = models.ForeignKey(Egresado, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} en {1} :{2}'.format(self.cargo, self.entidad, self.egresado)



