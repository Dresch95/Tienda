from datetime import datetime,timedelta
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Clients,Address, Order_Items, Orders, Products, Products_Details
from django.db.models import Q

#CLIENTES
def listarClientes(request):
    '''Devuelve una lista con todos los clientes y 
       llama al html que los muestra'''
    return render(request,'listaClientes.html',{"clientes": Clients.objects.all()})

def detallesCliente(request,id):
    '''Recibe el id del cliente del cual se quieren consultar sus datos.
       Devuelve el objeto cliente del cual le pasan el id, 
       una lista con todas las direcciones del cliente y 
       llama al html que lo muetra'''
    cliente=Clients.objects.get(id=int(id))
    return render(request,'detallesCliente.html',{"cliente":cliente,"direcciones":Address.objects.filter(client=int(cliente.id))})

def crearClienteVista(request):
    '''Llama al html que muestra el formulario para crear un cliente'''
    return render(request,'crearCliente.html')

def crearCliente(request):
    '''Recibe los datos del cliente que se va a crear.
       Crea el cliente con los datos del formulario, 
       despues crea la direccion obligatoria que tiene que tener el cliente de primeras y 
       llama a la funcion que muestra la lista de clientes'''
    cliente=Clients(name=request.POST['nombreClienteNuevo'],email=request.POST['emailClienteNuevo'],tel=request.POST['telefonoClienteNuevo'],unable=False)
    cliente.save()
    Address(client=cliente,street=request.POST['calleDireccionNueva'],city=request.POST['ciudadDireccionNueva'],code=request.POST['codigoDireccionNueva'],country=request.POST['paisDireccionNueva'],unable=False).save()
    return HttpResponseRedirect('/listarClientes')

def modificarClienteVista(request,id):
    '''Recibe el id del cliente el cual se quieren modificar sus datos.
       Llama al html que muestra el formario para modificar el cliente e
       introduce los datos actuales de dicho cliente'''
    return render(request,'modificarCliente.html',{"cliente":Clients.objects.get(pk=int(id))})

def modificarCliente(request):
    '''Recibe los datos del cliente que se va a modificar.
       Modifica el cliente con los datos del formulario y
       llama a la funcion que muestra los detalles del cliente'''
    id=request.POST['clienteID']
    Clients.objects.filter(pk=int(id)).update(name=request.POST['nombreClienteModificar'],email=request.POST['emailClienteModificar'],tel=request.POST['telefonoClienteModificar'])
    return HttpResponseRedirect(f'/detallesCliente/{id}')

def comprobarEmail(request):
    '''Recibe un string con el email a crear.
       Devuelve un booleano, 
       True si el email que se quiere introducir en el nuevo cliente ya existe y 
       False si no existe'''
    return JsonResponse({'email_existe':Clients.objects.filter(email=request.GET['email']).exists()})

def comprobarEmailModificar(request):
    '''Recibe un string con el email modificado.
       Devuelve un booleano,
       True si el email ya existe, se tiene en cuenta que el propio cliente ya lo esta usando, y
       False si el email o no se esta usando o ya lo esta usando el cliente a modificar'''
    return JsonResponse({'email_existe':Clients.objects.filter(email=request.GET['email']).exclude(id=int(request.GET['idCliente'])).exists()})

def cambiarEstadoCliente(request):
    '''Recibe el id del cliente que se quiere modificar su estado.
       Cambia el estado del cliente y 
       devuelve un booleano que indica el estado del cliente,
       True si esta deshabilitado y
       False si esta habilitado'''
    cliente=Clients.objects.filter(pk=int(request.POST['idCliente']))
    cliente.update(unable=not cliente[0].unable)
    data = {
       'estado_cambiado': cliente[0].unable
    }
    return JsonResponse(data)

def comprobarCliente(request):
    '''Recibe el id del cliente que se quiere eliminar.
       Comprueba si el cliente tiene pedidos realizados,
       si tiene pedidos devuelve True,
       si no tiene pedidos existentes lo borra y devuelve False'''
    idCliente = int(request.POST['idCliente'])
    if Orders.objects.filter(client=idCliente).exists():
        data = {
            'tiene_pedido': True
        }
    else:
        Clients.objects.get(pk=idCliente).delete()
        data = {
            'tiene_pedido': False
        }
    return JsonResponse(data)

#DIRECCIONES
def crearDireccionVista(request,id):
    '''Recibe el id del cliente de la direccion que se quiere crear.
       Llama al html que muestra el formulario para crear una direccion'''
    return render(request,'crearDireccion.html',{"idCliente":id})

