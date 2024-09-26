import io
import re
import time
import pandas as pd

# Regular expression to match words (including accented characters)
patro = re.compile(r"(?<!\S)[a-zA-ZÀÈÌÒÙÁÉÍÓÚÏÜàèìòùáéíóúçÇïüñÑ\.]+(?!\S)")

# Reading input file
with io.open("C:\\Users\\admin\\Desktop\\quintoelemento.txt", "r", encoding="utf-8") as fitxer:
    llista_linies = fitxer.readlines()

# Collect all matches
totes = []
for linia in llista_linies:
    totes += patro.findall(linia)

# Getting unique words and counting occurrences
diferents = list(set(totes))
cuenta = [[paraula, totes.count(paraula)] for paraula in diferents]

# Create DataFrame
df = pd.DataFrame(cuenta, columns=['Palabra', 'Frecuencia'])

# Sort DataFrame by 'Frecuencia' in descending order
df_ordenado = df.sort_values(by='Frecuencia', ascending=False)

# Write DataFrame to a file (better formatting with to_string or to_csv)
with io.open("C:\\Users\\admin\\Desktop\\resultado.txt", "w", encoding="utf-8") as fitxer:
    fitxer.write(df_ordenado.to_string(index=False))
