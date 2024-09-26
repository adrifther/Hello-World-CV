'''donat un nombre enter, escriu un programa 
que mostri un missatge q indiqui si el nombre es
 positiu 
 negatiu o 
 zero. 
 Només una opció de les 3 és certa.
'''
#control de entrada sin regex 
# try:           intenta algo 
#     break      si es correcto sigue a linea 20 (rompe el bucle). Si no hay break y es cierto: bucle infinito, cuidado! break rompe bucles try y for.
# except:        si hay error viene aquí y hace lo que le digas aqui
while True:
    try:
        numero=int(input("Escriu un número: "))
        break # rompe bucles try y for si la entrada es correcta. 
    
    except ValueError:  #Si se introduce un valor no numérico, se lanza la excepción
        print("Entrada Erronia, torna-hi, el numero es sencer?")
    
    except TypeError: 
        print("No es pot concatenar numero i text")

numero = int(input("dime un numero: "))

if numero > 0:
    print(f"el numero {numero} es positivo")

elif numero == 0:
    print(f"el numero {numero} es 0")

else:
    print(f"No queda más remedio que el numero {numero} sea negativo")    
