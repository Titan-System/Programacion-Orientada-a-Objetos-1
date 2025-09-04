import os #importo librería, la uso para borrar la terminal
class Alumno:
    def __init__(self): # self = this. Generamos atribuos de instancia al ponerle slf a los atributos
        print("El constru")
        #self.nombre=""
        self.nombre= input("Nombre del alumno: ") #Entrada por teclado
        apellido="" #atributo de clase que es fijo por no tener self
        self.__edad=input("Edad del alumno:") #el __ hago privada la edad
        self.promedio=input("Cuál es su promedio: ")
    def darExamne(self): #A los métodos de la clase les coloco "self" para señalar al objeto en la memoria
        return print("Listo pa, terminé el examen")
    def getEdad(self):
        return self.__edad 

def main():
    os.system('cls')
    alumno1 = Alumno()
    os.system('cls')
    print("Me llamo: "+ alumno1.nombre)
    print("Tengo "+ alumno1.getEdad() + " años")
    print("Mi humilde promedio")

    alumno1.darExamne()
if __name__ == "__main__":
    main()