# 1 - Solicite ao usuário que insira um número e, em seguida, use uma 
# estrutura if else para determinar se o número é par ou ímpar.

numero = int(input("Digite um número para sabe se ele é par ou impar: "))

if(numero % 2 == 0):
    print(f"Número digitado é par: {numero}")
else:
    print(f"Número digitado não é par: {numero}")

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura 
# if elif else para classificar a idade em categorias de acordo com as seguintes condições:

idade = int(input("Digite a sua idade: "))

if(idade > 0 and idade <= 12):
    print(f"Você é uma criança. Sua idade é: {idade}")
elif(idade >= 13 and idade <= 18):
    print(f"Você é um adolescente. SUa idade é: {idade}")
elif(idade > 18):
    print(f"Você é adulto. Sua idade é: {idade}")

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar
# se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

qx = float(input("Digite o eixo X: "))
qy = float(input("Digite o eixo y: "))

if (qx > 0 and qy > 0):
    print("O ponto está no primeiro quadrante.")
elif (qx < 0 and qy > 0):
    print("O ponto está no segundo quadrante.")
elif (qx < 0 and qy < 0):
    print("O ponto está no terceiro quadrante.")
elif (qx > 0 and qy < 0):
    print("O ponto está no quarto quadrante.")
else:
    print("o ponto está localizado no eixo ou origem")