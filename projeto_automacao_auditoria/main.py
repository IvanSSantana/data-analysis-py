from pathlib import Path
from src.validate import validar_premiacao_campanha, validar_volume
from src.extract import carregar_dados
from src.transform import filtrar_dados_brutos
from src.load import salvar_validacao_indicadores
import os

def main():
    PASTA_INPUT = Path("data/input")
    PASTA_OUTPUT = Path("data/output")

    dados = carregar_dados(PASTA_INPUT)

    print("Filtrando dados...")

    dados_apurados = filtrar_dados_brutos(
        dados["relatorio_bruto"],
        dados["relatorio_configuracao_campanha_cliente"],
        dados["relatorio_configuracao_campanha_produto"]
    )

    print("Validando volume...")

    validacao_volume = validar_volume(
        dados["relatorio_campanha_detalhamento"],
        dados_apurados
    )
    print("Validando premiação...")

    validacao_premiacao = validar_premiacao_campanha(
        dados["relatorio_campanha_premiacao"],
        dados["relatorio_campanha_detalhamento"]
    )

    print("Exportando resultados...")

    caminho_saida = os.path.join(PASTA_OUTPUT, "Validação Indicadores Automação.xlsx")
    salvar_validacao_indicadores(caminho_saida, validacao_volume, validacao_premiacao)

if __name__ == "__main__":
    main()