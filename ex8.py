#Exercício 8

soma = 0

for i in range(13, 74):
    if i%2 == 0:
        soma = soma + i
        media = soma / 30

print(media)