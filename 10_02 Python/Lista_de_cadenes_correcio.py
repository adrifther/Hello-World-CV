'''llista de strings que volem eliminar:
espais
el . de milers
el \n

'''

lista_de_listas_a_splitear = ["2, 3, hola, 24, 34.000, hola2 \n",
"3,4  hola, 24, 54.000, hola3 \n","3,4, hola, 24, 54.000, hola3 \n"]
import time 

import re

patro = "[a-z0-9\\.]+"

patro = re.compile("[a-z0-9\\.]+")

llistastrings = []

for contador in range(100000):

    llistastrings.append("2, 3, hola, 24, 34.000, hola2 \n")

inicial = time.time()

resultat=[]

for cadena in llistastrings:
    resultat.append(patro.findall(cadena))


final = time.time()

print(f"tiempototal{final-inicial}")