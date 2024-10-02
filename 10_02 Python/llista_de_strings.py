lista_de_listas_a_splitear = ["2, 3, hola, 24, 34.000, hola2 \n",
"3,4  hola, 24, 54.000, hola3 \n","3,4, hola, 24, 54.000, hola3 \n"]


#def elimina_espais(llista_de_cadenes):

for cadena in lista_de_listas_a_splitear:

    lista_nueva = []

    lista_nueva = cadena.replace(" ","")

print(lista_nueva)

'''
        lista_nueva = cadena.replace(".","")
        
        lista_nueva = cadena.replace("\n","")

    return cadena.split(",")
    
print(elimina_espais(lista_de_listas_a_splitear))'''