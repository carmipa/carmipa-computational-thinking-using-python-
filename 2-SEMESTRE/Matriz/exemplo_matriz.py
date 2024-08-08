def main():
    matriz = []
    ler_matriz(matriz,3, 3)
    exibir_matriz(matriz, 3)
    exibir_impares_matriz(matriz, 3, 3)
    print(f"Soma da diagonal princípal: {somar_diagonal_principal(matriz,3, 3)}")


def ler_matriz(matriz, nlin, ncol):
    for lin in range(nlin):
        linha = []
        for col in range(ncol):
            linha. append((int(input("Digite o elemento da matriz"))))
        matriz.append(linha)

def exibir_impares_matriz(matriz, nlin, ncol):
    for lin in range(nlin):
        for col in range(ncol):
            if (matriz [lin][col] % 2 != 0):
                print(matriz[lin][col])

def somar_diagonal_principal(matriz, nlin, ncol):
    soma_diagonal = 0
    for lin in range(nlin):
        for col in range(ncol):
            if (lin == col):
                soma_diagonal += matriz[lin][col]
    return (soma_diagonal)

def exibir_matriz(matriz, nlin):
    for lin in range(nlin):
        print(matriz[nlin])
