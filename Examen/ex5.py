'''Escriu una funcio que comprovi si un numero cau en un rang donat'''

def dinsrang(numero,rang1,rang2):
    if( numero >=rang1 and numero<=rang2):
        return True
    else: 
        return False
    

print(dinsrang(5,2,3))

print(dinsrang(3,2,5))
