'''
7. Funció que pren com a paràmetre una llista de números i retorna la llista en ordre
invertit
'''

def inverteix(l):
    l.reverse()
    return l

original = [-11,13,1,25]
l_invertida = inverteix(original)

print(original)
print(l_invertida)
'''Hemos machacado la misma lista pero preferimos tener en otra diferente el resultado'''


'''Aquí asignamos nueva lista, y no reescribimos encima de la primera lista original'''
def inverteix(l):
    resultat = l[:]
    resultat.reverse()
    return resultat

original = [-11,13,1,25]
l_invertida = inverteix(original)

print(original)
print(l_invertida)