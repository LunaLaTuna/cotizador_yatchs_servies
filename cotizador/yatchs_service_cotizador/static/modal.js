const modal = document.getElementById('miModal');
modal.addEventListener('show.bs.modal', function(event){
    const button = event.relatedTarget;
    const formType = button.getAttribute('data-form');
    const modalTitulo = modal.querySelector('#modalTitulo');
    const modalContenido = modal.querySelector('#modalContenido');

    if (formType == "servicio"){
        modalTitulo.textContent = "Crear Servicio";
        modalContenido.innerHTML = document.getElementById("form_servicio").innerHTML;
    } else if (formType == "producto") {
        modalTitulo.textContent = "Crear Producto";
        modalContenido.innerHTML = document.getElementById("form_producto").innerHTML;
    }else if(formType == "empresa"){
        modalTitulo.textContent = "Crear Empresa";
        modalContenido.innerHTML = document.getElementById("form_empresa").innerHTML;
    } else if (formType == "cliente") {
        modalTitulo.textContent = "Crear Cliente";
        modalContenido.innerHTML = document.getElementById("form_cliente").innerHTML;
    }
})