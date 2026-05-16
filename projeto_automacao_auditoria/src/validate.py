import pandas as pd 
import numpy as np

from src.rules import percentual_crescimento, validar_multiplas_regras

def validar_volume(relatorio_campanha_detalhamento, relatorio_apurado):
    validacao_campanha_dados_apurados = pd.merge(
        relatorio_campanha_detalhamento,
        relatorio_apurado[["CODIGOCLIENTE", "CODIGODOCUMENTO", "CODIGOPRODUTO", "VOLUMEBRUTO"]],
        how="left",
        on=["CODIGODOCUMENTO", "CODIGOCLIENTE", "CODIGOPRODUTO"]
    )

    validacao_campanha_dados_apurados["VALIDAÇÃO"] = np.where(
        validacao_campanha_dados_apurados["VOLUME"] != validacao_campanha_dados_apurados["VOLUMEBRUTO"],
        "DIVERGENTE",
        "CORRETO"
    )

    return validacao_campanha_dados_apurados


def validar_premiacao_campanha(relatorio_premiacao_campanha, relatorio_campanha_detalhamento):
    campanha_detalhamento = (
        relatorio_campanha_detalhamento.groupby(["CODIGOCLIENTE", "CODIGOPRODUTO"])
        ["VOLUME"]
        .sum()
        .reset_index()
    )

    validacao_premiacao = pd.merge(
        relatorio_premiacao_campanha,
        campanha_detalhamento,
        how="left",
        on=["CODIGOCLIENTE", "CODIGOPRODUTO"]
    )   
    
    validacao_premiacao["CRESCIMENTOCALCULADO"] = (
        (validacao_premiacao["VOLUME"] / validacao_premiacao["METAVOLUMEVENDA"]) - 1
    ).round(4)

    validacao_premiacao["PERCENTUALCALCULADO"] = (
        validacao_premiacao["CRESCIMENTOCALCULADO"].apply(percentual_crescimento)
    )

    validacao_premiacao["VALORPREMIACAOCALCULADO"] = (
        validacao_premiacao["VALORVENDAPREMIACAO"] * (validacao_premiacao["PERCENTUALCALCULADO"])
    ).round(4)
    
    validacao_premiacao["VALIDAÇÃO"] = validar_multiplas_regras(
        validacao_premiacao,
        regras=[
        (
            ~np.isclose( # Esse ~ funciona igual a um ! em outras linguagens: inverte a lógica
            validacao_premiacao["PERCENTUALCALCULADO"],
            validacao_premiacao["PERCENTUALPREMIACAO"]
        ),
            "PERCENTUAL DIVERGENTE"
        ),
        (
            ~np.isclose(
            validacao_premiacao["VALORPREMIACAOCALCULADO"],
            validacao_premiacao["VALORPREMIACAO"]
            ),
            "PREMIAÇÃO DIVERGENTE"
        )]   
    )

    return validacao_premiacao