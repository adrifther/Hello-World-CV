'''12. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les 
mateixes cadenes en minúscules.
'''

def minusculas(l):
    resultat=[]
    for cadena in l:
        resultat.append(cadena.lower())
    return resultat    

original =["akKSHFGshf", "kSDFGsf","aSDFGd"]
minus=minusculas(original)

def sumastrings(l):
    resultado=""
    for cadena in l:
        resultado += cadena
    return resultado

original =["akSDFdshf", "kjSDFGsf","SDFGsd"]
digits=sumastrings(original)