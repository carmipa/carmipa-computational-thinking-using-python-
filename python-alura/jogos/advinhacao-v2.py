print("************************************")
print("* Bem vindo ao jogo de Adivinhação *")
print("************************************")

numeroSecreto = 42

chute = input("Digite o seu número:")

if (numeroSecreto == chute):
    print("Você acertou, chute",chute)
else:
    print("Você errou",chute)