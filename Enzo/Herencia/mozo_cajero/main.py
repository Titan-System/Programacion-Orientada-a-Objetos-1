from mozo import Mozo
from cajero import Cajero
from empleado import Empleado
class Main:
    @staticmethod
    def calcula_sueldo(i:Empleado):

        i.Averiguar_sueldo()


    def __init__(self):
        pass

def main(): 

    mozo1 = Mozo("LUCAS")
    caj1 = Cajero("MARIO")

    Main.calcula_sueldo(mozo1)
    Main.calcula_sueldo(caj1)


if __name__ == "__main__":
    main()