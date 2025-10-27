import pickle

class Alumno:
    def __init__(self, nombre:str, edad:int, promedio:float):
        self.__nombre = nombre
        self.__edad = edad
        self.__promedio = promedio
        
    @property
    def nombre(self):
        return self.__nombre
        
    @property
    def edad(self):
        return self.__edad
    
    @property
    def promedio(self):
        return self.__promedio    
        
        
        
    
def main():
    
    lista_alu = []    
    alu1 = Alumno("Matias", 24, 9.90)
    alu2 = Alumno("Enzo", 23, 3.90) 
    alu3 = Alumno("Franco", 21, 7.90)     
    alu4 = Alumno("Luciano", 19, 1.90) 
    alu5 = Alumno("Gustavo", 424, 9.99)
    
    

    lista_alu.append(alu1)
    lista_alu.append(alu2)
    lista_alu.append(alu3)
    lista_alu.append(alu4)
    lista_alu.append(alu5)

    with open("datos_alumno.pkl", "wb") as archivo:
        pickle.dump((lista_alu), archivo)
    print("✅ Objetos guardados correctamente.")
             
    with open("datos_alumno.pkl", "rb") as archivo:
       probando_data = pickle.load(archivo)
    lista_alu2 = []   
    for i in probando_data:
        print(i.nombre, i.edad, i.promedio)
        lista_alu2.append(i)
    print("mostrando lista 2")
    for l in lista_alu2:
        print(l.nombre, l.edad, l.promedio, "🤐")    
           
       
   

   
    
    
    
    
    
    
    
    
if __name__ == "__main__":
     main()    
        
    
     