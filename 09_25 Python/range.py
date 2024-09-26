for num in range(10):  #0a9         #print al final hace \n (salto a linea por defecto)
    print(num, end=",") #en vez de salto de linea por defecto como dice la funcion hace, al finalde cada print.

#range(j) equivale range(0,j)    
# 0,1,2...,j-1
range(5)


#range(i,j)  
# i, i+1,...,j-2,j-1
range(2,6)


#range(start,stop,step)
#range(i,j,s)     
# i, i+s, i+2s,...,j-1
range(2,20,5) #de 2 a 

for num in range(2,20,5):
    print (num)

#range empezando por el final, se escribe con step (-)negativo y entonces va al reves con el step definido empezando por el final.
range(20,2,-2)
for num in range(20,2,-2): #imprime hasta el PENULTIMO valor: 4 
    print (num)    