class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = input("Nombre del PERRO: ")
        self.edad = input("edad del perro: ")
        self.raza = input("raza del perro: ")
    def ladrar(self):
        return print("guau")
    def mover_la_cola(self):
        return print("mueve la cola")
    def comer(self):
        return print("come")
    
import os
def main(): 
    #os.system('cls')
    perro1 = Perro()
    #os.system('cls')
    print("El perro se llama: " + perro1.nombre)
    print("Tengo "+ perro1.edad)
    print("Soy un: "+ perro1.raza)
    perro1.ladrar()

if __name__ == "__main__":
    main()    

    


