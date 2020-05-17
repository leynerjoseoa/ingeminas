from django import forms
from django.forms import ModelForm, models

from empleo.models import Empleo, Entidad

class EmpleoForm(models.ModelForm):
    class Meta:
        model = Empleo
        fields = '__all__'
        widgets = {
            'cargo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa tu nombre'
                }
            ),
            'fechaIngreso': forms.SelectDateWidget(
                years=range(1900, 2001),
                attrs={
                    'class': 'form-control col-md-4',
                }
            ),
            'fechaSalida': forms.SelectDateWidget(

                years=range(1900, 2001),
                attrs={
                    'class': 'form-control col-md-4',
                }

            ),
            'entidad': forms.Select(
                attrs={
                    'class': 'form-control',
                }

            ),

            'pk': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa tu nombre'
                }
            )
            # 'fechaSalida': forms.DateInput(
            #     format=('%d/%m/%Y'),
            #     attrs={
            #         'class': 'form-control'
            #     }),
        }
        # exclude = ['egresado']


# class EmpresaForm(models.ModelForm):
#     class Meta:
#         model = Entidad
#         fields = '__all__'
#         widgets = {
#             'nombre': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Nombre de la empresa'
#                 }
#             ),
#             'nit': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'NIT de la empresa'
#                 }
#             ),
#             'descripicion': forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Descripcion de la empresa ',
#                     'cols': 40, 'rows': 1,
#                 })
#         }
#         exclude = ['estado']
