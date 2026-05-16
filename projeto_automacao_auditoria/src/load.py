import pandas as pd
import os

def salvar_validacao_indicadores(caminho_saida, validacao_volume, validacao_premiacao):
    with pd.ExcelWriter(caminho_saida, engine="xlsxwriter") as writer:
        validacao_volume.to_excel(
            writer,
            sheet_name="Dados Apurados x Dados Brutos",
            index=False
        )

        validacao_premiacao.to_excel(
            writer,
            sheet_name="Premiação",
            index=False
        )