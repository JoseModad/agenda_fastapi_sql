document.body.style.zoom = "90%";

async function CargarAgendaGET(url) {
    let contactos = await fetch(url)
    .then(res => res.json())
    .then((agenda) => {
        return agenda;
    });

    return contactos;
}

async function CrearCargar() {
    let contactosAgenda = await CargarAgendaGET("http://127.0.0.1:8000/agenda/")

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
        tdOpc.innerHTML = '<button class = "btn btn-danger" onclick = "EliminarContactoAgenda(this)"><i class = "far fa-trash-alt"></i></button>';        
        tr.appendChild(tdOpc);
        tabla.appendChild(tr)
    }
}

async function CrearContactoPOST() {
    let nombre = document.getElementById("Nombre").value;
    let telefono = document.getElementById("Telefono").value;
    let correo = document.getElementById("Correo").value;

    contactoAgenda = {}
    contactoAgenda.nombre = nombre;
    contactoAgenda.telefono = telefono;
    contactoAgenda.correo = correo;

    let url = "http://127.0.0.1:8000/agenda/";

    await fetch(url, {
        method: "POST",
        body: JSON.stringify(contactoAgenda),
        headers: {
            "Content-Type": "application/json"

        }
    }).then(res => res.json())
    .catch(error => console.error("Error: ", error))
    .then(response => console.log("Exito:", response));
}



function EliminarContactoAgenda(btn) {
    let fila = btn.parentNode.parentNode;
    let id = fila.firstElementChild.innerHTML;
    let url = "http://127.0.0.1:8000/agenda/";
    alertify.confirm("Se eliminara el contacto de la agenda con el id" + id + "",
        function() {
            fetch(url + id, {
                method: "DELETE"
            })
                .then(res => res.json())
                .catch(err => console.error("Error: ", error))
                .then(response => console.log("Exito:", response))
                .then(()=> location.reload())
            alertify.success("Borrado");

        },
        function () {
            alertify.error("Cancelado")
        })
}