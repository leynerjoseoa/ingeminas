from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm
from django import forms

from empresas.models import EmpresaUsuario


class EmpresaForm(ModelForm):
    descripcion = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = EmpresaUsuario
        # fields = '__all__'
        fields = ['name', 'email', 'foto', 'descripcion']
        labels = {
            'name': 'Nombre de la empresa',
            'email': 'Email de la empresa',
            'foto': 'Foto de la eempresa',
            'descripcion': 'Descripcion de la epresa',
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
            # 'descripcion': forms.Textarea(
            #     attrs={
            #         'class': 'form-control col-md-12',
            #         'placeholder': 'Ingresa una breve descripcion de ti',
            #         'cols': 40, 'rows': 1,
            #     }
            # ),


        }

        exclude = ['user']


