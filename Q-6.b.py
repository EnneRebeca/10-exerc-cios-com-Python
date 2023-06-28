print("Reajuste salarial Letra B")

def CalcularSalarioReajustado(Salario, Percentual):
    return Salario + (Salario * Percentual / 100)
N = int(input("Digite o valor de N: "))
funcionarios = []

for i in range(N):
    print(f"\nFuncionário {i+1}:")
    Nome = input("Informe o nome do funcionário: ")
    Salario = float(input("Informe o Salário: "))
        
    funcionario = {
        "Nome": Nome,
        "Salario": Salario
    }

    funcionarios.append(funcionario)

print("\nInformações dos funcionários:")
print(f"Nome: {funcionario['nome']}")
print(f"Salário: {funcionario['salario']}")

if Salario != N:
    NovoSalario_25 = CalcularSalarioReajustado(Salario, 25)
    NovoSalario_20 = CalcularSalarioReajustado(Salario, 20)
    NovoSalario_15 = CalcularSalarioReajustado(Salario, 15)
    NovoSalario_10 = CalcularSalarioReajustado(Salario, 10)

print(funcionario,"seu salario de" , Salario, f"foi reajustado para 25%, sendo: R${NovoSalario_25:.2f}", "seu novo salario.")
print(funcionario,"seu salario de" , Salario, f"foi reajustado para 20%, sendo: R${NovoSalario_20:.2f}", "seu novo salario.")
print(funcionario,"seu salario de" , Salario, f"foi reajustado para 15%, sendo: R${NovoSalario_15:.2f}", "seu novo salario.")
print(funcionario,"seu salario de" , Salario, f"foi reajustado para 10%, sendo: R${NovoSalario_10:.2f}", "seu novo salario.")
         
   
print(".")
    