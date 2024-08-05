n = int(input("Informe a quantidade de alunos: "))
soma = 0

listaNotas = []

i = 0
while i < n:
    nota = float(input("Informe a nota do aluno: "))
    listaNotas.append((nota))
    soma = soma + nota
    i = i + 1

media = soma / n
print(f"A média da turma foi de {media}")
print(listaNotas,".")

for nota in listaNotas:
    if nota < media:
        abaixo = abaixo + 1
    else:
        acima = acima + 1
print(f"A quantidade de alunos abaixo é de {abaixo}")
print(f"A quantidade de alunos acima da média é de {acima}")