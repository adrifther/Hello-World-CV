def nolast (x):
    resultat=[]
    for cadena in x:
        resultat.append(cadena[0:len(cadena)-1])
    return  resultat    

original = ["hola","com","estas", "pink","FLOYD"]

print(nolast(original))    