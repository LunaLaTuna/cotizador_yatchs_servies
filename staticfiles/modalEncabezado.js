    const modalEncabezado = document.getElementById('modalEncabezado');

    modalEncabezado.addEventListener('show.bs.modal', function(event){
        const button = event.relatedTarget;

        const tableType = button.getAttribute('data-table');
        const modalEncabezadoTitulo = modalEncabezado.querySelector('#modalEncabezadoTitulo');
        const modalEncabezadoContenido = modalEncabezado.querySelector('#modalEncabezadoContenido');


        if (tableType == "empresa"){
            modalEncabezadoTitulo.textContent = "Empresas";
            modalEncabezadoContenido.innerHTML = document.getElementById("tabla_empresa_encabezado").innerHTML;

                modalEncabezadoContenido.querySelectorAll('.fila-empresa').forEach(fila =>{
                fila.addEventListener('click', function(){

                    document.getElementById('empresa_id').value = this.getAttribute('data-id');
                    document.getElementById('empresa_nombre').textContent = `Nombre: ${this.getAttribute('data-nombre')}`;
                    document.getElementById('empresa_dueño').textContent = `Dueño: ${this.getAttribute('data-dueño')}`;
                    document.getElementById('empresa_direccion').textContent = `Dirección: ${this.getAttribute('data-direccion')}`;

                    const urlLogo = this.getAttribute('data-logo');
                    console.log(urlLogo)
                    const logoImg = document.getElementById('empresa_logo');
                    if(urlLogo) {
                        logoImg.src = urlLogo;
                        logoImg.style.display = 'block';
                    } else {
                        logoImg.style.display = 'none';
                    }

                });
            });
        }else if(tableType == "cliente"){
            modalEncabezadoTitulo.textContent = "Clientes"
            modalEncabezadoContenido.innerHTML = document.getElementById('tabla_cliente_encabezado').innerHTML;

            modalEncabezadoContenido.querySelectorAll('.fila-cliente').forEach(fila => {
                fila.addEventListener('click', function(){
                    document.getElementById('cliente_id').value = this.getAttribute('data-id');
                    document.getElementById('cliente_nombre').textContent = `Nombre: ${this.getAttribute('data-nombre')} ${this.getAttribute('data-apellido')}` ;
                    document.getElementById('cliente_direccion').textContent = `Dirección: ${this.getAttribute('data-direccion')}` ;
                    document.getElementById('cliente_correo').textContent = `Correo: ${this.getAttribute('data-correo')}`;
                    document.getElementById('cliente_numero').textContent = `Teléfono: ${this.getAttribute('data-telefono')}`;
                    
                })
            })
        } else if(tableType == "items"){
            modalEncabezadoTitulo.textContent = "Productos y Servicios"
            modalEncabezadoContenido.innerHTML = document.getElementById('tabla_items_encabezado').innerHTML;


            // modalEncabezadoContenido.querySelectorAll('.fila-items').forEach(fila => {
            //     fila.addEventListener('click', function(){
            //         document.getElementById('cliente_nombre').textContent = this.getAttribute('data-nombre');
            //         document.getElementById('cliente_direccion').textContent = this.getAttribute('data-direccion');
            //         document.getElementById('cliente_correo').textContent = this.getAttribute('data-correo');
            //         document.getElementById('cliente_numero').textContent = this.getAttribute('data-telefono');
                    
            //     })
            // })
            
        }
        else if(tableType == "agentes"){
            modalEncabezadoTitulo.textContent = "Agentes"
            modalEncabezadoContenido.innerHTML = document.getElementById('tabla_agentes_encabezado').innerHTML;

            modalEncabezadoContenido.querySelectorAll('.fila-agentes').forEach(fila => {
                fila.addEventListener('click', function(){
                    document.getElementById('agente_id').value = this.getAttribute('data-id');
                    document.getElementById('agente_nombre').textContent = `Nombre: ${this.getAttribute('data-nombre')} ${this.getAttribute('data-apellido')}`
                    document.getElementById('agente_telefono').textContent = `Teléfono: ${this.getAttribute('data-telefono')}`;
                    document.getElementById('agente_empresa').textContent = `Empresa: ${this.getAttribute('data-empresa')}`;
                    
                })
            })

        }
    })

