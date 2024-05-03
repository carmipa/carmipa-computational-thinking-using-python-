preco = float(input("Preço do produto.....: "))
desconto = float(input("Desconto do Produto..: "))

precoDesconto = (preco * desconto) / 100
precoTotal = preco - precoDesconto

print("Preço Produto.........:", preco)
print("Desconto..............:", desconto)
print(f"Preço com desconto....: {precoTotal:.3}") # f e {precototal:.3} - significa que diminui as casas decimais em e digitos

#print("Preço Produto.........:", preco)
#print("Desconto..............:", desconto)
#print(f"Preço com desconto....: {precoTotal:.3}")