import os 
class estudiante():
    def __init__(self, __nombre="", __nota=0):
        self.__nombre = input ("Ingrese nombre --> ")
        self.__nota = int(input ("ingrese nota --> "))
    
    #getters y setters
    def get_nombre(self):
        return self.__nombre
    def get_nota(self):
        return self.__nota
    
    def set_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
    def set_nota(self, nueva_nota):
        self.__nota = nueva_nota

    #metodos de la clase
    def mostrar_datos(self):
        print("--Estos son los datos del alumno--")
        print("Nombre: ", self.get_nombre(), "\nNota: ",self.get_nota()) #en esta parte muy importante poner los parentesis a cada método
                                                                         #sino, nos mostrará la referencia del metodo sin su contenido
        if self.get_nota() >= 4:
            print("Aprobado")
        else:
            print("Desaprobado")
#Metodo main
def main():
    #Instancio los objetos
    os.system('cls') #Borrar terminal
    prueba1 = estudiante()
    os.system('cls')
    prueba2 = estudiante()

    #Muestro su contenido
    os.system('cls')
    prueba1.mostrar_datos()
    prueba2.mostrar_datos()

if __name__ == "__main__":
    main()