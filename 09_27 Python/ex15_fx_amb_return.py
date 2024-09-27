'''funcion con return'''
#


def ordenastrings(s):
    s.sort()         # no té return
    return s

cadena = ["com","estas","hola"] 

ordenastrings(cadena) 
print(cadena)

'''pero '''

cadena2=ordenastrings(cadena) # és None
print(cadena2)
'''no tiene sentido asignar si no hay return por eso da None cadena2. '''

#
#
#

original = ["com","estas","hola"] 
ordenada = original[:] # SLICING para no modificar la original creamos una lista nueva
resultado = ordenastrings(ordenada) # AQUI SÍ podemos asignar el resultado

print(f"La cadena original es {original} i la ordenada és {resultado}")
'''asi no modificamos la original'''
#SLICING se usa cuando quieres un objeto que no se modifique, modificas una copia no la original