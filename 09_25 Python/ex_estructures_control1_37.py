#Ejercicio 2: Escriure els múltiples de 2 menors o iguals a 100

# Programa per escriure els múltiples de 2 menors o iguals a 100
for i in range(2, 101, 2):  # Bucle que itera des de 2 fins a 100 amb un increment de 2
    print(i)  # Mostra el valor de 'i', que és un múltiple de 2

'''
Explicació del codi:

1. `for i in range(2, 101, 2)`: Aquesta línia inicialitza un bucle que comença a 2, 
   finalitza a 100 (incloent-lo) i s'incrementa de 2 en 2. Això ens permet obtenir 
   només els múltiples de 2.

2. `print(i)`: Per cada iteració, es mostra el valor actual de 'i', que serà sempre 
   un múltiple de 2 degut al pas de 2 especificat al bucle 'range()'.

Aquest codi no és complicat, però la funció `range()` és important. Té tres paràmetres:
   - El primer és el valor inicial (2 en aquest cas).
   - El segon és el valor final, que és excloent en Python. Com volem incloure 100, es posa 101.
   - El tercer és el pas, que indica en quant s'incrementa 'i' a cada iteració.
'''
#Ejercicio 3: Escriure els 10 primers múltiples de 2
# Programa per escriure els 10 primers múltiples de 2
for i in range(1, 11):  # Bucle que itera de l'1 al 10
    print(i * 2)  # Multiplica 'i' per 2 i mostra el resultat

'''
Explicació del codi:

1. `for i in range(1, 11)`: Aquest bucle itera 10 vegades, des de l'1 fins al 10 (ambdues 
   incluses), que representa les 10 primeres iteracions.

2. `print(i * 2)`: Cada vegada que el bucle itera, es pren el valor actual de 'i' i es 
   multiplica per 2 per obtenir els múltiples de 2. El resultat es mostra per pantalla.

El concepte de `range()` és el mateix que a l'exercici anterior, però aquí només itera 
del 1 al 10, i a cada iteració es fa una operació de multiplicació.
'''
#Ejercicio 4: Escriure els n primers múltiples de m
# Programa per escriure els n primers múltiples de m
n = int(input("Introdueix el valor de n: "))  # Llegeix i converteix l'entrada de l'usuari a un enter
m = int(input("Introdueix el valor de m: "))  # Llegeix i converteix l'entrada de l'usuari a un enter

for i in range(1, n + 1):  # Bucle que itera des de l'1 fins a 'n' inclòs
    print(i * m)  # Multiplica 'i' per 'm' i mostra el resultat

'''
Explicació del codi:

1. `n = int(input("Introdueix el valor de n: "))`: L'usuari introdueix un valor que es converteix 
   a un enter, aquest valor representa quants múltiples volem escriure.

2. `m = int(input("Introdueix el valor de m: "))`: Igual que abans, però aquest valor representa 
   el número base pel qual multiplicarem (múltiple).

3. `for i in range(1, n + 1)`: Aquest bucle comença des de 1 i arriba fins a 'n' (inclusiu), on 'n' 
   és l'entrada de l'usuari.

4. `print(i * m)`: A cada iteració es multiplica 'i' per 'm' i es mostra el resultat.

El codi és simple, però combina la lectura de valors per teclat amb el bucle `for` per generar els múltiples.
'''
#Ejercicio 5: Validar una adreça IP

# Programa per validar si una adreça IP és correcta
ip = input("Introdueix una adreça IP: ")  # Llegeix una adreça IP de l'usuari

parts = ip.split('.')  # Divideix l'adreça IP en parts utilitzant el punt com a separador

if len(parts) == 4 and all(0 <= int(part) <= 255 for part in parts):  # Comprova que hi ha 4 parts i cada part és entre 0 i 255
    print(f"{ip} és una adreça IP vàlida.")  # Si totes les condicions es compleixen, mostra que l'adreça IP és vàlida
else:
    print(f"{ip} no és una adreça IP vàlida.")  # Si no es compleixen les condicions, mostra que l'adreça IP no és vàlida

