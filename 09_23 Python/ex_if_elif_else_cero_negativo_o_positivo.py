import re

patro = re.compile(r"(?<!\S)-?[0-9]+(?!\S)")
patro = re.compile("(?<!\\S)-?[0-9]+(?!\\S)") # es lo mismo 
#print(patro.findall(entrada)) 
#chivato para saber el patrón que encuentra. no avanzar a partir de aqui a no ser que se tenga el patron claro

entrada = (input("Escriu un número: "))

while len(patro.findall(entrada)) != 1: #si entrem -13.52 per exemple o 1,123 no l'agafa

    entrada = (input("Escriu un número: "))

numero = patro.findall(entrada)[0]

if numero == "0":

    print(f" el número que has escrit és {numero} i té un valor de 0")

elif numero.isdigit():

    print(f" El nombre {numero} és positiu")

else:

    print(f"El nombre {numero} és negatiu")