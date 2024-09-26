''''CONTADORES
'''
'''modificara comptadors aquest bucle:
per cada element dels comptadors, sumas un al element.

Per poder modificar s ha de recorrer per posicions:
'''
comptadors = [0,0,0,0,0]     #una lista es mutable una string no

for element in comptadors: #recorremos una copia de los VALORES: el primer 0, el segundo 0,... pero NO los cambia.
    element +=1

print(comptadors) #no afageix ni modifica la llista. s'ha de recorrer la llista amb index. 



'''SÍ modifica comptadors
'''
for posicio in range(len(comptadors)): #recorremos las POSICIONES, y SÍ CAMBIA VALORES.
    comptadors[posicio] += 1 #comptadors[posicio] es el VALOR de comptadors en la posicio
print(comptadors) 



'''SÍ modifica comptadors
'''
resultat = []                #guardamos una lista vacia para GUARDAR el +1 del element del bucle for con un append, sino no se guarda element en la lista. 
for element in comptadors:   #recorremos una copia de los VALORES: el primer 0, el segundo 0,... pero NO los cambia.
    element +=1
    resultat.append(element) #append es solo para listas.
print(resultat)    



'''si volem modificar cadena: 
'''
cadena = "murder"
resultat = ""

for car in cadena:#bucle contador
    resultat += "a" 
print (cadena, resultat)   #aqui no se modifica cadena, resultat es aaaaa


