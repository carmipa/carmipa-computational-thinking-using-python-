def jogar():

    print("************************************")
    print("**** Bem vindo ao jogo de Forca ****")
    print("************************************")

        # Palavra a ser adivinhada
    palavra = "python"

    # Letras já escolhidas pelo usuário
    letras_usuario = []

    # Chances disponíveis
    chances = 7

    # Variável para verificar se o jogador ganhou
    ganhou = False

    while True:
        # Verifica se o jogador ganhou
        if ganhou:
            print(f"Parabéns, você ganhou! A palavra era: {palavra}")
            break
        # Verifica se o jogador perdeu
        elif chances == 0:
            print(f"Você perdeu! A palavra era: {palavra}")
            break

        # Exibe a palavra com as letras já adivinhadas
        palavra_mostrada = ""
        for letra in palavra:
            if letra in letras_usuario:
                palavra_mostrada += letra
            else:
                palavra_mostrada += "_ "

        print(f"Palavra: {palavra_mostrada}")
        print(f"Chances restantes: {chances}")

        # Pede ao jogador para escolher uma letra
        letra_escolhida = input("Escolha uma letra: ").lower()

        # Verifica se a letra está na palavra
        if letra_escolhida in palavra:
            letras_usuario.append(letra_escolhida)
            print("Letra correta!")
        else:
            chances -= 1
            print("Letra incorreta. Tente novamente.")

        # Verifica se todas as letras da palavra foram adivinhadas
        if all(letra in letras_usuario for letra in palavra):
            ganhou = True

if(__name__ == "__main__"):
    jogar()