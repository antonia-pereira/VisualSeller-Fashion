from typing import List, Dict, Any

from aura.vision_ai import analisar_imagem


# ============================================================
# AURA — VISÃO COMPLETA DO PRODUTO
# ============================================================

def analisar_produto(
    imagens: List[Dict[str, str]],
) -> Dict[str, Any]:
    """
    Analisa várias imagens pertencentes ao mesmo produto.

    Cada imagem deve possuir:
    - caminho
    - tipo
    """

    analises = []
    evidencias = []

    # ========================================================
    # ANALISAR CADA IMAGEM
    # ========================================================

    for imagem in imagens:

        caminho = imagem["caminho"]
        tipo = imagem["tipo"]

        print(
            f"\nAURA analisando: {tipo}"
        )

        resultado = analisar_imagem(
            caminho
        )

        # ----------------------------------------------------
        # GUARDAR ANÁLISE COMPLETA
        # ----------------------------------------------------

        analises.append(
            {
                "tipo_imagem": tipo,
                "caminho": caminho,
                "resultado": resultado,
            }
        )

        # ----------------------------------------------------
        # REUNIR EVIDÊNCIAS
        # ----------------------------------------------------

        for evidencia in resultado.get(
            "evidencias",
            [],
        ):

            evidencia_com_origem = (
                evidencia.copy()
            )

            evidencia_com_origem[
                "tipo_imagem"
            ] = tipo

            evidencia_com_origem[
                "caminho_imagem"
            ] = caminho

            evidencias.append(
                evidencia_com_origem
            )

    # ========================================================
    # RESULTADO CONSOLIDADO
    # ========================================================

    return {
        "quantidade_imagens":
            len(imagens),

        "quantidade_evidencias":
            len(evidencias),

        "analises":
            analises,

        "evidencias":
            evidencias,
    }