'''
Explicació del codi:

1. `ip = input("Introdueix una adreça IP: ")`: Es demana a l'usuari que introdueixi una cadena, 
   que representa una adreça IP.

2. `parts = ip.split('.')`: Aquesta línia divideix l'adreça IP en quatre parts separades pel punt. 
   El resultat és una llista de cadenes.

3. `len(parts) == 4`: Es comprova que l'adreça IP té exactament 4 parts, com una IP vàlida.

4. `all(0 <= int(part) <= 255 for part in parts)`: Aquesta és una combinació de funcions:
   - `int(part)`: Converteix cada part de la IP a enter.
   - `0 <= int(part) <= 255`: Comprova que cada part està entre 0 i 255, que és el rang vàlid.
   - `all()`: Retorna True només si totes les condicions són certes per a cada part.

Si totes les condicions es compleixen, l'adreça és vàlida; si no, es declara com no vàlida.
'''

#Ejercicio 6: Sumar els múltiples de 2 menors a 100
# Programa per sumar els múltiples de 2 menors a 100
suma = sum(i for i in range(2, 100, 2))  # Suma tots els múltiples de 2 menors a 100
print(f"La suma dels múltiples de 2 menors a 100 és: {suma}")  # Mostra el resultat

'''
Explicació del codi:

1. `suma = sum(i for i in range(2, 100, 2))`: 
   - `range(2, 100, 2)`: Genera els múltiples de 2 menors a 100.
   - `sum()`: Suma tots els valors generats pel bucle.

2. `print(f"La suma dels múltiples de 2 menors a 100 és: {suma}")`: Aquesta línia simplement mostra el resultat de la suma.

Aquest codi és bastant eficient perquè utilitza una expressió generadora amb `range()` i la funció `sum()`.
'''


#Ejercicio 7: Escriure els múltiples de 3 menors o iguals a 100

# Programa per escriure els múltiples de 3 menors o iguals a 100
for i in range(3, 101, 3):  # Bucle que itera des de 3 fins a 100, amb increment de 3
    print(i)  # Mostra cada múltiple de 3

'''
Explicació del codi:

1. `for i in range(3, 101, 3)`: Aquest bucle comença a 3 i augmenta en 3 a cada iteració, mostrant només els múltiples de 3 fins a 100.

2. `print(i)`: A cada iteració, es mostra el múltiple de 3 que ha estat generat.

Aquest codi segueix la mateixa lògica que els exercicis anteriors amb els múltiples, però amb 3 en lloc de 2.
'''
#Ejercicio 8: Escriure els n primers múltiples de m on n és llegit per teclat

# Programa per escriure els n primers múltiples de m
n = int(input("Introdueix el valor de n: "))  # Llegeix el nombre de múltiples que es volen
m = int(input("Introdueix el valor de m: "))  # Llegeix el número base per als múltiples

for i in range(1, n + 1):  # Bucle que itera de 1 a n
    print(i * m)  # Mostra el múltiple de 'm' per cada valor de 'i'

'''
Explicació del codi:

1. `n = int(input(...))` i `m = int(input(...))`: Aquí s'obtenen els valors de l'usuari per definir quants múltiples es volen i quin és el número base.

2. `for i in range(1, n + 1)`: Aquest bucle genera els primers 'n' nombres i els multiplica per 'm'.

3. `print(i * m)`: En cada iteració, es multiplica 'i' per 'm' i es mostra el resultat.

El programa permet personalitzar tant el nombre de múltiples com el número base.
'''


#Ejercicio 9: Calcular la suma de tots els números fins a n

# Programa per calcular la suma de tots els números fins a n
n = int(input("Introdueix un número: "))  # Llegeix un número enter de l'usuari
suma = sum(range(1, n + 1))  # Suma tots els números des de 1 fins a n
print(f"La suma de tots els números fins a {n} és {suma}")  # Mostra el resultat

'''
Explicació del codi:

1. `n = int(input(...))`: Es demana a l'usuari que introdueixi un número, que es convertirà en enter.

2. `sum(range(1, n + 1))`: Aquesta funció utilitza `range()` per generar una seqüència de nombres des de 1 fins a 'n' i després els suma tots amb la funció `sum()`.

3. `print(f"...")`: Finalment, es mostra el resultat de la suma en format clar.

Aquest codi utilitza `sum()` de manera eficient per sumar ràpidament una sèrie de nombres.
'''
#Ejercicio 10: Determinar si un nombre és parell o senar

