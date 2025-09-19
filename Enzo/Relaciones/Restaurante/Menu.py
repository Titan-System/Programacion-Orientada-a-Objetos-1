from plato import Plato
from Pedido import Pedido
from categoria_plato import categoria_plato

class Menu:
    
    def __init__(self,):
       self.__lista_menu = ["Milanesa Napolitana","Ravioles","Pesca del dia","Ensalada Cesar","Papas con cheddar y bacon","Tequeños","Empanadas fritas","Provoleta","Flan","Volcan de chocolate","Coca Cola","Agua sin gas"]  
       
    @property
    def lista_menu(self):
        return self.__lista_menu    
    
    def seleccionar_plato(self, num):
        i = 0
        for l in self.__lista_menu:
            i += 1
            if num == i:
                return self.__lista_menu[i-1]
    
    def select_categoria(self, cat):
        match cat:
            case 1:
                print("Categoria seleccionada: Entrada")
                return categoria_plato.ENTRADA
            case 2:
                print("Categoria seleccionada: Plato principal")
                return categoria_plato.PRINCIPAL
            case 3:
                print("Categoria seleccionada: Postre")
                return categoria_plato.POSTRE
            case 4:
                print("Categoria seleccionada: Bebida") 
                return categoria_plato.BEBIDA
            case _:
                print("Categoria no valida")
                pass
                
                           
    def mostrar_menu(self):
        i = 0
        print("Lista de platos -->")
        lista_menu = ["Milanesa Napolitana","Ravioles","Pesca del dia","Ensalada Cesar","Papas con cheddar y bacon","Tequeños","Empanadas fritas","Provoleta","Flan","Volcan de chocolate","Coca Cola","Agua sin gas"]              
        
        for p in lista_menu:
            i +=1
            print("Nro plato",i,f"{lista_menu[i-1]}")   
            print("------------------------") 
    def crear_menu(self):
        print("Desea iniciar el programa ? |S| SI /// |N| NO")
        op = input("--> ").upper()
        p1 = Menu() 
        lista_pedido = [] 
        while op != "N":
    
            print("----------------------------------")
            print("---------|    INICIO MENU    |----")
            print(" *|1|--> |MENU DE RESTAURANTE|    ")
            print(" *|2|--> |AGREGAR PEDIDO     |    ")
            print(" *|3|--> |MODIFICAR PEDIDO   |    ")
            print(" *|4|--> |MOSTRAR TICKET     |    ")
            print(" *|6|--> |SALIR DEL MENU     |    ")
                
            on = int(input("Ingrese Nro opcion --> "))
   
            match on:
                    case 1:
                        print("***|MENU|***\t")
                        
                        p1.mostrar_menu()
                        
                    case 2:
                    
                        lista_platos = []
                        p1.mostrar_menu()
                        print("***|AGREGAR PEDIDO|***\t")
                        print("------------------------")

                        print("|CATEGORIAS DE PLATOS|")
                        print("|1| Entradas\n|2| Platos principales\n|3| Postres\n|4| Bebidas\n|0| Salir")
                        num = int(input("Ingrese categoria del plato --> "))

                        while num != 0:
                            print("------------------------")
                            print("Ingrese el Nro de la lista  que desea agregar al pedido\t")
                            sp = int(input("--> "))
                            print(f"Plato {p1.seleccionar_plato(sp)} agregado al pedido")

                            if categoria_plato.ENTRADA.value == num:
                                nueva_categoria = categoria_plato.ENTRADA
                            elif categoria_plato.PRINCIPAL.value == num:
                                nueva_categoria = categoria_plato.PRINCIPAL
                            elif categoria_plato.POSTRE.value == num:
                                nueva_categoria = categoria_plato.POSTRE
                            elif categoria_plato.BEBIDA.value == num:
                                nueva_categoria = categoria_plato.BEBIDA

                            nuevo_nombre = p1.seleccionar_plato(sp)   
                            nuevo_precio = float(input("Ingrese precio del plato: "))
                            nuevo_plato = Plato(nuevo_precio, nuevo_nombre, nueva_categoria)

                            lista_platos.append(nuevo_plato)

                            print("------------------------")
                            print("QUIERE AGREGAR OTRO PLATO ? \n|1| Entradas\n|2| Platos principales\n|3| Postres\n|4| Bebidas \n|0| NO,SALIR")
                            num = int(input("Ingrese la opcion para continuar --> "))
                        nuevo_pedido = Pedido(lista_platos)
                        lista_pedido.append(nuevo_pedido)

                    case 3:
                       
                            print("***|MODIFICAR PEDIDO|***\t")

                            for i, pedido in enumerate(lista_pedido, start=1):
                                print(f"Nro pedido {i}:")
                                for pla in pedido.platos:  
                                    print(f"   - {pla.nombre} {pla.precio} {pla.categoria.name}")
                                    print("------------------------")

                            mo = int(input("Ingrese Nro del pedido --> "))

                            for i in range(len(lista_pedido)):
                                if (mo-1) == i:
                                    print("Que plato desea modificar\t")
                                    print("-->")
                                    pedido = lista_pedido[mo-1]   
                                    for j, pla in enumerate(pedido.platos, start=1):  
                                        print(f"Nro plato {j}: {pla.nombre} {pla.precio} {pla.categoria.name}")

                            pl = int(input("Ingrese Nro plato --> "))

                            for k in range(len(pedido.platos)):  
                                if (pl-1) == k:
                                    plato_modif = pedido.platos[pl-1]  
                                    print(plato_modif.nombre, plato_modif.precio, plato_modif.categoria.name)
                                    on = int(input("|1| Modificar nombre\n|2| Modificar precio\n|3| Modificar categoria\n|4| Salir\n--> "))
                                    match on:
                                        case 1:
                                            nuevo_nombre = input("Ingrese nuevo nombre: ")
                                            plato_modif.nombre = nuevo_nombre   
                                        case 2:
                                            nuevo_precio = float(input("Ingrese nuevo precio: "))
                                            plato_modif.precio = nuevo_precio   
                                        case 3:
                                            print("|CATEGORIAS DE PLATOS|")
                                            print("|1| Entradas\n|2| Platos principales\n|3| Postres\n|4| Bebidas\n")
                                            nueva_cat = int(input("Ingrese nueva categoria del plato --> "))
                                            plato_modif.categoria = p1.select_categoria(nueva_cat)   
                                        case 4:
                                            print("Saliendo...")
                                        case _:
                                            print("Opcion fuera de los parametros")


                    case 4:
                        print("***|MOSTRAR TICKET|***\t")
                        
                        for i, pedido in enumerate(lista_pedido, start=1):
                            print(f"Nro pedido {i} ({len(pedido.platos)} platos)")
                        num = int(input("Ingrese el nro de pedido que desea ver --> "))
                        if 1 <= num <= len(lista_pedido):
                            pedido = lista_pedido[num-1]  
                            pedido.ticket()                
                        else:
                            print("Número de pedido inválido")
                    case 5:
                        pass
                    case 6:
                        print("Saliendo del menu...")
                    
                    case _:
                        print("Opcion incorrecta, intente nuevamente")                    
            
            print("Desea continuar con el programa ? |S| SI /// |N| NO")
            op = input("--> ").upper()
        print("Saliendo del programa.....")                 
 
    
    
     
     
     
    
    
    
    