
numeroInteiro = int(input("Digite um número inteiro positivo: "))

contaSegmentos = 0
segmentoAtual = 1

anterior = int(input("Digite o primeiro número: "))

for i in range(numeroInteiro - 1):

    atual = int(input("Digite o próximo número: "))
    
    if (atual == anterior):
        segmentoAtual += 1
    else:
        contaSegmentos += 1
        segmentoAtual = 1
    
    anterior = atual

contaSegmentos += 1

print(f"Quantidade de segmentos de números iguais: {contaSegmentos}")


