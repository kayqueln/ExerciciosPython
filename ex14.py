#Exercício 14

n = int(input("Digite um número natural N: "))
s = 0
for i in range(1, n+1):
    s += 2*i/(2*i + 1)
print("O resultado da soma é:", round(s, 2))

