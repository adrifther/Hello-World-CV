'''entrada = input (" entra la frase i el numero de repeticions, separats per una coma")
resultado_split = entrada.split(',') #es lo mismo que la siguiente linea
#[frase,repeticiones] = entrada.split (',')
print (frase)
print (repeticiones)
'''

entrada = input (' entra la frase i el numero de repeticions, separats per una coma')
lista= entrada.split(',')
frase = lista [0] + "\n"
repeticiones = int(lista[1])
print(frase*repeticiones)
