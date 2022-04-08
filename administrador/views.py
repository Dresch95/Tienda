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
    cliente=Clients.objects.get(id=int(id))
    direccion=Address.objects.get(id=int(cliente.address_id))
    return render(request,'detallesCliente.html',{"cliente":cliente,"direccion":direccion})

def crearClienteVista(request):
    return render(request,'crearCliente.html')

def crearCliente(request):
    direccion=[]
    try:
        direccion.append(request.POST['calleDireccionNueva'])
        direccion.append(request.POST['ciudadDireccionNueva'])
        direccion.append(request.POST['codigoDireccionNueva'])
        direccion.append(request.POST['paisDireccionNueva'])
        direccion.append(request.POST['tiposDireccion'])
        Address(street=direccion[0],city=direccion[1],code=direccion[2],country=direccion[3],type=direccion[4]).save()
        Clients(name=request.POST['nombreClienteNuevo'],email=request.POST['emailClienteNuevo'],tel=request.POST['telefonoClienteNuevo'],imageURL=request.POST['urlImagenClienteNuevo'],address_id=Address.objects.filter(street=direccion[0],city=direccion[1],code=direccion[2],country=direccion[3],type=direccion[4])[0].id).save()
    except ValidationError as e:
        ValidationError(('Invalid value'), code='Hola')
    return HttpResponseRedirect('/listarClientes')

def modificarClienteVista(request,id):
    cliente=Clients.objects.get(pk=int(id))
    return render(request,'modificarCliente.html',{"cliente":cliente})

def modificarCliente(request):
    id=request.POST['clienteID']
    Clients.objects.filter(pk=int(id)).update(name=request.POST['nombreClienteModificar'],email=request.POST['emailClienteModificar'],tel=request.POST['telefonoClienteModificar'],imageURL=request.POST['urlImagenClienteModificar'])
    return HttpResponseRedirect(f'/detallesCliente/{id}')

def borrarCliente(request,id):
    Clients.objects.get(pk=id).delete()
    return HttpResponseRedirect('/listarClientes')

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