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