#Exercício 6

cont = 1
maiorIdade  = 0

while cont <= 5:
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do aluno: '))
    sexo = input('Digite o sexo do aluno: ')
    if idade > maiorIdade:
        nomeMaisVelho = nome
        maiorIdade = idade
        sexoMaisVelho = sexo
    cont += 1

print('Nome do aluno mais velho:', nomeMaisVelho)
print('Idade do aluno mais velho:',maiorIdade)
print('Sexo do aluno mais velho:',sexoMaisVelho)