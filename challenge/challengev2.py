#########################################################################################################################################
#
# INSTRUÇÕES DE USO:
#
# 1 - quando houver uma opção de pesquisa no menu use as seguinte opções:
#     ex: 1 ou 2 ou 3 - "sempre um destes 3 código"
#
# 2 - O programa usa a biblioteca "COLORAMA", como visto no importe, para que funcione corretamente use
#     o seguinte comando no console abaixo antes de rodar o programa:
#     "pip install colorama"
#     OBS: se a biblioteca já estiver instalada, não é necessário a instalar
#
#########################################################################################################################################
import os
import colorama

colorama.init()

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
    opcao = input("* DIGITE A OPÇÃO DESEJADA: ")
    print("*")
    print("****************************************************************************************************************")

#########################################################################################################################################

    if(opcao == "1"):
        os.system('cls')
        while True:
            print("**************************************** CADASTRAR NOVOS CLIENTES ****************************************")
            print("\n")
            print("1 - CADASTRAR NOVO CLIENTE")
            print("0 - VOLTAR AO MENU ANTERIOR")
            print("\n")
            opcao = input("DIGITE A OPÇÃO DESEJADA: ")
            if(opcao == "1"):
                print("**************************************** CADASTRAR NOVO CLIENTE ****************************************")
                print("DADOS DO CLIENTE")
                nomeCliente = input("NOME:...............: ")
                dataNascimento = input("DATA DE NASCIMENTO..: ")
                profissaoCliente = input("PROFISSÃO...........: ")
                cpfCliente = input("CPF.................: ")
                nascionalidadeCliente = input("NASCIONALIDADE......: ")
                print("\n")
                print("ENDEREÇO DO CLIENTE")
                ruaCliente = input("RUA.................: ")
                numeroCliente = input("NUMERO..............: ")
                cepCliente = input("CEP.................: ")
                estadoCliente = input("ESTADO..............: ")
                complementoCliente = input("COMPLEMENTO.........: ")

                os.system('cls')

                print(colorama.Fore.RED +"**************************************** DADOS DO CLIENTE CADASTRADOS COM SUCESSO ****************************************"+ colorama.Style.RESET_ALL)
                print("\n")
                print("NOME:...............: ",nomeCliente)
                print("DATA DE NASCIMENTO..: ",dataNascimento)
                print("PROFISSÃO...........: ",profissaoCliente)
                print("CPF.................: ",cpfCliente)
                print("NASCIONALIDADE......: ",nascionalidadeCliente)
                print("RUA.................: ",ruaCliente)
                print("NUMERO..............: ",numeroCliente)
                print("CEP.................: ",cepCliente)
                print("ESTADO..............: ",estadoCliente)
                print("COMPLEMENTO.........: ",complementoCliente)
                print("\n")

            elif(opcao == "0"):
                break
            else:
                print(colorama.Fore.RED +"OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!" + colorama.Style.RESET_ALL)

#########################################################################################################################################

    elif(opcao == "2"):
        os.system('cls')
        while True:
            print("**************************************** CADASTRO DE VEICULOS ****************************************")
            print("\n")
            print("1 - CADASTRAR NOVO VEICULO")
            print("0 - VOLTAR AO MENU ANTERIOR")
            print("\n")
            opcao = input("DIGITE A OPÇÃO DESEJADA: ")
            if(opcao == 1):
                print("**************************************** CADASTRAR NOVO VEICULO ****************************************")
                tipoVeiculo = input("TIPO DE VEICULO.....: ")
                fabricanteVeiculo = input("FABRICANTE..........: ")
                modeloVeiculo = input("MODELO..............: ")
                motorVeiculo = input("MOTOR...............: ")
                corVeciculo = input("COR.................: ")
                anoFabricaaoVeiculo = input("ANO DE FABRICAÇÃO...: ")
                placaVeiculo = input("PLACA...............: ")
                donoVeiculo = input("NOME DO DONO........: ")

                os.system('cls')

                print(colorama.Fore.RED +"**************************************** DADOS DO VEICULO CADASTRADOS COM SUCESSO ****************************************"+ colorama.Style.RESET_ALL)
                print("\n")
                print("TIPO DE VEICULO.....: ",tipoVeiculo)
                print("FABRICANTE..........: ",fabricanteVeiculo)
                print("MODELO..............: ",modeloVeiculo)
                print("MOTOR...............: ",motorVeiculo)
                print("COR.................: ",corVeciculo)
                print("ANO DE FABRICAÇÃO...: ",anoFabricaaoVeiculo)
                print("PLACA...............: ",placaVeiculo)
                print("NOME DO DONO........: ",donoVeiculo)
                print("\n")

            elif(opcao == "0"):
                break
            else:
                print(colorama.Fore.RED +"OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!" + colorama.Style.RESET_ALL)

