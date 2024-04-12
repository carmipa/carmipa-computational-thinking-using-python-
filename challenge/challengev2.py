# INSTRUÇÕES DE USO:
# quando houver uma opção de pesquisa no menu use as seguinte opções:
# ex: 1 ou 2 ou 3 - "sempre um destes 3 código"

import os
while True:
    os.system('cls')
    print("**************************************** PORTO SEGURO / OFICINA ON-LINE ****************************************")
    print("*")
    print("* 1 - CADASTRAR NOVOS CLIENTES")
    print("* 2 - CADASTRAR VEICULOS")
    print("* 3 - OFICINA ON-LINE / AGENDAMENTOS")
    print("* 4 - ORÇAMENTO / PAGAMENTO")
    print("* 5 - INDICAÇÃO E CADASTRO DE NOVAS OFICINAS")
    print("* 6 - PESQUISAR DADOS DE UM CLIENTE")

    print("* 0 - SAIR DO SISTEMA")
    print("*")
    opcao = int(input("* DIGITE A OPÇÃO DESEJADA: "))
    print("*")
    print("****************************************************************************************************************")

    if(opcao == 1):
        os.system('cls')
        while True:
            print("**************************************** CADASTRAR NOVOS CLIENTES ****************************************")
            print("\n")
            print("1 - CADASTRAR NOVO CLIENTE")
            print("0 - VOLTAR AO MENU ANTERIOR")
            print("\n")
            opcao = int(input("DIGITE A OPÇÃO DESEJADA: "))
            if(opcao == 1):
                print("**************************************** CADASTRAR NOVO CLIENTE ****************************************")
                print("DADOS DO CLIENTE")
                nomeCliente = input("NOME:...............: ")
                dataNascimento = input("DATA DE NASCIMENTO..: ")
                profissaoCliente = input("PROFISSÃO...........: ")
                cpfCliente = input("CPF.................: ")
                nascionalidadeCliente = input("NASCIONALIDADE......: ")
                print("ENDEREÇO DO CLIENTE")
                ruaCliente = input("RUA.................: ")
                numeroCliente = input("NUMERO..............: ")
                cepCliente = input("CEP.................: ")
                estadoCliente = input("ESTADO..............: ")
                complementoCliente = input("COMPLEMENTO.........: ")
                os.system('cls')
                print("**************************************** DADOS DO CLIENTE CADASTRADOS COM SUCESSO ****************************************")
                print("\n")
                print("DADOS DO CLIENTE")
                print("NOME:...............: ",nomeCliente)
                print("DATA DE NASCIMENTO..: ",dataNascimento)
                print("PROFISSÃO...........: ",profissaoCliente)
                print("CPF.................: ",cpfCliente)
                print("NASCIONALIDADE......: ",nascionalidadeCliente)
                print("ENDEREÇO DO CLIENTE")
                print("RUA.................: ",ruaCliente)
                print("NUMERO..............: ",numeroCliente)
                print("CEP.................: ",cepCliente)
                print("ESTADO..............: ",estadoCliente)
                print("COMPLEMENTO.........: ",complementoCliente)
                print("\n")

            elif(opcao == 0):
                break
            else:
                print("OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!")

    elif(opcao == 2):
        os.system('cls')
        while True:
            print("**************************************** CADASTRO DE VEICULOS ****************************************")
            print("\n")
            print("1 - CADASTRAR NOVO VEICULO")
            print("0 - VOLTAR AO MENU ANTERIOR")
            print("\n")
            opcao = int(input("DIGITE A OPÇÃO DESEJADA: "))
            if(opcao == 1):
                print("**************************************** CADASTRAR NOVO VEICULO ****************************************")
                print("DADOS DO VEICULO")
                tipoVeiculo = input("TIPO DE VEICULO.....: ")
                fabricanteVeiculo = input("FABRICANTE..........: ")
                modeloVeiculo = input("MODELO..............: ")
                motorVeiculo = input("MOTOR...............: ")
                corVeciculo = input("COR.................: ")
                anoFabricaaoVeiculo = input("ANO DE FABRICAÇÃO...: ")
                placaVeiculo = input("PLACA...............: ")
                donoVeiculo = input("NOME DO DONO........: ")
                os.system('cls')
                print("**************************************** DADOS DO VEICULO CADASTRADOS COM SUCESSO ****************************************")
                print("\n")
                print("DADOS DO VEICULO")
                print("TIPO DE VEICULO.....: ",tipoVeiculo)
                print("FABRICANTE..........: ",fabricanteVeiculo)
                print("MODELO..............: ",modeloVeiculo)
                print("MOTOR...............: ",motorVeiculo)
                print("COR.................: ",corVeciculo)
                print("ANO DE FABRICAÇÃO...: ",anoFabricaaoVeiculo)
                print("PLACA...............: ",placaVeiculo)
                print("NOME DO DONO........: ",donoVeiculo)
                print("\n")

            elif(opcao == 0):
                break
            else:
                print("OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!")


    elif(opcao == 3):
        os.system('cls')
        while True:
            print("**************************************** OFICINA ON-LINE / AGENDAMENTOSS ****************************************")
            print("\n")
            print("1 - INDICAR PROBLEMAS NO VEICULO E FAZER AGENDAMENTO")
            print("0 - VOLTAR AO MENU ANTERIOR")
            print("\n")
            opcao = int(input("DIGITE A OPÇÃO DESEJADA: "))

            if(opcao == 1):
                print("**************************************** INDICAR PROBLEMAS NO VEICULO E FAZER AGENDAMENTO ****************************************")
            elif(opcao == 0):
                break
            else:
                print("OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!")
    
    
    elif(opcao == 4):
        os.system('cls')
        print("**************************************** ORÇAMENTO / PAGAMENTO ****************************************")
    elif(opcao == 5):
        os.system('cls')
        print("**************************************** INDICAÇÃO E CADASTRO DE NOVAS OFICINAS ****************************************")
    elif(opcao == 6):
        os.system('cls')
        print("**************************************** PESQUISAR DADOS DE UM CLIENTE ****************************************")
    elif(opcao == 0):
        os.system('cls')
        print("**************************************** SAIR DO SISTEMA ****************************************")
    else:
        os.system('cls')
        print("OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!")


