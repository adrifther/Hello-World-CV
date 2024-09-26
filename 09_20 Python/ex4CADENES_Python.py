'''4. Majúscules i minúscules (upper, lower, capitalize):
Escriu un programa que demani una frase a l'usuari. El programa ha de mostrar la frase 
en tres versions: totes les paraules en majúscula, en minúscules, i amb només la primera 
lletra en majúscula. 
Entrada: 'el gat menja peix' 
Sortida esperada: 
Frase amb majúscules: EL GAT MENJA PEIX 
Frase en minúscules: el gat menja peix 
Frase capitalitzada: El gat menja peix 
La frase estava originalment en minúscules. 
'''

entrada = input("dame una frase, la pondre en mayusculas minusculas y con la inicial mayuscula.")


print("Frase amb majúscules: "+ entrada.upper()) #frase mayuscula

print("Frase amb minúscules: "+ entrada.lower()) #frase minuscula

print("Frase capitalitzada: "+ entrada.capitalize()) #frase capitalitzada