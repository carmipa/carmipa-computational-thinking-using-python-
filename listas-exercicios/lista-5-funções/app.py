# print("hello world")
# aspas triplas """ """ pode ser usada para quebra de linha
#
# IMPORT ##############################################################################################################

import os

#######################################################################################################################

# LISTA ##############################################################################################################

restaurantes = ["Pizza", "Sushi"]

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
    exibir_subtitulo("Encerrando o programa")

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu: ")
    main()

def opcao_invalidade():
    print("Opção inválidade!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto): # limpa os menus e exibe um titulos
    os.system("cls")
    print(texto)
    print()

def cadastrar_novo_restaurante():

    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_do_restaurante = input("digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso")
    voltar_ao_menu_principal()

def listar_restaurantes():
    
    exibir_subtitulo("Listar restaurantes:")
    
    for restaurante in restaurantes:
        print(f".{restaurante}")

    voltar_ao_menu_principal()

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
            listar_restaurantes()
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