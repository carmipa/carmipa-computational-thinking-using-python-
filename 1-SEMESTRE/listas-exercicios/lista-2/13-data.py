while True:
    print(".............................................................")
    print("Regra:", 
        "\n1- dia, mês e ano devem ser números inteiros",
        "\n2- O ano deve ser digitado com 4 digitos",
        "\n3- O mês deve ser digitado o número")

    print(".............................................................")
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    print(".............................................................")
    
    if(dia > 0 and dia <= 31):
        print("O dia está correto!")
    elif(dia <= 0 and dia >= 31):
        print("Dia digitado de forma errada!")

    if(mes > 0 and mes <= 12):
        ("O mês está correto")
    elif(mes <=0 and mes >12):
        print("mês digitado de forma errada!")

    if(ano >0 and ano <= 9999):
        ("O ano está correto")
    elif(ano <= 0 and ano > 9999):
        print("Ano está digitado de forma incorreta!")
    
    
    
    
    