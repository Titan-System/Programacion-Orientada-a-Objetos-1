from empleado import Empleado
import os
class Hospital:
    
    def __init__(self):
        pass
    def metodo_lista(self, lista_doc):
        self.__lista_doc = lista_doc
     
        for d in lista_doc:
            os.system('cls')
            print("Empleado: ",d._Empleado__nombre,d._Empleado__apellido,"Especialidad: ",d._Empleado__especialidad,"Edad: ",d._Empleado__edad)
            if d._Empleado__especialidad == "pediatra":
                acum =+ d.cantidad_pacientes
            if d._Empleado__especialidad == "Cirujano abdomen":
                cont =+ 1 
                
        print("la cantidad de pacientes de pediatria es: ",acum)
        print("la cantidad de cirujanos de abdomen es: ",cont)    
           
            
           
       
        
        
        
        
        