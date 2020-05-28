from django.contrib.auth.models import User
from django.db import models

# Create your models here.

"""se usa el parámetro blank=True en campos tipo Texto o null=True para campos tipo Fecha o Numéricos."""


class Egresado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    foto = models.ImageField(default='education.png', null=True, upload_to='', blank=True)
    email = models.EmailField(blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    fechaNacimiento = models.DateField(editable=True, blank=True, null=True)
    fechaGrado = models.DateField(editable=True, blank=True, null=True)
    ESTADO = (
        ('empleado', 'empleado'),
        ('desempleado', 'desempleado'),
    )
    estado = models.CharField(max_length=200, null=False, choices=ESTADO, blank=False)
    def __str__(self):
        return self.name
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    egresado = models.OneToOneField(Egresado, on_delete=models.CASCADE)
    #document = models.FileField(upload_to='documents/')
    document = models.FileField(upload_to='Archivos/egresados')
    uploaded_at = models.DateTimeField(auto_now_add=True)
