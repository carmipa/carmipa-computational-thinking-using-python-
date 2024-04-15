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

# importa bibiotecas de cores e para limpesa de tela
import os
import colorama

# inicializa o colorama que cria as corers personalizadas nos mesnus e alertas
colorama.init()

# cria o menu princípal e suas opções
while True:
    print("**************************************** PORTO SEGURO / OFICINA ON-LINE ****************************************")
    print("*")
    print("* 1 - CADASTRAR NOVOS CLIENTES")
    print("* 2 - CADASTRAR VEICULOS")
    print("* 3 - OFICINA ON-LINE / AGENDAMENTOS")
    print("* 4 - ORÇAMENTO / PAGAMENTO")
    print("* 5 - PESQUISAR DADOS DE UM CLIENTE")
    print("* 0 - SAIR DO SISTEMA")
    print("*")
    opcao = input("* DIGITE A OPÇÃO DESEJADA: ")
    print("*")
    print("****************************************************************************************************************")

#########################################################################################################################################

# cria a primeiro menu e suas opções
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
                
                # dadastra os dados do cliente
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
                
                # feito o cadastro desvolve uma mensagem de salvamento e exibe os dados digitados

                print(colorama.Fore.YELLOW +"**************************************** DADOS DO CLIENTE CADASTRADOS COM SUCESSO ****************************************"+ colorama.Style.RESET_ALL)
                print("\n")
                print(colorama.Fore.YELLOW +"NOME:...............: ",nomeCliente)
                print("DATA DE NASCIMENTO..: ",dataNascimento)
                print("PROFISSÃO...........: ",profissaoCliente)
                print("CPF.................: ",cpfCliente)
                print("NASCIONALIDADE......: ",nascionalidadeCliente)
                print("RUA.................: ",ruaCliente)
                print("NUMERO..............: ",numeroCliente)
                print("CEP.................: ",cepCliente)
                print("ESTADO..............: ",estadoCliente)
                print("COMPLEMENTO.........: ",complementoCliente + colorama.Style.RESET_ALL)
                print("\n")

            elif(opcao == "0"):
                break
            else:
                print(colorama.Fore.RED +"OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!" + colorama.Style.RESET_ALL)

#########################################################################################################################################

    elif(opcao == "2"):
        
        # cria a segundo menu e suas opções
        
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
                
                # feito o cadastro desvolve uma mensagem de salvamento e exibe os dados digitados

                print(colorama.Fore.YELLOW +"**************************************** DADOS DO VEICULO CADASTRADOS COM SUCESSO ****************************************"+ colorama.Style.RESET_ALL)
                print("\n")
                print(colorama.Fore.YELLOW +"TIPO DE VEICULO.....: ",tipoVeiculo)
                print("FABRICANTE..........: ",fabricanteVeiculo)
                print("MODELO..............: ",modeloVeiculo)
                print("MOTOR...............: ",motorVeiculo)
                print("COR.................: ",corVeciculo)
                print("ANO DE FABRICAÇÃO...: ",anoFabricaaoVeiculo)
                print("PLACA...............: ",placaVeiculo)
                print("NOME DO DONO........: ",donoVeiculo + colorama.Style.RESET_ALL)
                print("\n")

            elif(opcao == "0"):
                break
            else:
                print(colorama.Fore.RED +"OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!" + colorama.Style.RESET_ALL)

#########################################################################################################################################

    elif(opcao == "3"):
        
        # cria o terceiro menu e suas opções
        
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
                
                # feito o cadastro desvolve uma mensagem de salvamento e exibe os dados digitados

                print(colorama.Fore.YELLOW +"**************************************** PROBLEMAS DO VEÍCULO E AGENDAMENTO REALIZADO COM SUCESSO ****************************************"+ colorama.Style.RESET_ALL)
                print("\n")
                print(colorama.Fore.YELLOW +"DESCRIÇÃO DO PROBLEMA DO VEICULO............: ",problemaDescricao)
                print("PARTES AFETADAS.............................: ",problemasPartes)
                print("DIA DO AGENDAMENTO..........................: ",problemaDia)
                print("MÊS DO AGENDAMENTO..........................: ",problemaMes)
                print("ANO DE AGENDAMENTO..........................: ",problemaAno)
                print("PERÍODO DO AGENDAMENTO (MANHÃ OU TARDE).....: ",problemaPeriodo)
                print("HORÁRIO DE ATENDIMENTO......................: ",problemaHorario + colorama.Style.RESET_ALL)
                print("\n")

            elif(opcao == "0"):
                break
            else:
                print(colorama.Fore.RED +"OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!" + colorama.Style.RESET_ALL)

