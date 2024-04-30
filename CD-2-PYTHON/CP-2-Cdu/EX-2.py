def calcular_aumento(produtos):
    maior_aumento_percentual = 0
    maior_aumento_reais = 0
    
    for produto in produtos:
        preco_atual, preco_reajustado = produto
        aumento_reais = preco_reajustado - preco_atual
        aumento_percentual = (aumento_reais / preco_atual) * 100
        
        if aumento_reais > maior_aumento_reais:
            maior_aumento_reais = aumento_reais
            
        if aumento_percentual > maior_aumento_percentual:
            maior_aumento_percentual = aumento_percentual
            
    return maior_aumento_reais, maior_aumento_percentual

# Entrada de dados
n = int(input("Digite a quantidade de produtos: "))
produtos = []
for i in range(n):
    preco_atual = float(input(f"Digite o preço atual do produto {i+1}: "))
    preco_reajustado = float(input(f"Digite o preço reajustado do produto {i+1}: "))
    produtos.append((preco_atual, preco_reajustado))

# Chamada da função e impressão do resultado
maior_aumento_reais, maior_aumento_percentual = calcular_aumento(produtos)
print("Maior aumento em reais: R$", maior_aumento_reais)
print("Maior aumento percentual: ", maior_aumento_percentual, "%")

