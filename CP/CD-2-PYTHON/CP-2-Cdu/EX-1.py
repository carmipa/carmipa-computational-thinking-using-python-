def contarSeguimentos(n, numeros):
    if n == 0:
        return 0
    
    segmentos = 1
    for i in range(1, n):
        if numeros[i] != numeros[i-1]:
            segmentos += 1
            
    return segmentos

n = int(input("Digite o número de elementos na sequência: "))
sequencia = []
for j in range(n):
    numero = int(input("Digite um número: "))
    sequencia.append(numero)

resultado = contarSeguimentos(n, sequencia)
print("Número de segmentos de números iguais consecutivos:", resultado)