def crearDireccion(request):
    '''Recibe los datos de la direccion que se va a crear.
       Crea una direccion con los datos del formulario y
       llama a la funcion que muestra los detalles del cliente al que pertenece la direccion creada'''
    id=request.POST['cliente']
    Address(client=Clients.objects.get(pk=int(id)),street=request.POST['calleDireccionNueva'],city=request.POST['ciudadDireccionNueva'],code=request.POST['codigoDireccionNueva'],country=request.POST['paisDireccionNueva'],unable=False).save()
    return HttpResponseRedirect(f'/detallesCliente/{id}')

def modificarDireccionVista(request,id):
    '''Recibe el id de la direccion a modificar.
       Llama al html que muestra el formulario para modificar una direccion e
       introduce los datos actuales de dicha direccion'''
    return render(request,'modificarDireccion.html',{"direccion":Address.objects.get(pk=int(id))})

def modificarDireccion(request):
    '''Recibe los datos de la direccion a modificar.
       Modifica la direccion con los datos del formulario y
       llama a la funcion que muestra los datos del cliente a la que pertenece esa direccion'''
    direccion=Address.objects.filter(pk=int(request.POST['direccion']))
    direccion.update(street=request.POST['calleDireccionModificar'],city=request.POST['ciudadDireccionModificar'],code=request.POST['codigoDireccionModificar'],country=request.POST['paisDireccionModificar'])
    return HttpResponseRedirect(f'/detallesCliente/{direccion.client.id}')

def cambiarEstadoDeLaDireccion(request):
    '''Recibe el id de la direccion de la cual se quiere cambiar el estado.
       Cambia el estado de la direccion y 
       devuelve un booleano que indica el estado de la direccion,
       True si esta deshabilitada y
       False si esta habilitada'''
    direccion=Address.objects.filter(pk=int(request.POST['idDireccion']))
    direccion.update(unable=not direccion[0].unable)
    data = {
       'estado_cambiado': direccion[0].unable
    }
    return JsonResponse(data)

def comprobarDireccion(request):
    '''Recibe el id de la direccion que se quiere eliminar.
       Comprueba si la direccion se ha usado en algun pedido existente,
       si se ha usado se devuelve True,
       si no hay pedidos existentes con dicha direccion se borra y se devuelve False'''
    direccion=Address.objects.get(pk=request.POST['idDireccion'])
    if Orders.objects.filter(Q(billing_address=direccion.id) | Q(shipping_address=direccion.id)):
        data={"tiene_pedido":True}
    else:
        data={"tiene_pedido":False}
        direccion.delete()
    return JsonResponse(data)

#PRODUCTOS
def listarProductos(request):
    '''Devuelve una lista con los productos existentes y
       llama al html que los muestra'''
    return render(request,'listaProductos.html',{"productos":Products.objects.all()})

def detallesProducto(request,id):
    '''Recibe el id del producto del cual se quieren ver los detalles.
       Devuelve el objeto producto del cual le pasan el id y
       todos los articulos de producto(Product_Details) que se basan en el,
       despues llama al html que muestra toda la informacion'''
    return render(request,'detallesProducto.html',{"producto":Products.objects.get(id=int(id)),"detalles":Products_Details.objects.filter(product=int(id))})

def crearProductoVista(request):
    '''Llama al html que muestra el formulario para crear un producto'''
    return render(request,'crearProducto.html')

def crearProducto(request):
    '''Recibe los datos del producto a crear.
       Crea un producto y los articulos de producto(Product_Details) que se indiquen en el formulario,
       solo el producto y el precio del articulo de tamaño estandar son obligatorios,
       despues se llama a la funcion que muestra los datos del producto y sus articulos'''
    producto=Products(name=request.POST['nombreProductoNuevo'],imageURL=request.POST['urlImagenProductoNuevo'],unable=False)
    producto.save()
    Products_Details(product=producto,size='AV',price=request.POST['precioProductoNuevoEstandar'],weight=request.POST['pesoProductoNuevoEstandar'] if request.POST['pesoProductoNuevoEstandar']!='' and float(request.POST['pesoProductoEstandar'])>0 else None,unable=False).save()
    if request.POST['precioProductoNuevoPequenho']!='':
        Products_Details(product=producto,size='SM',price=request.POST['precioProductoNuevoPequenho'],weight=request.POST['pesoProductoNuevoPequenho'] if request.POST['pesoProductoNuevoPequenho']!='' and float(request.POST['pesoProductoNuevoPequenho'])>0 else None,unable=False).save()
    if request.POST['precioProductoNuevoGrande']!='':
        Products_Details(product=producto,size='BG',price=request.POST['precioProductoNuevoGrande'],weight=request.POST['pesoProductoNuevoGrande'] if request.POST['pesoProductoNuevoGrande']!='' and float(request.POST['pesoProductoNuevoGrande'])>0 else None,unable=False).save()
    return HttpResponseRedirect('/listarProductos')

