print("Sequencia de Fibonacci Letra b")

def fibonacci (N):
    Sequencia = []
    a, b = 0, 1

    while len(Sequencia) < N:
        Sequencia.append(a)
        a, b = b, a + b

    return Sequencia

N = int(input("Digite um valor para N: "))
result = fibonacci(N)
print("Sequência de Fibonacci:")
for num in result:
    print(num)

if N in result:
    print("\nO número", N, "faz parte da sequência de Fibonacci.")
else:
    print("\nO número", N, "não faz parte da sequência de Fibonacci.")