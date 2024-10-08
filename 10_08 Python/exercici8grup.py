# Ejercicio 8 
# 1 - Crear una clase Cálculos con un constructor por defecto (sin parámetros) que permita 
# realizar varios cálculos sobre números enteros.
# 2 - Crear un método llamado factorial() que permita calcular el factorial de un entero.
# 3 - Crear un método llamado suma() que permita calcular la suma de los primeros n 
# enteros 1 + 2 + 3 + .. + n.
# 4 - Crea un método llamado testPrimo() en la clase Cálculos para comprobar si un número 
# es primo. El resultado será True o False.
# 5 - Crear un método llamado testPrimos() que permita comprobar si dos números son 
# primos entre sí.
# 6 - Cree un método tablaMult() que cree y muestre la tabla de multiplicación de un 
# número entero dado. A continuación, cree un método allTablesMult() para mostrar 
# todas las tablas de multiplicación de enteros 1, 2, 3, ..., 9.
# 7 - Crear un método listDiv() que obtenga todos los divisores de un entero dado en una 
# nueva lista llamada Ldiv. 
import math


class Calculos:
    def __init__(self):
        self.numero = int(input(" escribe un número: "))

    def factorial(self):
        self.factorial1 = 1
        for valorposicio in range(self.numero, 0, -1):
            self.factorial1 *= valorposicio
        return self.factorial1
    
    def suma(self):
        self.suma1 = 0
        for valorposicio in range(self.numero, 0, -1):
            self.suma1 += valorposicio
        return self.suma1
    
    def testPrimo(self):
        for num in range(2, self.numero):
            if self.numero % num == 0:
                return False
        return True
    
    def TestPrimos(self, numero2):
        self.mcd = math.gcd(self.numero, numero2)
        print(f" El número {self.numero} y el número {numero2} son primos entre ellos? {self.mcd == 1}")
    
    def TablaMult(self):
        for numero in range(1, 11):
            print(f" {self.numero} x {numero} = {self.numero * numero}")
      
    def allTablesMulti(self):
        counter = 1
        while counter <= 9:
            for numero in range(1, 11):
                print(f" {counter} x {numero} = {counter * numero}")
            counter += 1

    def listDiv(self):
        listadivisor = []
        for num in range(1, self.numero):
            if self.numero % num == 0:
                listadivisor.append(num)
        return listadivisor
        
    
#################################################################################
                                # principal #
#################################################################################

calculo = Calculos()

print(f" El factorial de {calculo.numero} és {calculo.factorial()}")
print(f" La suma de los primeros {calculo.numero} números és {calculo.suma()}")
print(f" El número {calculo.numero} és primo? {calculo.testPrimo()}")
calculo.TablaMult()
print(f" la lista de divisores de {calculo.numero} és {calculo.listDiv()}")
num2 = int(input(" Escribe un número: "))
calculo.TestPrimos(num2)
calculo.allTablesMulti()