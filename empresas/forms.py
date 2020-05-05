from django.forms import ModelForm
from django import forms

from empresas.models import Empresa


class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        # fields = '__all__'
        fields = ['name', 'email', 'foto', 'descripcion']
        labels = {
            'name': 'Nombre del egresado',
            'email': 'Email del egresado',
            'foto': 'Foto del egresado',
            'descripcion': 'Descripcion del egresado',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa tu nombre'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa tu correo electronico'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                    'placeholder': 'Ingresa tu correo electronico'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa una breve descripcion de ti',
                    'cols': 40, 'rows': 1,
                }
            ),


        }

        exclude = ['user']


