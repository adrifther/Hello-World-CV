

class triangulo:

     
      
      def __init__(self, lado1, lado2, lado3):

           self.lado1 = lado1
           
           self.lado2 = lado2
           
           self.lado3 = lado3

          
             
      def estriangle(self):

            if (self.lado1 >= self.lado2 + self.lado3) or (self.lado2 >= self.lado1 + self.lado3) or (self.lado3 >= self.lado1 + self.lado2):

                  return False

            else:
                  return True
        

      def mayor(self):

            if self.estriangle():
            
               if self.lado1 >= self.lado2 and self.lado1 >= self.lado3:
                  
                    return self.lado1

               elif self.lado2 >= self.lado1 and self.lado2 >= self.lado3:

                    return self.lado2

               else:
                    return self.lado3
            return "El costat més gran no te'l dic perquè aixo no es triangle"

      def tipo(self):

            if self.estriangle():  
                if (self.lado1 != self.lado2) and (self.lado1 != self.lado3) and (self.lado2 != self.lado3):

                      return "El triangulo es Escaleno"

                elif (self.lado1 == self.lado2) and (self.lado2 == self.lado3):

                      return "El triangulo es equilatero"

                else:
                      return "El triangulo es isosceles"
                  
            return "El tipus no te'l dic perquè aixo no es triangle"
            

      def __str__(self):

            if self.estriangle():
                return f" Este es un objeto triangulo con lados {self.lado1},{self.lado2},{self.lado3}"
            return "aquest objecte no es triangle"

while True:
      
  try:
     triangle1 = triangulo(float(input()),float(input()),float(input()) )
     break
  except:
     pass
     
print(triangle1)

print(triangle1.mayor())

print(triangle1.tipo())


'''

   if self.estriangle():    <------------------------------->  if self.estriangle() == True:



   if not self.estriangle() <--------------------------------> if self.estriangle() == False:

'''






































   
