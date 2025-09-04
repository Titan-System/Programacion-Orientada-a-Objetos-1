import os 
class operaciones_aritmeticas:
    def __init__(self,__a=0,__b=0):
        self.__a = int(input("Ingrese el valor de a -->"))
        self.__b = int(input("Ingrese el valor de b -->"))

    def get_a(self):
        return self.__a
    def set_a(self, a):
        self.__a = a

    def get_b(self):
        return self.__b
    def set_b(self, b):
        self.__b = b


    def sumar(self):
         return print ("Resultado de la suma: ",self.__a + self.__b)
    def restar(self):
         return print("Resultado de la resta: ",self.__a - self.__b)
    def multiplicar(self):
         return print("Resultado de la multiplicacion : ",self.__a * self.__b)
    def dividir(self):
         return print("Resultado de la division: ",self.__a / self.__b)
    def resto(self):
         return print("Resultado del resto:",self.__a % self.__b)
    def exponencial(self):
         return print("Resultado de la potencia ",self.__a ** self.__b)
   
    
def main():
    
    valor = 0
   
    print("--> Seleccione la opcion <--")
    print(" |1|--> Suma  \n |2|--> Resta  \n |3|--> Multiplicacion  \n |4|--> Dsivision  \n |5|--> Resto  \n |6|--> Potencia  \n |7|--> Salir  ")
    valor = int( input ("-->")) 
    while  valor != 7 :
        
        os.system("cls")
        match valor :
            case 1:
                yo_sumo = operaciones_aritmeticas()
                yo_sumo.sumar()
            case 2:
                yo_resto = operaciones_aritmeticas()
                yo_resto.restar()
            case 3:
                yo_multiplico = operaciones_aritmeticas()
                yo_multiplico.multiplicar()
            case 4:
                yo_divido = operaciones_aritmeticas()
                yo_divido.dividir()
            case 5:
                yo_calculo_resto = operaciones_aritmeticas()
                yo_calculo_resto.resto()
            case 6:
                yo_calculo_exponencial = operaciones_aritmeticas()
                yo_calculo_exponencial.exponencial()
            case 7:
                print("Saliendo.....") 
            case _: print("Valor fuera de los parametros") 

        print("--> Quiere volver a operar ? <--")
        print(" |1|--> Suma  \n |2|--> Resta  \n |3|--> Multiplicacion  \n |4|--> Dsivision  \n |5|--> Resto  \n |6|--> Potencia  \n |7|--> Salir  ")
        valor = int( input ("-->")) 

    print("Saliendo....")
if __name__=="__main__":
    main()
      
"""   
        if valor == 1:
            yo_sumo.sumar()
        elif valor == 2:
            yo_resto.restar()
        elif valor ==3:
            yo_multiplico.multiplicar()
        elif valor == 4:
            yo_divido.dividir()
        elif valor == 5:
            yo_calculo_resto.resto()
        elif valor == 6:
            yo_calculo_exponencial.exponencial()
        elif valor == 7:
            print("Saliendo.......")   
        else :
             print("Opcion fuera de los parametros")         
"""