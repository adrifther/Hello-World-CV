'''
11. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb la
longitud de cadascuna de les cadenes que formen la llista.
'''

def longitud(l):
    resultat=[]
    for cadena in l:
        resultat.append(len(cadena))
    return resultat    


original =["akjdshf", "kjdsf","asd"]
digits=longitud(original)

print(original)
print(digits)

