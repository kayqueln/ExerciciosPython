#Exercício 3

maior = 0

for i in range(1, 11):
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num

print(maior)
