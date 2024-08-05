def calcular_conta_agua(consumo_anterior, consumo_atual):
    # Tabela de preços por faixa de consumo
    precos = [(20, 2.00), (35, 3.50), (50, 5.50), (float('inf'), 7.00)]
    
    # Função para calcular o valor do consumo
    def calcular_valor(consumo):
        valor = 0
        for faixa, preco in precos:
            if consumo > faixa:
                valor += faixa * preco
                consumo -= faixa
            else:
                valor += consumo * preco
                break
        return valor
    
    # Calcula o valor do consumo atual
    valor_consumo = calcular_valor(consumo_atual)
    
    # Verifica se haverá desconto ou multa
    if consumo_atual < consumo_anterior:
        desconto = valor_consumo * 0.15
        valor_final = valor_consumo - desconto
        return f"Valor do consumo: R$ {valor_consumo:.2f}\nDesconto: R$ {desconto:.2f}\nTotal da conta: R$ {valor_final:.2f}"
    elif consumo_atual > consumo_anterior:
        multa = valor_consumo * 0.10
        valor_final = valor_consumo + multa
        return f"Valor do consumo: R$ {valor_consumo:.2f}\nMulta: R$ {multa:.2f}\nTotal da conta: R$ {valor_final:.2f}"
    else:
        return f"Valor do consumo: R$ {valor_consumo:.2f}\nTotal da conta: R$ {valor_consumo:.2f}"

# Exemplo de uso da função
consumo_anterior = float(input("Digite o consumo em m3 do mês anterior: "))
consumo_atual = float(input("Digite o consumo em m3 do mês vigente: "))
print(calcular_conta_agua(consumo_anterior, consumo_atual))