import forca
import adivinhacaov11

def escolhe_jogo():
    print("************************************")
    print("******** Escolha o seu jogo ********")
    print("************************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacaov11.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()