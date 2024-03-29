consumo_atual = float(input("Digite o consumo atual: "))
consumo_ant = float(input("Digite o consumo anterior: "))

if consumo_atual <= 20:
    valor_m3 = 2.00
elif consumo_atual <= 35:
    valor_m3 = 3.50
elif consumo_atual <= 50:
    valor_m3 = 5.50
else:
    valor_m3 = 7.00            

valor_conta = consumo_atual * valor_m3

if consumo_atual > consumo_ant:
    multa = valor_conta * 0.10
    print(f"Multa: {multa}")
    valor_conta = valor_conta + multa

elif consumo_atual < consumo_ant:
    desconto = valor_conta * 0.15
    print(f"Desconto: {desconto}")    
    valor_conta = valor_conta - desconto

print(f"O valor da conta é {valor_conta}")