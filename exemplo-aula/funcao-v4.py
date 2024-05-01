# calcula fatorial

def fatoria(n):
    prod = 1
    while n >= 1:
        prod = prod * n
        n = n - 1
    return prod

fat = fatoria(6)
print(fat)