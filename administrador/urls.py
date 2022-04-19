from . import views
from django.urls import path

urlpatterns = [
    path('', views.listarClientes,name='listarClientes'),
    #CLIENTES
    path('listarClientes', views.listarClientes,name='listarClientes'),
    path('detallesCliente/<int:idCliente>', views.detallesCliente,name='detallesCliente'),
    path('crearClienteVista', views.crearClienteVista,name='crearClienteVista'),
    path('crearCliente', views.crearCliente,name='crearCliente'),
    path('modificarClienteVista/<int:idCliente>', views.modificarClienteVista,name='modificarClienteVista'),
    path('modificarCliente', views.modificarCliente,name='modificarCliente'),
    path('comprobarEmail', views.comprobarEmail,name='comprobarEmail'),
    path('comprobarEmailModificar', views.comprobarEmailModificar,name='comprobarEmailModificar'),
    path('cambiarEstadoCliente', views.cambiarEstadoCliente,name='cambiarEstadoCliente'),
    path('comprobarCliente', views.comprobarCliente,name='comprobarCliente'),
    #DIRECCIONES
    path('crearDireccionVista/<int:idCliente>', views.crearDireccionVista,name='crearDireccionVista'),
    path('crearDireccion', views.crearDireccion,name='crearDireccion'),
    path('modificarDireccionVista/<int:idDireccion>', views.modificarDireccionVista,name='modificarDireccionVista'),
    path('modificarDireccion', views.modificarDireccion,name='modificarDireccion'),
    path('comprobarDireccion', views.comprobarDireccion,name='comprobarDireccion'),
    path('cambiarEstadoDeLaDireccion', views.cambiarEstadoDeLaDireccion,name='cambiarEstadoDeLaDireccion'),
    #PRODUCTOS
    path('listarProductos', views.listarProductos,name='listarProductos'),
    path('detallesProducto/<int:idProducto>', views.detallesProducto,name='detallesProducto'),
    path('crearProductoVista', views.crearProductoVista,name='crearProductoVista'),
    path('crearProducto', views.crearProducto,name='crearProducto'),
    path('modificarProductoVista/<int:idProducto>', views.modificarProductoVista,name='modificarProductoVista'),
    path('modificarProducto', views.modificarProducto,name='modificarProducto'),
    path('cambiarEstadoDelProducto', views.cambiarEstadoDelProducto,name='cambiarEstadoDelProducto'),
    path('cambiarEstadoArticuloProducto', views.cambiarEstadoArticuloProducto,name='cambiarEstadoArticuloProducto'),
    path('borrarProducto', views.borrarProducto,name='borrarProducto'),
    path('comprobarProducto', views.comprobarProducto,name='comprobarProducto'),
    path('comprobarProductoModificar', views.comprobarProductoModificar,name='comprobarProductoModificar'),
    
    #PEDIDOS
    path('listarPedidos', views.listarPedidos,name='listarPedidos'),
    path('detallesPedido/<int:idPedido>', views.detallesPedido,name='detallesPedido'),
    path('crearPedidoVista', views.crearPedidoVista,name='crearPedidoVista'),
    path('crearPedido', views.crearPedido,name='crearPedido'),
    path('eliminarPedido', views.eliminarPedido,name='eliminarPedido'),
    path('direccionesCliente', views.direccionesCliente,name='direccionesCliente'),
]