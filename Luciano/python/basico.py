#Introduccion a python con rpogramas faciles

# print('hola mundo')

#hola mundo en variables

# P1='hola'
# p2='mundo'

# print(P1,p2)

#Hola usuarios

# juan=input("Ingrese su nombre: ")

# print("hola: "+juan)

#operacion aritmetica

# resultado= (3+2/2*5)**2

# print(resultado)

#Suma

# varol= int(input("Ingrese el primer valor: "))

# varol+=int(input("Ingese el segundo valor: ")

# print("la suma es: ",varol)

#Pago

# Horas=int(input("Ingrese las horas trabajadas: "))
# Horas*=int(input("Ingrese el pago por horas trabajadas: "))


# print("El pago que le corresponde es: ",Horas)

# num=int(input("Ingrese un numero: "))

# for i in range(num):
#     print(i+1)

# IMC

# Kg=int(input("ingrse su indice su peso: "))
# Alt= float(input("Ingrese su altura: "))

# IMC=float(Kg/Alt*Alt)

# print("tu IMC es: ",IMC)

#Cociente y resto

# num1=int(input("Ingrese el primer valor: "))
# num2=int(input("Ingrese el Segundo valor: "))


# print("la suma es: ",num1+num2)
# print("la resta es: ",num1-num2)
# print("la multiplicacipo: ",num1*num2)
# print("el resto es: ",num1 % num2)

#Iversion 

# Dinero=int(input("Ingrese el dinero a invertir: "))
# interes=int(input("Ingrese el dinero a invertir: "))
# retorno = Dinero + (Dinero * interes / 100)

# print("El retorno de la inversion anual es: ",retorno)
# print("El rendimiento es: ",interes,"%")

#Jugueteria 

munieca=0
autos=0
pM=0
pA=0

while True:
    print("\nMenu")
    print("1. Muniecas")
    print("2. Autos")
    print("3. salir")

    op=int(input("Ingrese su accion: "))

    if op == 1:
        munieca+=1
        pM+=75
        
    elif op == 2:
        autos+=1
        pA+=112
    elif op ==3:

        print("saliendo del programa..")
        break
    else:
        print("opcion invalida, intenta de nuevo. ")


print("La cantidad de muniecas total es: ",munieca)
print("El peso total de las muniecas acumulda es: ",pM)

print("La cantidad total de autos es: ",autos)
print("El peso total de los autos acumulda es: ",pA)


print("El peso acumulado total es: ",pM+pA)
