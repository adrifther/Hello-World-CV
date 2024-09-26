'''' 
5 Funció que pren com a paràmetre una llista de números i retorna el seu valor mínim
'''

def minim(l):
    minim=l[0]          # elemento en posicion 0
    for num in l[1:]:   # elementos desde 1 en adelante hasta final
        if num < minim:
            minim=num   

    return minim        

original=[-11,13,1,25]
print(minim(original))