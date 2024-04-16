def fibonacci(n):
    fib_sequence = [0, 1]  # Inicializa a sequência com os dois primeiros números
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]  # Calcula o próximo número
        fib_sequence.append(next_fib)  # Adiciona o próximo número à sequência
    return fib_sequence

# Exemplo: Calculando os primeiros 10 números da sequência de Fibonacci
n = 10
fib_numbers = fibonacci(n)
print(f"Os primeiros {n} números da sequência de Fibonacci são:")
print(fib_numbers)