# Programa per determinar si un nombre és parell o senar
n = int(input("Introdueix un número: "))  # Llegeix un número enter de l'usuari

if n % 2 == 0:  # Comprova si el residu de dividir per 2 és 0 (parell)
    print(f"{n} és un número parell")  # Si és parell, mostra aquest missatge
else:
    print(f"{n} és un número senar")  # Si no és parell, és senar, i es mostra aquest missatge

'''
Explicació del codi:

1. `n = int(input(...))`: Es llegeix el número introduït per l'usuari.

2. `if n % 2 == 0`: Aquesta línia fa ús de l'operador de mòdul `%` per comprovar si el número és divisible per 2. Si el residu és 0, el número és parell.

3. `else`: Si el residu no és 0, es tracta d'un número senar.

El codi utilitza una estructura condicional bàsica per diferenciar números parells de senars.
'''

#Ejercicio 11: Escriure els múltiples de 5 menors o iguals a 100
# Programa per escriure els múltiples de 5 menors o iguals a 100
for i in range(5, 101, 5):  # Bucle que itera des de 5 fins a 100, amb increment de 5
    print(i)  # Mostra cada múltiple de 5

'''
Explicació del codi:

1. `for i in range(5, 101, 5)`: Aquest bucle comença a 5 i augmenta en 5 a cada iteració fins a arribar a 100.

2. `print(i)`: A cada iteració es mostra el múltiple de 5.

És el mateix principi que amb els altres exercicis de múltiples, simplement canviant el valor de 5.
'''
#Ejercicio 12: Escriure tots els nombres primers menors o iguals a n

# Programa per escriure tots els nombres primers menors o iguals a n
def es_primer(num):  # Defineix una funció que comprova si un número és primer
    if num < 2:  # Si el número és menor que 2, no és primer
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Comprova divisors fins a l'arrel quadrada del número
        if num % i == 0:  # Si es troba un divisor, no és primer
            return False
    return True  # Si no es troba cap divisor, és primer

n = int(input("Introdueix un número: "))  # Llegeix el valor de n de l'usuari

for i in range(2, n + 1):  # Bucle que itera des de 2 fins a n
    if es_primer(i):  # Comprova si 'i' és primer
        print(i)  # Si 'i' és primer, el mostra

'''
Explicació del codi:

1. `def es_primer(num)`: Aquesta funció comprova si un número és primer. 
   - Comença descartant qualsevol número menor que 2, ja que aquests no són primers.
   - Després, utilitza un bucle per comprovar si el número té divisors menors o iguals a la seva arrel quadrada, perquè els divisors majors ja s'haurien detectat.

2. `for i in range(2, n + 1)`: Es genera un bucle que recorre tots els nombres de 2 a 'n' i comprova si són primers utilitzant la funció `es_primer()`.

3. `print(i)`: Si es troba que 'i' és primer, es mostra per pantalla.

El codi implementa una manera eficient de comprovar la primalitat d'un número, limitant els possibles divisors fins a l'arrel quadrada.
'''

 
#Ejercicio 13: Escriure els nombres de n fins a 1
 
# Programa per escriure els nombres de n fins a 1
n = int(input("Introdueix un número: "))  # Llegeix el valor de n de l'usuari

for i in range(n, 0, -1):  # Bucle que itera des de n fins a 1, amb decrement de 1
    print(i)  # Mostra cada número en ordre decreixent

'''
Explicació del codi:

1. `n = int(input(...))`: Demana a l'usuari que introdueixi un número sencer.

2. `for i in range(n, 0, -1)`: El bucle comença amb el valor de 'n' i decreix fins a 1, mostrant cada número a mesura que avança.

3. `print(i)`: A cada iteració, es mostra el número actual.

Això crea un compte enrere des del número 'n' fins a 1.
'''


#Ejercicio 14: Calcular el factorial d'un número

# Programa per calcular el factorial d'un número
n = int(input("Introdueix un número: "))  # Llegeix el valor de n de l'usuari
factorial = 1  # Inicialitza el factorial a 1

