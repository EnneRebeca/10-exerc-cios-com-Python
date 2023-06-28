print("Reajuste salarial Letra A")

def CalcularSalarioReajustado(Salario, Percentual):
    return Salario + (Salario * Percentual / 100)

    
NomeFuncionario = input("Qual o nome do funcionario? : ")
Salario = float(input("Informe o salário atual: "))

if Salario != 0:
    NovoSalario_25 = CalcularSalarioReajustado(Salario, 25)
    NovoSalario_20 = CalcularSalarioReajustado(Salario, 20)
    NovoSalario_15 = CalcularSalarioReajustado(Salario, 15)
    NovoSalario_10 = CalcularSalarioReajustado(Salario, 10)

print(NomeFuncionario,"seu salario de" , Salario, f"foi reajustado para 25%, sendo: R${NovoSalario_25:.2f}", "seu novo salario.")
print(NomeFuncionario,"seu salario de" , Salario, f"foi reajustado para 20%, sendo: R${NovoSalario_20:.2f}", "seu novo salario.")
print(NomeFuncionario,"seu salario de" , Salario, f"foi reajustado para 15%, sendo: R${NovoSalario_15:.2f}", "seu novo salario.")
print(NomeFuncionario,"seu salario de" , Salario, f"foi reajustado para 10%, sendo: R${NovoSalario_10:.2f}", "seu novo salario.")
         
   
print(".")
