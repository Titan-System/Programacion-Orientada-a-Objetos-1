class Empleado:
    
    def __init__(self,especialidad:str):
        self.__nombre = input("ingrese el nombre: ")
        self.__apellido = input("ingrese el apellido: ")
        self.__edad = input("ingrese la edad: ")
        self.__especialidad = especialidad
        
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def especialidad(self):
        return self.__especialidad

    