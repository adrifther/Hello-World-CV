def concatenar(l):
    '''una llista de cadenes la retorna en una única cadena amb tots els elements concatenats (Suma d'strings o cadenes).'''
    for cadena in l:
        resultat=[]
        resultat = ''.join(l)
    return resultat

print(concatenar(["1","2","3"]))