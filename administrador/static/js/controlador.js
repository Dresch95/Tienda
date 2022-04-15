function add(){
    var contenedor=document.getElementById("contenedorProductoPedido");
    var linea=document.createElement("span");
    var producto=document.createElement("label");
    var cantidad=document.createElement("label");

    var productoEscogido=document.getElementById("productoEscogido");
    var cantidadEscogida=document.getElementById("cantidadProductoPedido");
    cantidad.innerText=cantidadEscogida.value;
    cantidad.setAttribute("name","cantidadProducto");
    producto.innerText=productoEscogido.options[(productoEscogido.value-1)].innerText;
    producto.setAttribute("name","productoEscogido");
    producto.setAttribute("value",productoEscogido.value);

    linea.appendChild(producto);
    linea.appendChild(cantidad);
    contenedor.appendChild(linea);
}
function anhadirProducto(event) {
    var contenedor = document.getElementById("listaProductosPedido");
    var yaExiste = false;
    for (var i = 0; i < contenedor.children.length; i += 2) {
        if (contenedor.children[i].value == event.target.value) {
            contenedor.children[i + 1].textContent++;
            contenedor.children[i + 1].value++;
            yaExiste=true;
        }
    }
    if (!yaExiste) {
        var producto = document.createElement("input");
        var cantidad = document.createElement("input");
        producto.setAttribute("type", "text");
        producto.setAttribute("disabled", true);
        producto.setAttribute("value", event.target.value);
        cantidad.setAttribute("type", "text");
        cantidad.setAttribute("disabled", true);
        cantidad.setAttribute("value", 1);
        producto.textContent = event.target.parentElement.parentElement.children[1].children[0].children[0].textContent;
        cantidad.textContent = 1;
        contenedor.appendChild(producto);
        contenedor.appendChild(cantidad);
    }
}
function modificarEstadoDelCliente(event) {
    var boton = event.target;
    var id = boton.value;
    $.ajaxSetup({ data: { csrfmiddlewaretoken: '{{ csrf_token }}' } });
    $.ajax({
        url: "{% url 'cambiarEstadoCliente' %}",
        type: 'POST',
        data: { 'idCliente': id },
        dataType: 'json'
    }).done(function (response) {
        if (response['estado_cambiado']) {
            boton.textContent = "Habilitar";
            boton.setAttribute("class", "botonCambiarEstado botonHabilitar");
        } else {
            boton.textContent = "Deshabilitar";
            boton.setAttribute("class", "botonCambiarEstado botonDeshabilitar");
        }
    }).fail(function () {
        console.log("failed");
    })
}
function comprobarCliente(e) {
    $.ajax({
        url: "{% url 'comprobarCliente' %}",
        type: 'POST',
        headers:{'X-CSRFToken':'{{ csrf_token }}'},
        data: { 'idCliente': e.target.name },
        dataType: 'json',
        success: function (data) {

        }
    }).done(function (response) {
        if (response['tiene_pedido']) {
            alert("Cliente tiene pedidos");
        }else{
            document.getElementById(e.target.name).remove();
        }
    })
        .fail(function () {
            console.log("failed");
        })
}
/*
{% if pr.size == 'BG' %}
Grande
{% elif pr.size == 'AV' %}
Estandar
{% elif pr.size == 'SM' %}
Pequeño
{% endif %}*/