cpf = int(input("Digite CPF: "))

digitos = cpf % 100
cpf = cpf // 100
cpf3 = cpf % 1000
cpf = cpf // 1000

cpf2 = cpf % 1000   
cpf3 = cpf % 1000

print(cpf".", cpf2 , "." , cpf3 , "-" ,cpf1)