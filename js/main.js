document.addEventListener('DOMContentLoaded', () => {
    const submitButton = document.getElementById('submit');
    submitButton.addEventListener('click', () => {
        loadPage('contact.html');
    });
});

function loadPage(url) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onload = function () {
        if (xhr.status === 200) {
            var main = document.getElementById('main');
            main.innerHTML = xhr.responseText;
            initializeForm();
        }
    };
    xhr.send();
}

function initializeForm() {
    const formulario = document.getElementById('formulario');

    const getData = async (event) => {
        event.preventDefault();
        const { nombre, tipo_documento, numero_documento, direccion, telefono, email, servicio, profesional, fecha, hora } = event.target;

        const datos = {
            nombre: nombre.value,
            tipo_identificacion: tipo_documento.value,
            numero_identificacion: numero_documento.value,
            telefono: telefono.value,
            direccion: direccion.value,
            email: email.value,
            servicio: servicio.value,
            profesional: profesional.value,
            fecha: fecha.value,
            hora: hora.value
        }

        const url = 'http://127.0.0.1:8000/api/cita/?format=json'

        try {
            const response = await fetch(url, {
                method: 'POST',
                body: JSON.stringify(datos),
                headers: {
                    'Content-Type': 'application/json'
                }
            }

            )
            const data = await response.json()
            console.log(data);
        } catch (error) {
            console.log(error);
        }
    };

    formulario.addEventListener('submit', getData);
}
