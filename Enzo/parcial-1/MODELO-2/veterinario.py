from animal import Animal
from gato import Gato
from perro import Perro


class Veterinario:
    def init(self, nombre: str, experiencia: int, especialidad: str):
        self.nombre = nombre
        self.experiencia = experiencia
        self.especialidad = especialidad

    @staticmethod
    def atiende_animal(a: Animal):
        a.hacersonido()


def main():

    lista = []
    op = input("desea cargar animales? si/no")
    while op == "si":

        op2 = int(
            input("ingrese el animal (1 para Perro, 2 para Gato, 3 para salir): "))
        match op2:
            case 1:
                dog = Perro("Bobbo", 2)
                lista.append(dog)
            case 2:
                cat = Gato("Gere", 4)
                lista.append(cat)
            case 3:
                print("saliendo...")
            case _:
                print("opcion incorrecta")

        op = input("desea cargar mas animales? si/no")
    for a in lista:
        print("El animal", a.nombre, "tiene", a.edad, "años")
        a.hacer_sonido()
   # Veterinario.atiende_animal(dog)
   # Veterinario.atiende_animal(cat)


if __name__ == "__main__":
    main()


"""
Polimorfismo en Colecciones (ArrayList)
Crea una lista de objetos Animal que incluya tanto objetos Perro como Gato. Itera sobre la lista y haz que cada animal haga su sonido mediante el uso de polimorfismo."""