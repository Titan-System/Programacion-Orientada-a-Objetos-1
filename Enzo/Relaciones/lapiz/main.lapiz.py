from alumnolapiz import alumno
from lapiz import lapiz


def main():

    lapiz1=lapiz("rojo",10)
    alu1=alumno("juan",43567890)
    alu2=alumno ("mati",34567890)
    alu1.dibuja_alumno(lapiz1)
    alu2.pinta_alumno(lapiz1)


if __name__ == "__main__":
    main()


