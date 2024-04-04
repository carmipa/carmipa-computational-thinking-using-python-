def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(950)
print(f"O fatorial de 20 é **{resultado}**.")