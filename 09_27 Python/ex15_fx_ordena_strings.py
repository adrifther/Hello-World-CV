

def ordenastrings(s):
    s.sort()         # no té return


cadena = ["com","estas","hola"] 


ordenastrings(cadena) 
print(cadena)

'''pero '''

cadena2=ordenastrings(cadena) # és None
print(cadena2)
'''no tiene sentido asignar si no hay return por eso da None cadena2. '''


original = ["com","estas","hola"] 
ordenada = original[:] # para no modificar la original creamos una
ordenastrings(ordenada)

print(f"La cadena original es {original} i la ordenada és {ordenada}")
'''asi no modificamos la original'''