from lapiz import lapiz
class alumno:
    def __init__(self,nom:str,dni:int):
        self.__nombre=nom
        self.__DNI=dni
    def pinta_alumno(self,lapiz1):
        lapiz1.lapiz_pintar()
        
    def dibuja_alumno(self,lapiz1):
        lapiz1.lapiz_dibujar()
