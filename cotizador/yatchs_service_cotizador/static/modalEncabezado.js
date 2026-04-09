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
                    document.getElementById('empresa_nombre').textContent = this.getAttribute('data-nombre');
                    document.getElementById('empresa_dueño').textContent = this.getAttribute('data-dueño');
                    document.getElementById('empresa_direccion').textContent = this.getAttribute('data-direccion');

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
                    document.getElementById('cliente_nombre').textContent = this.getAttribute('data-nombre');
                    document.getElementById('cliente_direccion').textContent = this.getAttribute('data-direccion');
                    document.getElementById('cliente_correo').textContent = this.getAttribute('data-correo');
                    document.getElementById('cliente_numero').textContent = this.getAttribute('data-telefono');
                    
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
    })

document.getElementById('tabla_items_encabezado').addEventListener('click', function(e){
                const fila = e.target.closest('.fila-items');

                const nombre = fila.getAttribute('data-nombre');
                const tipo = fila.getAttribute('data-tipo');
                const codigo = fila.getAttribute('data-codigo');
                const precio = fila.getAttribute('data-precio');
            
                const tablaDetalle = document.querySelector('#tabla_detalle tbody');
                
                const nuevaFila = document.createElement('tr');
                nuevaFila.innerHTML = `
                    <tr>
                        <th></th>
                        <td>${nombre}</td>
                        <td>${tipo}</td>
                        <td>${codigo}</td>
                        <td>${precio}</td>
                    </tr>
                `
                tablaDetalle.appendChild(nuevaFila);
            });

  