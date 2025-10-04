from empleado import Empleado
class Cirujano_corazon(Empleado):
    
    def __init__(self):
        super().__init__("cirujano corazon")
        self.__cantidad_bypass = int(input("ingrese la cantidad de bypass "))
    
    def curar(self):
        print("enfermedad corazon fue curada de :",self.__cantidad_bypass)
        print("pacientes")              