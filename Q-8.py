print("Emprestimo Bancário")

P = float(input("Qual o valor do empréstimo? : "))
A = float(input("Informe o valor da parcela: "))
i = float(input("Informe a taxa de juros mensal: "))

JurosAcumulados = 0
Meses = 0

while P > 0:
    Juros = P * i / 100
    JurosAcumulados += Juros
    reducao_divida = A - Juros
    
    if reducao_divida > P:
        reducao_divida = P
    
    P -= reducao_divida
    Meses += 1
    
    print(f"Mês {Meses}:")
    print(f"Valor dos juros pagos: R${Juros:.2f}")
    print(f"Valor aplicado no pagamento da dívida: R${reducao_divida:.2f}")
    print(f"Valor acumulado de juros já pagos: R${JurosAcumulados:.2f}")
    print(f"Valor restante para pagar do empréstimo: R${P:.2f}\n")

print(f"Número de meses faltantes: {Meses}")
print(f"Valor da última prestação: R${P:.2f}")


print()