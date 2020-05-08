from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class EmpresaUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    foto = models.ImageField(default='education.png', upload_to='', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
