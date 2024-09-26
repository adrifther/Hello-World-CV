#ex2: 2. Operacions amb cadenes (+, *, \n):
'''
Escriu un programa que demani a l'usuari una frase i un número. El programa ha de 
concatenar la frase amb una versió repetida de la mateixa frase el número de vegades 
indicat, amb cada repetició en una línia nova. 
Entrada: 'Hola, món!', 3 
Sortida esperada: 
Hola, món!
Hola, món!
Hola, món!
'''

print("dame una frase")
frase_entrada = input()

print("dame un numero")
numero_entrada = int((input()))

print((frase_entrada+"\n")*numero_entrada)


#ex3 setmana1
'''
3. Cerca de caràcters (count, index, find):
Escriu un programa que demani una cadena i un caràcter. El programa ha de mostrar 
quantes vegades apareix el caràcter en la cadena, la seva primera aparició i la seva última 
aparició. 
Entrada:'supercalifragilistico', 'i' 
Sortida esperada: 
El caràcter 'i' apareix 3 vegades. 
La seva primera aparició és a la posició 7. 
La seva última aparició és a la posició 17.
'''

print("dame una cadena de texto: ")
cadena_texto = input()

print("dame un caracter de la cadena: ")
caracter = input()

for caracteres in cadena_texto:
    find
    print(caracteres.split())
    if caracter == caracteres.split()