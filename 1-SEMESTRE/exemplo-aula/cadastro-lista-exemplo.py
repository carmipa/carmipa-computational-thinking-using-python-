def adiciona(lista, nome, cpf, tel, nascimento):
    lista.append(nome)
    lista.append(cpf)
    lista.append(tel)
    lista.append(nascimento)

bancoDados = []

resp = "s"
while (resposta != 'n'):
    nome = input("nome: ")
    cpf = input("CPF: ")
    telefone = input("tel: ")
    nascimento = input("Nascimento: ")

    resposta = input("Deseja inserir mais alguém (s/n): ")


    adiciona(bancoDados, nome, cpf, telefone, nascimento)
    print(bancoDados)

bancoDados = ["sueli", "29902327885", "(99)9999-9999", "99/99/9999"]
i = 0
while i < len(bancoDados):
    print(f"{i}" - {bancoDados[i] : {bancoDados[i + 3]}})
    i = i + 4

    resp = int(input("Qual pessoa deseja alteral: "))
    nome = input(f"Nome ({bancoDados[resp]}): ))")
    if len(nome) > 0:
        bancoDados[resp + 1] = nome
    cpf = input(f"cpf ({bancoDados[resp + 1]}): ))")
    if len(nome) > 0:
        bancoDados[resp + 2] = telefone
    cpf = input(f"telefone ({bancoDados[resp + 2]}): ))")
    if len(nome) > 0:
        bancoDados[resp + 3] = nome
    cpf = input(f"data de nascimento ({bancoDados[resp + 3]}): ))")
    
    print(bancoDados)