from Figura import Figura
class Rectangulo(Figura):
 def __init__(self):
  self.__altura = int(input("Ingrese la altura del rectangulo: "))
  self.__base = int(input("Ingrese la base del rectangulo: "))
 
 def calcular_area(self):
  return self.__altura * self.__base