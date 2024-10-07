import math

class circulo:

     
      
      def __init__(self, radio):

           self.radio = radio

        
      def area(self):
            '''El area es pi*radio**2'''
            return math.pi*(self.radio)**2

      def perimetro(self):
            '''El perimetro es 2*pi*radio'''
            return 2*math.pi*self.radio

      def __str__(self):

            return f" Este es un objeto circulo con radio {self.radio}"


circulo1 = circulo(10)

print(circulo1)

print(circulo1.area())

print(circulo1.perimetro())

print(circulo1.radio)

circulo1.radio = 1

print(circulo1)

print(circulo1.area())

print(circulo1.perimetro())

print(circulo1.radio)
