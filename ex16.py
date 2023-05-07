#Exercício 16

n = int(input('Digite a quantidade de números: '))
cont = 1

while cont <= n:
    numero = int(input('Digite um número: '))
    if numero != 0:
        if numero%2 == 0:
            print('Este número é par')
        else:
            print('Este número é impar')

        if numero > 0:
            print('Este número é positivo')
        else:
            print('Este número é negativo')
    else:
        print('NUlO')
    cont += 1