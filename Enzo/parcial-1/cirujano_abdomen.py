from empleado import Empleado
class Cirujano_abdomen(Empleado):
    
    def __init__(self):
        super().__init__("Cirujano abdomen")
        self.__cantidad_cirugias = int(input("ingrese la cantidad de cirugias: "))
            
    def curar(self):
        print("enfermedad abdomen fue curada de :",self.__cantidad_cirugias)
        print("pacientes")               