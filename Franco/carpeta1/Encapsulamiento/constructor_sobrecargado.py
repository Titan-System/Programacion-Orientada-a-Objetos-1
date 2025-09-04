#Para entender Constructor sobrecargado y el uso de getter y setter
import os
class Alumno:
  def __init__(self, nom, ed, pro):
     print("Soy el Constructor Sobrecargado, voy a poner datos en atributos")     
     self.nombre=nom                
     self.__edad=ed      	
     self.promedio=pro
  def getEdad(self):
    return self.__edad   
  def darExamen(self):
    return print(self.nombre, " da examen")  
  def setNombre(self, nom):
    self.nombre=nom
  def setEdad(self, ed):
     self.__edad=ed
  def setPromedio(self, pro):
     self.promedio=pro    
def main(): 
  os.system('cls')
  nom =input("Ingrese nombre de Alumna/o: ")
  eda =input("Ingrese la edad de Alumna/o: ")
  prom =input("Ingrese promedio de Alumna/o: ")  
  
  alumno1= Alumno(nom,eda,prom)
  alumno2 = Alumno("Ana",20, 9)
  alumno3 = Alumno("",0,0.0)
  alumno3.setNombre("María")
  alumno3.setEdad(17)
  alumno3.setPromedio(10)
  
  print("DatosAlumna/o nombre:", alumno1.nombre, " edad: ",alumno1.getEdad(),"promedio: ", alumno1.promedio)
  print("DatosAlumna/o nombre:", alumno2.nombre, " edad: ",alumno2.getEdad(),"promedio: ", alumno2.promedio)
  print("DatosAlumna/o nombre:", alumno3.nombre, " edad: ",alumno3.getEdad(),"promedio: ", alumno3.promedio)
  alumno1.darExamen()
  alumno2.darExamen()
  alumno3.darExamen()
if __name__ == "__main__":    
  main()
