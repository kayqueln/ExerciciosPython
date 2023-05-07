#Exercício 13

n = int(input("Digite um número natural N: "))
s = 0
numerator = 1
denominator = 1
for i in range(1, n+1):
    s += numerator/denominator
    numerator *= (i+1)
    denominator *= (2*i + 1)
print("O resultado da soma é:", round(s, 2))
