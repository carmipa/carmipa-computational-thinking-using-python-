import math

def mediaGeometrica(numero1 : float, numero2 :float):
    mult = (numero1 * numero2)
    geometrica = math.sqrt(mult)
    
    return geometrica

print(f"A média geométrica é: {mediaGeometrica(10, 30)}")