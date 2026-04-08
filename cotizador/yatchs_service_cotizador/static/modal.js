
// recolectamos el modal
const modal = document.getElementById('miModal'); 

//ahora cuando el modal se muestre, escuchamos es evento que se ejecuta cuando se va a mostar el modal
modal.addEventListener('show.bs.modal', function(event){ 
    //funcion(event): es la funcion que esta relacionada al evento y event es el objeto que contiene toda la infromación del evento


    //esto se usa para saber que boton se uso para abrir el modal 
    const button = event.relatedTarget;
    //del boton que identificamos, ahoora recolectamos su atributo data-form
    const formType = button.getAttribute('data-form');
    //aquí usar query en lugar de id porque estas buscando dentro del modal, y esta opcion es más flexible 
    const modalTitulo = modal.querySelector('#modalTitulo');
    const modalContenido = modal.querySelector('#modalContenido');
    const modalFooter = modal.querySelector('#modalFooter');

//ni modo que no sepas que esto we
    if (formType == "servicio"){
        modalTitulo.textContent = "Crear Servicio";
        modalContenido.innerHTML = document.getElementById("form_servicio").innerHTML;
        modalFooter.innerHTML = document.getElementById("tabla_servicio").innerHTML;
    } else if (formType == "producto") {
        modalTitulo.textContent = "Crear Producto";
        modalContenido.innerHTML = document.getElementById("form_producto").innerHTML;
        modalFooter.innerHTML = document.getElementById("tabla_producto").innerHTML;
    }else if(formType == "empresa"){
        modalTitulo.textContent = "Crear Empresa";
        modalContenido.innerHTML = document.getElementById("form_empresa").innerHTML
        modalFooter.innerHTML = document.getElementById("tabla_empresa").innerHTML;
    } else if (formType == "cliente") {
        modalTitulo.textContent = "Crear Cliente";
        //cargar el formulario
        modalContenido.innerHTML = document.getElementById("form_cliente").innerHTML;
        //cargar la tabla con los datos
        modalFooter.innerHTML = document.getElementById("tabla_cliente").innerHTML;

    }
})

document.addEventListener('click', function(event){
    if (event.target.closest('.btn-editar')) {
        const button = event.target.closest('.btn-editar');
        const form = modalContenido.querySelector('form');
        console.log("Nombre:", button.getAttribute('data-nombre'));

   //mandar a mostrar los datos que se quieran editar en los inputs 
        form.querySelector('#id_nombre').value = button.getAttribute('data-nombre');
        form.querySelector('#id_apellido').value = button.getAttribute('data-apellido');
        form.querySelector('#id_direccion').value = button.getAttribute('data-direccion');
        form.querySelector('#id_telefono').value = button.getAttribute('data-telefono');
        form.querySelector('#id_correo').value = button.getAttribute('data-correo');

        form.querySelector('#id_id').value = button.getAttribute('data-id');
    }
});
