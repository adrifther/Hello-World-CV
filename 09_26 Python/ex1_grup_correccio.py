'''Funció que pren com a paràmetre una llista de números i retorna una altra llista 
ordenada.
'''
'''variant1: la 1 da none porque no tiene return'''
def ordenada(l):

     l.sort()

llista = [4,13,1,25]

'''otra variante de la 1'''
def ordenada(l):

     return l.sort()

llista = [4,13,1,25]

print(ordenada(llista)) #none
print(llista)           #retorna llista ordenada


'''variant2 modificas la original'''
def ordenada(l):
    l.sort() 
    return l

llista = [4,13,1,25]

print(ordenada(llista)) #retorna llista ordenada
print(llista)           #retorna llista ordenada


'''variant3: mejor, no modificas la original'''
def ordenada(l):
    resultat =l[:]

    resultat.sort()

    return resultat