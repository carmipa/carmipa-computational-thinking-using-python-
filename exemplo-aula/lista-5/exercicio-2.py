def verificaInteiro(n):
    
    if(n % 2 == 0):
        return True
    else:
        return False 

print(verificaInteiro(2))
print(verificaInteiro(1))

numero = int(input("Digite um número para saver se é primo: "))

if(verificaInteiro(numero)):
    print("é primo")
else:
    print("não é primo")

