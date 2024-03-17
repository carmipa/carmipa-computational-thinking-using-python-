ponto1 = 10
ponto2 = 0

chute = int(input("digite sua tentativa: "))
tentativa = 15

if (chute == tentativa):
    print("Você acertou!", "Pontos Ganhos:", ponto1)
elif(chute != tentativa):
    print("Você errou!", "Ponto ganhos:", ponto2)
