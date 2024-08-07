def main():
    resp =1
    lista_palavras =[]
    while(resp != 0):
        print("1- Ler  lista de palavrs")
        print("2- Contar palavras palindromas")
        print()
        
        opc = int(input("Digite a opção desejada (1-3):"))
        
        match opc:
            case 1:
                ler_lista_palavra(lista_palavras)
            case 2: 
                if (len(lisya_palavraa)>0):
                    print("")
                else:
                    print("Lista Vazia")
            case 3:
                if(len(lista_palavras)>0):
                    print("Lista palavras que començam com a letra A: ")
                else:
                    print("Lista vazia")
            case _:
                print("Opção inválida")
                
    
def ler_lista_palavras(lista_palavras):
    for i in range(10):
        lista_palavras.append(input("Digite a palavra: "))

def contar_palindromas(lista_palavras):
    qtde_palindromas = 0
    for i in range(10):
        if (lista_palavras[i] == lista_palavras[i][::-1]):
            qtde_palindromas += 1
        return (qtde_palindromas)

def criar_lista_letraA(lista_palavras):
    lista_letraA = []
    for i in range(10):
        if (lista_palavras[i][0] =="A"):
            lista_letraA.append(lista_palavras[i])
    return(lista_letraA)   

if __name__ == "__main__":
        main