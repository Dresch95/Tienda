from http import client
from django.forms import ValidationError
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .models import Clients,Address

# Create your views here.
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
    cliente=[]
    try:
        cliente.append(request.POST['nombreClienteNuevo'])
        cliente.append(request.POST['emailClienteNuevo'])
        cliente.append(request.POST['telefonoClienteNuevo'])
        cliente.append(request.POST['urlImagenNuevoCliente'])
        direccion.append(request.POST['calleDireccionNueva'])
        direccion.append(request.POST['ciudadDireccionNueva'])
        direccion.append(request.POST['codigoDireccionNueva'])
        direccion.append(request.POST['paisDireccionNueva'])
        direccion.append(request.POST['tiposDireccion'])
        if all(item for item in cliente) and all(item for item in direccion):
            Address(street=direccion[0],city=direccion[1],code=direccion[2],country=direccion[3],type=direccion[4]).save()
            Clients(name=cliente[0],email=cliente[1],tel=cliente[2],imageURL=cliente[3],address_id=Address.objects.filter(street=direccion[0],city=direccion[1],code=direccion[2],country=direccion[3],type=direccion[4])[0].id).save()
    except ValidationError as e:
        ValidationError(('Invalid value'), code='Hola')
    return HttpResponseRedirect('/listarClientes')

def borrarCliente(id):
    Clients.objects.get(pk=id).delete()
    return HttpResponseRedirect('/listarClientes')