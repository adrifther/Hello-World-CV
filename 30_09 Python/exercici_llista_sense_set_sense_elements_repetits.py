llista=[4,4,4,1,1,1,2,3,4,4,4,5]


#versio1
lista_final=[]
for elemento in range (len(llista)):
    if elemento in llista:
        lista_final.append(elemento)
print (lista_final)    

#versio2
resultat=[]
[resultat.append(element) for element in llista if element not in resultat]
print(f"versio2 amb comprehension lists: {resultat}")