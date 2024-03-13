nome = input("Nome do trabalhador....................: ")
valorHora = float(input("Valor hora recebido....................: "))
horasTrabalhada = int(input("Quantidade de horas trabalhada.........: "))
# dias = int(input("Quantidade de dias trabalhado no mês...: "))

horasLimite = 160

if (horasTrabalhada > horasLimite):

    horaMes = valorHora * horasTrabalhada
    horaMetade = horaMes / 2
    horaAdicional = horaMes + horaMetade

    print("..............................................................")
    print("O trabalhador, trabalhou mais horas do que o permitido no mês!")
    print("..............................................................")
    print("Nome..................................:", nome)
    print("Valor hora............................: R$", valorHora)
    print("horas trabalhadas.....................:", horasTrabalhada)
    # print("Dias trabalhados......................:", dias)
    print("..............................................................")
    print("Salário calculado com o adicional de a horas extras:")
    print()
    print("Valor do salário com adicional de 50%.: R$", horaAdicional)
    print("..............................................................")

elif (horasTrabalhada <= horasLimite):

    horaMes = valorHora * horasTrabalhada

    print("Trabalhador não tem direito as horas extras este mês")
    print("..............................................................")
    print("Nome..................................:", nome)
    print("Valor hora............................: R$", valorHora)
    print("horas trabalhadas.....................:", horasTrabalhada)
    print("Salário do mês........................: R$", horaMes)
    print("..............................................................")











