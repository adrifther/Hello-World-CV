'''llista de strings que volem eliminar:espais,el . de milers, el \n
I obtenim camps separats per comes
'''
lista_de_listas_a_splitear = ["2, 3, hola, 24, 34.000, hola2 \n",
"3,4  hola, 24, 54.000, hola3 \n",
"3,4, hola, 24, 54.000, hola3 \n"]

'''primer fem una cadena normal'''
#versio1
cadena ="2, 3, hola, 24, 34.000, hola2 \n"
 #cadena = cadena.replace(" ","").replace(".","").replace("\n","").split(",")

'''O'''

#versio2
def string_to_list(cadena):
    for caracter in " .\n":                   # para estos caracteres " " "." \n
        cadena = cadena.replace(caracter,"")
    cadena = cadena.split(",")
    return cadena

'''ahora con listas de strings'''

lista_de_listas_a_splitear = ["2, 3, hola, 24, 34.000, hola2 \n",
"3,4  hola, 24, 54.000, hola3 \n",
"3,4, hola, 24, 54.000, hola3 \n"]

resultat= []

for cadena in lista_de_listas_a_splitear:
    resultat.append(string_to_list(cadena))
print(resultat)    