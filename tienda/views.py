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

def productosAdd(request):
    if request.method is not 'POST':
        categorias = Categoria.objects.all()
        context = {'categorias': categorias}
        return render(request, 'tienda/productos_add.html', context)
    else:
        id = request.POST['id_producto']
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']
        categoria = request.POST['categoria']

        objCategoria = Categoria.objects.get(id_categoria = id)
        obj = Producto.objects.create(  id_producto = id, 
                                        nombre = nombre, 
                                        descripcion = descripcion, 
                                        precio = precio,
                                        stock = stock, 
                                        categoria = objCategoria)
        obj.save()
        context = {'mensaje': 'Producto agregado'}
        return render(request, 'tienda/productos_add.html', context)