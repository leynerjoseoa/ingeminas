from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from egresados.models import Egresado
from empresas.models import EmpresaUsuario


class Convocatoria(models.Model):
    titulo = models.CharField(max_length=200, blank=True)
    descripcion = models.CharField(max_length=200, blank=True)
    contenido = RichTextField('Descripcion', null=False, blank=False,config_name='default')
    imagen = models.URLField('Imagen de Fondo', max_length=100, null=False, blank=False)
    fechaCreacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    egresados = models.ManyToManyField(Egresado)
    empresa = models.ForeignKey(EmpresaUsuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo