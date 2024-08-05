n1 = float(input("Número 1:"))
n2 = float(input("Número 1:"))
n3 = float(input("Número 1:"))
n4 = float(input("Número 1:"))



if(n1 <= 0 or n2 <= 0 or n3 <= 0 or n3 <= 0):
    
    mediaAritimetica = (n1 + n2 + n3 + n4)/4
    print("Média aritimética é igual a =", mediaAritimetica)

elif(n1 > 0 and n2 > 0 and n3 > 0 and n4 > 0):

    mediaGeometrica = (n1 * n2 * n3 * n4) ** 0.25
    print("A media geométrica é igual a =", mediaGeometrica)