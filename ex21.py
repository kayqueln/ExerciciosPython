#Exercício 21

n = int(input('Digite um número: '))
divisor = 0

for i in range(1, n):
    if n%i == 0:
        divisor += i

if divisor == n:
    print('O número', n ,'é perfeito')
else:
    print('O número', n ,'não é perfeito')
