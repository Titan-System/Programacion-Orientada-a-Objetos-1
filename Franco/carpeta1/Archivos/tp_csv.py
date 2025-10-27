



def main():
   
    nombres = ["pedro", "juan", "josue"]
    DNI = ("43519848","42548632","41258741")
    lista = dict(zip(nombres,DNI))
    
    for p,t in lista.items():
        print(p,t)
    fichero = open("datos_guardados.csv", 'w')

    for nombre,dni in lista.items():
        fichero.write(nombre + " "+ dni + "\n")

    fichero.close()

    
    fichero = open('datos_guardados.csv')
    caracter = fichero.readline()
    while caracter != "":
        print(caracter)
        caracter = fichero.readline()
    
       
       
   

   
    
    
    
    
    
    
    
    
if __name__ == "__main__":
     main()    
        
    
     