import io
import re
import time
import pandas as pd


patro= re.compile("(?<!\\S)[a-zA-ZÀÈÌÒÙÁÉÍÓÚÏÜàèìòùáéíóúçÇïüñÑ\\.]+(?!\\S)")
fitxer = io.open("C:\\Users\\Alumne_mati1.EQUIPHECTOR\\Desktop\\quintoelemento.txt","r", encoding ="utf-8")
llista_linies = fitxer.readlines()
# llista_linies = [linia1, linia2, linia3,......]
fitxer.close()

fitxer =io.open("C:\\Users\\Alumne_mati1.EQUIPHECTOR\\Desktop\\resultado.txt","w",encoding="utf-8")

totes = []

for linia in llista_linies:
    
    totes += patro.findall(linia)

diferents = list(set(totes))

cuenta=[]
for paraula in diferents:

    cuenta.append([paraula, totes.count(paraula)])
    
# Configuració per mostrar totes les files i columnes
pd.set_option('display.max_rows', None)  # Mostrar totes les files
pd.set_option('display.max_columns', None)  # Mostrar totes les columnes
pd.set_option('display.expand_frame_repr', False)  # Evitar que es trenqui en múltiples línies
    

# Us del Pandas Suggerit per la Chattie
df = pd.DataFrame(cuenta, columns=['Palabra', 'Frecuencia'])

# Ordenar por la columna de 'Frecuencia' de mayor a menor
df_ordenado = df.sort_values(by='Frecuencia', ascending=False)

fitxer.write(str(df_ordenado))

fitxer.close()