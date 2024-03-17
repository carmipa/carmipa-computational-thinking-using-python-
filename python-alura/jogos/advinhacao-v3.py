print("************************************")
print("* Bem vindo ao jogo de Adivinhação *")
print("************************************")

numeroSecreto = 42

chute = int(input("Digite o seu número:"))

acertou = numeroSecreto == chute

if (acertou):
    print("Você acertou, chute!",chute_str)
else:
    if(chute > numeroSecreto):
        print("Você errou! seu chute foi maior que o número secreto.", chute)
    elif(chute < numeroSecreto):
        print("Você errou!, seu chute foi menor que o numero secreto." , chute)

    
print("Fim do jogo")