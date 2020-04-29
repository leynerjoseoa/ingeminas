from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from egresados.models import Egresado


class GraduadoForm(ModelForm):
    class Meta:
        model = Egresado
        # fields = '__all__'
        fields = ['name', 'email', 'foto', 'descripcion', 'fechaGrado', 'fechaNacimiento']
        labels = {
            'name': 'Nombre del egresado',
            'email': 'Email del egresado',
            'foto': 'Foto del egresado',
            'descripcion': 'Descripcion del egresado',
            'fechaNacimiento': 'fecha nacimiento del egresado',
            'fechaGrado': 'fecha de grado del egresado',
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

            'fechaGrado': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class': 'form-control'
                }),
            'fechaNacimiento': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class': 'form-control'
                }),

        }

        exclude = ['user']
