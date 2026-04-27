
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
        let modalDialog = document.querySelector("#miModal .modal-dialog");
        modalDialog.classList.remove("modal-xl");
        modalDialog.classList.add("modal-lg");
    } else if (formType == "producto") {
        modalTitulo.textContent = "Crear Producto";
        modalContenido.innerHTML = document.getElementById("form_producto").innerHTML;
        modalFooter.innerHTML = document.getElementById("tabla_producto").innerHTML;
        let modalDialog = document.querySelector("#miModal .modal-dialog");
        modalDialog.classList.remove("modal-xl");
        modalDialog.classList.add("modal-lg");
    }else if(formType == "empresa"){
        modalTitulo.textContent = "Crear Empresa";
        modalContenido.innerHTML = document.getElementById("form_empresa").innerHTML
        modalFooter.innerHTML = document.getElementById("tabla_empresa").innerHTML;
        let modalDialog = document.querySelector("#miModal .modal-dialog");
        modalDialog.classList.remove("modal-xl");
        modalDialog.classList.add("modal-lg");
    } else if (formType == "cliente") {
        modalTitulo.textContent = "Crear Cliente";
        //cargar el formulario
        modalContenido.innerHTML = document.getElementById("form_cliente").innerHTML;
        //cargar la tabla con los datos
        modalFooter.innerHTML = document.getElementById("tabla_cliente").innerHTML;
        let modalDialog = document.querySelector("#miModal .modal-dialog");
        modalDialog.classList.remove("modal-xl");
        modalDialog.classList.add("modal-lg");

    }else if(formType == "agente"){
        modalTitulo.textContent = "Crear Agente";
        modalContenido.innerHTML = document.getElementById("form_agente").innerHTML;
        modalFooter.innerHTML = document.getElementById("tabla_agente").innerHTML;
        let modalDialog = document.querySelector("#miModal .modal-dialog");
        modalDialog.classList.remove("modal-xl");
        modalDialog.classList.add("modal-lg");
    } else if(formType == "cotizacion"){
        modalTitulo.textContent = "Busqueda de Cotizaciones"
        modalContenido.innerHTML = document.getElementById("form_buscar").innerHTML;
        modalFooter.innerHTML = document.getElementById("tabla_cotizacion").innerHTML;

        //obetenemos el div que controla el tamaño, no es modal es .modal.dialog
        let modalDialog = document.querySelector("#miModal .modal-dialog");
        modalDialog.classList.remove("modal-lg");
        modalDialog.classList.add("modal-xl");
    }
})


//se separo la parte en donde se colocan los valores en el formulario 


//esuchamos el evento de click del boton de editar 
document.addEventListener('click', function(event){
    if (event.target.closest('.btn-editar')) {
        const button = event.target.closest('.btn-editar');
        const modalContenido = document.querySelector('#modalContenido');
        const form = modalContenido.querySelector('form');
        const formType = button.getAttribute('data-form');
        console.log("Nombre:", button.getAttribute('data-nombre'));

   //mandar a mostrar los datos que se quieran editar en los inputs 
  
   if(formType == 'servicio'){
        form.querySelector('#id_nombre').value = button.getAttribute('data-nombre');
        form.querySelector('#id_precio').value = button.getAttribute('data-precio');
        form.querySelector('#id_id').value = button.getAttribute('data-id');
        
   }else if (formType == 'producto'){
    //from producto
        form.querySelector('#id_nombre').value = button.getAttribute('data-nombre');
        form.querySelector('#id_precio').value = button.getAttribute('data-precio');
        form.querySelector('#id_codigo').value = button.getAttribute('data-codigo')
        form.querySelector('#id_id').value = button.getAttribute('data-id');
   }else if (formType == 'empresa'){
    //form empresa
        form.querySelector('#id_nombre').value = button.getAttribute('data-nombre');
        form.querySelector('#id_tipo').value = button.getAttribute('data-tipo')
        form.querySelector('#id_dueño').value = button.getAttribute('data-dueño')
        form.querySelector('#id_direccion').value = button.getAttribute('data-direccion')
        form.querySelector('#id_id').value = button.getAttribute('data-id');
    
   }else if (formType == 'cliente'){
        //form cliente
        form.querySelector('#id_nombre').value = button.getAttribute('data-nombre');
        form.querySelector('#id_apellido').value = button.getAttribute('data-apellido');
        form.querySelector('#id_direccion').value = button.getAttribute('data-direccion');
        form.querySelector('#id_telefono').value = button.getAttribute('data-telefono');
        form.querySelector('#id_correo').value = button.getAttribute('data-correo');
        form.querySelector('#id_id').value = button.getAttribute('data-id');

   }else if (formType == 'agente'){
        //form agente
        form.querySelector('#id_nombre').value = button.getAttribute('data-nombre');
        form.querySelector('#id_apellido').value = button.getAttribute('data-apellido');
        form.querySelector('#id_telefono').value = button.getAttribute('data-telefono');
        
        const empresaSelect = form.querySelector('#id_empresa'); //toma el select
        const empresaNombre = button.getAttribute('data-empresa');// toma el valor de la tabla con el id data empresa

            for (let option of empresaSelect.options) {//recore todas las opciones del del select 
                if (option.text === empresaNombre) { // compara los textos de las opciones con las de la tabla
                    empresaSelect.value = option.value; //se lo asigna si coinciden y los coloca en el select pero como numero no como text 
                    break;
                }
    }


        } 
    }
});
