#Exercício 9

alunos = int(input('Digite o número de alunos: '))
cont = 0

while cont <= alunos:
    nota1 = int(input('Digite a nota 1: '))
    nota2 = int(input('Digite a nota 2: '))
    nota3 = int(input('Digite a nota 3: '))
    media = (nota1 + nota2 + nota3) / 3
    cont += 1
    print('Média do aluno', cont, ':', round(media, 1))
