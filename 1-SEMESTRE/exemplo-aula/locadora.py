


while True:
    
    print("LOCADORA FIAP")
    print("1 - Alugar Carro")
    print("2 - Cadastra Cliente")
    print("3 - Consulta Carro Disponível")
    print("4 - Análise de Crédito")
    print("5 - Fale Conosco")
    print("6 - Sair")

    opcao = int(input("Digite a opção desejada: "))
    
    if(opcao == 1):
        CPF = int(input("informe o CPF"))
        categoria = input(("Informe a categoria (básico, premium e luxo):"))
        print("cod: 239 BMW 2020 R$ 500")
        print("cod: 284 Audi q3 R$ 420,00")
        print("cod: 267 Mercedez Bens 2022 R$ 580,00")
        codigo = int(input("Escolha o carro:"))
        dias = int(input("informe a quantidade de dias: "))
        print(f"Você alugou um q3 e vai pagar {dias * 420}")
    
    elif(opcao == 2):
        pass
    
    elif(opcao == 3):
        pass
    
    elif(opcao == 4):
        pass
    
    elif(opcao == 5):
        email = input("informe o e-mail")
        pergunta = input("Mais tarde entraremos em contato ou responderemos sua pergunta!")
    
    elif(opcao == 6):
        ("Obrigado por usar nosso sistema")
    
    elif(opcao != 1 or opcao != 2 or opcao != 3 or opcao != 4 or opcao != 5 or opcao != 6):
        print("opcao inválida")
        print("Digite uma opção válida!")
        