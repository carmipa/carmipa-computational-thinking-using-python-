#########################################################################################################################################
#
#     INSTRUÇÕES DE USO:
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
import sys
import colorama

#########################################################################################################################################

# inicializa o colorama que cria as corers personalizadas nos mesnus e alertas

colorama.init()

#########################################################################################################################################

def exibir_nome_do_programa():
    print("""
██████╗░░█████╗░██████╗░████████╗░█████╗░  ░██████╗███████╗░██████╗░██╗░░░██╗██████╗░░█████╗░  ░░░░██╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗  ██╔════╝██╔════╝██╔════╝░██║░░░██║██╔══██╗██╔══██╗  ░░░██╔╝
██████╔╝██║░░██║██████╔╝░░░██║░░░██║░░██║  ╚█████╗░█████╗░░██║░░██╗░██║░░░██║██████╔╝██║░░██║  ░░██╔╝░
██╔═══╝░██║░░██║██╔══██╗░░░██║░░░██║░░██║  ░╚═══██╗██╔══╝░░██║░░╚██╗██║░░░██║██╔══██╗██║░░██║  ░██╔╝░░
██║░░░░░╚█████╔╝██║░░██║░░░██║░░░╚█████╔╝  ██████╔╝███████╗╚██████╔╝╚██████╔╝██║░░██║╚█████╔╝  ██╔╝░░░
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░  ╚═════╝░╚══════╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝░╚════╝░  ╚═╝░░░░

░█████╗░███████╗██╗░█████╗░██╗███╗░░██╗░█████╗░  ░█████╗░███╗░░██╗░░░░░░██╗░░░░░██╗███╗░░██╗███████╗
██╔══██╗██╔════╝██║██╔══██╗██║████╗░██║██╔══██╗  ██╔══██╗████╗░██║░░░░░░██║░░░░░██║████╗░██║██╔════╝
██║░░██║█████╗░░██║██║░░╚═╝██║██╔██╗██║███████║  ██║░░██║██╔██╗██║█████╗██║░░░░░██║██╔██╗██║█████╗░░
██║░░██║██╔══╝░░██║██║░░██╗██║██║╚████║██╔══██║  ██║░░██║██║╚████║╚════╝██║░░░░░██║██║╚████║██╔══╝░░
╚█████╔╝██║░░░░░██║╚█████╔╝██║██║░╚███║██║░░██║  ╚█████╔╝██║░╚███║░░░░░░███████╗██║██║░╚███║███████╗
░╚════╝░╚═╝░░░░░╚═╝░╚════╝░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚══╝░░░░░░╚══════╝╚═╝╚═╝░░╚══╝╚══════╝""")

#########################################################################################################################################

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibeMenu()
    sairDoPrograma()
    escolherOpcao()
    #exibirSubtitulo()
    voltarMenuPrincipal()
    opcaoInvalida()

#########################################################################################################################################

# cria o menu princípal e suas opções

def exibeMenu():
        
    print(colorama.Fore.BLUE +"**************************************** PORTO SEGURO / OFICINA ON-LINE ****************************************"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"*                                                                                                              *"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"*                                                                                                              *"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"*"+ colorama.Style.RESET_ALL, "1 - CADASTRAR NOVOS CLIENTES")
    print(colorama.Fore.BLUE +"*                                                                                                              *"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"*"+ colorama.Style.RESET_ALL, "2 - CADASTRAR VEICULOS")
    print(colorama.Fore.BLUE +"*                                                                                                              *"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"*"+ colorama.Style.RESET_ALL, "3 - OFICINA ON-LINE / AGENDAMENTOS")
    print(colorama.Fore.BLUE +"*                                                                                                              *"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"*"+ colorama.Style.RESET_ALL, "4 - ORÇAMENTO / PAGAMENTO")
    print(colorama.Fore.BLUE +"*                                                                                                              *"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"*"+ colorama.Style.RESET_ALL, "5 - PESQUISAR OU LISTAR DADOS DE UM CLIENTE")
    print(colorama.Fore.BLUE +"*                                                                                                              *"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"*"+ colorama.Style.RESET_ALL, "0 - SAIR DO SISTEMA")
    print(colorama.Fore.BLUE +"*                                                                                                              *"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"*                                                                                                              *"+ colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE +"****************************************************************************************************************"+ colorama.Style.RESET_ALL)

#########################################################################################################################################

# finaliza a aplicação

def sairDoPrograma():
    print(colorama.Fore.RED + "**************************************** Sair do programa! ****************************************" + colorama.Style.RESET_ALL)
    sys.exit()
#########################################################################################################################################

# limpa a tela e os menus

#def exibirSubtitulo(texto):
#    os.system("cls")
#    print(texto)
#    print()

#########################################################################################################################################

def voltarMenuPrincipal():
    input("\nDigite uma tecla para voltar ao menu: ")
    main()

#########################################################################################################################################

# mensagem de erro quando o usuário digitar algo errado

def opcaoInvalida():
    print(colorama.Fore.RED + "**************************************** OPÇÃO INVÁLIDA ****************************************" + colorama.Style.RESET_ALL)
    voltarMenuPrincipal()

#########################################################################################################################################

# escolhe quais são as opções desejadas no menu princípal

def escolherOpcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrarNovosClientes()
        elif opcao_escolhida == 2: 
            cadastrarVeiculos()
        elif opcao_escolhida == 3: 
            oficinaAgendamento()
        elif opcao_escolhida == 4: 
            orcamentoPagamento()
        elif opcao_escolhida == 5: 
            pesquisarListar()
        elif opcao_escolhida == 0: 
            sairDoPrograma()
        else: 
            opcaoInvalida()
    except:
        opcaoInvalida()

#########################################################################################################################################

# cadastro de clientes

def cadastrarNovosClientes():
    print(colorama.Fore.BLUE +"**************************************** CADASTRAR NOVOS CLIENTES ****************************************"+colorama.Style.RESET_ALL)
    voltarMenuPrincipal()

#########################################################################################################################################

# cadastro de veiculos

def cadastrarVeiculos():
    print(colorama.Fore.BLUE +"**************************************** CADASTRO DE VEICULOS ****************************************"+colorama.Style.RESET_ALL)
    voltarMenuPrincipal()


#########################################################################################################################################

# oficina e agendamento

def oficinaAgendamento():
    print(colorama.Fore.BLUE +"**************************************** OFICINA ON-LINE / AGENDAMENTOSS ****************************************"+colorama.Style.RESET_ALL)
    voltarMenuPrincipal()

#########################################################################################################################################

# orçamento e pagamento

def orcamentoPagamento():
    print(colorama.Fore.BLUE +"**************************************** ORÇAMENTO / PAGAMENTO ****************************************"+colorama.Style.RESET_ALL)
    voltarMenuPrincipal()

#########################################################################################################################################

# cadastro de clientes

def pesquisarListar():
    print(colorama.Fore.BLUE +"**************************************** PESQUISAR DADOS DE UM CLIENTE ****************************************"+colorama.Style.RESET_ALL)
    voltarMenuPrincipal()




if __name__ == '__main__':
    main()

#########################################################################################################################################
