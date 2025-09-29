class Pedido:
    def __init__(self, lista_platos=None):
    
        self.platos = lista_platos if lista_platos else []

    def agregar_plato(self, nuevo_plato):
        self.platos.append(nuevo_plato)

    def calcular_total(self):
        total = sum(plato.precio for plato in self.platos)
        return total

    def ticket(self):
        print("***|MOSTRAR TICKET|***\t")
        print("------------------------")
        for i, plato in enumerate(self.platos, start=1):
            print(f"Nro plato {i}: {plato.nombre} {plato.precio} {plato.categoria.name}")
            print("------------------------")
        total = self.calcular_total()
        print(f"El total a pagar es: {total}")
        print("------------------------")
        print("Propina sugerida (10%):", total * 0.10)
        print("------------------------")
        print("Ticket no valido como factura")
