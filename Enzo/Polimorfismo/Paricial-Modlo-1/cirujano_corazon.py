from empleado import Empleado
class Ciujano_corazon(Empleado):
    
    def __init__(self):
        self.__cantidad_bypass = int(input("ingrese la cantidad de bypass "))
    
    def curar(self):
        print("enfermedad corazon fue curada de :",self.__cantidad_bypass)
        print("pacientes")              