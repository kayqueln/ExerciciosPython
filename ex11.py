#Exercício 11

n = int(input("Digite um número natural N: "))
s = 0
for i in range(1, n+1):
    if i % 2 == 0:
        s -= 1/i
    else:
        s += 1/i
print(round(s, 2))
