from Figura import Figura
import math
class Circulo(Figura):
 def __init__(self):
  self.__radio = int(input("Ingrese el tamaño del radio del circulo: "))
 
 def calcular_area(self):
  return self.__radio * self.__radio * math.pi