from django import forms
from .models import Categoria
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ["nom_categoria"]
        labels = {'nom_categoria':'Categoría'}