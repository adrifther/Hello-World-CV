'''Escriu una fx q accepta  una string i calcula el numero de majuscules i minuscules q apareixen a la cadena.
La funcio retornara una llista amb dos elements el numero de majuscules i minuscules'''

cadena_prueba =" Cadena Prova amb 3 Majuscules i 25 min"
todo_junto = cadena_prueba.replace(" ","")
lista_letras = list(todo_junto)

print (lista_letras)

def aparicions(cadena):

    
    todo_junto = cadena_prueba.replace(" ","")
    lista_letras = list(todo_junto)
    
    lista=[majuscules,minuscules]
    majuscules=0
    minuscules=0

    lista=[majuscules,minuscules]

    for letra in lista_letras:
        if letra.islower():
            minuscules+=1

        if letra.isupper():
            majuscules+=1    
    
    lista=[majuscules,minuscules]

    return lista


print(aparicions(cadena_prueba))