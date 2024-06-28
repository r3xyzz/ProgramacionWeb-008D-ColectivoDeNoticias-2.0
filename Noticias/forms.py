from .models import Categoria
from django.forms import ModelForm
from django import forms
from .models import Noticia

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ["nom_categoria"]
        labels = {'nom_categoria':'Categoría'}

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