#########################################################################################################################################  
    
    elif(opcao == "4"):
        
        # cria o quarto menu e suas opções
        
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
                print("ORÇAMENTO - PEÇAS")
                pecas1Pagamento = input ("PEÇAS 1.......................: ")
                valor1Peca = float(input("PREÇO (apenas números)........: R$ "))
                pecas2Pagamento = input ("PEÇAS 2.......................: ")
                valor2Peca = float(input("PREÇO (apenas números)........: R$ "))
                pecas3Pagamento = input ("PEÇAS 3.......................: ")
                valor3Peca = float(input("PREÇO (apenas números)........: R$ "))
                maoDeObra = float(input("MÃO DE OBRA (apenas números)..: R$ "))

                # valor total
                total = valor1Peca + valor2Peca + valor3Peca + maoDeObra
                # a vista com 10% de desconto
                total10 = total / 10
                aVista = total - total10
                # crédito com 5% de desconto
                total5 = (total * 5) / 100
                credito = total = total5
                # parcelado em 5x
                parcelado = total / 5
                print("\n")
                print("PAGAMENTO ")
                print("TOTAL....................................: R$",total)
                print("A VISTA (10% DESCONTO)...................: R$",aVista)
                print("NO CRÈDITO (5% DESCONTO).................: R$",credito)
                print("PARCELADO (5X - SEM DESCONTO)............: R$",parcelado, "5x")

                os.system('cls')
                
                # feito o cadastro desvolve uma mensagem de salvamento e exibe os dados digitados

                print(colorama.Fore.YELLOW +"**************************************** ORÇAMENTO / PAGAMENTO REALIZADO COM SUCESSO ****************************************"+ colorama.Style.RESET_ALL)

                print(colorama.Fore.YELLOW +"ORÇAMENTO - PEÇAS")
                print("PEÇAS 1..................................:",pecas1Pagamento)
                print("PREÇO....................................: R$",valor1Peca)
                print("PEÇAS 2..................................:",pecas2Pagamento)
                print("PREÇO....................................: R$",valor2Peca)
                print("PEÇAS 3..................................:",pecas3Pagamento)
                print("PREÇO....................................: R$",valor3Peca)
                print("MÃO DE OBRA..............................: R$",maoDeObra)
                print("\n")
                print("PAGAMENTO ")
                print("TOTAL....................................: R$",total)
                print("A VISTA (10% DESCONTO)...................: R$",aVista)
                print("NO CRÈDITO (5% DESCONTO).................: R$",credito)
                print("PARCELADO (5X - SEM DESCONTO)............: R$",parcelado, "5x"+ colorama.Style.RESET_ALL)
                print("\n")

            elif(opcao == "0"):
                break
            else:
                print(colorama.Fore.RED +"OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!" + colorama.Style.RESET_ALL)

