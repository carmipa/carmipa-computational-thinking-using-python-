salario = float(input("Digite o valor do seu salário: "))
percentual = float(input("Digite o percentual de aulmento: "))

desconto = (salario * percentual) / 100
valorAumento = salario + desconto

print("Sálario antes do aumento........:", salario)
print("Percentual de aumento...........: %", percentual)
print("Salário após o aumento..........:", valorAumento)