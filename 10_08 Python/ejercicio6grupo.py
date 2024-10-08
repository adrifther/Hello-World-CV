# Ejercicio 6
# Escribe una clase de Python, y define dos métodos que devuelvan el área del cuadrado 
# y el perímetro.


class cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return self.lado * 4

try:
    lado = int(input("escribe un numero para dar valor al lado de un cuadrado: "))

    cuadrado_1 = cuadrado(lado)


    print(f" En un cuadrado de lado {lado}, el área será {cuadrado_1.area()} y su perímetro {cuadrado_1.perimetro()}")
except:
    print("El costat ha de contenir números, no lletres o símbols")