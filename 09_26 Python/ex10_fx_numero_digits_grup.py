def digits(l):
    resultat = []
    for num in l:
        if num<0:
            resultat.append(len(str(num))-1)
        else:
            resultat.append(len(str(num)))   

    return resultat


original = [-11,13,1,25]
digits = digits(original)

print(original)
print(digits)


'''otra variante'''
def digits(l):
    resultat = []
    for num in l:
        num = str(num).replace("-","")
        resultat.append(len(num))   

    return resultat


original = [-11,13,1,25]
digits = digits(original)

print(original)
print(digits)