#########################################################################################################################################

    elif(opcao == "3"):
        os.system('cls')
        while True:
            print("**************************************** OFICINA ON-LINE / AGENDAMENTOSS ****************************************")
            print("\n")
            print("1 - INDICAR PROBLEMAS NO VEICULO E FAZER AGENDAMENTO")
            print("0 - VOLTAR AO MENU ANTERIOR")
            print("\n")
            opcao = input("DIGITE A OPÇÃO DESEJADA: ")

            if(opcao == "1"):
                print("**************************************** INDICAR PROBLEMAS NO VEICULO E FAZER AGENDAMENTO ****************************************")
                print("\n")
                print("PROBLEMAS NO VEICULO")
                problemaDescricao = input("DESCRIÇÃO DO PROBLEMA DO VEICULO..: ")
                problemasPartes = input("PARTES AFETADAS.....................: ")
                print("\n")
                print("AGENDAR OFICINA")
                problemaDia = input("DIGITE O DIA DO AGENDAMENTO.............: ")
                problemaMes = input("DIGITE O MÊS DO AGENDAMENTO.............: ")
                problemaAno = input("DIGITE O ANO DE AGENDAMENTO.............: ")
                problemaPeriodo = input("PERÍODO DO DIA (MANHÃ OU TARDE).........: ")
                print(colorama.Fore.RED +"ALERTA! A OFICINA ATENDE DAS 8H AS 20H DE SEGUNDA A SÁBADO!"+ colorama.Style.RESET_ALL)
                problemaHorario = input("DIGITE O HORÁRIO DE ATENDIMENTO.........: ")
                
                os.system('cls')

                print(colorama.Fore.RED +"**************************************** PROBLEMAS DO VEÍCULO E AGENDAMENTO REALIZADO COM SUCESSO ****************************************"+ colorama.Style.RESET_ALL)
                print("\n")
                print("DESCRIÇÃO DO PROBLEMA DO VEICULO............: ",problemaDescricao)
                print("PARTES AFETADAS.............................: ",problemasPartes)
                print("DIA DO AGENDAMENTO..........................: ",problemaDia)
                print("MÊS DO AGENDAMENTO..........................: ",problemaMes)
                print("ANO DE AGENDAMENTO..........................: ",problemaAno)
                print("PERÍODO DO AGENDAMENTO (MANHÃ OU TARDE).....: ",problemaPeriodo)
                print("HORÁRIO DE ATENDIMENTO......................: ",problemaHorario)

            elif(opcao == "0"):
                break
            else:
                print(colorama.Fore.RED +"OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!" + colorama.Style.RESET_ALL)

#########################################################################################################################################  
    
    elif(opcao == "4"):
        os.system('cls')
        while True:
            print("**************************************** ORÇAMENTO / PAGAMENTO ****************************************")
            print("\n")
            print("1 - ORÇAMENTO E PAGAMENTO")
            print("0 - VOLTAR AO MENU ANTERIOR")
            print("\n")
            opcao = input("DIGITE A OPÇÃO DESEJADA: ")

            if(opcao == "1"):
                print("**************************************** ORÇAMENTO / PAGAMENTO ****************************************")
                print("\n")
                print("PEÇAS USADAS")
                input("PEÇAS 1............: ")
                input("PREÇO: R$..: ")
                input("PEÇAS 2............: ")
                input("PREÇO: R$..: ")
                input("PEÇAS 3............: ")
                input("PREÇO: R$..: ")
                
                
                


    elif(opcao == "5"):
        os.system('cls')
        print("**************************************** INDICAÇÃO E CADASTRO DE NOVAS OFICINAS ****************************************")
    elif(opcao == "6"):
        os.system('cls')
        print("**************************************** PESQUISAR DADOS DE UM CLIENTE ****************************************")
    elif(opcao == "0"):
        os.system('cls')
        print("**************************************** SAIR DO SISTEMA ****************************************")
        break
    else:
        print(colorama.Fore.RED + "OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!" + colorama.Style.RESET_ALL)


