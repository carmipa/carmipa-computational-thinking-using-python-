print("************************************")
print("* Bem vindo ao jogo de Adivinhação *")
print("************************************")

numeroSecreto = 42
totalTentativas = 3
rodada = 1

while (rodada <= totalTentativas):
    print("Tentativa {} de {}".format(rodada, totalTentativas))
    chute = int(input("Digite o seu número:"))

    acertou = chute == numeroSecreto
    maior   = chute <  numeroSecreto
    menor   = chute <  numeroSecreto

    if (acertou):
        print("Você acertou, chute!",chute)
    else:
        if(maior):
            print("Você errou! seu chute foi maior que o número secreto.", chute)
        elif(menor):
            print("Você errou!, seu chute foi menor que o numero secreto." , chute)
    
        print("Fim do jogo")
    
    rodada = rodada + 1
