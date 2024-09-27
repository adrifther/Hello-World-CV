'''FUNCIONS / FUNCIONES'''
def ordenada(l):
    ''' Funció que pren com a paràmetre una llista de números i retorna una altra llista 
    ordenada.'''
    resultat =l[:]

    resultat.sort()

    return resultat



def suma(lista):   # per llista
    '''suma dels elements d'una llista'''
    total=0        # iniciador dins bucle
    for element in lista:
        total += element
    return total



def sumaquadrats(l):
    '''suma els cuadrats dels elements'''
    suma=0
    for numero in l:
        suma+=numero**2 #si queremos funcion suma los cubos: ponemos **3
    return suma



def sumacubs(l):
    ''''suma els cubs dels elements'''
    suma=0
    for numero in l:
        suma+=numero**3 
    return suma





def minim(l):
    '''valor mínim de llista de números'''
    minim=l[0]          # elemento en posicion 0
    for num in l[1:]:   # elementos desde 1 en adelante hasta final
        if num < minim:
            minim=num   

    return minim 



def maximisim(l):
    '''valor màxim de números d'una llista'''
    maxim=l[0]          # elemento en posicion 0
    for num in l[1:]:   # elementos desde 1 en adelante hasta final
        if num > maxim:
            maximisim=num   #reasigna con num si num es > a la posicion anterior

    return maximisim   




def inverteix(l):
    '''inverteix l'ordre de llista de números'''
    resultat = l[:]    #Aquí asignamos nueva lista, y no reescribimos encima de la primera lista original
    resultat.reverse()
    return resultat



def parell(l):
    '''Retorna els elements d'una llista en posicio par'''
    resultat=[]
    for posicio in range(len(l)):
        if posicio %2 == 0:
            resultat.append(l[posicio])
    return resultat


def senar(l):
    '''pren llista i retorna llista amb els elements en posició senar'''
    resultat=[]
    for posicio in range(len(l)):
        if posicio %2 == 1: # o bien se puede poner: != 0
            resultat.append(l[posicio])
    return resultat



def digits(l):
    '''pren llista i retorna una altra llista amb el número de dígits de cada element.'''
    resultat = []
    for num in l:
        num = str(num).replace("-","")
        resultat.append(len(num))   

    return resultat




def longitud(l):
    '''pren llista de cadenes i retorna una altra llista amb la longitud de cadascuna de les cadenes que formen la llista.'''
    resultat=[]
    for cadena in l:
        resultat.append(len(cadena))
    return resultat   



def sumastrings(l):
    '''pren una llista de cadenes i retorna una altra llista amb les mateixes cadenes en minúscules.'''
    resultado=""
    for cadena in l:
        resultado += cadena
    return resultado



def minusculas(l):
    '''pren com a paràmetre una llista de cadenes i retorna una altra llista amb les cadenes en minúscules.'''
    resultat=[]
    for cadena in l:
        resultat.append(cadena.upper())
    return resultat    


def concatenar(l):
    '''una llista de cadenes la retorna en una única cadena amb tots els elements concatenats (Suma d'strings o cadenes).'''
    for cadena in l:
        resultat=[]
        resultat = ''.join(l)
    return resultat


def ordenastrings(x):
    '''funcion con orden'''
                            #asi no modificamos la original'''
    ordenada = x[:]         # SLICING para no modificar la original creamos una lista nueva
    
    ordenada.sort()         # no té return en sí
    return ordenada




def parelles(x):
    '''pren com a paràmetre una llista de cadenes i retorna una altra llista amb les cadenes que es troben en posició parell.'''
    resultat=[]
    for posicio in range(len(x)): #o in range(.......)
        if posicio %2 ==0:
            print(x[posicio])


def senars(x):
    '''Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les cadenes que es troben en posició senar.'''
    resultat=[]
    for posicio in range(len(x)): #o in range(.......)
        if posicio %2 == 1:
            print(x[posicio])


def nofirst (x):
    '''elimina el primer element d'una llista'''
    resultat=[]
    for cadena in x:
        resultat.append(cadena[1:len(cadena)])
    return  resultat 


def nolast (x):
    '''elimina l'ultim element d una llista'''
    resultat=[]
    for cadena in x:
        resultat.append(cadena[0:len(cadena)-1])
    return  resultat  


def inversion_cadena(c):
    '''invierte el orden una cadena'''
    resultat=''
    for char in c:
        resultat = char + resultat  #para invertir cadena #debug para ver como funciona
    return resultat


def lista_invertida(lista):
    '''guarda lista con cadenas invertidas'''
    invertida = []

    for cadena in lista:

           invertida.append(inversion_cadena(cadena))

    return(invertida)
