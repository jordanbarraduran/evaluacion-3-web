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
    if request.method != 'POST':
        categorias = Categoria.objects.all()
        context = {'categorias': categorias}
        return render(request, 'tienda/productos_add.html', context)
    else:
        id_producto = request.POST.get('id_producto')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        categoria_id = request.POST.get('categoria')

        objCategoria = Categoria.objects.get(id_categoria = categoria_id)
        obj = Producto(
                    id_producto=id_producto,
                    nombre=nombre,
                    descripcion=descripcion,
                    precio=precio,
                    stock=stock,
                    id_categoria=objCategoria
                )
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
        id_producto = request.POST.get('id_producto')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        categoria_id = request.POST.get('categoria')


        objCategoria = Categoria.objects.get(id_categoria = categoria_id)

        producto = Producto.objects.get(id_producto=id_producto)
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