entrada = input("Digite uma string: ")

invertida = ""

i = len(entrada) - 1
while (i >= 0):
    invertida += entrada[i]
    i -= 1

print("String invertida:", invertida)