for i in range(1, n + 1):  # Bucle que itera des de 1 fins a n
    factorial *= i  # Multiplica el valor actual del factorial per 'i'

print(f"El factorial de {n} és {factorial}")  # Mostra el resultat

'''
Explicació del codi:

1. `n = int(input(...))`: Demana a l'usuari que introdueixi un número sencer.

2. `factorial = 1`: Inicialitzem la variable 'factorial' a 1 perquè multiplicarem progressivament els valors.

3. `for i in range(1, n + 1)`: Aquest bucle recorre els nombres des de 1 fins a 'n', multiplicant el valor actual de 'factorial' per cada valor de 'i'.

4. `factorial *= i`: Aquesta operació multiplica 'factorial' pel valor actual de 'i' i guarda el resultat.

5. `print(...)`: Al final, es mostra el factorial del número introduït.

Aquesta implementació del factorial segueix el concepte matemàtic estàndard de multiplicar tots els nombres des de 1 fins a 'n'.
'''


#Ejercicio 15: Calcular la suma de tots els nombres parells fins a n

# Programa per calcular la suma de tots els nombres parells fins a n
n = int(input("Introdueix un número: "))  # Llegeix el valor de n de l'usuari
suma = sum(range(2, n + 1, 2))  # Suma tots els nombres parells des de 2 fins a n
print(f"La suma de tots els nombres parells fins a {n} és {suma}")  # Mostra el resultat

'''
Explicació del codi:

1. `n = int(input(...))`: Demana a l'usuari que introdueixi un número sencer.

2. `sum(range(2, n + 1, 2))`: Aquí fem servir `range()` per generar només els nombres parells des de 2 fins a 'n'. La funció `sum()` els suma tots i retorna el resultat.

3. `print(...)`: Finalment, es mostra el resultat de la suma de tots els nombres parells.

El codi utilitza una solució ràpida i eficient gràcies a la funció `sum()` i la seqüència de nombres parells generada per `range()`.
'''


#Ejercicio 16: Comprovar si un número és primer
# Programa per comprovar si un número és primer
n = int(input("Introdueix un número: "))  # Llegeix el valor de n de l'usuari

def es_primer(num):  # Defineix una funció que comprova si un número és primer
    if num < 2:  # Si el número és menor que 2, no és primer
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Comprova divisors fins a l'arrel quadrada del número
        if num % i == 0:  # Si es troba un divisor, no és primer
            return False
    return True  # Si no es troba cap divisor, és primer

if es_primer(n):  # Comprova si 'n' és primer
    print(f"{n} és un número primer")  # Si 'n' és primer, mostra aquest missatge
else:
    print(f"{n} no és un número primer")  # Si 'n' no és primer, mostra aquest missatge

'''
Explicació del codi:

1. `def es_primer(num)`: Aquesta funció comprova si un número és primer. 
   - Rebutja els números menors que 2.
   - Utilitza un bucle que recorre els divisors fins a l'arrel quadrada del número, ja que un divisor més gran ja hauria estat detectat.

2. `if es_primer(n)`: Si la funció retorna `True`, significa que 'n' és primer i es mostra el missatge corresponent.

El codi ofereix una manera eficient de comprovar si un número és primer, limitant els possibles divisors.
'''


#Ejercicio 17: Escriure els múltiples de 7 menors o iguals a 100
# Programa per escriure els múltiples de 7 menors o iguals a 100
for i in range(7, 101, 7):  # Bucle que itera des de 7 fins a 100, amb increment de 7
    print(i)  # Mostra cada múltiple de 7

'''
Explicació del codi:

1. `for i in range(7, 101, 7)`: Aquest bucle comença a 7 i augmenta en 7 a cada iteració, mostrant els múltiples de 7 fins a 100.

2. `print(i)`: Mostra cada múltiple de 7 durant cada iteració.

El codi segueix la mateixa lògica que els altres exercicis de múltiples, simplement canviant el valor de 7.
'''

#Ejercicio 18: Escriure un programa que demani N números i en digui quin és el més gran i el més petit i la seva posició

