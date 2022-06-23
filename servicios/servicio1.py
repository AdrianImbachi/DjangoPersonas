# importar las librerias que necesitamos como Flask
from flask import Flask
from operaciones import suma,resta

#Creando la variable app que contendrá la aplicación de inicio de flask 
app=Flask(__name__) #__name__ - variable de entorno, ruta donde se ubica la aplicación

# Se define la ruta donde se expondrá el método asociado al decorador
# el decorador inicia con @, en este caso @app.route("/")
# el método expuesto es main() en este caso
@app.route("/") # route - ruta donde se va a conectar
def main():
    return "<h1>Hola desde el universo de servicios web</h1>"

@app.route("/suma")
def s_suma():
    numero1 = 4
    numero2 = 5
    s = suma(numero1,numero2)
    respuesta = {"numero1":numero1, "numero2":numero2, "operacion":"suma", "resultado":str(s)} #diccionario de python
    return respuesta

@app.route("/resta")
def r_resta():
    numero1 = 4
    numero2 = 5
    s = resta(numero1,numero2)
    respuesta = {"numero1":numero1, "numero2":numero2, "operacion":"resta", "resultado":str(s)} #diccionario de python
    return respuesta

@app.route("/operacion")
def o_operacion():
    numero1 = 4
    numero2 = 5
    s = suma(numero1,numero2)
    r = resta(numero1,numero2)
    respuesta = {"numero1":numero1, "numero2":numero2, "operacion":"suma", "suma":str(s), "operacion":"resta", "resta":str(r)} #diccionario de python
    return respuesta

#Forma de correr el proyecto, cuando el puerto 5000 está ocupado
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=9000)
