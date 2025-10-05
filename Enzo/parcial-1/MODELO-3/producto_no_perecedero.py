from producto import Producto
class Producto_no_perecedero(Producto):
    def __init__(self):
        super().__init__()
        self.__categoria = input("ingrese la categoira  del producto ")