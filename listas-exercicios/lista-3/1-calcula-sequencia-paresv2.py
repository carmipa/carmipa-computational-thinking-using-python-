# Inicializa a variável para armazenar a soma dos números pares
soma_pares = 0

# Coleta os números dos usuários até que o valor digitado seja 0
while True:
    try:
        numero = int(input("Digite um número (0 para encerrar): "))
        if numero == 0:
            break
        if numero % 2 == 0:
            soma_pares += numero
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Exibe a soma dos números pares
print(f"A soma dos números pares é: {soma_pares}")