from empleado import Empleado

class Cajero(Empleado):

 def Averiguar_sueldo(self):
        
        hora = int(input("ingrese la cantidad de horas trabajadas en el mes "))
        print("--> ")

        print ("el salario del cajero es ", self.nombre , hora * 10000 )
 
      