nome = input ('Qual o seu nome?: ')
idade = input('Qual a sua idade?: ')

curso = input('Alguém já fez algum curso superior?: ')
qual = input('Se sim, qual?: ')
escolha = input('Por que escolher ti?: ')
area = input('Area que deseja trabalhar?: ')
hobbies = input('Quais são os seus hobbies?: ')

arq = open("dados.txt", "w")
arq.write(f"{nome}&{idade}&{curso}&{qual}&{escolha}&{area}&{hobbies}")
arq.close()