document.body.style.zoom = "90%";

async function CargarAgendaGet(url) {
    let contactos = await fetch(url)
    .then(res => res.json())
    .then((agenda) => {
        return agenda;
    });

    return contactos;
}

async function CrearCargar() {
    let contactosAgenda = await CargarAgendaGet("http://127.0.0.1:8000/agenda/")

    let tabla = document.getElementById("tbody");
    for (let k in contactosAgenda) {
        let contactos = contactosAgenda[k];
        tr = document.createElement("tr");
        for (let x in contactos) {
            td = document.createElement("td");
            td.innerHTML = contactos[x];
            tr.appendChild(td);
        }

        tdOpc = document.createElement("td");
        tdOpc.innerHTML = 
        <button class = "btn btn-danger" onclick = "EliminarContactoAgenda(this)"><i class = "far fa-trash-alt"></i></button> ;
        tr.appendChild(tdOpc);
        tabla.appendChild(tr)
    }
}


function EliminarContactoAgenda(btn) {
    let file = btn.parentNode.parentNode;
    let id = fila.firstElementChild.innerHTML;
    let url = "http://127.0.0.1:8000/agenda/";
    alertify.confirm("Se eliminara el contacto de la agenda con el id" + id + "",
    function() {
        fetch(url + id, {
            method: "DELETE"
        })
            .then(res => res.json())
            .catch(err => console.error["Error: ", error])
            .then(response => console.log("Exito:", response))
            .then(()=> location.reload())
        alertify.success("Borrado");

    }),
    function () {
        alertify.error("Cancelado")
    }
}