numeros1 = int(input("Digite a quantidade de números que você deseja: "))
soma = 0

while (numeros1 > 0):
        
    inteiro1 = int(input(f"Digite {numeros1} números inteiros positivos: "))
    
    if(inteiro1 < 0):
        print("Número tem de ser positivo")
    else:
        soma += inteiro1
        numeros1 -= 1

print(f"A soma de todos os números inteiros é: {soma}")       

