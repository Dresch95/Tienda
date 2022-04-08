from . import views
from django.urls import path

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('listarClientes', views.listarClientes,name='listarClientes'),
    path('detallesCliente/<int:id>', views.detallesCliente,name='detallesCliente'),
    path('crearClienteVista', views.crearClienteVista,name='crearClienteVista'),
    path('crearCliente', views.crearCliente,name='crearCliente'),
    path('modificarClienteVista/<int:id>', views.modificarClienteVista,name='modificarClienteVista'),
    path('modificarCliente', views.modificarCliente,name='modificarCliente'),
    path('borrarCliente/<int:id>', views.borrarCliente,name='borrarCliente'),

    path('listarProductos', views.listarProductos,name='listarProductos'),
    path('detallesProducto/<int:id>', views.detallesProducto,name='detallesProducto'),
    path('crearProductoVista', views.crearProductoVista,name='crearProductoVista'),
    path('crearProducto', views.crearProducto,name='crearProducto'),
    path('modificarProductoVista/<int:id>', views.modificarProductoVista,name='modificarProductoVista'),
    path('modificarProducto', views.modificarProducto,name='modificarProducto'),

    path('listarPedidos', views.listarPedidos,name='listarPedidos'),
    path('detallesPedido/<int:id>', views.detallesPedido,name='detallesPedido'),
    path('crearPedidoVista', views.crearPedidoVista,name='crearPedidoVista'),
    path('crearPedido', views.crearPedido,name='crearPedido'),
    path('modificarPedidoVista/<int:id>', views.modificarPedidoVista,name='modificarPedidoVista'),
    path('modificarPedido', views.modificarPedido,name='modificarPedido'),
]