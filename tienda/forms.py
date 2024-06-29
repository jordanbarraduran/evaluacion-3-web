from django import forms
from .models import Categoria, Producto

from django.forms import ModelForm

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"
        labels = {
            'categoria':'Categoría',
        }

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        labels = {
            'categoria':'Categoría',
        }