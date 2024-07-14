from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crud/', views.crud, name='crud'),
    path('clientes/add/', views.clientes_add, name='clientes_add'), 
    path('clientes/edit/<int:pk>/', views.clientes_edit, name='clientes_edit'),
    path('clientes/del/<int:pk>/', views.clientes_del, name='clientes_del'), 
    path('nosotros/', views.nosotros, name='nosotros'),
    path('productos/', views.productos, name='productos'),
    path('productos_list/', views.productos_list, name='productos_list'),
    path('productos/add/', views.producto_add, name='producto_add'),
    path('productos/edit/<int:pk>/', views.producto_edit, name='producto_edit'),
    path('productos/del/<int:pk>/', views.producto_del, name='producto_del'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
    path('recarga/', views.recarga, name='recarga'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
