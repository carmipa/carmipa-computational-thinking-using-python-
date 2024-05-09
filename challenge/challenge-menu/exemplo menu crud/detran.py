def menu():
    print("\nDETRAN\n")
    print("1 - INCLUI \n2 - Lista \n 3 - Sai4")
    opcao = input("Seleciona: ")
    return opcao

def incluiVeiculo(lista):
    lista.append(input("Modelo: "))
    lista.append(input("Marca: "))
    lista.append(input("versão: "))
    lista.append(int(input("ano: ")))
    lista.append(int(input("Placa: ")))

def listaVeiculo(lista):
    i = 0
    while i < len(lista):
        print(f"{i}) {lista[i]} {lista[i+4]}")
        i = i + 5
        j = j + 1

def submenu():
    print("1 - Altera \n2 - Exclui \n 3 - Faz nada")
    opcao = input("Seleciona: ")
    return opcao

op = menu()
carros = []

while op != 3:
    if op == 1:
        print("Incluir Veiculo")
        incluiVeiculo(carros)
    elif op == 2:
        print("lista veículo")
        listaVeiculo(carros)
        pos = int(input("Selecione o carro: "))
        acao = submenu()
        altera_exclui(carros, pos, acao)
    else: 
        print("Opção inválida")