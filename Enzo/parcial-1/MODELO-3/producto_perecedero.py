from producto import Producto
class Producto_perecero(Producto):
    def __init__(self):
        super().__init__()
        self.__fecha_caducidad = input("ingrese la fecha de caducidad ")