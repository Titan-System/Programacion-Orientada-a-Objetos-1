

class Verduleria:
    def __init__(self):
        pass
    
frutas = {}

frutas["platano"] = 1.35
frutas["manzana"] = 0.8
frutas["naranja"] = 0.7
frutas["pera"] = 0.85

op = int(input("desea ingreasar al programa |1| si |2| no"))
while op == 1:
    f = input("que fruta desea llevar?: ")
    
    
    if f not in frutas:
        print("la fruta ", f, " no se encuentra en la verduleria")
    else:
        k = float(input("cuantos kilos desea llevar?: "))
        total = frutas[f] * k
        
        print("el total del valor de la fruta es :",total,"por los ",k,"kg ")
            
        

    #entrada = input("desea llevar otra fruta?: ")





