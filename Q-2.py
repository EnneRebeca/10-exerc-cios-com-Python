print('Exercício 2: Reajuste a critério do empregador')

SalarioDoFuncionario = float(input("Digite o valor atual do salário do funcionário: "))
ReajusteComPorcentagem = float(input("Digite a porcentagem de reajuste: "))

SalarioNew = SalarioDoFuncionario * (1 + ReajusteComPorcentagem/100)

print("Salário do funcionário é com reajuste é: R$", SalarioNew)
