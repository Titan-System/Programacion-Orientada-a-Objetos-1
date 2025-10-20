

class Producto:
    def __init__(self):
        self.__codigo_de_producto = int(input ("ingrese el codigo de producto: "))
        self.__descripcion = str(input ("ingrese la descripcion del producto: "))
        self.__precio = float(input ("ingrese el precio del producto: "))
        self.__stock = int(input("ingrese el stock del producto: "))
    
    
    @property
    def codigo_de_producto(self):
        return self.__codigo_de_producto
    
    @codigo_de_producto.setter
    def codigo_de_producto(self,nuevo_codigo_producto):
        self.__codigo_de_producto = nuevo_codigo_producto
        
        
        
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self,nueva_descripcion):
        self.__descripcion = nueva_descripcion
        
     
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,nuevo_precio):
        self.__precio = nuevo_precio
        
        
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self,nuevo_stock):
        self.__stock = nuevo_stock        
        
        
    
    
    
        
    def borrar(self):
        pass
        
    def modificar(self):
        pass
    
    def mostrar_lista(self):
        pass    
        
        