#Clases

class cadena:

    lista = [] #variable de clase, lista queda en este entorno

                #sempre self
    def __init__(self, cadena): #variables d inicialitzacio:self
        
        self.cadena = cadena

    def get_string(self):  #get da valor 

        return self.cadena
    
    def set_string(self,new_cadena):  #set establece el valor

        self.cadena=new_cadena

    def print_string(self):

        print(self.cadena)

    def quitaespacios(self):

        self.cadena = self.cadena.replace(" ", "")    #hay que poner el = sino no retorna nada replace.

    def listadepalabras(self):

        lista = self.cadena.split()

        return lista

    def longitud(self):

        return len(self.cadena)

    def __str__(self):

        return f"Este objeto es una cadena tiene este valor:{self.cadena}"
    

c1 = cadena("soy tu primera cadena") #primer objeto de cadena

print("c1",c1)
c1.print_string() 

c1.set_string("hola")
c1.print_string()

print("c1.longitud",c1.longitud()) #cambiamos c1 a Hola con 4 letras

print("c1 es ahora",c1.cadena)

c1.cadena = "Esta es ahora la cadena c1"

print(c1.cadena)

print(c1.__str__())

print("lista de palabras hecha en la clase con replace, hemos usado lista como variable de clase",c1.listadepalabras())

c1.quitaespacios()

print("c1 con quitaespacios()",c1)