from flask import Flask, request, jsonify, render_template
from persona import Persona
# jsonify - retorna un resultado en json

app = Flask(__name__)

ListaPersonas = [] # Para guardar los datos de las personas, temporalmente en la cache


def searchPersonaByName(name):
    p = next((i for i, item in enumerate(
        ListaPersonas) if item["nombre"] == name), -1)
    if p != -1:
        return jsonify(ListaPersonas[p])
    else:
        return jsonify({"respuesta":"Persona " +name+ " no existe en el sistema"})

def deletePersonaById(id):
    p = next((i for i, item in enumerate(ListaPersonas) if item["id"] == id), -1)
    if p != -1:
        del ListaPersonas[p]
        return jsonify({"respuesta ": "Persona eliminada"})
    else:
        return jsonify({"respuesta":"Persona no fue eliminada"})



@app.route("/")
def servicio():
    return render_template("personas.html")


@app.route("/personas", methods=["GET", "POST"])
def getPersonas():
    if request.method == "GET":
        return jsonify(ListaPersonas)
    else:
        lapersona = Persona(request.json["id"],request.json["nombre"], request.json["apellido"],request.json["telefono"], request.json["email"])
        ListaPersonas.append(lapersona.getPersona()) #append - añadir a la lista
        return request.json  # los request solo funcionan con los métodos POST


# busqueda de una persona con un nombre
@app.route("/personas/<nombre>", methods=["GET"])
def getPersonasByName(nombre):
    return searchPersonaByName(nombre)

@app.route("/personas/<int:id>", methods=["DELETE"])
def delPersona(id):
    return deletePersonaById(id)

@app.route("/personas/<int:id>", methods=["PUT"])
def updatePersona(id):
    lapersona = Persona(request.json["id"],request.json["nombre"], request.json["apellido"],request.json["telefono"], request.json["email"])
    p=next((i for i, item in enumerate(ListaPersonas) if item["id"]==id),-1)
    ListaPersonas[p] = lapersona.getPersona()
    return jsonify({"respuesta":"Fue actualizada"})


# para evitar configurar variables de entorno, se tiene una fija
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)