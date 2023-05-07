#Exercício 12

n = int(input("Digite um número natural N: "))
s = 0
for i in range(1, n):
    s += (i/n) - ((i-1)/2)
s += n/1
print("O resultado da soma é:", s)
