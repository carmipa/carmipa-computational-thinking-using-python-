quantidade = int(input("Digite a quantidade de produtos: "))

maiorAumentoReal = 0
maiorAumentoPercentual = 0


for i in range(quantidade):

    precoAtual = float(input(f"Digite o preço atual do produto {i+1}: R$ "))
    precoReajustado = float(input(f"Digite o preço reajustado do produto {i+1}: R$ "))
    
    aumentoReal = precoReajustado - precoAtual
    aumentoPercentual = (aumentoReal / precoAtual) * 100
    

    if (aumentoReal > maiorAumentoReal):

        maiorAumentoReal = aumentoReal

    if (aumentoPercentual > maiorAumentoPercentual):

        maiorAumentoPercentual = aumentoPercentual

print(f"Maior aumento em reais: R$ {maiorAumentoReal:.2f}")
print(f"Maior aumento percentual: {maiorAumentoPercentual:.2f} %")