from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Categoria, TestProducto
from .forms import CategoriaForm, TestProductoForm

# Create your views here.
def productos_list(request):
    productos = TestProducto.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda/productos_list.html', context)
    
def modificar_producto(request, pk):
    #with ModelForm TestProductoForm and using pk, and Categorias
    context = {}
    try:
        producto = get_object_or_404(TestProducto, id_producto=pk)
        if request.method == 'POST':
            form = TestProductoForm(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                context['mensaje'] = 'Producto actualizado'
            else:
                context['mensaje'] = 'Formulario no válido'
        else:
            form = TestProductoForm(instance=producto)
        context['form'] = form
        context['producto'] = producto
    except:
        context['mensaje'] = 'Producto no encontrado'
        context['producto'] = None
    return render(request, 'tienda/productos_edit.html', context)

def eliminar_producto(request, pk):
    context = {}
    try:
        producto = get_object_or_404(TestProducto, id_producto=pk)
        producto.delete()
        context['mensaje'] = 'Producto eliminado'
    except:
        context['mensaje'] = 'Producto no encontrado'

    test_productos = TestProducto.objects.all()
    context['productos'] = test_productos
    return render(request, 'tienda/productos_list.html', context)

def add_producto(request):
    if request.method == 'POST':
        form = TestProductoForm(request.POST)
        if form.is_valid():
            form.save()
            form = TestProductoForm()
            context = {'mensaje': 'Producto agregado', 'form': form}
        else:
            context = {'form': form}
    else:
        form = TestProductoForm()
        context = {'form': form}

    return render(request, 'tienda/productos_add.html', context)

def inicio(request):
    context = {}
    return render(request, 'tienda/inicio.html', context)

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