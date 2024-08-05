# calcula número perfeito

def perfeito(n):
    div = 1
    soma = 0

    while div < n:
        if n % div == 0:
            soma = soma + div
        div = div + 1
    
    if n == soma:
        return True
    else:
        return False
    
resp = perfeito(6)
print(resp)