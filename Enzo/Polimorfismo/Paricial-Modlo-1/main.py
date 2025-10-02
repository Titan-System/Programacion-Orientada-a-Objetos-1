from cirujano_abdomen import Cirujano_abdomen
from cirujano_corazon import Ciujano_corazon
from pediatra import Pediatra
from empleado import Empleado

class Main:

        @staticmethod
        def metodo_puente(d:Empleado):
            return d.curar() 

def main():
    
      
    
    doc1 = Pediatra()
    doc2 = Cirujano_abdomen()
    doc3= Ciujano_corazon()   
  
    print ("El resutaldo es: ",Main.metodo_puente(doc1)) 
    print ("El resutaldo es: ",Main.metodo_puente(doc2)) 
    print ("El resutaldo es: ",Main.metodo_puente(doc3))    
    
    
if __name__ == "__main__":
    main()    