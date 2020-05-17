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
            'foto': 'Foto de la empresa',
            'descripcion': 'Descripcion de la empresa',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el nombre de la empresa'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el correo electronico de la empresa'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control-file',
                }
            )
        }

        exclude = ['user']


