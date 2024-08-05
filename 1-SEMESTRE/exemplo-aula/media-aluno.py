aux = input("digite a primeira nota:")
nota1 = float(aux)

while nota1 < 0 or nota1 > 10:
    aux = input("Nota inválida, digite a 1ª nota: ")
    nota1 - float(aux)

aux = input("Digite a 2 nota: ")
nota2 = float(aux)

while nota1 < 0 or nota1 > 10:
    aux = input("Nota inválida, digite a 2 nota: ")
    nota2 = float (aux)

media = (nota1 + nota2) / 2
print("a média vale:", media) 