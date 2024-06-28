from django import forms
from .models import Categoria, TestProducto

from django.forms import ModelForm

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"
        labels = {
            'categoria':'Categoría',
        }

class TestProductoForm(ModelForm):
    class Meta:
        model = TestProducto
        fields = "__all__"
        labels = {
            'categoria':'Categoría',
        }