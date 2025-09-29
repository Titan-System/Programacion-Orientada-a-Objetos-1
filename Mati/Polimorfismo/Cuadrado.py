from Figura import Figura
class Cuadrado(Figura):
 def __init__(self):
  self.__lado = int(input("Ingrese el tamaño de los lados del cuadrado: "))
 
 def calcular_area(self):
  return self.__lado * self.__lado