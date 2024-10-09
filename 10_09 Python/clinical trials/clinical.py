import io


arxiu = io.open('clinicaltrials.txt', 'r', encoding = 'utf-8')

llistadecadenes= arxiu.readlines()

arxiu.close()

estudis=[]
arxiu = io.open('llistat.txt','w',encoding = 'utf-8')
for pos in range(len(llistadecadenes)):
    if llistadecadenes[pos] == "NEW\n":
        estudis.append(llistadecadenes[pos+1])
for estudi in estudis:

    arxiu.write(estudi + '\n')

arxiu.close()        
