nome = input("Nome do trabalhador....................: ")
valorHora = float(input("Valor hora recebido....................: "))
horasTrabalhada = float(input("Quantidade de horas trabalhada.........: "))
limiteHorasEmpresa = float(input("Limite de horas por mês................:"))
# dias = int(input("Quantidade de dias trabalhado no mês...: "))



if (horasTrabalhada > limiteHorasEmpresa):

    horaMes = valorHora * horasTrabalhada
    horaMetade = horaMes / 2
    horaAdicional = horaMes + horaMetade
    diasTrabalhado = horasTrabalhada / 8
    

    print("..............................................................")
    print("O trabalhador, trabalhou mais horas do que o permitido no mês!")
    print("..............................................................")
    print("Nome..................................:", nome)
    print("Valor hora............................: R$", valorHora)
    print("horas trabalhadas.....................:", horasTrabalhada)
    print("Dias trabalhados......................:", diasTrabalhadoPaulo)
    
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











