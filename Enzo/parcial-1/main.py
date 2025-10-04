from cirujano_abdomen import Cirujano_abdomen
from cirujano_corazon import Cirujano_corazon
from pediatra import Pediatra
from empleado import Empleado
from hospital import Hospital
import os

class Main:

    @staticmethod
    def metodo_puente(d:Empleado):
        return d.curar() 

def main():
    
    print("Bienvenido al sistema de gestion hospitalaria")
    print("Desea ingresar un empleado? |si|no|")
    op = input("--> :")
    
    lista_doc = []
    while op == "si":
        print("Ingrese el tipo de empleado")
        print("|1| Pediatra\n|2| Cirujano de abdomen\n|3| Cirujano de corazon")
        op2 = int(input())
        match  op2:
             
            case 1:
               doc1 = Pediatra()
               lista_doc.append(doc1) 
            case 2:
                doc2 = Cirujano_abdomen()
                lista_doc.append(doc2)
            case 3:
                doc3= Cirujano_corazon()
                lista_doc.append(doc3)
            case 4:
                print("Saliendo del sistema........")
            case _:
                print("Opcion incorrecta") 
                       
        print("Desea ingresar otro empleado? |si|no|")
        op = input()
    
    os.system('cls')        
    Hos = Hospital()
    Hos.metodo_lista(lista_doc)
    
    Main.metodo_puente(doc1) 
    Main.metodo_puente(doc2) 
    Main.metodo_puente(doc3)    
    
    
if __name__ == "__main__":
    main()    