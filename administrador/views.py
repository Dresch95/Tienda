from http import client
import re
from django.forms import ValidationError
from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Clients,Address, Order_Items, Orders, Products, Products_Details

# Create your views here.
def inicio(request):
    return render(request,'base.html')

#CLIENTES
def listarClientes(request):
    return render(request,'listaClientes.html',{"clientes": Clients.objects.all()})

def detallesCliente(request,id):
    direcciones=[]
    cliente=Clients.objects.get(id=int(id))
    direcciones=Address.objects.filter(client=int(cliente.id))
    return render(request,'detallesCliente.html',{"cliente":cliente,"direcciones":direcciones})

def crearClienteVista(request):
    return render(request,'crearCliente.html')

def crearCliente(request):
    Clients(name=request.POST['nombreClienteNuevo'],email=request.POST['emailClienteNuevo'],tel=request.POST['telefonoClienteNuevo']).save()
    Address(client=Clients.objects.filter(name=request.POST['nombreClienteNuevo'],email=request.POST['emailClienteNuevo'],tel=request.POST['telefonoClienteNuevo'])[0],street=request.POST['calleDireccionNueva'],city=request.POST['ciudadDireccionNueva'],code=request.POST['codigoDireccionNueva'],country=request.POST['paisDireccionNueva']).save()
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

def cambiarEstadoCliente(request):
    id=request.POST['idCliente']
    cliente=Clients.objects.filter(pk=int(id))
    cliente.update(unable=not cliente[0].unable)
    data = {
       'estado_cambiado': cliente[0].unable
    }
    return JsonResponse(data)

#DIRECCIONES
def crearDireccionVista(request,id):
    return render(request,'crearDireccion.html',{"idCliente":id})

def crearDireccion(request):
    id=request.POST['cliente']
    Address(client=Clients.objects.get(pk=int(id)),street=request.POST['calleDireccionNueva'],city=request.POST['ciudadDireccionNueva'],code=request.POST['codigoDireccionNueva'],country=request.POST['paisDireccionNueva']).save()
    return HttpResponseRedirect(f'/detallesCliente/{id}')

def modificarDireccionVista(request,id):
    direccion=Address.objects.get(pk=int(id))
    cliente=Clients.objects.get(pk=int(direccion.client.id))
    return render(request,'modificarDireccion.html',{"direccion":direccion,"cliente":cliente})

def modificarDireccion(request):
    idDireccion=request.POST['direccion']
    Address.objects.filter(pk=int(idDireccion)).update(street=request.POST['calleDireccionModificar'],city=request.POST['ciudadDireccionModificar'],code=request.POST['codigoDireccionModificar'],country=request.POST['paisDireccionModificar'])
    return HttpResponseRedirect(f'/detallesCliente/{Address.objects.get(pk=int(idDireccion)).client.id}')

def borrarDireccion(request,id):
    direccion=Address.objects.get(pk=id)
    cliente=direccion.client.id
    direccion.delete()
    return HttpResponseRedirect(f'/detallesCliente/{cliente}')


#PRODUCTOS
def listarProductos(request):
    return render(request,'listaProductos.html',{"productos":Products.objects.all()})

def detallesProducto(request,id):
    producto=Products.objects.get(id=int(id))
    detallesProducto=Products_Details.objects.filter(product=int(id))
    return render(request,'detallesProducto.html',{"producto":producto,"detalles":detallesProducto})

def crearProductoVista(request):
    return render(request,'crearProducto.html')

def crearProducto(request):
    Products(name=request.POST['nombreProductoNuevo'],imageURL=request.POST['urlImagenProductoNuevo']).save()
    producto=Products.objects.get(name=request.POST['nombreProductoNuevo'])
    pesos=[request.POST['pesoProductoNuevoEstandar'],request.POST['pesoProductoNuevoPequenho'],request.POST['pesoProductoNuevoGrande']]
    if pesos[0]=='':
        Products_Details(product=producto,size='AV',price=request.POST['precioProductoNuevoEstandar'],weight=None).save()
    else:
        Products_Details(product=producto,size='AV',price=request.POST['precioProductoNuevoEstandar'],weight=request.POST['pesoProductoNuevoEstandar']).save()
    try:
        if pesos[1]=='':
            Products_Details(product=producto,size='SM',price=request.POST['precioProductoNuevoPequenho'],weight=None).save()
        else:
            Products_Details(product=producto,size='SM',price=request.POST['precioProductoNuevoPequenho'],weight=float(request.POST['pesoProductoNuevoPequenho'])).save()
    except:
        Products_Details(product=producto,size='SM',price=0,weight=None,unable=True).save()
    try:
        if pesos[2]=='':
            Products_Details(product=producto,size='BG',price=request.POST['precioProductoNuevoGrande'],weight=None).save()
        else:
            Products_Details(product=producto,size='BG',price=request.POST['precioProductoNuevoGrande'],weight=float(request.POST['pesoProductoNuevoGrande'])).save()
    except:
        Products_Details(product=producto,size='BG',price=0,weight=None,unable=True).save()
    return HttpResponseRedirect('/listarProductos')

