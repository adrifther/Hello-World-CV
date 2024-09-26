import io
import re
import time

patro = re.compile("(?<!\\S)[a-zA-ZÀèÌÒÙÁÉÍÓÚàèìòùáéíóúçÇïüñÑ\\.]+(?!\\S)")
fitxer: = io.open("C:\\_____________.txt", "r", encoding= "utf-8")
llista_linies = fitxer.readlines()

#llista_linies =[linia1, linia2...]

totes=[]

for linia in llista_linies:

    totes+= patro.findall(linia)

diferents= list(set(totes))    

cuenta =  []

for paraula in diferents:

    cuenta.append([paraula, totes.count(paraula)])

