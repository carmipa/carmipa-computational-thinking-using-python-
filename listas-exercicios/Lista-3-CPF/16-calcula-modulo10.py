
num = int(input("Digite um número: "))

soma = 0 
mult = 2

while num != 0:
    dig = num % 10
    prod = dig * mult
    soma = soma + prod // 10 + prod % 10
    if mult == 2:
        multi =1
    else:
        mult = 2
    num = num // 10
resto = soma % 10

