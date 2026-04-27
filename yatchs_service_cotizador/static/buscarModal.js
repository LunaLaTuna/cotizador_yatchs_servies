document.addEventListener("DOMContentLoaded", function() {
    const modal = document.getElementById("miModal");
    let pagina = 1;

    function cargarResultados() {
        // buscar dentro del modal
        console.log("dentro de la funcion")
        let input = modal.querySelector("#id_query");
        let tbody = modal.querySelector("#tabla_cotizaciones tbody");
        let paginador = modal.querySelector("#paginador");

        if (!input || !tbody || !paginador) {
            return;
        }
        let query = input.value;

        console.log("Llamando a fetch con query:", query);
        fetch(`/cotizador/busqueda_ajax/?q=${query}&page=${pagina}`)
            .then(res => {
            console.log("Respuesta cruda:", res);
            return res.json();
        })
            .then(data => {

                console.log("Datos recibidos:", data);
                // limpiar y agregar filas
                tbody.innerHTML = "";
                data.resultados.forEach(item => {
                    let fila = `<tr>
                                    <td>${item.numero_cotizacion}</td>
                                    <td>${item.empresa}</td>
                                    <td>${item.cliente}</td>
                                    <td>${item.fecha_creacion}</td>
                                    <td>${item.fecha_caducidad}</td>
                                    <td>${item.agente}</td>
                                    <td>${item.subtotal}</td>
                                    <td>${item.iva}</td>
                                    <td>${item.total}</td>
                                    <td>${item.pdf_url ? `<a href="${item.pdf_url}" target="_blank">Ver PDF</a>` : "No disponible"}</td>
                                    </tr>`;
                    tbody.innerHTML += fila;
                });

                // paginador dinámico
                let pagHtml = "";
                for (let i = 1; i <= data.num_paginas; i++) {
                    pagHtml += `<button class="btn btn-dark paginador" data-pagina="${i}">${i}</button>`;
                }
                paginador.innerHTML = pagHtml;

                paginador.querySelectorAll('.paginador').forEach(btn => {
                btn.addEventListener('click', function() {
                    pagina = parseInt(this.getAttribute('data-pagina'));
                    cargarResultados();
                });
            });
            });
    }

    // hacer que se agarre el evento del modal que este en el input
    modal.addEventListener("keyup", function(e) {
        if (e.target && e.target.id === "id_query") {
            pagina = 1;
            cargarResultados();
        }
    });

    // inicializar búsqueda solo cuando el modal se abre con cotización
    modal.addEventListener("show.bs.modal", function(event) {
        const button = event.relatedTarget;
        const formType = button.getAttribute("data-form");

        if (formType === "cotizacion") {
            pagina = 1;
            cargarResultados();
        }
    });
});