import time

inicial = time.time()

llistastrings =[]

for contador in range (1000):
    llistastrings.append("2, 3, hola, 24, 34.000, hola2 \n")

resultat = []

for cadena in llistastrings:

    cadena = cadena.replace(" ","").replace(".","").replace("\n","").split(",")
    
    resultat.append(cadena)

final = time.time()

print(f"timepo total {final - inicial}")
