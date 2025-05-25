import json

def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        dados = json.load(f)
    return [dia['valor'] for dia in dados if dia['valor'] > 0]

def calcular_estatisticas(faturamentos):
    menor = min(faturamentos)
    maior = max(faturamentos)
    media = sum(faturamentos) / len(faturamentos)
    return menor, maior, media

def contar_dias_acima_da_media(faturamentos, media):
    return sum(1 for valor in faturamentos if valor > media)

faturamentos = carregar_dados('dados.json')
menor, maior, media = calcular_estatisticas(faturamentos)
dias_acima_media = contar_dias_acima_da_media(faturamentos, media)

print(f"Menor faturamento: R$ {menor:.2f}")
print(f"Maior faturamento: R$ {maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
