'''llista de strings que volem eliminar:espais,el . de milers, el \n
I obtenim camps separats per comes
'''
llistastrings = ["2, 3, hola, 24, 34.000, hola2 \n",
"3,4  hola, 24, 54.000, hola3 \n",
"3,4, hola, 24, 54.000, hola3 \n"]

resultat = []

for cadena in llistastrings:

    for caracter in " .\n":

        cadena = cadena.replace(caracter,"")

    cadena = cadena.split(",")    

    resultat.append(cadena)
    
print (llistastrings)    


'''equival al list comprehension_: '''
resultat = [cadena.replace(" ", "").replace(".","").replace("\n", "").split(",") for cadena in llistastrings]

print(resultat)