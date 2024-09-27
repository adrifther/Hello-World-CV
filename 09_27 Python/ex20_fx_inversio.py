'''20. Funció que pren com a paràmetre una llista de cadenes i retorna una altra 
llista amb les mateixes cadenes invertides.'''


def inversion_cadena(c):
    resultat=''
    for char in c:
        resultat = char + resultat  #para invertir cadena #debug para ver como funciona
    return resultat


def lista_invertida(lista):
    
    invertida = []

    for cadena in lista:

           invertida.append(inversion_cadena(cadena))

    return(invertida)


original = ["hola","com","estas", "pink","FLOYD"]

print(lista_invertida(original))   

''''''
