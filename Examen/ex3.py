'''
Escriure una funcio que, donada una string, retorni la longitud de l ultima paraula.
Es considera que les paraules estan separades per un o mes espais.
tambe podria haver-hi espais al final o inici de string'''




mi_string="   Tinc tanta son que a les cinc tinc son  "


def ultimaen(cadena):
    modificada = ""
    modificada = cadena.split()
    return len(modificada[-1])

print(ultimaen(mi_string))

'''tests
modificada= mi_string.split()
print( len(modificada[-1]))
print (mi_string)
print (modificada)
'''