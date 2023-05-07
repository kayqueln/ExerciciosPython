#Exercício 18

n = int(input("Digite um número menor que 46: "))
fibonacci = [0, 1]

for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print("Os", n, "primeiros números da série de Fibonacci são:", fibonacci)