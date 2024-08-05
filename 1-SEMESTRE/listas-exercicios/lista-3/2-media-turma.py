# Solicita a quantidade de alunos na classe
alunos = int(input("Quantidade de alunos na classe: "))

# Verifica se a quantidade de alunos é válida (maior que zero)
while alunos <= 0:
    print("Digite uma quantidade válida de alunos!")
    alunos = int(input("Quantidade de alunos na classe: "))

# Inicializa a variável para armazenar a soma das notas
somaNotas = 0

# Coleta as notas dos alunos
for i in range(alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    somaNotas += nota

# Calcula a média das notas
media = somaNotas / alunos

# Exibe a média da turma
print(f"A média da turma é: {media:.2f}")



