soma = 0

while True:
    numero = int(input("Digite um número (0 para encerrar): "))
    if (numero == 0):
        break
    elif(numero %2 == 0):
        soma += numero
    else:
        print("Digite um número inteiro válido")    

print("A soma dos números pares é:", soma)