# print("hello world")
# aspas triplas """ """ pode ser usada para quebra de linha
#
# IMPORT ##############################################################################################################

import os

#######################################################################################################################

# LISTA ##############################################################################################################

restaurantes = []

#######################################################################################################################

def exibir_nome_do_programa():
    print(""" 
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurantes")
    print("3 - Ativar Restaurantes")
    print("4 - Sair\n")

def finalizar_app():
    os.system("cls")
    print("Encerrando o progrma\n")

def opcao_invalidade():
    print("Opção inválidade!\n")
    input("Digite uma tecla para voltar ao menu princípal: ")
    main()

def cadastrar_novo_restaurante():
    os.system("cls")
    print("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso")
    input("Digite um tecla para voltar ao menu princípal: ")
    main()
    pass


def escolher_opcao():
    try:

        opcao_escolhida = int(input("Escolha uma opção: "))
        #print(f"Você escolheu a opção: {opcao_escolhida}")

        # type como no exemplo abaixo mostra o que está retornando como resposta no programa
        #
        # print(type(opcao_escolhida))
        # print(type(1))

        if (opcao_escolhida == 1):
            cadastrar_novo_restaurante()
        elif (opcao_escolhida == 2):
            print("2 - Listar restaurantes")
        elif (opcao_escolhida == 3):
            print("3 - Ativar Restaurantes")
        elif(opcao_escolhida == 4):
            finalizar_app()
        else:
            opcao_invalidade()

    except:
        opcao_invalidade()
    
    # try / except - tenta rodar o programa se for digitado tanto um número errado como uma letra e se isso ocorrer ele oferece a mensagem correta e volta ao ciclo

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()