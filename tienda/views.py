from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Producto, Categoria

from .forms import CategoriaForm

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
    
def productos_del(request, pk):
    context = {}
    try:
        producto = Producto.objects.get(id_producto = pk)
        producto.delete()
        mensaje = 'Producto eliminado'
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
        return render(request, 'tienda/productos_list.html', context)
    except:
        mensaje = 'Producto no encontrado'
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
        return render(request, 'tienda/productos_list.html', context)
        
def productos_findEdit(request, pk):
    if pk != "":
        producto = Producto.objects.get(id_producto = pk)
        categorias = Categoria.objects.all()

        context = {'producto': producto, 'categorias': categorias}

        if producto:
            return render(request, 'tienda/productos_edit.html', context)
        else:
            context = {'mensaje': 'Producto no encontrado'}
            return render(request, 'tienda/productos_edit.html', context)
        
def productosUpdate(request):
    if request.method == 'POST':
        id_producto = request.POST['id_producto']
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']
        categoria = request.POST['categoria']

        objCategoria = Categoria.objects.get(id_categoria = categoria)

        producto = Producto()
        producto.id_producto = id_producto
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.stock = stock
        producto.id_categoria = objCategoria
        producto.save()

        categorias = Categoria.objects.all()
        context = {'producto': producto, 'categorias': categorias, 'mensaje': 'Producto actualizado'}
        return render(request, 'tienda/productos_edit.html', context)
    else:
        productos = Producto.objects.all()
        context = {'productos': productos}
        return render(request, 'tienda/productos_edit.html', context)
    
def crud_categorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'tienda/categorias_list.html', context)
    
def categoriasAdd(request):
    context = {}
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoriaForm()
            context = {'mensaje': 'Categoria agregada', 'form': form}
        else:
            context = {'form': form}
        
        return render(request, 'tienda/categorias_add.html', context)
    else:
        form = CategoriaForm()
        context = {'form': form}
        return render(request, 'tienda/categorias_add.html', context)


def categorias_del(request, pk):
    mensajes = []
    errores = []
    categorias = Categoria.objects.all()

    try:
        categoria = Categoria.objects.get(id_categoria = pk)
        context = {}
        if categoria:
            categoria.delete()
            mensajes.append('Categoria eliminada')
            context = {'categorias': categorias, 'mensajes': mensajes, 'errores': errores}
            return render(request, 'tienda/categorias_list.html', context)
    except:
        categorias = Categoria.objects.all()
        mensaje = 'Categoria no encontrada'
        context = {'categorias': categorias, 'mensaje': mensaje}
        return render(request, 'tienda/categorias_list.html', context)
    
def categorias_edit(request, pk):
    try:
        categoria = Categoria.objects.get(id_categoria = pk)
        context = {}
        if categoria:
            if request.method == 'POST':
                form = CategoriaForm(request.POST, instance=categoria)
                form.save()
                mensaje = 'Categoria actualizada'
                context = {'categoria': categoria, 'form': form, 'mensaje': mensaje}
                return render(request, 'tienda/categorias_edit.html', context)
            else:
                form = CategoriaForm(instance=categoria)
                mensaje = ''
                context = {'categoria': categoria, 'form': form, 'mensaje': mensaje}
                return render(request, 'tienda/categorias_edit.html', context)
    except:
        categorias = Categoria.objects.all()
        mensaje = 'Categoria no encontrada'
        context = {'categorias': categorias, 'mensaje': mensaje}
        return render(request, 'tienda/categorias_list.html', context)