# Programa que demana N números i diu quin és el més gran, el més petit i la seva posició
n = int(input("Quants números vols introduir? "))  # Llegeix el nombre de números a introduir
numeros = []  # Crea una llista buida per emmagatzemar els números

for i in range(n):  # Bucle per recollir els números
    num = int(input(f"Introdueix el número {i + 1}: "))  # Llegeix cada número
    numeros.append(num)  # Afegeix cada número a la llista

max_num = max(numeros)  # Troba el número més gran
min_num = min(numeros)  # Troba el número més petit
max_pos = numeros.index(max_num) + 1  # Troba la posició del número més gran
min_pos = numeros.index(min_num) + 1  # Troba la posició del número més petit

print(f"El número més gran és {max_num} a la posició {max_pos}")
print(f"El número més petit és {min_num} a la posició {min_pos}")

'''
Explicació del codi:

1. `numeros = []`: S'inicialitza una llista buida per emmagatzemar els números introduïts per l'usuari.

2. `for i in range(n)`: Aquest bucle s'executa 'n' vegades per recollir els números.

3. `max(numeros)` i `min(numeros)`: Utilitzem aquestes funcions per trobar els números més gran i més petit de la llista.

4. `numeros.index(...)`: Aquesta funció retorna la posició del número més gran o més petit, i s'afegeix +1 perquè l'index comença en 0.
'''


#Ejercicio 19: Calcula el factorial d'un número (n!)
# Programa que calcula el factorial d'un número
n = int(input("Introdueix un número: "))  # Llegeix el número de l'usuari
factorial = 1  # Inicialitza el factorial a 1

for i in range(1, n + 1):  # Bucle que recorre els números des de 1 fins a n
    factorial *= i  # Multiplica cada número pel factorial

print(f"El factorial de {n} és {factorial}")  # Mostra el resultat

'''
Explicació del codi:

1. `factorial *= i`: A cada iteració, el valor de 'factorial' es multiplica pel valor de 'i', acumulant així el producte de tots els nombres fins a 'n'.

Aquest codi segueix l'algorisme clàssic per calcular el factorial d'un número.
'''

#Ejercicio 20: Taula de multiplicar d'un número introduït per l'usuari
# Programa que mostra la taula de multiplicar d'un número
n = int(input("Dóna'm un número: "))  # Llegeix el número de l'usuari

for i in range(1, 11):  # Bucle que recorre els nombres de l'1 al 10
    print(f"{n} x {i} = {n * i}")  # Mostra la multiplicació

'''
Explicació del codi:

1. `for i in range(1, 11)`: Aquest bucle genera els nombres de l'1 al 10.

2. `print(f"{n} x {i} = {n * i}")`: A cada iteració, es calcula la multiplicació de 'n' pel valor actual de 'i' i es mostra el resultat.
'''

#Ejercicio 21: Desglossament en bitllets i monedes d'una quantitat sencera d'euros
# Programa que desglossa una quantitat d'euros en bitllets i monedes
quantitat = int(input("Introdueix una quantitat d'euros: "))  # Llegeix la quantitat d'euros

bitllets = [500, 200, 100, 50, 20, 10, 5]  # Llista de bitllets
monedes = [2, 1]  # Llista de monedes

for bitllet in bitllets:  # Bucle per recórrer els bitllets
    if quantitat >= bitllet:  # Comprova si la quantitat és major o igual al bitllet
        num_bitllets = quantitat // bitllet  # Calcula quants bitllets d'aquell valor es poden donar
        quantitat %= bitllet  # Actualitza la quantitat restant
        print(f"{num_bitllets} bitllet(s) de {bitllet}€")  # Mostra el nombre de bitllets

for moneda in monedes:  # Bucle per recórrer les monedes
    if quantitat >= moneda:  # Comprova si la quantitat és major o igual a la moneda
        num_monedes = quantitat // moneda  # Calcula quantes monedes es poden donar
        quantitat %= moneda  # Actualitza la quantitat restant
        print(f"{num_monedes} moneda(es) de {moneda}€")  # Mostra el nombre de monedes

