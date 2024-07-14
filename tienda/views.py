from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def productos_comprar(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda/productos_comprar.html', context)

def productos_list(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda/productos_list.html', context)

@login_required    
def modificar_producto(request, pk):
    context = {}
    try:
        producto = get_object_or_404(Producto, id_producto=pk)
        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES, instance=producto)
            if form.is_valid():
                form.save()
                context['mensaje'] = 'Producto actualizado'
            else:
                context['mensaje'] = 'Formulario no válido'
        else:
            form = ProductoForm(instance=producto)
        context['form'] = form
        context['producto'] = producto
    except:
        context['mensaje'] = 'Producto no encontrado'
        context['producto'] = None
    return render(request, 'tienda/productos_edit.html', context)

@login_required
def eliminar_producto(request, pk):
    context = {}
    try:
        producto = get_object_or_404(Producto, id_producto=pk)
        producto.delete()
        context['mensaje'] = 'Producto eliminado'
    except:
        context['mensaje'] = 'Producto no encontrado'

    productos = Producto.objects.all()
    context['productos'] = productos
    return render(request, 'tienda/productos_list.html', context)

@login_required
def add_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductoForm()
            context = {'mensaje': 'Producto agregado', 'form': form}
        else:
            context = {'form': form}
    else:
        form = ProductoForm()
        context = {'form': form}

    return render(request, 'tienda/productos_add.html', context)

# @login_required
def inicio(request):
    if request.user.is_authenticated:
        usuario = request.session.get('usuario', request.user.username)
        productos = Producto.objects.all()
        context = {'productos': productos, 'usuario': usuario}
    else:
        context = {'productos': Producto.objects.all()}
    return render(request, 'tienda/inicio.html', context)

@login_required
def crud_categorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'tienda/categorias_list.html', context)
    
@login_required
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

@login_required
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

@login_required    
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