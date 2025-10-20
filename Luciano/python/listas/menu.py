
from producto import Producto

class Menu:
    def __init__(self):
        pass
   
def main():
    lista_productos = []
    on = int(input("Desea ingresar al programa? \n|1|SI \n|2|NO\n-->"))
    while on == 1 :
    
     op = int(input ("|1| ALTA \n|2| BAJA\n|3|MODIFICACION\n|4|MOSTRAR PRODUCTOS ESCASOS\n|5|MOSTRAR LISTA PORDUCTOS\n|6|MOSTRAR LISTA+ 10%\n|7|SALIR\n-->"))
     
     match op:
        case 1:
            pro = Producto()
            lista_productos.append(pro)
            for p in lista_productos:
                print(p.descripcion)
        case 2:
                i=0
                for p in lista_productos:
                    i+=1
                    print("#- Nro prducto",i,"||",p.codigo_de_producto,"--",p.descripcion,"--", p.precio,"--", p.stock)
                op2 = int(input("Que numero de pructo desea eliminar : "))
                lista_productos.pop(op2 - 1)
        case 3:
                i=0
                for p in lista_productos:
                    i+=1
                    print("#- Nro prducto",i,"||",p.codigo_de_producto,"--",p.descripcion,"--", p.precio,"--", p.stock)
                op3 = int(input("Que numero de pructo desea modificar : "))
                
                for i in range(len(lista_productos)):
                                if (op3-1) == i:
                                    print(lista_productos[op3-1].codigo_de_producto, lista_productos[op3-1].descripcion, lista_productos[op3-1].precio, lista_productos[op3-1].stock) 
                                    on = int(input("|1| Modificar codigo\n|2| Modificar descripcion\n|3| Modificar precio\n|4| Modificar stock\n |5| Salir\n--> "))
                                    match on:
                                            case 1:
                                                nuevo_codigo_producto = input("Ingrese nuevo codigo: ")
                                                lista_productos[op3-1].codigo_de_producto = nuevo_codigo_producto
                                            case 2:
                                                nueva_descripcion = input("Ingrese nueva descripcion: ")
                                                lista_productos[op3-1].descripcion = nueva_descripcion
                                            case 3:
                                                nuevo_precio = int(input("Ingrese nuevo precio: "))
                                                lista_productos[op3-1].precio = nuevo_precio
                                            case 4:
                                                nuevo_stock = int(input("Ingrese nuevo stock: "))
                                                lista_productos[op3-1].stock = nuevo_stock
                                            case 5:
                                                print("Saliendo...")
                                            case _: 
                                                print("Opcion fuera de los parametros")
        case 4:
                i=0
                for p in lista_productos:
                 if p.stock < 50 :
                  i+=1
                  print("#- Nro prducto",i,"||",p.codigo_de_producto,"--",p.descripcion,"--", p.precio,"--", p.stock)    
        case 5:
                i=0
                for p in lista_productos:
                 i+=1
                 print("#- Nro prducto",i,"||",p.codigo_de_producto,"--",p.descripcion,"--", p.precio,"--", p.stock)
        case 6:
                i=0
                for p in lista_productos:
                 i+=1
                 print("#- Nro prducto",i,"||",p.codigo_de_producto,"--",p.descripcion,"--", p.precio*1.1,"--", p.stock)
                
        case 7:
            print("Saliendo......")        
        case _:
            print("valor incorrecto")
     on = int(input("Desea ingresar otra vez al  programa? |1|SI \n|2|NO\n-->"))       
                 
            
            
if __name__ == "__main__":
    main()            