''' 
Escriure els n primers múltiples de m
'''

n = int(input("escriu per quants multiples vols: "))
m = int(input("escriu de quin numero vols el multiple: "))

for i in range(m,(n+1),m): 
    print(i)