from categoria_plato import categoria_plato
class Plato:
    
    def __init__(self,precio:float, nombre:str,categoria:categoria_plato):
        self.__nombre = nombre
        self.__precio = precio
        self.__categoria = categoria
        print("------------------------")
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio
        
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, nueva_categoria):
        self.__categoria = nueva_categoria
         
    