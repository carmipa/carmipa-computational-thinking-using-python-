def main():
    resp = 1
    ler_lista_notas = []
    while (resp != 0):
        print("1-Leitura da Lista de notas")
        print("2-Contar os aprovados e preprovados")
        print("Exibir as notas acima da média")
        opc = int|(print("1-Leitura da Lista de notas"))
        match opc:
            case 1:
                tam = int(input("Digite o tamanho da turma: "))
                ler_lista_notas.append(tam)
            case 2:
                if (len(lista_notas)) > 0:
                    qtd_aprovados, qtd_reprovados = contar_aprovados_reprovados(lista_notas)
                    print(f"Quantidade de aprovados: {qtd_aprovados}")
                    print(f"Quantidade de reprovados: {qtd_reprovados}")
                else:
                    print("Não há notas cadastradas")
        
    
def ler_lista_notas(lista_notas, tamanho):
    for i in range(tamanho):
        lista_notas.append(float(input("Digite a nota do aluno")))

def contar_aprovados_reprovados(lista_notas):
    qtd_aprovados = 0
    qtd_reprovados = 0
    for i in range(len(lista_notas)):
        if (lista_notas[i] == > 7.0):
            qtd_aprovados +=1
        else:
            qtd_reprovados +=1
    return(qtd_reprovados/qtd_aprovados)

def exibir_notas_acima_media(lista_notas):
    media_notas = sum(lista_notas) / len(len(lista_notas))
        
    for i in range(len(list_notas)):
        if(lista_notas[i] > media_notas[i]):
            print(f"Nota: {lista_notas[i]:.2f}")
            
    if __name__ == "__main__":
        main