from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Circulo import Circulo
from Figura import Figura

class Main:

  @staticmethod
  def mf(f:Figura):
    return f.calcular_area()
 
def main():
  
  c = Cuadrado()
  r = Rectangulo()
  ci = Circulo()

  print ("El resutaldo es: ",Main.mf(c)) 
  print ("El resutaldo es: ",Main.mf(ci)) 
  print ("El resutaldo es: ",Main.mf(r))                       

if __name__ == "__main__":
 main()