'''
Explicació del codi:

1. `for bitllet in bitllets`: Aquest bucle recorre cada valor de bitllet a la llista de bitllets disponibles.

2. `quantitat // bitllet`: Aquí dividim la quantitat per obtenir el nombre de bitllets que es poden donar.

3. `quantitat %= bitllet`: Després de donar els bitllets, actualitzem la quantitat restant.

Aquest mateix procés es repeteix per a les monedes.
'''


#Ejercicio 22: Mostrar els números parells compresos entre 0 i 200 (ambdós inclosos)
# Programa que mostra els números parells compresos entre 0 i 200
for i in range(0, 201, 2):  # Bucle que recorre els nombres de 0 a 200 amb increment de 2
    print(i)  # Mostra cada número parell

'''
Explicació del codi:

1. `for i in range(0, 201, 2)`: Utilitzem un bucle que comença a 0 i va sumant 2 a cada iteració, mostrant només els números parells.

Això garanteix que es mostrin tots els números parells entre 0 i 200.
'''

#Ejercicio 23: Mostrar els números parells positius entre 2 i un número qualsevol que introdueixi l'usuari per teclat
# Programa que mostra els números parells positius entre 2 i un número introduït per l'usuari
limite = int(input("Introdueix un número: "))  # Llegeix el número màxim introduït per l'usuari

for i in range(2, limite + 1, 2):  # Bucle que recorre des del 2 fins al número introduït, amb increments de 2
    print(i)  # Mostra cada número parell

'''
Explicació del codi:

1. `range(2, limite + 1, 2)`: Aquest bucle comença des de 2 i s'incrementa de 2 en 2 fins a arribar al número màxim introduït per l'usuari.

Aquest mètode ens assegura que només es mostren els números parells entre 2 i el número indicat.
'''

#Ejercicio 24: Sumar els quadrats de dos nombres introduïts per l'usuari
# Programa que suma els quadrats de dos nombres introduïts per l'usuari
n = int(input("Introdueix el primer número: "))  # Llegeix el primer número
m = int(input("Introdueix el segon número: "))  # Llegeix el segon número

suma_quadrats = n**2 + m**2  # Calcula la suma dels quadrats dels dos números
print(f"La suma dels quadrats de {n} i {m} és {suma_quadrats}")  # Mostra el resultat

'''
Explicació del codi:

1. `n**2 + m**2`: Aquí es calculen els quadrats de 'n' i 'm', i es sumen en la mateixa línia.

Aquest procés és senzill: simplement s'eleven els números al quadrat i es fa la suma.
'''
#Ejercicio 25: Determinar si un número és primer
# Programa que comprova si un número és primer
n = int(input("Introdueix un número: "))  # Llegeix el número introduït per l'usuari

es_primer = True  # Inicialitzem una variable booleana que assumeix que el número és primer

if n <= 1:  # Si el número és menor o igual a 1, no és primer
    es_primer = False
else:
    for i in range(2, int(n ** 0.5) + 1):  # Bucle que va des de 2 fins a la arrel quadrada de n
        if n % i == 0:  # Si el número és divisible per qualsevol valor en aquest interval, no és primer
            es_primer = False
            break  # Sortim del bucle

if es_primer:
    print(f"{n} és un número primer")
else:
    print(f"{n} no és un número primer")

'''
Explicació del codi:

1. `for i in range(2, int(n ** 0.5) + 1)`: Aquest bucle només comprova divisors fins a la arrel quadrada de 'n'. És un truc d'optimització per millorar l'eficiència.

2. `n % i == 0`: Si 'n' és divisible per 'i' sense residu, això vol dir que no és un número primer, i es marca com a tal.
'''


#Ejercicio 26: Mostrar els números primers menors que un número introduït per l'usuari
# Programa que mostra tots els números primers menors que el número introduït per l'usuari
limite = int(input("Introdueix un número: "))  # Llegeix el número límit introduït per l'usuari

def es_primer(n):  # Funció per comprovar si un número és primer
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Bucle que va fins a l'arrel quadrada de 'n'
        if n % i == 0:
            return False  # Retorna False si no és primer
    return True  # Retorna True si és primer

for i in range(2, limite):  # Bucle que recorre tots els números fins al límit
    if es_primer(i):  # Comprova si el número és primer
        print(i)  # Si ho és, el mostra

