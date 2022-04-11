from http import client
import re
from django.forms import ValidationError
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .models import Clients,Address, Orders, Products

# Create your views here.
def inicio(request):
    return render(request,'base.html')

#CLIENTES
def listarClientes(request):
    clientes=[]
    for item in Clients.objects.all():
        clientes.append(item)
    return render(request,'listaClientes.html',{"clientes":clientes})

def detallesCliente(request,id):
    direcciones=[]
    cliente=Clients.objects.get(id=int(id))
    direcciones=Address.objects.filter(client=int(cliente.id))
    return render(request,'detallesCliente.html',{"cliente":cliente,"direcciones":direcciones})

def crearClienteVista(request):
    return render(request,'crearCliente.html')

def crearCliente(request):
    Clients(name=request.POST['nombreClienteNuevo'],email=request.POST['emailClienteNuevo'],tel=request.POST['telefonoClienteNuevo']).save()
    Address(client=Clients.objects.filter(name=request.POST['nombreClienteNuevo'],email=request.POST['emailClienteNuevo'],tel=request.POST['telefonoClienteNuevo'])[0],street=request.POST['calleDireccionNueva'],city=request.POST['ciudadDireccionNueva'],code=request.POST['codigoDireccionNueva'],country=request.POST['paisDireccionNueva'],type='FL').save()
    return HttpResponseRedirect('/listarClientes')

def modificarClienteVista(request,id):
    cliente=Clients.objects.get(pk=int(id))
    return render(request,'modificarCliente.html',{"cliente":cliente})

def modificarCliente(request):
    id=request.POST['clienteID']
    Clients.objects.filter(pk=int(id)).update(name=request.POST['nombreClienteModificar'],email=request.POST['emailClienteModificar'],tel=request.POST['telefonoClienteModificar'])
    return HttpResponseRedirect(f'/detallesCliente/{id}')

def borrarCliente(request,id):
    Clients.objects.get(pk=id).delete()
    return HttpResponseRedirect('/listarClientes')

#DIRECCIONES
def crearDireccionVista(request,id):
    return render(request,'crearDireccion.html',{"idCliente":id})

def crearDireccion(request):
    id=request.POST['cliente']
    Address(client=Clients.objects.get(pk=int(id)),street=request.POST['calleDireccionNueva'],city=request.POST['ciudadDireccionNueva'],code=request.POST['codigoDireccionNueva'],country=request.POST['paisDireccionNueva'],type=request.POST['tipoDireccion']).save()
    return HttpResponseRedirect(f'/detallesCliente/{id}')

def modificarDireccionVista(request,idDireccion,idCliente):
    direccion=Address.objects.get(pk=int(idDireccion))
    return render(request,'modificarDireccion.html',{"direccion":direccion,"idCliente":idCliente})

def modificarDireccion(request,id):
    Address.objects.filter(pk=int(request.POST['direccion'])).update(street=request.POST['calleDireccionModificar'],city=request.POST['ciudadDireccionModificar'],code=request.POST['codigoDireccionModificar'],country=request.POST['paisDireccionModificar'],type=request.POST['tipoDireccion'])
    return HttpResponseRedirect(f'/detallesCliente/{id}')

def borrarDireccion(request,id):
    direccion=Address.objects.get(pk=id)
    cliente=direccion.client.id
    direccion.delete()
    return HttpResponseRedirect(f'/detallesCliente/{cliente}')


#PRODUCTOS
def listarProductos(request):
    productos=[]
    for item in Products.objects.all():
        productos.append(item)
    return render(request,'listaProductos.html',{"productos":productos})

def detallesProducto(request,id):
    producto=Products.objects.get(id=int(id))
    return render(request,'detallesProducto.html',{"producto":producto})

def crearProductoVista(request):
    return render(request,'crearProducto.html')

def crearProducto(request):
    try:
        Products(name=request.POST['nombreProductoNuevo'],size=request.POST['tiposTamanho'],weight=request.POST['pesoProductoNuevo'],price=request.POST['precioProductoNuevo'],imageURL=request.POST['urlImagenProductoNuevo']).save()
    except ValidationError as e:
        ValidationError(('Invalid value'), code='Hola')
    return HttpResponseRedirect('/listarClientes')

def modificarProductoVista(request,id):
    producto=Products.objects.get(pk=int(id))
    return render(request,'modificarProducto.html',{"producto":producto})

def modificarProducto(request):
    id=request.POST['productoID']
    Products.objects.filter(pk=int(id)).update(name=request.POST['nombreProductoModificar'],size=request.POST['tiposTamanhoModificar'],weight=request.POST['pesoProductoModificar'],imageURL=request.POST['urlImagenProductoModificar'],price=request.POST['precioProductoModificar'])
    return HttpResponseRedirect(f'/detallesProducto/{id}')

#PEDIDOS
def listarPedidos(request):
    pedidos=[]
    for item in Orders.objects.all():
        pedidos.append(item)
    return render(request,'listaPedidos.html',{"pedidos":pedidos})

def detallesPedido(request,id):
    pedido=Orders.objects.get(id=int(id))
    return render(request,'detallesPedido.html',{"pedido":pedido})

def crearPedidoVista(request):
    productos=[]
    clientes=[]
    try:
        for item in Products.objects.filter(unable=False):
            productos.append(item)
        for item in Clients.objects.filter(unable=False):
            clientes.append(item)
    except:
        pass
    return render(request,'crearPedido.html',{"clientes":clientes,"productos":productos})

def crearPedido(request):
    try:
        Products(name=request.POST['nombreProductoNuevo'],size=request.POST['tiposTamanho'],weight=request.POST['pesoProductoNuevo'],price=request.POST['precioProductoNuevo'],imageURL=request.POST['urlImagenProductoNuevo']).save()
    except ValidationError as e:
        ValidationError(('Invalid value'), code='Hola')
    return HttpResponseRedirect('/listarClientes')

def modificarPedidoVista(request,id):
    producto=Products.objects.get(pk=int(id))
    return render(request,'modificarProducto.html',{"producto":producto})

def modificarPedido(request):
    id=request.POST['productoID']
    Products.objects.filter(pk=int(id)).update(name=request.POST['nombreProductoModificar'],size=request.POST['tiposTamanhoModificar'],weight=request.POST['pesoProductoModificar'],imageURL=request.POST['urlImagenProductoModificar'],price=request.POST['precioProductoModificar'])
    return HttpResponseRedirect(f'/detallesProducto/{id}')