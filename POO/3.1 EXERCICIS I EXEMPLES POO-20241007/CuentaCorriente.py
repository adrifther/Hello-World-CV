class CuentaBancaria:
    def __init__(self):
        
        self.nombre = ""
        
        self.apellido1 = ""
        
        self.apellido2 = ""
        
        self.numero = ""
                
        self.tipo = "corriente"
        
        self.saldo = 0
     
    
    def consulta(self):
        
        return self.saldo
    
    def ingresar(self, ingreso):
    
        self.saldo = self.saldo + ingreso
    
    def retirar(self, retiro):
        if self.saldo - retiro > 0:
            self.saldo = self.saldo - retiro
            return f"Su Saldo es {self.saldo}"
        else:
            return "no posible"
     
    def __str__(self):    
        
        return f" Los datos de su cuenta son:\n\
                  nombre: {self.nombre}\n\
                  apellido1: {self.apellido1}\n\
                  apellido2: {self.apellido2}\n\
                  numero: {self.numero}\n\
                  tipo: {self.tipo}\n\
                  saldo: {self.saldo}\n\
                  "
c1 = CuentaBancaria()

c1.nombre, c1.apellido1, c1. apellido2, c1.numero, c1.tipo, c1.saldo = "Joan", "Candemor", "Martins", "0100984344","corriente", 80000



while True:
    
    cadena = input("1. Info 2. Consulta  3. Ingreso 4. Retiro  5.Salir")
        
    if cadena == '1':
        print(c1)
        
    elif cadena == '2':
        print(c1.consulta())
    elif cadena == '3':
        ingreso = input("Introduzca cantidad a ingresar")
        c1.ingresar(int(ingreso))
        
    elif cadena == '4':
        retiro = input("Introduzca cantidad a retirar")
        print(c1.retirar(int(retiro)))
    elif cadena == '5':
        print("Fins la propera")
        break
    else:
        print("Introduzca una opción válida")
        
    
   
   
