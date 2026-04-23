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
                                  <td>${item.fecha}</td>
                                  <td>${item.agente}</td>
                                  <td>${item.subtotal}</td>
                                  <td>${item.iva}</td>
                                  <td>${item.total}</td>
                                </tr>`;
                    tbody.innerHTML += fila;
                });

                // paginador dinámico
                let pagHtml = "";
                for (let i = 1; i <= data.num_paginas; i++) {
                    pagHtml += `<button class="btn btn-dark" onclick="pagina=${i};cargarResultados()">${i}</button>`;
                }
                paginador.innerHTML = pagHtml;
            });
    }

    // delegar evento al modal: cada vez que se escriba en el input
    modal.addEventListener("keyup", function(e) {
        if (e.target && e.target.id === "id_query") {
            console.log("Detectado input dentro del modal:", e.target.value);
            pagina = 1;
            cargarResultados();
        }
    });

    // inicializar búsqueda solo cuando el modal se abre con cotización
    modal.addEventListener("show.bs.modal", function(event) {
        const button = event.relatedTarget;
        const formType = button.getAttribute("data-form");

        console.log("Modal abierto con formType:", event.relatedTarget.getAttribute("data-form"));

        if (formType === "cotizacion") {
            pagina = 1;
            console.log("entro al form")
            cargarResultados();
        }
    });
});