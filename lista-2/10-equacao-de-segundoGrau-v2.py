import math

while True:
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))

    if (a != 0):
        d = (b ** 2 - 4 * a * c)
        x1 = (-b + d ** (1 / 2)) / (2 * a)
        x2 = (-b - d ** (1 / 2)) / (2 * a)
        
        print("Valor de x1:", x1)
        print("Valor de x2:", x2)
        break
    else:
        print("'a' tem de ser diferente de '0'!")