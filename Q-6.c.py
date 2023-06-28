def CalcularSalarioReajustado(Salario, Percentual):
    return Salario + (Salario * Percentual / 100)

funcionarios = []
NomeFuncionario = input("Qual o nome do funcionario? : ")
Salario = float(input("Informe o salário atual: "))
salarios_atuais = []
salarios_reajustados = []

funcionarios.append(NomeFuncionario)

if Salario != 0:
    NovoSalario_25 = CalcularSalarioReajustado(Salario, 25)
    NovoSalario_20 = CalcularSalarioReajustado(Salario, 20)
    NovoSalario_15 = CalcularSalarioReajustado(Salario, 15)
    NovoSalario_10 = CalcularSalarioReajustado(Salario, 10)

print(NomeFuncionario,"seu salario de" , Salario, f"foi reajustado para 25%, sendo: R${NovoSalario_25:.2f}", "seu novo salario.")
print(NomeFuncionario,"seu salario de" , Salario, f"foi reajustado para 20%, sendo: R${NovoSalario_20:.2f}", "seu novo salario.")
print(NomeFuncionario,"seu salario de" , Salario, f"foi reajustado para 15%, sendo: R${NovoSalario_15:.2f}", "seu novo salario.")
print(NomeFuncionario,"seu salario de" , Salario, f"foi reajustado para 10%, sendo: R${NovoSalario_10:.2f}", "seu novo salario.")

   
salarios_atuais.append(Salario)
novo_salario = CalcularSalarioReajustado(Salario, 25)
salarios_reajustados.append(novo_salario)

soma_salarios_atuais = sum(salarios_atuais)
soma_salarios_reajustados = sum(salarios_reajustados)
diferenca_somas = soma_salarios_reajustados - soma_salarios_atuais

print(f"Soma dos salários atuais: R${soma_salarios_atuais:.2f}")
print(f"Soma dos salários reajustados: R${soma_salarios_reajustados:.2f}")
print(f"Diferença entre as somas: R${diferenca_somas:.2f}")


      
