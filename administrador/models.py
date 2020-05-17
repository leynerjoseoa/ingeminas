from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=200, null=True)
    email = models.EmailField(blank=True, null=True)
    foto = models.ImageField(blank=True, default='education.png', null=True, upload_to='')
    def __str__(self):
        return self.name