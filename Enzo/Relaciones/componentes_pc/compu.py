from unidad_disco import unidad_disco
from consola import consola
class computadora:
    def __init__(self):
        self.__consola=consola()
        self.__unidad_disco=unidad_disco()
        print("compu construida")

def main():
    #CMD=consola()
    #SSD=unidad_disco()

    compugamer=computadora()


if __name__ == "__main__":
    main()        

        

        
