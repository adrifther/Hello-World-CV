import io 
import re

patro = re.compile("[A-Za-z0-9 \\-_]+")

arxiu = io.open("C:\\Users\\Alumne_mati1.EQUIPHECTOR\\Desktop\\Python\\10_02 Python\\workwork.csv","r",encoding="utf-8")

llistadecadenes = arxiu.readlines()

print(len(llistadecadenes))

matriz =[]
longituds=[]
for cadena in llistadecadenes[1:]: #nos cargamos la primera cadena que son los titulos

    matriz.append(patro.findall(cadena))
    if len(patro.findall(cadena)) != 20:
        longituds.append(len(patro.findall(cadena)))

#print(llistadecadenes[0])   #el encabezado

#print(matriz[1]) chivato para saber ha funcionado
