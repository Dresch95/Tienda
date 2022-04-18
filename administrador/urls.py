from . import views
from django.urls import path

urlpatterns = [
    path('', views.listarClientes,name='listarClientes'),
    #CLIENTES
    path('listarClientes', views.listarClientes,name='listarClientes'),
    path('detallesCliente/<int:id>', views.detallesCliente,name='detallesCliente'),
    path('crearClienteVista', views.crearClienteVista,name='crearClienteVista'),
    path('crearCliente', views.crearCliente,name='crearCliente'),
    path('modificarClienteVista/<int:id>', views.modificarClienteVista,name='modificarClienteVista'),
    path('modificarCliente', views.modificarCliente,name='modificarCliente'),
    path('comprobarEmail', views.comprobarEmail,name='comprobarEmail'),
    path('comprobarEmailModificar', views.comprobarEmailModificar,name='comprobarEmailModificar'),
    path('cambiarEstadoCliente', views.cambiarEstadoCliente,name='cambiarEstadoCliente'),
    path('comprobarCliente', views.comprobarCliente,name='comprobarCliente'),
    #DIRECCIONES
    path('crearDireccionVista/<int:id>', views.crearDireccionVista,name='crearDireccionVista'),
    path('crearDireccion', views.crearDireccion,name='crearDireccion'),
    path('modificarDireccionVista/<int:id>', views.modificarDireccionVista,name='modificarDireccionVista'),
    path('modificarDireccion', views.modificarDireccion,name='modificarDireccion'),
    path('comprobarDireccion', views.comprobarDireccion,name='comprobarDireccion'),
    path('cambiarEstadoDeLaDireccion', views.cambiarEstadoDeLaDireccion,name='cambiarEstadoDeLaDireccion'),
    #PRODUCTOS
    path('listarProductos', views.listarProductos,name='listarProductos'),
    path('detallesProducto/<int:id>', views.detallesProducto,name='detallesProducto'),
    path('crearProductoVista', views.crearProductoVista,name='crearProductoVista'),
    path('crearProducto', views.crearProducto,name='crearProducto'),
    path('modificarProductoVista/<int:id>', views.modificarProductoVista,name='modificarProductoVista'),
    path('modificarProducto', views.modificarProducto,name='modificarProducto'),
    path('cambiarEstadoDelProducto', views.cambiarEstadoDelProducto,name='cambiarEstadoDelProducto'),
    path('borrarProducto', views.borrarProducto,name='borrarProducto'),
    path('comprobarProducto', views.comprobarProducto,name='comprobarProducto'),
    path('comprobarProductoModificar', views.comprobarProductoModificar,name='comprobarProductoModificar'),
    path('cambiarEstadoProducto', views.cambiarEstadoProducto,name='cambiarEstadoProducto'),
    #DETALLES_PRODUCTOS

    #PEDIDOS
    path('listarPedidos', views.listarPedidos,name='listarPedidos'),
    path('detallesPedido/<int:id>', views.detallesPedido,name='detallesPedido'),
    path('crearPedidoVista', views.crearPedidoVista,name='crearPedidoVista'),
    path('crearPedido', views.crearPedido,name='crearPedido'),
    path('eliminarPedido', views.eliminarPedido,name='eliminarPedido'),
    path('direccionesCliente', views.direccionesCliente,name='direccionesCliente'),
]