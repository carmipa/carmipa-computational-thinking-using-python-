print("************************************")
print("* Bem vindo ao jogo de Adivinhação *")
print("************************************")

numeroSecreto = 42

chute_str = int(input("Digite o seu número:"))

if (numeroSecreto == chute_str):
    print("Você acertou, chute!",chute_str)
else:
    print("Você errou!",chute_str)