'''
9. Funció que pren com a paràmetre una llista de números i retorna una altra llista amb 
els elements en posició senar.
'''
def parell(l):
    resultat=[]
    for posicio in range(1,len(l),2): #range(start,stop,step)
        resultat.append(l[posicio])   #deste start hasta stop-1 step by step
    return resultat


original = [-11,13,1,25]
parells = parell(original)

print(original)
print(parells)


''' otra variante'''
def parell(l):
    resultat=[]
    for posicio in range(len(l)):
        if posicio %2 == 1: # o bien se puede poner: != 0
            resultat.append(l[posicio])
    return resultat

original = [-11,13,1,25]
parells = parell(original)

print(original)
print(parells)