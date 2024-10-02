import io 
import re

patro = re.compile('[A-Za-z0-9\\-":]+')

arxiu = io.open("C:\\Users\\Alumne_mati1.EQUIPHECTOR\\Desktop\\Python\\10_02 Python\\marvel_dc.csv","r",encoding="utf-8")

llistadecadenes = arxiu.readlines()

print(len(llistadecadenes))

matriz =[]
longituds=[]
for cadena in llistadecadenes[1:]: #nos cargamos la primera cadena que son los titulos


    matriz.append(patro.findall(cadena))
    longituds.append(len(patro.findall(cadena)))

    if '"' in cadena:
        "".join(cadena[]) 

print(f"El encabezado es: {llistadecadenes[0]}")   #el encabezado

print(f"El la primera matriz es: {matriz[0]}") #chivato para saber ha funcionado
