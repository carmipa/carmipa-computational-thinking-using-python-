def troca_dinheiro(cedula, moeda1, moeda2):
    # Verifica se é possível efetuar a troca
    if cedula % moeda1 == 0:
        return True, cedula // moeda1, 0
    elif cedula % moeda2 == 0:
        return True, 0, cedula // moeda2
    
    # Tenta todas as combinações possíveis
    for i in range(1, cedula // moeda1 + 1):
        for j in range(1, cedula // moeda2 + 1):
            if cedula == i * moeda1 + j * moeda2:
                return True, i, j
    
    # Se nenhuma combinação for encontrada, retorna False
    return False, 0, 0

# Entrada de dados
cedula = int(input("Digite o valor da cédula: "))
moeda1 = int(input("Digite o valor de uma moeda: "))
moeda2 = int(input("Digite o valor da outra moeda: "))

# Chamada da função e impressão do resultado
possivel, qtd_moeda1, qtd_moeda2 = troca_dinheiro(cedula, moeda1, moeda2)
if possivel:
    print("Possível:", qtd_moeda1, "moeda(s) de", moeda1, "e", qtd_moeda2, "moeda(s) de", moeda2)
else:
    print("Não é possível fazer a troca.")
