numeroInteiro = int(input("Digite um número inteiro: "))


somaMaiores = 0
contaMenores = 0


for i in range(numeroInteiro):
    numero = float(input("Digite um número real: "))
    

    if (numero > 50):
        somaMaiores += numero

    if (numero < 100):
        contaMenores += 1

print(f"Soma dos números maiores que 50: {somaMaiores}")
print(f"Quantidade de números menores que 100: {contaMenores}")