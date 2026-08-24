# ============================================================
# VISUALSELLER FASHION
# AURA — DESEJOS ASSOCIADOS AO PRODUTO
# ============================================================

from dataclasses import dataclass
from typing import List


# ============================================================
# 1. MODELO DE DESEJO
# ============================================================

@dataclass
class DesejoProduto:
    desejo: str
    confianca: str
    motivo: str
    evidencias: List[str]


# ============================================================
# 2. CRIAR DESEJO
# ============================================================

def criar_desejo(
    desejo,
    confianca,
    motivo,
    evidencias,
):
    """
    Cria uma hipótese de desejo sustentada
    pelas conexões já identificadas pela Aura.
    """

    return DesejoProduto(
        desejo=desejo,
        confianca=confianca,
        motivo=motivo,
        evidencias=evidencias,
    )


# ============================================================
# 3. ANALISAR DESEJOS
# ============================================================

def analisar_desejos(
    conexoes,
):
    """
    Transforma possíveis conexões com o produto
    em hipóteses de desejos.

    IMPORTANTE:
    A Aura não afirma sentimentos como fatos.
    Ela formula possibilidades sustentadas
    pelas conexões anteriores.
    """

    desejos = []


    for conexao in conexoes:

        busca = conexao.busca.lower()


        # ----------------------------------------------------
        # SENSUALIDADE
        # ----------------------------------------------------

        if (
            "sensualidade" in busca
            and "delicadeza" not in busca
        ):

            desejos.append(
                criar_desejo(
                    desejo=(
                        "expressar sensualidade "
                        "de forma visualmente marcante"
                    ),

                    confianca=conexao.confianca,

                    motivo=(
                        "A conexão identificada sugere "
                        "uma busca por expressão sensual "
                        "por meio dos elementos visuais "
                        "do produto."
                    ),

                    evidencias=conexao.evidencias.copy(),
                )
            )


        # ----------------------------------------------------
        # SENSUALIDADE + DELICADEZA
        # ----------------------------------------------------

        elif (
            "sensualidade" in busca
            and "delicadeza" in busca
        ):

            desejos.append(
                criar_desejo(
                    desejo=(
                        "equilibrar sensualidade "
                        "e delicadeza na própria expressão"
                    ),

                    confianca=conexao.confianca,

                    motivo=(
                        "A combinação entre elementos "
                        "sensuais e delicados sugere uma "
                        "possível busca por equilíbrio "
                        "entre presença e suavidade."
                    ),

                    evidencias=conexao.evidencias.copy(),
                )
            )


        # ----------------------------------------------------
        # PRESENÇA VISUAL
        # ----------------------------------------------------

        elif (
            "presença visual" in busca
            or "contraste" in busca
        ):

            desejos.append(
                criar_desejo(
                    desejo=(
                        "usar uma peça com presença visual "
                        "e construção marcante"
                    ),

                    confianca=conexao.confianca,

                    motivo=(
                        "A conexão baseada em contraste "
                        "sugere interesse por uma peça cuja "
                        "construção visual tenha destaque."
                    ),

                    evidencias=conexao.evidencias.copy(),
                )
            )


    return desejos


# ============================================================
# 4. FORMATAR DESEJOS
# ============================================================

def formatar_desejos(
    desejos,
):
    """
    Formata os desejos para leitura humana.
    """

    if not desejos:

        return (
            "A Aura ainda não possui evidências "
            "suficientes para formular desejos."
        )


    linhas = [
        "POSSÍVEIS DESEJOS",
        "",
    ]


    for numero, desejo in enumerate(
        desejos,
        start=1,
    ):

        linhas.append(
            f"DESEJO {numero}"
        )

        linhas.append(
            f"Possível busca: {desejo.desejo}"
        )

        linhas.append(
            f"Confiança: {desejo.confianca}"
        )

        linhas.append(
            f"Por quê: {desejo.motivo}"
        )

        linhas.append(
            "Evidências:"
        )


        for evidencia in desejo.evidencias:

            linhas.append(
                f"- {evidencia}"
            )


        linhas.append(
            ""
        )


    return "\n".join(
        linhas
    )