'''
Explicació del codi:

1. `es_primer(n)`: Aquesta funció comprova si un número és primer, utilitzant el mateix enfocament que l'exercici anterior.

2. `for i in range(2, limite)`: Aquest bucle recorre tots els números des del 2 fins a un menys del número introduït.
'''
#Ejercicio 27: Calcular el màxim comú divisor (MCD) de dos nombres
# Programa que calcula el màxim comú divisor (MCD) de dos nombres
n = int(input("Introdueix el primer número: "))  # Llegeix el primer número
m = int(input("Introdueix el segon número: "))  # Llegeix el segon número

def mcd(a, b):  # Funció que calcula el MCD
    while b != 0:  # Bucle que es repeteix fins que b sigui 0
        a, b = b, a % b  # Algorisme d'Euclides per trobar el MCD
    return a  # Retorna el MCD

resultat = mcd(n, m)  # Calcula el MCD dels dos números
print(f"El MCD de {n} i {m} és {resultat}")  # Mostra el resultat

'''
Explicació del codi:

1. `while b != 0`: Aquest bucle utilitza l'algorisme d'Euclides per calcular el MCD. Es repeteix fins que 'b' és 0.

2. `a, b = b, a % b`: A cada iteració, assignem el valor de 'b' a 'a', i 'a % b' a 'b'. Quan 'b' arriba a 0, 'a' conté el MCD.
'''

#Ejercicio 28: Llegeix els minuts i els segons i realitza un compte enrere
import time  # Importem el mòdul 'time' per a la pausa en el compte enrere

# Programa que llegeix els minuts i els segons i fa un compte enrere
minuts = int(input("Introdueix els minuts: "))  # Llegeix els minuts
segons = int(input("Introdueix els segons: "))  # Llegeix els segons

# Convertim tot a segons per simplificar el compte enrere
temps_total = minuts * 60 + segons  # Converteix el temps total a segons

while temps_total > 0:  # Bucle que fa el compte enrere mentre hi hagi temps
    mins, secs = divmod(temps_total, 60)  # Divideix el temps restant en minuts i segons
    print(f"{mins:02}:{secs:02}")  # Mostra el temps en format mm:ss
    time.sleep(1)  # Pausa d'1 segon
    temps_total -= 1  # Resta 1 segon al temps total

print("Compte enrere finalitzat!")  # Missatge quan acaba el compte enrere

'''
Explicació del codi:

1. `divmod(temps_total, 60)`: Aquesta funció divideix 'temps_total' per 60, retornant minuts i segons com a resultat.

2. `time.sleep(1)`: Pausa el programa durant un segon abans de continuar amb el següent bucle.
'''

#Ejercicio 29: Llegeix un nombre sencer i escriu el nombre de xifres que té
# Programa que calcula el nombre de xifres d'un número sencer
num = int(input("Introdueix un número sencer: "))  # Llegeix el número sencer

# Converteix el número a una cadena i compta els seus caràcters
num_digits = len(str(abs(num)))  # Utilitzem 'abs' per eliminar el signe negatiu si n'hi ha

print(f"El número {num} té {num_digits} xifres")  # Mostra el nombre de xifres

'''
Explicació del codi:

1. `len(str(abs(num)))`: Converteix el número a una cadena (string) i després compta el nombre de caràcters. 'abs' s'assegura que es compten correctament els números negatius.
'''


#Ejercicio 30: Llegeix un nombre sencer positiu i escriu la suma de les seves xifres
# Programa que suma les xifres d'un número sencer positiu
num = int(input("Introdueix un número sencer positiu: "))  # Llegeix el número sencer positiu

# Converteix el número a una cadena i suma les xifres
suma_xifres = sum(int(digit) for digit in str(num))  # Itera sobre cada xifra i la suma

print(f"La suma de les xifres de {num} és {suma_xifres}")  # Mostra la suma de les xifres

'''
Explicació del codi:

1. `sum(int(digit) for digit in str(num))`: Converteix el número en una cadena, itera per cada caràcter, el converteix en enter i els suma tots.
'''

#Ejercicio 31: Seguiment del bucle
# Seguiment d'un bucle simple
i = 0  # Inicialitza la variable i a 0

