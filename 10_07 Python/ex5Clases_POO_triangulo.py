##Clases no funciona ESTE

class triangulo:

                #sempre self
    def __init__(self, lado1, lado2, lado3): #variables d inicialitzacio:self
        
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
        
    def estriangle(self):
        if (self.lado1 > self.lado2 + self.lado3) or (self.lado2 > self.lado1 + self.lado3) or (self.lado3 > self.lado2 + self.lado1):

            return False
            
        
        else:

            return True

    def mayor(self): #lado + grande

        if self.estriangle():
            
            return max([self.lado1,self.lado2,self.lado3])
        
        else: 
            
            return False

    def tipo(self):
        if self.estriangle():
            if self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado2 != self.lado3:

                return "triangulo escaleno"
        
            elif self.lado1 == self.lado2 and self.lado2==self.lado3:

                return "El triangulo es equilatero"
            
            else:

                return "El triangulo es isosceles"

        return "El tipus no te l puc dir"        



    def __str__(self):
        if self.estriangle():

            return f"Este es un objeto triangulo con lados {self.lado1},{self.lado2},{self.lado3}"



while True:

    try:
        lado1 = float(input())
        lado2 = float(input())
        lado3 = float(input())
        triangle1 = triangulo(lado1, lado2, lado3)
        break
    except:
        print("dades incorrectes, torna-hi")



triangle1=triangulo(3,2,2)

print(triangle1)

print(triangle1.mayor())

print(triangle1.tipo())


print(f"Es triangle aixo?:{triangle1.estriangle()}")

