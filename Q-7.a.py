print("Sequencia de Fibonacci Letra A")

def fibonacci(n):
    Sequencia = []
    a, b = 0, 1

    while len(Sequencia) < n:
        Sequencia.append(a)
        a, b = b, a + b

    return Sequencia

n = int(input("Digite o número de termos que você quer mostrar: "))

result = fibonacci(n)
print("Sequência de Fibonacci:")
for num in result:
    print(num)
