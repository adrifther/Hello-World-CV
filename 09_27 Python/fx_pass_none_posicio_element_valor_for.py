def parelles(x):
    pass

original = ["hola","com","estas"] 

resultado = parelles(original)

print(f"La cadena original es {original} i la ordenada és {resultado}")

'''
element que es troba a la posicio 0 es hola i es reconeix com original[0]
element que es troba a la posicio 1 es hola i es reconeix com original[1]
element que es troba a la posicio 2 es hola i es reconeix com original[2]
''' 

for element in original:
    print(element)

for posicio in range(len(original)):
    print(posicio, original[posicio])

#creamos indice y posicion
'''
'''