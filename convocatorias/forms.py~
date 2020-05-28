from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm
from django import forms

from convocatorias.models import Convocatoria


class ConvocatoriaForm(ModelForm):
    # contenido = forms.TextInput(widget=CKEditorWidget())
    contenido = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Convocatoria
        fields = ['titulo', 'descripcion', 'contenido','empresa','egresados']
        # content = forms.CharField(widget=CKEditorWidget())
        # contenido = forms.CharField(widget=CKEditorWidget())

        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el titulo de la convocatoria'
                }
            ), 'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa una descripcion'
                }
            ),

            # 'contenido':forms.CharField(widget=CKEditorWidget())
        }
