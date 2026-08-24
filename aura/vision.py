# ============================================================
# VISUALSELLER FASHION
# AURA — CAMADA DE VISÃO
# ============================================================
#
# Responsabilidade:
#
# Receber observações extraídas de imagens de produto
# e transformá-las em evidências estruturadas.
#
# IMPORTANTE:
# A visão NÃO decide se uma informação é verdadeira.
# Ela apenas observa e registra evidências.
#
# Quem decide o que fazer com a evidência é o
# sistema de decisão da AURA.
#
# ============================================================


def criar_evidencia_visual(
    campo,
    valor,
    confianca,
    origem="foto_produto",
    observacao=None,
):
    """
    Cria uma evidência proveniente da análise visual
    de uma imagem.
    """

    niveis_validos = {
        "baixa",
        "media",
        "alta",
    }

    if confianca not in niveis_validos:
        raise ValueError(
            "Confiança deve ser: baixa, media ou alta."
        )

    evidencia = {
        "campo": campo,
        "valor": valor,
        "fonte": "visao",
        "origem": origem,
        "confianca": confianca,
        "observacao": observacao,
    }

    return evidencia


# ============================================================
# TIPOS DE IMAGEM
# ============================================================


def classificar_tipo_imagem(tipo):
    """
    Normaliza o tipo de imagem recebido pela AURA.
    """

    tipos_validos = {
        "frente",
        "costas",
        "detalhe",
        "etiqueta",
        "tecido",
        "fechamento",
        "outro",
    }

    tipo = str(tipo).strip().lower()

    if tipo in tipos_validos:
        return tipo

    return "outro"