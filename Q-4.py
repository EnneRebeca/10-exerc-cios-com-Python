print('Exercício 4: Ração do Gatinho')

def CalcularRacaoRestante(PesoSaco, QuantidadeRacao):
    TotalRacaoConsumida = QuantidadeRacao / 1000 * 10
    RacaoRestante = PesoSaco - TotalRacaoConsumida
    return RacaoRestante

PesoSaco = float(input("Digite o peso do saco de ração em kg: "))
QuantidadeRacao = float(input("Informe a quantidade de ração fornecida para o gatinho 1 em gramas: " ))
QuantidadeRacao = float(input("Informe a quantidade de ração fornecida para o gatinho 2 em gramas: " ))

RacaoRestante = CalcularRacaoRestante(PesoSaco, QuantidadeRacao)

print(f"A quantidade de ração restante após cinco dias será de {RacaoRestante} kilos.")



