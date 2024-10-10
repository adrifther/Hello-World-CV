'''funcio retornant maxim d una llista sense el max()'''

def maximissim(l):
    maxim=l[0]          # elemento en posicion 0
    for num in l[1:]:   # elementos desde 1 en adelante hasta final
        if num > maxim:
            minim=num   #reasigna con num si num es > a la posicion anterior

    return minim        

original=[-11,13,1,25]
print(maximissim(original))