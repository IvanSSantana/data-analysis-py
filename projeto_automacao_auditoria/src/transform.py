CFOPS_CAMPANHA = (5102, 5106, 5110, 6102, 6106, 6110, 5160, 6160, 6910, 5910)

def filtrar_dados_brutos(
        relatorio_bruto,
        relatorio_configuracao_campanha_cliente,
        relatorio_configuracao_campanha_produto
    ):

    relatorio_apurado = relatorio_bruto[
        (
            relatorio_bruto["CODIGOCLIENTE"].isin(
                relatorio_configuracao_campanha_cliente["CODIGOCLIENTE"]
            )
        )
        &
        (
            relatorio_bruto["CODIGOPRODUTO"].isin(
                relatorio_configuracao_campanha_produto["CODIGOPRODUTO"]
            )
        )
        &
        (
            relatorio_bruto["CFOP"].isin(CFOPS_CAMPANHA)
        )
    ]

    relatorio_apurado = relatorio_apurado.rename(columns={
        "VOLUME": "VOLUMEBRUTO"
    })

    return relatorio_apurado