valorIptuAvista = float(input("Digite o valor do IPTU................: R$ "))
valorDescontoIptu = float(input("Digite o valor de desconto do IPTU....:  % "))

desconto = (valorIptuAvista * valorDescontoIptu) / 100
valorParcelado = valorIptuAvista + desconto
valorIptuparcela = (valorIptuAvista + desconto) / 10
descontoIptuAvista = valorIptuAvista - desconto

print(".......................................")
print("Valor do IPTU.........................: R$", valorIptuAvista)
print("Percentual de desconto do IPTU........:  %",valorDescontoIptu)
print("Valor do IPTU com desconto............: R$", descontoIptuAvista)
print("Valor do total do IPTU parcelado......: R$", valorParcelado)
print("Valor da parcela de IPTU em 10 X......: R$", valorIptuparcela)
