def sumaquadrats(l):
    suma=0
    for numero in l:
        suma+=numero**2 #si queremos funcion suma los cubos: ponemos **3
    return suma


original = [11,13,1,25]
suma=sumaquadrats(original)
print(suma)