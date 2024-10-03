import re

import io


patro =re.compile(r"[A-Za-z0-9-': \/\_\.!$?]+|\"[^\"]*\"")

arxiu = io.open(r"C:\Users\Alumne_mati1.EQUIPHECTOR\Desktop\Python\10_03 Python\New_study\StudentPerformanceFactors.csv", "r", encoding = 'utf-8')

#llistadecadenes = arxiu.readlines() # readlines() con len() es el numero de lineas: len(llistadecadenes)


llistadecadenes = [cadena.replace(",,",",ND,") for cadena in arxiu.readlines()]


matriu = []

for cadena in llistadecadenes:

    matriu.append(patro.findall(cadena))

implicacio_ascendents = []
Llista_elements_de_text =[]

scores = []

scorebaix = 0
indexbaix = 0
scoremig  = 0
indexmig = 0
scorealt  = 0
indexalt = 0

for llista in matriu[1:]:
    
    implicacio_ascendents.append(llista[2])#aqui podem agafar la columna que volguis
    Llista_elements_de_text.append(llista[5])#aqui podem agafar la columna que volguis
    scores.append(int(llista[-1]))

for pos in range(len(implicacio_ascendents)):
    
    if implicacio_ascendents[pos] == "High":
        
        scorealt += scores[pos]
        indexalt  += 1

    elif implicacio_ascendents[pos] == "Medium":

        scoremig += scores[pos]
        indexmig   += 1 


    else:

        scorebaix += scores[pos]
        indexbaix   += 1

      
print(scorebaix/indexbaix,scoremig/indexmig,  scorealt/indexalt)
    
hores_estudiades = []

scores = []
for llista in matriu[1:]:
    
    hores_estudiades.append(int(llista[0]))
    scores.append(int(llista[-1]))
   
scorebaix = 0
indexbaix = 0
scoremig  = 0
indexmig = 0
scorealt  = 0
indexalt = 0
scoreover = 0
indexover = 0

scorebaix_ = 0
indexbaix_ = 0
scoremig_  = 0
indexmig_ = 0
scorealt_  = 0
indexalt_ = 0
scoreover_ = 0
indexover_ = 0

for pos in range(len(hores_estudiades)):
    
    if 0 <= hores_estudiades[pos] < 5:

       scorebaix += scores[pos]
       indexbaix   += 1
    elif  5 <= hores_estudiades[pos] < 10:

      scorebaix_ += scores[pos]
      indexbaix_   += 1
    elif 10 <= hores_estudiades[pos] < 15:

        scoremig += scores[pos]
        indexmig   += 1


    elif  15 <= hores_estudiades[pos] < 20:

       scoremig_ += scores[pos]
       indexmig_   += 1
       
    elif 20 <= hores_estudiades[pos] < 25:

        scorealt += scores[pos]
        indexalt  += 1

    elif 25 <= hores_estudiades[pos] < 30:

        scorealt_ += scores[pos]
        indexalt_  += 1
        
        
    else:
        scoreover += scores[pos]
        indexover += 1
        
print(scorebaix/indexbaix,scorebaix_/indexbaix_, scoremig/indexmig, scoremig_/indexmig_, scorealt/indexalt, scorealt_/indexalt_, scoreover/indexover)



#cuando es texto es diferente 
count_si = 0
count_no = 0
for pos in Llista_elements_de_text: 

    if pos == "Yes":
        count_si += 1

    else:
        count_no +=1

print (count_no,count_si)