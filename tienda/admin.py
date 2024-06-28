from django.contrib import admin
from .models import Categoria, Producto, TestProducto   # Importar los modelos

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(TestProducto)