def modificarProductoVista(request,id):
    '''Recibe el id del producto a modificar.
       Llama al html que muestra el formulario para modificar el producto y sus articulos(Product_Details) e
       introduce los datos que ya existan'''
    producto=Products.objects.get(pk=int(id))
    return render(request,'modificarProducto.html',{"producto":producto,"estandar":Products_Details.objects.get(product=producto.id,size='AV'),"pequenho":Products_Details.objects.get(product=producto.id,size='SM') if Products_Details.objects.filter(product=producto.id,size='SM').exists() else '',"grande":Products_Details.objects.get(product=producto.id,size='BG') if Products_Details.objects.filter(product=producto,size='BG').exists() else ''})

def modificarProducto(request):
    '''Recibe los datos del producto y los datos de los articulos de producto(Product_Details) a modificar .
       Modifica el producto y sus articulos(Product_Details) con los datos del formulario,
       comprobando que datos se han modificado y crea los tamaños de articulo si hay que crearlos,
       despues llama a la funcion que muestra los detalles del producto y sus articulos'''
    id=request.POST['productoID']
    producto=Products.objects.filter(id=int(id))
    producto.update(name=request.POST['nombreProductoModificar'],imageURL=request.POST['urlImagenProductoModificar'])
    productoEstandar=Products_Details.objects.filter(product=producto[0].id,size='AV')
    productoPequenho=Products_Details.objects.filter(product=producto[0].id,size='SM')
    productoGrande=Products_Details.objects.filter(product=producto[0].id,size='BG')
    if productoEstandar.exists:
        productoEstandar.update(price=request.POST['precioProductoModificarEstandar'],weight=request.POST['pesoProductoModificarEstandar'] if request.POST['pesoProductoModificarEstandar']!='' and float(request.POST['pesoProductoModificarEstandar'])>0 else None,unable=False)
    if float(request.POST['precioProductoModificarPequenho'] if request.POST['precioProductoModificarPequenho']!='' else 0)>0:
        if productoPequenho.exists():
            productoPequenho.update(price=request.POST['precioProductoModificarPequenho'],weight=request.POST['pesoProductoModificarPequenho'] if request.POST['pesoProductoModificarPequenho']!='' and float(request.POST['pesoProductoModificarPequenho'])>0 else None,unable=False)
        else:
            Products_Details(product=producto[0],size='SM',price=request.POST['precioProductoModificarPequenho'],weight=request.POST['pesoProductoModificarPequenho'] if request.POST['pesoProductoModificarPequenho']!='' and float(request.POST['pesoProductoModificarPequenho'])>0 else None,unable=False).save()
    if float(request.POST['precioProductoModificarGrande'] if request.POST['precioProductoModificarGrande']!='' else 0)>0:
        if productoGrande.exists():
            productoGrande.update(price=request.POST['precioProductoModificarGrande'],weight=request.POST['pesoProductoModificarGrande'] if request.POST['pesoProductoModificarGrande']!='' and float(request.POST['pesoProductoModificarGrande'])>0 else None,unable=False)
        else:
            Products_Details(product=producto[0],size='BG',price=request.POST['precioProductoModificarGrande'],weight=request.POST['pesoProductoModificarGrande'] if request.POST['pesoProductoModificarGrande']!='' and float(request.POST['pesoProductoModificarGrande'])>0 else None,unable=False).save()
    return HttpResponseRedirect(f'/detallesProducto/{id}')

def cambiarEstadoDelProducto(request):
    '''Recibe el id del producto al cual se le quiere cambiar el estado.
       Se cambia el estado del producto y devuelve un booleano,
       True si el producto esta deshabilitado,
       False si el articulo esta habilitado'''
    producto=Products.objects.filter(pk=int(request.POST['idProducto']))
    producto.update(unable=not producto[0].unable)
    data = {
       'estado_cambiado': producto[0].unable
    }
    return JsonResponse(data)

def comprobarProducto(request):
    '''Recibe un string con el nombre a comprobar.
       Devuelve un booleano,
       True si el nombre del producto ya existe,
       False si el nombre aun no existe'''
    return JsonResponse({'producto_existe':Products.objects.filter(name=request.GET['producto']).exists()})

def comprobarProductoModificar(request):
    '''Recibe un string con el nombre a comprobar.
       Devuelve un booleano,
       True si el nombre del producto a modificar lo esta usando algun otro producto,
       False si no el nombre del producto a modificar solo lo esta usando el propio producto'''
    return JsonResponse({'producto_existe':Products.objects.filter(name=request.GET['producto']).exclude(id=int(request.GET['idProducto'])).exists()})

