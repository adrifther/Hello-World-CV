'''implementar un programa que soliciti numeros a l usuari entrats un per un fins que ingressi 0. 
al final el programa mostrara cada numero i al costat la suma dels seus digits.
el zero no cala presentar lo (el programa contindra una funcio que realitzara i retornara la suma dels d igits d un numero)'''

def suma_digitos(numero):
    suma = 0
    for digito in str(numero):  # Convertim a cadena x iterar
        suma += int(digito)  # Convertim a int x operar
    return suma


numero = int(input("Dona'm un número, amb 0 m'en vaig: "))
numeros_llegits = []

while numero != 0:
    numeros_llegits.append(numero)
    numero = int(input("Dona'm un número, amb 0 m'en vaig: "))

# Mostrar cada número y la suma de sus dígitos
for num in numeros_llegits:
    print(f"La suma de dígits de {num} és {suma_digitos(num)}")