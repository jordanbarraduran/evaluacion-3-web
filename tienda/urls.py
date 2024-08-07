from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('', views.inicio, name='inicio'),

    path('crud_categorias', views.crud_categorias, name='crud_categorias'),
    path('categoriasAdd', views.categoriasAdd, name='categoriasAdd'),
    path('categorias_del/<str:pk>', views.categorias_del, name='categorias_del'),
    path('categorias_Edit/<str:pk>', views.categorias_edit, name='categorias_edit'),

    path('productos_list/', views.productos_list, name='productos_list'),
    path('modificar_producto/<int:pk>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar_producto/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('add_producto/', views.add_producto, name='add_producto'),
    path('productos_comprar/', views.productos_comprar, name='productos_comprar'),
    
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)