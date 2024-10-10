numero = int(input("Dona'm un número, amb 0 m'en vaig: "))

def factorial(numero):
    fact = 1
    for i in range(1, numero + 1):
        fact *= i
    return fact

contador = 0  # Contador de números leídos

while numero != 0:
    print(f"El factorial de {numero} és {factorial(numero)}")
    contador += 1
    numero = int(input("Dona'm un número, amb 0 m'en vaig: "))

print(f"Quantitat total de números llegits: {contador}")

