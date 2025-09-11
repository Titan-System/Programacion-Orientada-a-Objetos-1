from driver import controlador
from disk import disco

class unidad_disco:

    def __init__(self):
        self.__controlador=controlador()
        self.__disco=disco()
        print("unidad disco construida")
    


        
    