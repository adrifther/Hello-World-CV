'''
Escriu una funcio per comprovar si un numero es perfecte o no:
-nombre sencer positiu
-es igual a la suma dels seus divisors positius propis (la suma dels seus divisors positius excloent el mateix numero)
un nombre perfecte es un nombre que es la meitat de la suma de tots els seus divisors positius(inclos ell mateix)
'''
numero_dado= int(input("numero sera perfect?"))

def perfecte(numero):

    lista_divisor=[]
    

    for i in range (1,numero):
        if numero % i == 0:
            lista_divisor.append(i)

    suma_divisores = 0 
    for divisor in lista_divisor:
        suma_divisores += divisor


    if (numero > 0 and suma_divisores==numero):
        return True
    else:
        return False


print(perfecte(numero_dado))