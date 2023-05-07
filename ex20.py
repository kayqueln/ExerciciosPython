#Exercício 20

saldo = float(input('Digite o saldo: '))

operacao = int(input('Digite a operação desejada'
                     '\n1 - Depositar'
                     '\n2 - Sacar'
                     '\n3 - Sair \n'))

while operacao != 3:
    match operacao:
        case 1:
            deposito = float(input('Digite o valor a ser depositado: '))
            saldo += deposito
            print('Operação finalizada com sucesso')
        case 2:
            saque = float(input('Digite o valor a ser sacado: '))
            saldo -= saque
            print('Operação finalizada com sucesso')
        case _:
            print('Operação inválida')

    operacao = int(input('Digite a operação desejada'
                         '\n1 - Depositar'
                         '\n2 - Sacar'
                         '\n3 - Sair \n'))

if saldo > 0:
    print('Conta preferencial')
elif saldo == 0:
    print('Conta zerada')
else:
    print('Conta estourada')
