while True:
    # menu de cadastro
    print("\n")
    print("****************** PORTO SEGURO - OFICINAS ******************")
    print("\n")
    print("Escolha uma das opções abaixo:")
    print("\n")
    print("1 - Cadastro")
    print("2 - Cadastro de Veiculo")
    print("3 - Descrição do Defeito")
    print("4 - Agendar Oficina")
    print("5 - Orçamento e pagamento")
    print("6 - Pagamento")
    print("7 - Indicar uma Oficina para convênio")
    print("0 - Sair")
    print("\n")
    opcao = int(input("Digite a opção desejada: "))
    print("\n")
    print("*************************************************************")

    # Nessa opção é possível fazer o cadastro de um novo usuário/cliente ou pesquisar por um usuário existente
    if(opcao == 1):
    
        while True:
            print("\n")
            print("CADASTRO")
            print("1 - Pesquisar usuário")
            print("2 - Novo usuário")
            print("0 - Menu princípal")
            print("\n")
            opcao = int(input("Digite a opção desejada: "))
            print("\n")

            if (opcao == 1):
                # faz a pesquisa se o usuário existe ou não no sistema
                while True:
                    # usuário cadastrado para teste:
                    cli1 = 1
                    cli2 = 2
                    cli3 = 3

                    codigo = int(input("Digite o código do usuário: "))

                    # criado um cliente qualquer apenas para efeito de funcionamento de exemplo
                    if (codigo == cli1 or codigo == cli2 or codigo == cli3):
                        print("\n")
                        print("**** Usuário já cadastrado! Você já pode ir para o agendamento! ****")
                        print("\n")
                        print("* Código..............: 3")
                        print("* CPF.................: 999.999.999-99")
                        print("* Nome do cliente.....: João Mévio")
                        print("* Data de nascimento..: 12/08/1984")
                        print("* Logradouro..........: rua: José Andrade")
                        print("* Número..............: 223")
                        print("* CEP.................: 99999-999")
                        print("\n")
                        print("********************************************************************")
                        break
                    # caso não exista um cadastro volta ao menu inicial para escolher o que fazer
                    elif(codigo != cli1 or codigo != cli2 or codigo != cli3):
                        print("\n")
                        print("Usuário não está cadastrado! Faça o seu cadastro!")
                        print("\n")
                        break
            
            # faz o cadastro do cliente salva automáticamente e exibe os dados
            elif(opcao == 2):
                print("\n")
                print("CADASTRAR NOVO CLIENTE")
                print("\n")
                print("Dados do Cliente:")
                codigoCli = int(input("Digite o código do cliente (apenas número....: "))
                cpf = int(input("Digite o CPF ou CNPJ(apenas números).........: "))
                nome = input("Digiter o nome...............................: ")
                dataNascimento = int(input("Digite a data de nascimento (apenas números).: "))
                print("Endereço do cliente:")
                logradouro = input("Digite o logradouro..........................: ")
                numero = int(input("Digite o número (apenas números).............: "))
                cep = int(input("Digite o CEP (apenas números)................: "))
                
                # imprime os dados cadastrados e informa que os dados foram salvos
                print("\n")
                print("****************** Cliente cadastrado com sucesso! *****************")
                print("\n")
                print("* Dados do cliente:")
                print("* Código...............:", codigoCli)
                print("* CPF..................:", cpf)
                print("* Nome.................:", nome)
                print("* Data de nascimento...:", dataNascimento)
                print("* Endereço do cliente..:")
                print("* Logradouro...........:", logradouro)
                print("* Número...............:", numero)
                print("* CEP..................:", cep)
                print("\n")
                print("*********************************************************************")
            
            # testa as opções do menu
            elif(opcao != 1 or opcao != 2 or opcao != 0):
                print("\n")
                print("Opção inválida! Digite a opção correta!")
                print("\n")

            # quando escolhe o "0" volta ao menu princípal do sistema
            elif(opcao == 0):
                break
            break

    # nessa opção é possível verificar se o usuário cadastrado possui um veiculo cadastrado, ou ainda cadastrar um novo veiculo.
    elif(opcao == 2):

        while True:
            print("\n")
            print("CADASTRO DE VEICULO")
            print("1 - Pesquisar veiculo do usuário")
            print("2 - Novo veiculo")
            print("0 - Menu princípal")
            print("\n")
            opcao = int(input("Digite a opção desejada: "))
            print("\n")

            if (opcao == 1):
                # faz a pesquisa se o usuário possui um veiculo cadastrado no sistema
                while True:
                    # usuário cadastrado para teste:
                    # 1
                    # 2
                    # 3

                    cli1 = 1
                    cli2 = 2
                    cli3 = 3

                    codigo = int(input("Digite o código do cliente: "))
                    # Exibe os dados do veiculo de um cliente já cadastrado previamente como exemplo
                    if (codigo == cli1 or codigo == cli2 or codigo == cli3):
                        print("\n")
                        print("**** Cliente já tem um veiculo cadastrado! Você pode cadastrar um novo veiculo ou voltar ao menu princípal ****")
                        print("\n")
                        print("* Código.................: 3")
                        print("* Nome do cliente........: João Mévio")
                        print("* Tipo de veiculo........: Carro")
                        print("* Modelo do veiculo......: Corolla")
                        print("* Fabricante.............: Toyota")
                        print("* Ano de fabricação......: 2012")
                        print("* Tipo de motor..........: 2.0 gasoline/alcool")
                        print("* versão do carro........: Corola XEI")
                        print("\n")
                        print("****************************************************************************************************************")
                        break
                    # não havendo veiculo cadastrado retrona uma mensagem de erro
                    elif(codigo != cli1 or codigo != cli2 or codigo != cli3):
                        print("\n")
                        print("Cliente não possui nenhum veiculo cadastrado! Por favos, cadastre um veiculo.")
                        print("\n")
                        break
                    else:
                        break
            
            # faz o cadastro do veiculo e salva automáticamente
            elif(opcao == 2):
                print("\n")
                print("CADASTRAR NOVO VEICULO")
                print("\n")
                tipoVeiculo =input("Digite o tipo de veiculo................................: ")
                modeloVeiculo =input("Digite o modelo do veiculo..............................: ")
                fabricanteVeiculo = input("Digite o fabricante do veiculo..........................: ")
                anoFabricacao = int(input("Digite o ano de fabricação do veiculo (apenas números)..: "))
                tipoMotor =input("Digite o Tipo de motor do veiculo.......................: ")
                versaoVeiculo =input("Digite a verção do veiculo..............................: ")
                print("\n")
                print("*************************************** Veiculo cadastrado com sucesso! ***************************************")
                print("\n")
                print("* Tipo de veiculo........:", tipoVeiculo)
                print("* Modelo do veiculo......:", modeloVeiculo)
                print("* Fabricante.............:", fabricanteVeiculo)
                print("* Ano de fabricação......:", anoFabricacao)
                print("* Tipo de motor..........:", tipoMotor)
                print("* versão do carro........:", versaoVeiculo)
                print("\n")
                print("****************************************************************************************************************")
                print("\n")
            
            # testa as opções do menu
            elif(opcao != 1 or opcao != 2 or opcao != 0):
                print("Opção inválida! Digite a opção correta!")

            # quando escolhe o "0" volta ao menu princípal do sistema
            elif(opcao == 0):
                break
            break
    elif(opcao == 3):

        while True:

            print("\n")
            print("DESCRIÇÃO DO PROBLEMA DO VEICULO")
            print("1 - Pesquisar veiculo")
            print("2 - Novo defeito")
            print("0 - Menu princípal")
            print("\n")
            opcao = int(input("Digite a opção desejada: "))
            print("\n")

            if (opcao == 1):

                cli1 = 1
                cli2 = 2
                cli3 = 3

                codigo = int(input("Digite o código do cliente: "))
                
                # Exibe os dados do veiculo de um cliente já cadastrado previamente como exemplo
                if (codigo == cli1 or codigo == cli2 or codigo == cli3):
                    print("\n")
                    print("**** Cliente já tem um registro de problema anteriormente cadastrado ****")
                    print("\n")
                    print("* Código.......................: 3")
                    print("* Nome do cliente..............: João Mévio")
                    print("* Tipo de veiculo..............: Carro")
                    print("* Modelo do veiculo............: Corolla")
                    print("* Fabricante...................: Toyota")
                    print("* Ano de fabricação............: 2012")
                    print("* Tipo de motor................: 2.0 gasoline/alcool")
                    print("* versão do carro..............: Corola XEI")
                    print("* Descrição breve do defeito...: Quebra de roda, e perfuração de tanque de combustível com vazamento")
                    print("* Parte do carro afetada.......: Roda dianteira direita e tanque de combustível")
                    print("* Possível problema do carro...: Quebra de rodam, desalinhamento,furo de pneu e tanque de combustível perfurado")
                    print("\n")
                    print("****************************************************************************************************************")
                    break

                # não havendo defeito cadastrado retorna uma mensagem de erro
                elif(codigo != cli1 or codigo != cli2 or codigo != cli3):
                    print("\n")
                    print("Cliente não possui defeito veicular cadastrado! Por favor faça uma nova inclusão.")
                    print("\n")
                    break
                else:
                    break

            elif (opcao == 2):

                print("\n")
                print("CADASTRAR NOVO DEFEITO")
                print("\n")
                descricaoDefeito = input("Descreva brevemente o defeito........................: ")
                parteCarro = input("Digite em que parte do carro está havendo o problema.: ")
                aponteProblema = input("Aponte qual é o problema do carro....................: ")
                print("\n")
                print("*************************************** Defeito cadastrado com sucesso! ***************************************")
                print("\n")
                print("* Descrição breve do defeito.............:", descricaoDefeito)
                print("* Parte do carro afetada.................:", parteCarro)
                print("* Possível problema do carro.............:", aponteProblema)
                print("\n")
                print("****************************************************************************************************************")
                print("\n")

            # testa as opções do menu
            elif(opcao != 1 or opcao != 2 or opcao != 0):
                print("Opção inválida! Digite a opção correta!")

            # quando escolhe o "0" volta ao menu princípal do sistema
            elif(opcao == 0):
                break
            break

    elif(opcao == 4):
                
        while True:

            print("\n")
            print("AGENDAR AFICINA")
            print("1 - Pesquisar agendamento do cliente")
            print("2 - Novo agendamento")
            print("0 - Menu princípal")
            print("\n")
            opcao = int(input("Digite a opção desejada: "))
            print("\n")
            
            if(opcao == 1):

                cli1 = 1
                cli2 = 2
                cli3 = 3

                codigo = int(input("Digite o código do cliente: "))
                
                # Exibe os dados do agendamento de um cliente já cadastrado previamente como exemplo
                if (codigo == cli1 or codigo == cli2 or codigo == cli3):
                    print("\n")
                    print("**** Cliente já possui um agendamento cadastrado ****")
                    print("\n")
                    print("* Código.......................: 3")
                    print("* Nome do cliente..............: João Mévio")
                    print("* Descrição breve do defeito...: Quebra de roda, e perfuração de tanque de combustível com vazamento")
                    print("* Parte do carro afetada.......: Roda dianteira direita e tanque de combustível")
                    print("* Possível problema do carro...: Quebra de rodam, desalinhamento,furo de pneu e tanque de combustível perfurado")
                    print("Data agendada: 22/05/2024")
                    print("Periodo do dia: manhã")
                    print("Hora do dia: 10h a.m.")                    
                    print("\n")
                    print("****************************************************************************************************************")
                    break
            
            elif(opcao == 2):
                print("NOVO AGENDAMENTO")
                print("Escolha o horário de atendimento:")
                print("1 - Manha")
                print("2 - tarde")
                print("\n")
                periodoAgendamento = int(input("Digite 1 ou 2 para escolher o perido: "))

                if (periodoAgendamento != 1 or periodoAgendamento != 2):
                    print("Opção inválida! digite a opção correta")
                
                horarioAgendamento = int(input("Digite o horário do agendamento (formato 24h, por Ex: 0700 ou 1130): "))
                print("Atedimento de Segunda a Sábado das 8h as 29h.")

                if (horarioAgendamento >= 8 or horarioAgendamento <= 20):
                    print("Agendamento feito!")
                elif(horarioAgendamento < 8 or horarioAgendamento > 20):
                    print("Horário escolhido não é atendido! escolha um novo horário")
                
                print("Digite a data para agendamento: ")
                diaAgendamento = int(input("Digite o dia (apenas números): "))
                mesAgendamento = int(input("Digite o mês (apenas números): "))
                anoAgendamento = int(input("Digite o ano do agendamento (ano com 4 digitos): "))

                if(diaAgendamento >= 1 or diaAgendamento <= 31):
                    print("Dia agendado")
                if(mesAgendamento >= 1 or mesAgendamento <-12):
                    print("Mês agendado")
                if(anoAgendamento >= 2024):
                    print("Ano agendado")
                elif(diaAgendamento < 1 or diaAgendamento > 31):
                    print("escolha um dia entre 1 e 31!")
                elif(mesAgendamento < 1 or mesAgendamento > 12):
                    print("Escolha o mês entre 1 e 12!")
                elif(anoAgendamento < 2024):
                    print("Ano escolhido não pode ser menor que 2024!")

                    
            # testa as opções do menu
            elif(opcao != 1 or opcao != 2 or opcao != 0):
                print("Opção inválida! Digite a opção correta!")

            # quando escolhe o "0" volta ao menu princípal do sistema
            elif(opcao == 0):
                break
            break

    elif(opcao != 1 or opcao != 2 or opcao != 3 or opcao != 4 or opcao != 5 or opcao != 6 or opcao != 7 or opcao != 0):
        print("Opção inválida!")
        print("Digite a opção correta!")