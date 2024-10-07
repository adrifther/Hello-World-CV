

class cadena:

      

      def __init__(self, cadena):
           self.cadena = cadena

 
           
      def dime_string(self):
         return self.cadena

      def establece_string(self,new_cadena):

            self.cadena = new_cadena

      def print_string(self):

          print(self.cadena)

      def quitaespacios(self):

            self.cadena = self.cadena.replace(" ","")

      def listadepalabras(self,caracter):

            lista = self.cadena.split(caracter)

            return lista
      
      def longitud(self):

            return len(self.cadena)

      def __str__(self):

          return f"Este objeto es una cadena con valor: {self.cadena}"
     
#Creado el objeto c1 que es la cadena 1		  
c1 = cadena("Soy tu primera cadena")

print("c1",c1)

c1.print_string()

print("c1.longitud", c1.longitud())

c1.establece_string("Hola")

print("c1", c1)

c1.print_string()

print("c1.longitud: ", c1.longitud())

print("c1.__str__()",c1.__str__())

print("c1.cadena :" , c1.cadena)

c1.cadena = "Te,he,canviado,accediendo,a,la,variable,cadena,de,init"

print("c1", c1)

c1.print_string()

print("c1.longitud: ", c1.longitud())

print("c1.__str__()",c1.__str__())

c1.quitaespacios()

print("c1", c1)

c1.print_string()

print("c1.longitud: ", c1.longitud())

print("c1.__str__()",c1.__str__())

print(c1.listadepalabras(','))


