from empleado import Empleado
class Pediatra(Empleado):
    
    def __init__(self):
        super().__init__("pediatra")
        self.__cantidad_pacientes = int(input("ingrese la cantidad de pacientes: "))
    
    @property
    def cantidad_pacientes(self):
        return self.__cantidad_pacientes 
                 
    def curar(self):
        
        print("enfermedad infantil fue curada de :",self.__cantidad_pacientes)
        print("pacientes")                 
        
        
       
        