


class Peliculas:
    def __init__(self):
        pass
    
    
titulos = ('Volver al futuro', 'El señor de los anillos', 'El Padrino')

precio = [20, 30, 40]

peliculas = dict(zip(titulos, precio))
band = 0
band2 = 0
maximo = 0
minimo = 0
for p, t in peliculas.items():
    if band == 0:
        maximo = t
        minimo = t
        band = 1
    else:
        if t > maximo:
            maximo = t
        if t < minimo:
            minimo = t

    print(p, t)
print("la pelicual mas cara es: ", maximo)
print("la pelicual mas barata es: ", minimo)
                       
                       
                       
                       
    



    