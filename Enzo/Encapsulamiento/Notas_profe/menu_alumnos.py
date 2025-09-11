from alumnos import Alumno
import os
class menu:
    def __init__(self):
        
       
            print("***|MENU|***\t")
            lista_alumnos = []
            i = 0
            print("Ingrese la opcion\t")
            print("|1| Carga de Alumnos\n|2| Modificacion de Alumnos\n|3| Eliminacion de Alumnos\n|4| Mostrar lista\n|5| Salir")
            Op = int(input("--> "))

            while Op != 5:

                match Op:

                    case 1:
                            os.system("cls")
                            alumno = Alumno("",0,0.0)
                            lista_alumnos.append(alumno)
                        
                            print("Lista de alumnos -->")
                            i = 0
                            for alu in lista_alumnos:
                                i += 1
                                print("Nro alumno",i,f"{alu.nombre, alu.edad, alu.promedio}")
                            os.system("cls")
                            print("Alumno cargado correctamente")
                            print("------------------------")    
                                
                    case 2:
                            os.system("cls")
                            print("Lista de alumnos -->")
                            i = 0
                            for alu in lista_alumnos:
                                i += 1
                                print("Nro alumno",i,f"{alu.nombre, alu.edad, alu.promedio}")
                                

                            print("Que alumno desea modificar\t")
                            print("-->")
                            mo = int(input("Ingrese Nro alumno --> "))
                            
                            for i in range(len(lista_alumnos)):
                                if (mo-1) == i:
                                    print(lista_alumnos[mo-1].nombre, lista_alumnos[mo-1].edad, lista_alumnos[mo-1].promedio) 
                                    on = int(input("|1| Modificar nombre\n|2| Modificar edad\n|3| Modificar promedio\n|4| Salir\n--> "))
                                    match on:
                                            case 1:
                                                nuevo_nombre = input("Ingrese nuevo nombre: ")
                                                lista_alumnos[mo-1].nombre = nuevo_nombre
                                            case 2:
                                                nueva_edad = int(input("Ingrese nueva edad: "))
                                                lista_alumnos[mo-1].edad = nueva_edad
                                            case 3:
                                                nuevo_promedio = float(input("Ingrese nuevo promedio: "))
                                                lista_alumnos[mo-1].promedio = nuevo_promedio
                                            case 4:
                                                print("Saliendo...")
                                            case _: 
                                                print("Opcion fuera de los parametros")                
                                
                            """alumno_a_modificar = Alumno("",0,0.0)
                            lista_alumnos.pop(mo-1)
                            lista_alumnos.insert(mo-1,alumno_a_modificar)
                            os.system("cls")"""
                            
                            
                            print("Modificado correctamente")
                            print("------------------------") 
                            print("Nueva lista ->")
                            i = 0
                            for alu in lista_alumnos:
                                i += 1
                                print("-> Nro alumno",i,f"{alu.nombre, alu.edad, alu.promedio}")
                                
                    case 3:
                            os.system("cls")
                            print("|Lista de alumnos| -->")
                            i = 0
                            for alu in lista_alumnos:
                                i += 1
                                print("->Nro alumno",i,f"{alu.nombre, alu.edad, alu.promedio}")
                                

                            print("Que alumno desea eliminar?\t")
                            print("-->")
                            el = int(input("Ingrese Nro alumno --> "))
                            lista_alumnos.pop(el-1)
                            os.system("cls")
                            print("Eliminando.......")
                            print("eliminado correctamente")
                            print("------------------------") 
                            print("-->|lista actualizada|<--")
                            i = 0
                            for alu in lista_alumnos:
                                i += 1
                                print(" -> Nro alumno",i,f"{alu.nombre, alu.edad, alu.promedio}")
                    case 4:
                            os.system("cls")
                            print("\t-->| lista de alumnos |<--")
                            i = 0
                            for alu in lista_alumnos:
                                i += 1
                                print("->Nro alumno",i,f"{alu.nombre, alu.edad, alu.promedio}")
                            print("\t<- - - - - - - - - - - - - - - -> ")    
                            
                    case 5:
                            print("Saliendo...")       
                    case _: 
                            
                            print("opcion fuera de los parametros")                
                        
                print("Ingrese la opcion nuevamente\t")
                print("|1| Carga de Alumnos\n|2| Modificacion de Alumnos\n|3| Eliminacion de Alumnos\n|4| Mostrar lista\n|5|Salir")
                Op = int(input("--> "))    
            print("Saliendo...")   
                