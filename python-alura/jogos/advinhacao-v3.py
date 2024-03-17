print("************************************")
print("* Bem vindo ao jogo de Adivinhação *")
print("************************************")

numeroSecreto = 42

chute = int(input("Digite o seu número:"))

acertou = chute == numeroSecreto
maior   = chute <  numeroSecreto
menor   = chute <  numeroSecreto

if (acertou):
    print("Você acertou, chute!",chute_str)
else:
    if(maior):
        print("Você errou! seu chute foi maior que o número secreto.", chute)
    elif(menor):
        print("Você errou!, seu chute foi menor que o numero secreto." , chute)

    
print("Fim do jogo")