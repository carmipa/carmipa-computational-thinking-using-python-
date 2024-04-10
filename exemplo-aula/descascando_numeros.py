# escreva um programa que recebe um número inteiro  representando um cpf
# e imprim ca um dos digitos
# ex: cpf = 23430938107
# apareça na tela os seguinte digitos 7, 0, 1, 8, 3, 9, 0, 3, 4, 3, 2

import os

os.system("cls") 

cpf = int(input("Informe o CPF: "))

# guada a resposta
resp = ""

while (cpf != 0):
    # pega o resto da divisao
    dig = cpf % 10
    resp = resp + str(dig) + ' , '

    # guarda o divisor
    cpf = cpf // 10

print(resp)    