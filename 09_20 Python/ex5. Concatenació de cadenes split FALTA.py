'''5. Concatenació de cadenes (''.join()):
Escriu un programa que demani a l'usuari una llista de paraules separades per comes i un 
símbol escollit per l'usuari per unir-les. 
Entrada: 'poma,plàtan,taronja', '@' 
Sortida esperada: 
poma@plàtan@taronja 
'''

entrada = input("dame una lista de palabras separadas por comas, y el símbolo escogido para unirlas ")
# Sol·licitem la llista de paraules i el símbol
paraules = input("Introdueix una llista de paraules separades per comes: ")
simbol = input("Introdueix un símbol per unir-les: ")

# Dividim la cadena de paraules utilitzant la coma com a separador
llista_paraules = paraules.split(',')

# Unim les paraules amb el símbol proporcionat
resultat = simbol.join(llista_paraules)

# Mostrem el resultat
print(resultat)

print(entrada.split("@")) # ex entrada: "Ana,23,Madrid,Luis,30,Barcelona,María,25,Sevilla" cadena.split(caràcter)