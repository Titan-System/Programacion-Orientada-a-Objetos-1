#Para entender Constructor sobrecargado y el uso de getter y setter.
#Vamos a usar dos clases, en la Main es donde está el método main().
#En los próximos programas que hagan, siempre usen la clase Main desde donde se prueba todo lo 
#que quieran que haga el programa.En la clase Main estará Siempre el método main() donde se crean los Objetos #de otra u otras clases y se les pide que hagan todos los métodos de la otra u otras clases.

import os
class Alumno:
  def __init__(self, __nombre, __edad, __promedio):     
     self.__nombre= input("Nombre: ")             
     self.__edad= int(input("Edad: "))      	
     self.__promedio= float(input("Promedio: "))

  
  @property
  def nombre(self):
    return self.__nombre

  @nombre.setter
  def nombre(self, nuevo_nombre):
    self.__nombre = nuevo_nombre

  @property
  def edad(self):
     return self.__edad
  @edad.setter
  def edad(self, nueva_edad):
    self.__edad = nueva_edad

  @property
  def promedio(self):
    return self.__promedio

  @promedio.setter
  def promedio(self, nuevo_promedio):
    self.__promedio = nuevo_promedio

  
  