'''
2. Funció que pren com a paràmetre una llista de números i retorna la suma dels seus
elements
'''

def suma(lista):   # per llista
    total=0        # iniciador dins bucle
    for element in lista:
        total += element
    return total

llista = [1,2,3,4,5]

#codi principal
print(suma(llista)) #suma es 15