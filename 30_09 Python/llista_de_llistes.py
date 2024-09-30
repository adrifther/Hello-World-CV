'''Despres de passar pel codi, tindrem la llista amb tots els elements incrementats amb '''
'''csv. excel'''

#versió 1: amb funcio i for
matriu =[[2,5,10],
         [6,7,9],
         [4,5,10]]

llista_mes_1= []

def incremento(fila):
    resultado=[]
    for columna in fila:
        resultado.append(columna+1)    
    return resultado

resultat = []
for fila in matriu:
   # print(fila)
    resultat.append(incremento(fila))

print(f"versio 1: {resultat}")


#versió2: amb dos for
'''utilitzar rangs'''
matriu2 =[[1,2,3],
         [4,5,6],
         [7,8,9]]

for element in matriu2:
    
    for posicion in range(len(element)):
   
        element[posicion] += 1

print(f"versio 2: {matriu2}")

#versió3: 
''''''


llista_mes_1= []

def incremento(fila):
    return [element +1 for element in fila] #LIST COMPREHENSION: equivale al bucle for

matriu =[[2,5,10],
         [6,7,9],
         [4,5,10]]

resultat= [incremento(fila) for fila in matriu]    

print(f"versio 3: {resultat}")

#List comprehension sólo sirve con listas y retorna lista:
'''LIST COMPREHENSION: 
A) es lo mismo que B).
A)
resultat =[]
for element in llista:
	resultat.append(element**2)
B)
resultat=[element**2 for element in llista]
'''