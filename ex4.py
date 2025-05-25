def calcular_percentuais(faturamento_estados):
    total = sum(faturamento_estados.values())
    percentuais = {}
    for estado, valor in faturamento_estados.items():
        percentual = (valor / total) * 100
        percentuais[estado] = percentual
    return percentuais

faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

percentuais = calcular_percentuais(faturamento_estados)

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")