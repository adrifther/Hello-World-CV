'''
16. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb 
les cadenes que es troben en posició parell.
'''

def parelles(x):
    resultat=[]
    for posicio in range(len(x)): #o in range(.......)
        if posicio %2 ==0:
            print(x[posicio])

original = ["hola","com","estas", "pink","FLOYD"]

print(parelles(original))