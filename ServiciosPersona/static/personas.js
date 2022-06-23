// COMO CONSUMIR UNA API REST
//fetch  libreria por defecto de js
// fetch -  forma de hacer una consulta
// .then - promesa
// https://developer.mozilla.org/es/docs/Web/API/Fetch_API/Using_Fetch

var url = 'http://localhost:9000/personas';

var data = {
    "id":"4",
    "nombre": "Joe",
    "apellido": "Burbano",
    "telefono": "43434",
    "email": "joe@unicomfacauca.edu.co"
};

function getPersonabyName() {
    let nombre = document.getElementById("nombre").value
    fetch(url + "/" + nombre)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            var ret = "<ul><li>nombre: " + data["nombre"] + "</li>" + "<li>apellido: " + data["apellido"] + "</li></ul>";
            var content = document.getElementById("content")
            content.innerHTML = ret;
        });
}

function getPersonas() { // Se obtiene todas las personas
    let nombre = document.getElementById("nombre").value
    fetch(url)
        .then(response => response.json())
        .then(data => console.log(data)); //procesar los datos
}

function savePersona() {
    fetch(url, {
        method: 'POST', // or 'PUT'
        body: JSON.stringify(data), // data can be `string` or {object}!
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then(response => console.log('Success:', response));
}