#########################################################################################################################################  
    elif(opcao == "5"):
        
        # cria o quinto menu e suas opções
        
        os.system('cls')
        while True:
            print("**************************************** PESQUISAR DADOS DE UM CLIENTE ****************************************")
            print("\n")
            print("1 - PESQUISAR DADOS DE UM CLIENTE")
            print("0 - VOLTAR AO MENU ANTERIOR")
            print("\n")
            opcao = input("DIGITE A OPÇÃO DESEJADA: ")

            if(opcao == "1"):
                print("**************************************** PESQUISAR DADOS DE UM CLIENTE ****************************************")
                # faz a pesquisa se o usuário existe ou não no sistema
                while True:
                    
                    codigo = int(input("DIGITE O CÓDIGO DO CLIENTE: "))

                    # criado um cliente qualquer apenas para efeito de funcionamento de exemplo
                    # neste caso como exemplo digite o COD "1" para fazer a pesquisa por cliente cadastrado
                    
                    if (codigo == 1 ):
                        print("\n")
                        print(colorama.Fore.YELLOW + "**************************************** O CLIENTE POSSUI CADASTRO ****************************************" +colorama.Style.RESET_ALL)
                        print("\n")
                        print(colorama.Fore.YELLOW +"DADOS DO CLIENTE:"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"NOME:...............: JOÃO MÉVIO"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"DATA DE NASCIMENTO..: 01/01/1978"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"PROFISSÃO...........: PADEIRO"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"CPF.................: 999.999.999.99"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"NASCIONALIDADE......: BRASILEIRO"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"RUA.................: BRAUILIO ANTÓNIO"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"NUMERO..............: 1050"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"CEP.................: 99999-99"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"ESTADO..............: RJ"+colorama.Style.RESET_ALL)
                        print("\n")
                        print(colorama.Fore.YELLOW +"COMPLEMENTO.........: CASA"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"DADOS DO VEÍCULO:"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"TIPO DE VEICULO.....: CARRO"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"FABRICANTE..........: GM"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"MODELO..............: OMEGA"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"MOTOR...............: 4.0"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"COR.................: PRETO-ECLIPSE"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"ANO DE FABRICAÇÃO...: 2000"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"PLACA...............: ABCD-586"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"NOME DO DONO........: JOÃO MÉVIO"+colorama.Style.RESET_ALL)
                        print("\n")
                        print(colorama.Fore.YELLOW +"PROBLEMAS NO VEÍCULO / AGENDAMENTO"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"DESCRIÇÃO DO PROBLEMA DO VEICULO............: QUEBRA DE ROD, FURO NO TANQUE DE COMBUSTÍVEL"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"PARTES AFETADAS.............................: RODA DIANTEIRA ESQUERDA E TANQUE DE COMBUSTÍVEL"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"DIA DO AGENDAMENTO..........................: 22"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"MÊS DO AGENDAMENTO..........................: FEVEREIRO"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"ANO DE AGENDAMENTO..........................: 2025"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"PERÍODO DO AGENDAMENTO (MANHÃ OU TARDE).....: TARDE"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"HORÁRIO DE ATENDIMENTO......................: 18H"+colorama.Style.RESET_ALL)
                        print("\n")
                        print(colorama.Fore.YELLOW +"ORÇAMENTO - PEÇAS"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"PEÇAS 1..................................: RODA"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"PREÇO....................................: R$ 1.1900"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"PEÇAS 2..................................: TANQUE DE COMBUSTÍVEL"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"PREÇO....................................: R$ 900.00"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"PEÇAS 3..................................: "+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"PREÇO....................................: R$ 0"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"MÃO DE OBRA..............................: R$ 500.00"+colorama.Style.RESET_ALL)
                        print("\n")
                        print(colorama.Fore.YELLOW +"PAGAMENTO "+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"TOTAL....................................: R$ 3.300"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"A VISTA (10% DESCONTO)...................: R$ 2.970"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"NO CRÈDITO (5% DESCONTO).................: R$ 3.135"+colorama.Style.RESET_ALL)
                        print(colorama.Fore.YELLOW +"PARCELADO (5X - SEM DESCONTO)............: R$ 660.00 5x"+colorama.Style.RESET_ALL)
                        print("\n")
                        print(colorama.Fore.YELLOW + "********************************************************************************"+colorama.Style.RESET_ALL)
                    # caso não exista um cadastro volta ao menu inicial para escolher o que fazer
                    else:
                        print("\n")
                        print(colorama.Fore.RED + "CLIENTE NÃO CADASTRADO, POR FAVOR DIGITE UM CÓDIGO VÁLIDO!"+ colorama.Style.RESET_ALL)
                        print("\n")
                        break
            elif(opcao == "0"):
                break
            else:
                print(colorama.Fore.RED +"OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!" + colorama.Style.RESET_ALL)
        
    elif(opcao == "0"):
        
        # cria uma opção para sair do programa 
        
        os.system('cls')
        print(colorama.Fore.RED + "**************************************** SAIR DO SISTEMA ****************************************"+colorama.Style.RESET_ALL)
        break
    else:
        print(colorama.Fore.RED + "OPÇÃO INCORRETA. DIGITE O APÇÃO CORRETA!" + colorama.Style.RESET_ALL)


