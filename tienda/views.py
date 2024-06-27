from django.shortcuts import render

from .models import Producto, Categoria

# Create your views here.
def inicio(request):
    context = {}
    return render(request, 'tienda/inicio.html', context)

def crud(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda/productos_list.html', context)