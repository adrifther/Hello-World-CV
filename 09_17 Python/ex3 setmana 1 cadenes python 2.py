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

texto = input("dame una CADENA, separalo por una COMA por el CARACTER que deseas buscar ")
cadena_y_caracter = texto.split(',') 
cadena= cadena_y_caracter[0] 
caracter= cadena_y_caracter[1]  
print(cadena)
print(caracter)
#frase= cadena.split() 
veces_repetida=0
for caracteres in cadena: 
    if caracter == caracteres: 
        veces_repetida+=1
       # veces_repetida = int(veces_repetida)
  

#print (veces_repetida)
print("el caracter " + caracter +" apareix "+ str(veces_repetida)  + " vegades")

