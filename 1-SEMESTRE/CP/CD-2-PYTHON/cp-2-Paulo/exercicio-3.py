x = int(input("Digite o valor da cédula (x): "))
a = int(input("Digite o valor da moeda a: "))
b = int(input("Digite o valor da moeda b: "))

quantidadeA = x // a
quantidadeB = (x - quantidadeA * a) // b

if (quantidadeA * a + quantidadeB * b == x):
    print(f"É possível efetuar a troca. Quantidade de moedas a: {quantidadeA}, moedas b: {quantidadeB}")
else:
    print("Não é possível efetuar a troca com as moedas disponíveis.")