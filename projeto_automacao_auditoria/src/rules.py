import numpy as np


def validar_multiplas_regras(dataframe, regras, separador=" | "):
    """
    Aplica múltiplas regras vetorizadas e retorna uma única coluna:
    - "Correto" se nenhuma regra falhar
    - Texto com os motivos se houver divergências
    """
    mensagens = np.full(len(dataframe), "", dtype=object)

    for mascara, texto in regras:
        mensagens = np.where(
            mascara,
            np.where(
                mensagens == "",
                texto,
                mensagens + separador + texto,
            ),
            mensagens,
        )

    return np.where(mensagens == "", "Correto", mensagens)

def percentual_crescimento(crescimento):
    if crescimento >= 0.2:
        return 0.1

    elif crescimento >= 0.15:
        return 0.08
    
    elif crescimento >= 0.1:
        return 0.06
    
    elif crescimento >= 0.05:
        return 0.03
    
    else:
        return 0
 