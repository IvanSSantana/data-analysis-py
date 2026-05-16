import pandas as pd 
import os

def carregar_dados(pasta_input):
    dados_campanha = os.path.join(pasta_input, 'Campanha Incentivo - Distribuição Vinho.xlsx')
    dados_configuracao = os.path.join(pasta_input, 'Configuracao da Campanha.xlsx')
    dados_brutos = os.path.join(pasta_input, 'Dados_Brutos.csv')

    relatorio_campanha_premiacao = pd.read_excel(dados_campanha, sheet_name="Premiação Distribuidores")
    relatorio_campanha_detalhamento = pd.read_excel(dados_campanha, sheet_name="Detalhamento Mês Apurado")
    relatorio_configuracao_campanha_cliente = pd.read_excel(dados_configuracao, sheet_name="Cliente")
    relatorio_configuracao_campanha_produto = pd.read_excel(dados_configuracao, sheet_name="Produto")
    relatorio_bruto = pd.read_csv(dados_brutos, sep=";", encoding="utf-8", dtype={"NUMERODOCUMENTO": "str"})

    return {
        "relatorio_campanha_premiacao": relatorio_campanha_premiacao,
        "relatorio_campanha_detalhamento": relatorio_campanha_detalhamento,
        "relatorio_configuracao_campanha_cliente": relatorio_configuracao_campanha_cliente,
        "relatorio_configuracao_campanha_produto": relatorio_configuracao_campanha_produto,
        "relatorio_bruto": relatorio_bruto
    }