//encanchar el listener pero no solo al evento del modal, si no a todo el documento, porque este ya existe desde el inicio 
document.addEventListener('click', function(e){
                const fila = e.target.closest('.fila-items');
                if (!fila) return;
        
                const nombre = fila.getAttribute('data-nombre');
                const tipo = fila.getAttribute('data-tipo');
                const codigo = fila.getAttribute('data-codigo');
                const precio = fila.getAttribute('data-precio');
            
                const tablaDetalle = document.querySelector('#tabla_detalle tbody');
                
                const nuevaFila = document.createElement('tr');

                if (tipo === "Producto"){
                    nuevaFila.innerHTML = `
                    <tr>
                        <td><input type="number" value="1" min="1" class="cantidad-input"></td>
                        <td>${nombre}</td>
                        <td>${tipo}</td>
                        <td>${codigo}</td>
                        <td>${precio}</td>
                        <td class="subtotal">${precio}</td>
                        <td> 
                            <a href="#" class="btn-eliminar">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
                                    <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
                                </svg>
                            </a>
                        </td>
                    </tr>
                    <!-- inputs ocultos -->
                    <input type="hidden" name="detalle_nombre" value="${nombre}">
                    <input type="hidden" name="detalle_tipo" value="${tipo}">
                    <input type="hidden" name="detalle_codigo" value="${codigo}">
                    <input type="hidden" name="detalle_cantidad" value="1">
                    <input type="hidden" name="detalle_precio" value="${precio}">
                    <input type="hidden" name="detalle_subtotal" value="${precio}">
                `

                } else {
                    nuevaFila.innerHTML = `
                    <tr>
                        <td><input type="number" value="1" min="1" readonly class="cantidad-input"></td>
                        <td>${nombre}</td>
                        <td>${tipo}</td>
                        <td>${codigo}</td>
                        <td>${precio}</td>
                        <td class="subtotal">${precio}</td>
                        <td><a href="#" class="btn-eliminar">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
                                    <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
                                </svg>
                            </a>
                        </td>
                    </tr>
                    <!-- inputs ocultos -->
                    <input type="hidden" name="detalle_nombre" value="${nombre}">
                    <input type="hidden" name="detalle_tipo" value="${tipo}">
                    <input type="hidden" name="detalle_codigo" value="${codigo}">
                    <input type="hidden" name="detalle_cantidad" value="1">
                    <input type="hidden" name="detalle_precio" value="${precio}">
                    <input type="hidden" name="detalle_subtotal" value="${precio}">
                `
                }
                
                tablaDetalle.appendChild(nuevaFila);
                calcularTotales()

                tablaDetalle.addEventListener('input', function(e){
                if (e.target.classList.contains('cantidad-input')){
                    const fila = e.target.closest('tr');
                    const precio = parseFloat(fila.querySelector('td:nth-child(5)').textContent);
                    const cantidad = parseInt(e.target.value);
                    const subtotalCell = fila.querySelector('.subtotal');
                    subtotalCell.textContent = (precio * cantidad.toFixed(2))
                    calcularTotales()
                    }
                })

                tablaDetalle.addEventListener('click', function(e){
                    if (e.target.closest('.btn-eliminar')){
                        const fila = e.target.closest('tr');
                        fila.remove();
                        calcularTotales()
                    }
                })

            });

                   //crear funcion para calcular los totales
                    function calcularTotales(){

                        //obetenemos todos los subtotales de las filas
                        const filas  = document.querySelectorAll('#tabla_detalle tbody tr');
                        let subtotalGeneral = 0;

                        filas.forEach(fila => {
                            const subtotalCell = fila.querySelector('.subtotal');
                            if (subtotalCell){
                                subtotalGeneral += parseFloat(subtotalCell.textContent) || 0;
                            } 

                        });

                        const tasaIva = 0.16;
                        const iva = subtotalGeneral * tasaIva;
                        const total = subtotalGeneral + iva;
                        
                        document.getElementById('input_iva').value = iva.toFixed(2);
                        document.getElementById('input_subtotal_general').value = subtotalGeneral.toFixed(2);
                        document.getElementById('input_total').value = total.toFixed(2);

                        document.getElementById('subtotal-general').textContent = `Subtotal: ${subtotalGeneral.toFixed(2)}`;
                        document.getElementById('iva').textContent = `IVA:         ${iva.toFixed(2)}`;
                        document.getElementById('total').textContent = `Total: ${total.toFixed(2)}`; 

                    }


document.addEventListener('DOMContentLoaded', function(){
    const hoy = new Date();
    const año = hoy.getFullYear();
    const mes = String(hoy.getMonth() + 1).padStart(2, '0');
    const dia = String(hoy.getDate()).padStart(2, '0');

    const fecha = `${dia}-${mes}-${año}`;
    const fechaBackend = `${año}-${mes}-${dia}`;

    const caducidad = new Date();
    caducidad.setMonth(caducidad.getMonth() + 1);

    const añoCad = caducidad.getFullYear();
    const mesCad = String(caducidad.getMonth() + 1).padStart(2, '0');
    const diaCad = String(caducidad.getDate()).padStart(2, '0');

    const fechaCaducidad = `${diaCad}-${mesCad}-${añoCad}`;
    const fechaCadBackend = `${añoCad}-${mesCad}-${diaCad}`;

    document.getElementById('fecha_actual').textContent = `Fecha Actual: ${fecha}`;
    document.getElementById('fecha_caducidad').textContent = `Fecha Caducidad: ${fechaCaducidad}`;

    document.getElementById('fecha_input').value = fechaBackend;
    document.getElementById('fecha_caducidad_input').value = fechaCadBackend;

})
