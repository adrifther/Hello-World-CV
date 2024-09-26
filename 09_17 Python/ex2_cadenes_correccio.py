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

frase= input ("Entra Frase") + "\n"

repeticions = int (input("entra repeticions"))

# print(type(frase), type(repeticions))     para saber tipos datos

print(frase * repeticions)


#otra versión, mismo resultado:
entrada=input("escriu una frase: ")
repeticions = int(input("escriu un numero baix: "))
contador=0
while contador < repeticions:
    print(entrada)
    contador += 1

#otra versión, mismo resultado:
entrada=input("escriu una frase: ")
repeticions = int(input("escriu un numero baix: "))
while repeticions >0:
    print (entrada)
    repeticions -= 1


