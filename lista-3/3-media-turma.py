# Solicita a quantidade de alunos na classe
alunos = int(input("Quantidade de alunos na classe: "))

# Verifica se a quantidade de alunos é válida (maior que zero)
while alunos <= 0:
    print("Digite uma quantidade válida de alunos!")
    alunos = int(input("Quantidade de alunos na classe: "))

# Inicializa as variáveis para contagem
aprovados = 0
exame = 0
reprovados = 0

# Coleta as notas dos alunos e faz a contagem
for i in range(alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    if 0 <= nota < 5.0:
        reprovados += 1
    elif nota >= 5.0:
        aprovados += 1
    else:
        exame += 1

# Calcula a média das notas
somaNotas = sum([float(input(f"Digite a nota do aluno {i+1}: ")) for i in range(alunos)])
media = somaNotas / alunos

# Exibe os resultados
print(f"A média da turma é: {media:.2f}")
print(f"Alunos aprovados: {aprovados}")
print(f"Alunos em exame: {exame}")
print(f"Alunos reprovados: {reprovados}")