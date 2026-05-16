from pathlib import Path
from src.extract import carregar_dados
from src.transform import filtrar_dados_brutos

PASTA_INPUT = Path("data/input")

dados = carregar_dados(PASTA_INPUT)

dados_apurados = filtrar_dados_brutos(
    dados["relatorio_bruto"],
    dados["relatorio_configuracao_campanha_cliente"],
    dados["relatorio_configuracao_campanha_produto"]
)

print(dados_apurados)