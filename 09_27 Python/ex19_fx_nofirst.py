'''19 Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb 
les mateixes cadenes sense el primer caràcter.
'''

def nofirst (x):
    resultat=[]
    for cadena in x:
        resultat.append(cadena[1:len(cadena)])
    return  resultat    

original = ["hola","com","estas", "pink","FLOYD"]

print(nofirst(original))    