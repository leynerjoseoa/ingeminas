from django import forms
from django.forms import ModelForm, models

from empleo.models import Empleo, Entidad


class EmpleoForm(models.ModelForm):
    class Meta:
        model = Empleo
        fields='__all__'
        widgets={
            'cargo':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa tu nombre'
                }
            ),
            'fechaIngreso': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class': 'form-control'
                }),
            'fechaSalida': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class': 'form-control'
                }),
        }
        exclude = ['egresado','entidad']

class EmpresaForm(models.ModelForm):
    class Meta:
        model = Entidad
        fields='__all__'
        widgets={
            'nombre':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la empresa'
                }
            ),
            'nit': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'NIT de la empresa'
                }
            ),
            'descripicion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripcion de la empresa ',
                    'cols': 40, 'rows': 1,
                })
        }
        exclude=['estado']