
while True:
    produto = input("Produto..: ")
    preco = float(input("Preço....: "))
    print("...............................................................")
    print("Digite uma das opções desejadas:")
    print("1 - A vista no dinheiro ou cheque, 10% de desconto")
    print("2 - A vista no cartão de crédito, 5% de desconto")
    print("3 - Em 2 vezes, preço normal de etiqueta sem juros")
    print("4 - Em 4 vezes, preço normal de etiqueta mais 7% de juro")
    opcao = input("Opção: ")
    print("...............................................................")

    if(opcao == "1"):
        desconto = (preco * 10) / 100
        precoF = preco - desconto
        
        print("Produto..........:", produto)
        print("Preço............:", preco)
        print("Desconto.........:", desconto)
        print("Preço da compra..:", precoF)
        print("................................................................")
        break
    
    if(opcao == "2"):
        desconto = (preco * 5) / 100
        precoF = preco - desconto
        
        print("Produto..........:", produto)
        print("Preço............:", preco)
        print("Desconto.........:", desconto)
        print("Preço da compra..:", precoF)
        print("................................................................")
        break

    if(opcao == "3"):
        
        print("Produto..........:", produto)
        print("Preço............:", preco)
        print("Preço da compra..:", preco)
        print("................................................................")
        break

    if(opcao == "4"):
        acrescimo = (preco * 7) / 100
        precoF = preco + acrescimo
    
        print("Produto..........:", produto)
        print("Acrescimo........:", acrescimo)
        print("Preço da compra..:", precoF)
        print("................................................................")
        break

    elif(opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4"):
        print("Escolha a opção correta!")