def cambiarEstadoProducto(request):
    '''Recibe el id del producto del cual se quiere modificar el estado.
       Se cambia el estado del articulo del producto y devuelve un booleano,
       True si el articulo esta deshabilitado,
       False si el articulo esta habilitado'''
    producto=Products_Details.objects.filter(pk=int(request.POST['idProducto']))
    producto.update(unable=not producto[0].unable)
    data = {
       'estado_cambiado': producto[0].unable
    }
    return JsonResponse(data)

def borrarProducto(request):
    '''Recibe el id del producto a borrar.
       Comprueba si algun articulo de producto esta en algun pedido existente,
       si tiene algun articulo en algun pedido devuelve un True,
       si no tiene ningun articulo en ningun pedido elimina el producto y sus articulos, despues devuelve False'''
    producto=Products.objects.get(pk=int(request.POST['idProducto']))
    if Order_Items.objects.filter(product__in=Products_Details.objects.filter(product=int(producto.id))).exists():
        data ={
            'tiene_pedido':True
        }
    else:
        data ={
            'tiene_pedido':False
        }
        producto.delete()
    return JsonResponse(data)

#PEDIDOS
def listarPedidos(request):
    '''Devuelve una lista con todos los pedidos y
       llama al html que los muestra'''
    return render(request,'listaPedidos.html',{"pedidos":Orders.objects.all()})

def detallesPedido(request,id):
    '''Recibe el id del pedido y devuelve todos los detalles de dich pedido y sus subpedidos(Order_Items),
       calcula el total y
       despues llama al html que muestra toda la informacion'''
    pedido=Orders.objects.get(id=int(id))
    detalles=Order_Items.objects.filter(order=pedido.id)
    total=0
    for item in detalles:
        total+=(float(item.price)*int(item.quantity))
    return render(request,'detallesPedido.html',{"pedido":pedido,"productos_del_pedido":detalles,"total":total})

def crearPedidoVista(request):
    '''Llama al html que muestra el formulario para crear un pedido,
       enviando: 
                -una lista con todos los clientes que esten habilitados y
                 tengan al menos una direccion creada habilitada,
                -una lista con todos los articulos de producto(Product_Details) que esten habilitados y
                 el producto en el que se basan tambien este habilitado'''
    return render(request,'crearPedido.html',{"clientes":Clients.objects.filter(id__in=Address.objects.filter(unable=False).values_list('client'),unable=False),"productos":Products_Details.objects.filter(unable=False).exclude(product__in=Products.objects.filter(unable=True).values_list('id'))})

def crearPedido(request):
    '''Recibe tres listas que indican los productos, las cantidades de dichos productos y los precios actuales, 
       asi como el cliente y la direccion de facturacion y envio;
       se crea el pedido con los datos del cliente pasado y las direcciones que se indican, 
       con la fecha actual como fecha de realizacion del pedido y 10 dias despues la de entrega.
       Despues se crean tantos subpedidos como longitud tenga la lista con sus productos, sus cantidades y sus precios, dado que tienen la misma longitud.
       Al acabar se llama a la funcion que muestra la lista de los pedidos'''
    listaProductos=[]
    listaCantidades=[]
    listaPrecios=[]
    if request.POST.getlist('producto'):
        for item in request.POST.getlist('producto'):
            listaProductos.append(Products_Details.objects.get(pk=int(item)))
    if request.POST.getlist('cantidad'):
        for item in request.POST.getlist('cantidad'):
            listaCantidades.append(item)
    if request.POST.getlist('precio'):
        for item in request.POST.getlist('precio'):
            listaPrecios.append(item)   
    pedido=Orders(client=Clients.objects.get(pk=int(request.POST['selectClientes'])),order_date=datetime.now(),delivery_date=(datetime.now()+timedelta(days=10)),billing_address=Address.objects.get(pk=int(request.POST['selectFacturacion'])),shipping_address=Address.objects.get(pk=int(request.POST['selectEnvio'])))
    pedido.save()
    for index in range(len(listaProductos)):
        Order_Items(order=pedido,product=listaProductos[index],quantity=listaCantidades[index],price=float(listaPrecios[index])).save()
    return HttpResponseRedirect('/listarPedidos')

def direccionesCliente(request):
    '''Recibe el id de un cliente.
       Devuelve una lista con todas las direcciones que esten habilitadas de ese cliente'''
    listaDirecciones=[]
    for item in Address.objects.filter(client=int(request.GET['idCliente'])).exclude(unable=True):
        listaDirecciones.append([item.id,item.street])
    data = {
       'listaDirecciones':listaDirecciones
    }
    return JsonResponse(data)

def eliminarPedido(request):
    '''Recibe el id del pedido a eliminar.
       Elimina el pedido.
       Devuelve True'''
    Orders.objects.get(pk=int(request.POST['idPedido'])).delete()
    return JsonResponse({'pedido_eliminado':True})