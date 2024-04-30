def calcular_soma_e_contar(n, sequencia):
    soma_maior_que_50 = 0
    quantidade_menor_que_100 = 0
    
    for numero in sequencia:
        if numero > 50:
            soma_maior_que_50 += numero
        if numero < 100:
            quantidade_menor_que_100 += 1
    
    return soma_maior_que_50, quantidade_menor_que_100

# Exemplo de uso
n = int(input("Digite o número de elementos na sequência: "))
sequencia = []
for i in range(n):
    elemento = float(input(f"Digite o {i+1}º número da sequência: "))
    sequencia.append(elemento)

soma, quantidade = calcular_soma_e_contar(n, sequencia)
print("A soma dos números maiores que 50 é:", soma)
print("A quantidade de números menores que 100 é:", quantidade)
