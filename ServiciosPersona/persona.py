class Persona:
    def __init__(self, id, nombre, apellido, telefono, correo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
    
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getTelefono(self):
        return self.telefono

    def getCorreo(self):
        return self.correo
    
    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setCorreo(self, correo):
        self.correo = correo

# para convertir la clase en un diccionario
    def getPersona(self):
        return self.__dict__
