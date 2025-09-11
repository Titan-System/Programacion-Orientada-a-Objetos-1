from pantalla import pantalla
from teclado import teclado
class consola:

    def __init__(self):
        self.__pantalla=pantalla()
        self.__teclado=teclado()
        print("consola construido")
     