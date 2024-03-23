etiqueta = float(input("Digite o preço: "))

print("Escolha uma das opções abaixo:",
      "\n1 - A vista em dinheiro ou pix, recebe 10% de desconto",
      "\n2 - A vista no débito, recebe 5% de desconto",
      "\n3 - Em duas vezes, preço normal de etiqueta sem juros",
      "\n4 - Em três vezes, juros de 5%",
      "\n5 - Em quatro vezes, juros de 8%")
print(".......................................................................")
opcao = int(input("digite a opção desejada: "))
print(".......................................................................")

if(opcao == 1):
    desc = (etiqueta * 10) / 100
    pix = etiqueta - desc
    print("A vista no pix!")
    print("valor sem desconto.......:", etiqueta)
    print("Valor do desconto........:", desc)
    print("valor final com desconto.:", pix)

elif(opcao == 2):
    desc = (etiqueta * 5) / 100
    debito = etiqueta - desc
    print("A vista no débito!")
    print("valor sem desconto.......:", etiqueta)
    print("Valor do desconto........:", desc)
    print("valor final com desconto.:", debito)

elif(opcao == 3):
    print("pagamento em 2x!")
    print("Não tem desconto")
    print("valor final..............:", etiqueta)

elif(opcao == 4):
    desc = (etiqueta * 5) / 100
    parcela3X = etiqueta + desc
    print("Pagamento em 3x!")
    print("valor sem desconto.......:", etiqueta)
    print("Valor do juro............:", desc)
    print("valor final com juro.....:", parcela3X)

elif(opcao == 5):
    desc = (etiqueta * 8) / 100
    parcela4X = etiqueta + desc
    print("Pagamento em 4x!")
    print("valor sem desconto.......:", etiqueta)
    print("Valor do juro............:", desc)
    print("valor final com juro.....:", parcela4X)






