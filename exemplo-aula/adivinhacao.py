import random

print("***Jogo da Adivinhação***")


while True:
    
    chute = int(input("Digite seu Chute: "))
    
    resposta = round(random.randrange(1, 1001))

    if (chute == resposta):
        print("Você acertou!")

    elif(chute != resposta):
        print("Chute errado!", resposta)
            
        if(chute < resposta):
            print("Seu chute foi menor!", resposta)
            
        elif(chute > resposta):
            print("Seu chute foi maior", resposta)
    else:
        print("fim da tentativas")
        break
    
        


    


