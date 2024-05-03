def contar_segmentos_iguais(n, numeros):
    if n == 0:
        return 0
    
    segmentos = 1
    for i in range(1, n):
        if numeros[i] != numeros[i-1]:
            segmentos += 1
            
    return segmentos

# Entrada de dados
n = int(input("Digite o número de elementos na sequência: "))
sequencia = []
for _ in range(n):
    numero = int(input("Digite um número: "))
    sequencia.append(numero)

# Chamada da função e impressão do resultado
resultado = contar_segmentos_iguais(n, sequencia)
print("Número de segmentos de números iguais consecutivos:", resultado)

