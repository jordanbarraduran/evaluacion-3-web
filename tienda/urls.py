from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),

    path('crud', views.crud, name='crud'),
    path('productosAdd', views.productosAdd, name='productosAdd'),
    path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
    path('productos_findEdit/<str:pk>', views.productos_findEdit, name='productos_findEdit'),
    path('productosUpdate', views.productosUpdate, name='productosUpdate'),

    path('crud_categorias', views.crud_categorias, name='crud_categorias'),
    path('categoriasAdd', views.categoriasAdd, name='categoriasAdd'),
    path('categorias_del/<str:pk>', views.categorias_del, name='categorias_del'),
    path('categorias_Edit/<str:pk>', views.categorias_edit, name='categorias_edit'),
]