nome = input("Nome do aluno......................: ")
nota1 = float(input("Nota 1.............................: "))
nota2 = float(input("Nota 2.............................: "))
aulasM = int(input("Quantidade de aulas ministradas....: "))
aulasA = int(input("QUantidade de aulas assistidadas...: "))

media = ((nota1 * 4) + (nota2 * 6)) / 10

mediaP = (aulasM * aulasA) /1000

if (media  < 5 ):
    print("Aluno...............:", nome)
    print("Aluno Reprovado.....: ", media)
    print("Aulas frequentadas..:", mediaP, "%")
elif(media >= 5 and media < 7):
    print("Aluno...............:", nome)
    print("Aluno de exame......: ", media)
    print("Aulas frequentadas..:", mediaP, "%")
elif(media >= 7):
        print("Aluno...............:", nome)
        print("Aluno Aprovado......: ", media)
        print("Aulas frequentadas..:", mediaP, "%")
