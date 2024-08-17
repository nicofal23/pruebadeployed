# blog/forms.py

from django import forms
from .models import Post, Imagen

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'cuerpo', 'categoria', 'color', 'zona']
        labels = {
            'titulo': 'Nombre de la mascota',
            'subtitulo': 'Nombre del dueño',
            'cuerpo': 'Mensaje descriptivo',
            'categoria': 'Categoría',
            'color': 'Color',
            'zona': 'Zona',
        }

class FiltroForm(forms.Form):
    CATEGORIA_CHOICES = [('----', '----')] + [(choice[0], choice[1]) for choice in Post.CATEGORIA_CHOICES]
    COLOR_CHOICES = [('----', '----')] + [(choice[0], choice[1]) for choice in Post.COLOR_CHOICES]
    ZONA_CHOICES = [('----', '----')] + [(choice[0], choice[1]) for choice in Post.ZONA_CHOICES]

    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES, required=False)
    color = forms.ChoiceField(choices=COLOR_CHOICES, required=False)
    zona = forms.ChoiceField(choices=ZONA_CHOICES, required=False)
