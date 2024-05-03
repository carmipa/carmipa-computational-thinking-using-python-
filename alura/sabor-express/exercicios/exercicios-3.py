# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
lista_4_nomes = ["Paulo", "André", "Carminati", "Bormanas",]
lista_ano = [1979, 2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

lista_padarias = ["Fabrique - pão e café", "Padária - Favos de mél"]

for padarias in lista_padarias:
        print(f".{padarias}")
        
# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

impares = []

for num in range(1, 11):
    if num % 2 != 0:
        impares.append(num)

print(f"Números ímpares de 1 a 10: {impares}")

soma = sum(impares)

print(f"A soma dos valores é: {soma}")

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para 
# imprimir a tabuada desse número, indo de 1 a 10./

numero = int(input("Digite um número para saber sua tabuada: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    
    resultado = numero * i
    
    print(f"{numero} * {i} = {resultado}")
    

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma 
# de todos os elementos. Utilize um bloco try-except para lidar com 
# possíveis exceções.

lista_numeros = [55, 100, 200, 1000, 8, 1979]
contador = 0

try:
    for numeros in lista_numeros:
        contador += numeros
    print("A soma dos numeros é: " , contador)
except Exception as e:
    print(f"erro: {e}")

# 7 - Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")