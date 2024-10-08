# Ejercicio 4
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase:
# • Un constructor, donde los datos pueden estar vacíos.
# • Los setters y getters para cada uno de los atributos. Hay que validar las 
# entradas de datos.
# • mostrar(): Muestra los datos de la persona.
# • esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.


class persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def set_nombre(self, new_nombre):
        self.nombre = new_nombre

    def set_edad(self, new_edad):
        self.edad = new_edad

    def set_dni(self, new_dni):
        self.dni = new_dni

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def esMayorDeEdad(self):
        if int(self.get_edad()) >= 18:
            return True
    
    def get_dni(self):
        return self.dni
    
    def show_persona(self):
        return f"Nombre: {self.get_nombre()}, edad: {self.get_edad()} y dni: {self.get_dni()}"


def validacion(nombre, edad, dni):
    if (nombre.isalpha() and edad.isdigit() and ((dni[:-1]).isdigit() and dni[-1:].isalpha())):
        print("Validado")
        return True
    
    print("dades full incorrectes, torna-hi")
    return False

while True:
    nombre = input("Escribe tu nombre: ")
    edad = input("Escribe tu edad: ")
    dni = input("Escribe tu dni: ")
    if validacion(nombre, edad, dni): 
        break

persona1 = persona(nombre, edad, dni)
print(persona1.show_persona())
if persona1.esMayorDeEdad():
    print("es mayor de edad")
else:
    print(" no es mayor de edad, que no beba")