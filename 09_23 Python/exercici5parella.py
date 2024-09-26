# 5. Llegeix els quatre nombres que conformen una adreça IP, valida si és una IP 
# correcta i ho escriu.

entrada = input("Escriu 4 números separats per un punt")

#Usuari entri  entrada
#  8.45.78.43
octets = entrada.split('.')

#octets ['8','45','78','43'] 
Esip =True

if len(octets) != 4:
   Esip = False

else:
   

    for octet in octets:

        try:
            octet = int(octet) 
            if octet < 0 or octet > 255:
                print("això no és una IP")
                Esip = False
            break
         

        except:
            print("això no és una IP")
            Esip = False
            break

    if Esip:
   
     print("IP es Correcta")

