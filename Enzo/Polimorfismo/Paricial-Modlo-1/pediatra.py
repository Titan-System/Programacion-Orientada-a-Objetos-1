from empleado import Empleado
class Pediatra(Empleado):
    
    def __init__(self):
        self.__cantidad_pacientes = int(input("ingrese la cantidad de pacientes: "))
                 
    def curar(self):
        
        print("enfermedad infantil fue curada de :",self.__cantidad_pacientes)
        print("pacientes")                 
        
        
       
        