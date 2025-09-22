from empleado import Empleado

class Mozo(Empleado):

   def Averiguar_sueldo(self):
        
        hora = int(input("ingrese la cantidad de horas trabajadas en el mes "))
        print("--> ")
        propina = float(input("ingrese la cantidad de propina recibida en pesos "))
        print("--> ")
        print ("el salario del mozo es ", self.nombre , hora * 8000 + propina)
   
   