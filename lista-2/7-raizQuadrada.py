import math

raiz = int(input("Entre com um número para saber sua raiz quadrada: "))

raizQ = math.sqrt(raiz)

if(raiz < 0):
    print("A raiz quadrada de:", raiz, " é ", raizQ)
else:
    print("não é possível fazer a razia quadrada")