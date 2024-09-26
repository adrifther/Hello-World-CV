'''
FUNCIONS
introducció
'''

llista = [1,25,3,13,10]

#OPCION SIN RETORNO
def ordenada0 (llista): #llista.sort() NO tiene return
    return llista.sort()  # NO RETORNA NADA

print(ordenada0(llista))

#OPCION CON RETORNO
def ordenada1 (llista): #llista.sort() NO tiene return
    llista.sort() # ORDENA PERO NO RETORNA NADA: llista.sort() no tiene resultado
    return llista  # return resultat
                 
print(ordenada1(llista))

#OPCION CON RETORNO
def ordenada2 (llista): 
    resultado = llista[:]
    resultado.sort()
    return llista 

print(ordenada2(llista))


#UNA FUNCION SIN RETURN no devuelve nada, no puede asignar resultado a ninguna variable, y el datatype es None. 
def ordenar4(llista):
    llista.sort()    #en la funcion no hay return

llista = ordenar4(llista)
print(llista) #None porque en la funcion no hay return


#B)
#OPCION CON RETORNO
llista = [1,25,3,13,10]

def ordenar (l): 
    resultat = l[:]
    resultat.sort()
    return resultat                 #retorna resultat

ordenada = ordenar(llista)          #guardem a la variable ordenada sino no imprimeix res ordenar(llista)
           #ordenar(llista) sol no imprimeix
print('B)', llista)                   #llista original
print('B)', ordenada, "esta ordenada") #llista ordenada

'''
HAY que poner RETURN para MODIFICAR la LISTA ORIGINAL
'''