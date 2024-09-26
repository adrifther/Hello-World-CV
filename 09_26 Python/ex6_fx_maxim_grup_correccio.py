'''
6. Funció que pren com a paràmetre una llista de números i retorna el seu valor màxim.
'''



def minim(l):
    maxim=l[0]          # elemento en posicion 0
    for num in l[1:]:   # elementos desde 1 en adelante hasta final
        if num > maxim:
            minim=num   #reasigna con num si num es > a la posicion anterior

    return minim        

original=[-11,13,1,25]
print(minim(original))