nome = input("nome: ")
idade = int(input("Idade: "))

if (idade >= 5 and idade <= 7):
    print(nome, idade, "Infantil")
elif(idade  >= 8 and idade <= 10):
    print(nome, idade, "Juvenil")
elif(idade >= 11 and idade <= 15):
    print(nome, idade, "Adolescente")
elif(idade >= 16 and idade <= 30):
    print(nome, idade, "Adulto")
elif(idade > 30):
    print(nome, idade, "Senior")