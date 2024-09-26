def parell(l):
    resultat=[]
    for posicio in range(len(l)):
        if posicio %2 == 0:
            resultat.append(l[posicio])
    return resultat

original = [-11,13,1,25]
parells = parell(original)

print(original)
print(parells)


''' otra variante con range'''

def parell(l):
    resultat=[]
    for posicio in range(0,len(l),2): #range(start,stop,step)
        resultat.append(l[posicio])   #deste start hasta stop-1 step by step
    return resultat

print(original)
print(parells)