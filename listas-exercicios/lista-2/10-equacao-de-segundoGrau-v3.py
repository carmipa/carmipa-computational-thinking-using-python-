import math

while True:
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))

    d = (b ** 2 - 4 * a * c)

    if d >= 0:
        # Calcula as raízes reais
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("Valor de x1:", x1)
        print("Valor de x2:", x2)
    else:
        # Calcula as raízes complexas
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-d) / (2 * a)
        print("Valor de x1:", complex(real_part, imaginary_part))
        print("Valor de x2:", complex(real_part, -imaginary_part))
    break