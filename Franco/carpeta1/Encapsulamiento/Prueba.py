
import os
#os.system('cls')
#print("Hola Universo")

#def hola(): 
#    print("Hola Universo en funcion hola")
class Universo:
    def hola(self):
        print("Holas Universo en la clase gato")

def main():
    os.system('cls')
    serhumano = Universo()
    print("Acá se viene le objeto serhumano")
    serhumano.hola()
if __name__ == "__main__":
    main()