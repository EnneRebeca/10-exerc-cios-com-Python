print('Exercício 3: idade')

DataNasc = int(input("Informe o ano de nascimento: "))
DataAtual = int(input("Informe o ano atual: "))

idade_em_anos = (DataAtual - DataNasc)
idade_em_meses = idade_em_anos * 12
idade_em_dias = idade_em_anos * 365
idade_em_semanas = idade_em_dias // 7

print("A pessoa tem:")
print(idade_em_anos, "anos, ", idade_em_meses, "meses, ", idade_em_dias, "dias e", idade_em_semanas, "semanas. ")


