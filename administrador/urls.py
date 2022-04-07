from . import views
from django.urls import path

urlpatterns = [
    path('listarClientes', views.listarClientes,name='listarClientes'),
    path('detallesCliente/<int:id>', views.detallesCliente,name='detallesCliente'),
    path('crearClienteVista', views.crearClienteVista,name='crearClienteVista'),
    path('crearCliente', views.crearCliente,name='crearCliente'),
    path('borrarCliente/<int:id>', views.borrarCliente,name='borrarCliente'),
]