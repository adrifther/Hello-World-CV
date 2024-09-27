'''funcion con return mejorada'''

#asi no modificamos la original'''

def ordenastrings(x):

    ordenada = x[:]         # SLICING para no modificar la original creamos una lista nueva
    
    ordenada.sort()         # no té return en sí
    return ordenada


original = ["hola","com","estas"] 

resultado = ordenastrings(original) # AQUI SÍ podemos asignar el resultado

print(f"La cadena original es {original} i la ordenada és {resultado}")
'''asi no modificamos la original'''
#SLICING se usa cuando quieres un objeto que no se modifique, modificas una copia no la original