num = int(input("Digite o número: "))
num_back = num
soma = 0

while (num != 0):
    
    dig = num % 10
    soma = soma * 10 + dig
    num = num // 10

# print(soma)

if (num_back == soma):
    print("é palindromio")
else:
    print("Não é palindromo")