while i <= 3:  # Comença un bucle mentre i sigui menor o igual a 3
    print(i)  # Mostra el valor de i
    i += 1  # Incrementa i en 1 a cada iteració

print("Hecho")  # Mostra el missatge "Hecho" quan acaba el bucle

'''
Explicació del codi:

1. `while i <= 3`: Aquest bucle s'executa mentre i sigui menor o igual a 3.

2. `i += 1`: Incrementa el valor de 'i' a cada iteració, fins que supera el valor límit.
'''


#Ejercicio 32: Seguiment del bucle amb canvi de línia final
# Seguiment d'un bucle amb missatge final
i = 0  # Inicialitza la variable i a 0

while i <= 3:  # Comença un bucle mentre i sigui menor o igual a 3
    print(i)  # Mostra el valor de i
    i += 1  # Incrementa i en 1 a cada iteració

print("Hecho")  # Mostra el missatge "Hecho" quan acaba el bucle

'''
Explicació del codi:

Aquest és un exemple senzill d'un bucle que mostra valors de 0 a 3. El missatge "Hecho" es mostra després que acabi el bucle.
'''

#Ejercicio 33: Seguiment d'un bucle que incrementa i en 2
# Seguiment d'un bucle que incrementa 'i' en 2
i = 0  # Inicialitza la variable i a 0

while i <= 3:  # Comença un bucle mentre i sigui menor o igual a 3
    print(i)  # Mostra el valor de i
    i += 2  # Incrementa i en 2 a cada iteració

print("Hecho")  # Mostra el missatge "Hecho" quan acaba el bucle

'''
Explicació del codi:

1. `i += 2`: Aquesta línia incrementa el valor de 'i' en 2 a cada iteració del bucle.
'''

#Ejercicio 34: Seguiment d'un bucle amb increment dins del bucle
# Seguiment d'un bucle que incrementa dins del bucle
i = 0  # Inicialitza la variable i a 0

while i <= 3:  # Comença un bucle mentre i sigui menor o igual a 3
    i += 2  # Incrementa i en 2 al començament del bucle
    print(i)  # Mostra el valor de i

print("Hecho")  # Mostra el missatge "Hecho" quan acaba el bucle

'''
Explicació del codi:

1. `i += 2`: L'increment de 'i' passa abans de la impressió, per tant, el primer valor mostrat serà 2, no 0.
'''


#Ejercicio 35: Seguiment d'un bucle amb multiplicació per 2
# Seguiment d'un bucle que multiplica per 2
i = 1  # Inicialitza la variable i a 1

while i < 100:  # Comença un bucle mentre i sigui menor que 100
    i *= 2  # Multiplica i per 2 a cada iteració
    print(i)  # Mostra el valor de i

'''
Explicació del codi:

1. `i *= 2`: A cada iteració, el valor de 'i' es multiplica per 2, creant una progressió geomètrica.
'''
#Ejercicio 36: Seguiment d'un bucle que no s'executa
# Seguiment d'un bucle que no s'executa
i = 10  # Inicialitza la variable i a 10

while i < 2:  # El bucle no s'executa perquè la condició no es compleix
    i *= 2  # Multiplica i per 2 (no s'executa mai)
    print(i)  # No es mostra res, perquè el bucle no s'executa

'''
Explicació del codi:

1. `while i < 2`: Aquesta condició és falsa des del principi, per tant, el bucle mai s'executa.
'''


#Ejercicio 37: Seguiment per a diferents valors de i
# Seguiment d'un bucle per a diferents valors de 'i'
i = int(input("Valor inicial: "))  # Llegeix el valor inicial de 'i'

while i < 10:  # Bucle que s'executa mentre i sigui menor que 10
    print(i)  # Mostra el valor de i
    i += 1  # Incrementa i en 1 a cada iteració

print("Hecho")  # Mostra el missatge "Hecho" quan acaba el bucle

'''
Explicació del codi:

1. Si 'i' és major o igual a 10, el bucle no s'executa.

2. Si 'i' és negativa, el bucle s'executarà fins que 'i' arribi a 10.

3. `i += 1`: Incrementa el valor de 'i' en 1 a cada iteració.
'''

