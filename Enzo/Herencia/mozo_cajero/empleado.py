class Empleado:

    def __init__(self,nombre:int):
    
        self.__nombre = nombre
        
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        nombre = nuevo_nombre 
    

    def Averiguar_sueldo(self):
        pass

    def Calcula_sueldo(self):

        pass






