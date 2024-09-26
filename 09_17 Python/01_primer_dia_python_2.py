import time 

entrada= input()
paraules= entrada.split('')

print(f"La entrada es (entrada)")
paraula_maxima=''
paraula_minima=''   

print(f"Después de split queda asi (paraules)")



for paraula in paraules:
    print(f" la actual es esta: (paraula)")

    #time.sleep(3)

    if len(paraula) > len(paraula_maxima):
        paraula_maxima=paraula    
        print(f"La palabra maxima es (paraula_maxima)")
    if len(paraula) < len(paraula_minima):
        paraula_minima=paraula    
        print(f"La palabra mínima es (paraula_minima)")

