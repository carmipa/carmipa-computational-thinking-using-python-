import random
def jogarAdivinhacao():

    print("************************************")
    print("* Bem vindo ao jogo de Adivinhação *")
    print("************************************")

    numeroSecreto = round(random.randrange(1, 101)) #gera número entre 1 e 100
    int(numeroSecreto)
    totalTentativas = 0

    pontos = 1000

    print("Qual nível de dificulade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == "1"):
        totalTentativas = 202
    elif(nivel == "2"):
        totalTentativas = 10
    else:
        totalTentativas = 5

    for rodada in range (1, totalTentativas + 1):
        print("Tentativa {} de {}".format(rodada, totalTentativas))
        chute = int(input("Digite número entre 1 e 100:"))

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numeroSecreto
        maior   = chute <  numeroSecreto
        menor   = chute <  numeroSecreto

        if (acertou):
            print("Você acertou, chute!", "E fez: {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! seu chute foi maior que o número secreto.", chute)
            elif(menor):
                print("Você errou!, seu chute foi menor que o numero secreto." , chute)
            pontosPerdidos = abs(numeroSecreto - chute) 
            pontos = pontos - pontosPerdidos
        
    print("Fim do jogo! ", "\nA resposta correta éra:", numeroSecreto)