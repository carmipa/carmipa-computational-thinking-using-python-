# mmc python

numA = 6
numB = 8

inicio = 1
fim = 100

while True:
    if (numA != numB):
        for i in range(inicio, fim +1):
            if i % numA == 0:
                for j in range(inicio, fim +1):
                    if j % numB == 0:
                        print(i,j)
    else:
        print(i,j)
    break
########################################################



#a = int (input("Informe A: "))
#b = int (input("Informe B: "))

#x = a

#while x % b != 0:
#    x = x + a
#print("menor multiplo de A e B é: ", a , b)

#def mmc(a, b):
#   x = x + a
#    while x % b != 0:
#        x = x + a