def modificarProductoVista(request,id):
    producto=Products.objects.get(pk=int(id))
    detallesEstandar=Products_Details.objects.get(product=producto.id,size='AV')
    detallesPequenho=''
    detallesGrande=''
    try:
        detallesPequenho=Products_Details.objects.get(product=producto.id,size='SM')
    except:
        pass
    try:
        detallesGrande=Products_Details.objects.get(product=producto.id,size='BG')
    except:
        pass
    return render(request,'modificarProducto.html',{"producto":producto,"estandar":detallesEstandar,"pequenho":detallesPequenho,"grande":detallesGrande})

def modificarProducto(request):
    id=request.POST['productoID']
    producto=Products.objects.filter(id=int(id))
    producto.update(imageURL=request.POST['urlImagenProductoModificar'])
    pesos=[request.POST['pesoProductoModificarEstandar'],request.POST['pesoProductoModificarPequenho'],request.POST['pesoProductoModificarGrande']]
    if pesos[0]=='':
        Products_Details.objects.filter(product=producto[0],size='AV').update(price=request.POST['precioProductoModificarEstandar'],weight=None)
    else:
        Products_Details.objects.filter(product=producto[0],size='AV').update(price=request.POST['precioProductoModificarEstandar'],weight=request.POST['pesoProductoModificarEstandar'])
    try:
        if pesos[1]=='':
            Products_Details.objects.filter(product=producto[0].id,size='SM').update(price=request.POST['precioProductoModificarPequenho'],weight=None)
        else:
            Products_Details.objects.filter(product=producto[0].id,size='SM').update(price=request.POST['precioProductoModificarPequenho'],weight=float(request.POST['pesoProductoModificarPequenho']))
    except:
        pass
    try:
        if pesos[2]=='':
            Products_Details.objects.filter(product=producto,size='BG').update(price=request.POST['precioProductoModificarGrande'],weight=None)
        else:
            Products_Details.objects.filter(product=producto,size='BG').update(price=request.POST['precioProductoModificarGrande'],weight=float(request.POST['pesoProductoModificarGrande']))
    except:
        pass



    return HttpResponseRedirect(f'/detallesProducto/{id}')

def borrarProducto(request,id):
    pass

def comprobarProducto(request):
    producto = request.GET['producto']
    data = {
       'producto_existe':Products.objects.filter(name=producto).exists()
    }
    return JsonResponse(data)

#PEDIDOS
def listarPedidos(request):
    return render(request,'listaPedidos.html',{"pedidos":Orders.objects.all()})

def detallesPedido(request,id):
    pedido=Orders.objects.get(id=int(id))
    return render(request,'detallesPedido.html',{"pedido":pedido})

def crearPedidoVista(request):
    listaClientes=[]
    for item in Clients.objects.filter(unable=False):
        if len(Address.objects.filter(client=item.id))!=0:
            listaClientes.append(item)
    return render(request,'crearPedido.html',{"clientes": listaClientes,"productos":Products_Details.objects.filter(unable=False)})

def crearPedido(request):
    listaProductos=[]
    listaCantidades=[]
    if request.POST.getlist('producto'):
        for item in request.POST.getlist('producto'):
            listaProductos.append(Products_Details.objects.filter(pk=int(item)))
        for item in request.POST.getlist('producto'):
            listaCantidades.append(int(item))
    Orders(client=request.POST['selectClientes'])
    for index in range(len(listaProductos)):
        Order_Items
    return HttpResponseRedirect('/listarClientes')

def modificarPedidoVista(request,id):
    producto=Products.objects.get(pk=int(id))
    return render(request,'modificarProducto.html',{"producto":producto})

def modificarPedido(request):
    id=request.POST['productoID']
    Products.objects.filter(pk=int(id)).update(name=request.POST['nombreProductoModificar'],size=request.POST['tiposTamanhoModificar'],weight=request.POST['pesoProductoModificar'],imageURL=request.POST['urlImagenProductoModificar'],price=request.POST['precioProductoModificar'])
    return HttpResponseRedirect(f'/detallesProducto/{id}')

def borrarPedido(request,id):
    pass

def direccionesCliente(request):
    idCliente = request.GET['idCliente']
    listaDirecciones=[]
    for item in Address.objects.filter(client=int(idCliente)):
        listaDirecciones.append([item.id,item.street])
    data = {
       'listaDirecciones':listaDirecciones
    }
    return JsonResponse(data)