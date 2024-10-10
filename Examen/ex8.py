'''ex8
Escriu una funcio de python per comprovar si una cadena es un pangrama o no.
pangrama es una paraula o frase que conte cada lletra de l alfabet almenys una vegada.
'''
import re

def es_pangrama(texto):
    # Convertir el texto a minúsculas
    texto = texto.lower()
    
    # Usar regex para encontrar todas las letras del alfabeto
    patron = re.compile(r'[a-z]')
    
    # Buscar todas las letras
    letras_encontradas = set(patron.findall(texto))
    
    # Verificar si el número de letras encontradas es igual al tamaño del alfabeto
    return len(letras_encontradas) == 26

# Prueba con dos cadenas
cadena = "esto es una cadena con algunas palabras"
cadena_pangrama = "The quick brown fox jumps over the lazy dog"

print(es_pangrama(cadena))  #  False
print(es_pangrama(cadena_pangrama))  #  True
