# ============================================================
# VISUALSELLER FASHION
# AURA — IDENTIDADE DO PRODUTO
# ============================================================

from dataclasses import dataclass
from typing import List


# ============================================================
# 1. MODELO DA IDENTIDADE
# ============================================================

@dataclass
class IdentidadeProduto:

    leitura_principal: str

    tracos_dominantes: List[str]

    tracos_apoio: List[str]

    evidencias: List[str]


# ============================================================
# 2. PESO DAS CONFIANÇAS
# ============================================================

PESO_CONFIANCA = {
    "alta": 3,
    "media": 2,
    "média": 2,
    "baixa": 1,
}


# ============================================================
# 3. NORMALIZAR CONFIANÇA
# ============================================================

def obter_peso_confianca(
    confianca,
):

    if not confianca:

        return 0


    valor = str(
        confianca
    ).strip().lower()


    return PESO_CONFIANCA.get(
        valor,
        0,
    )


# ============================================================
# 4. ORDENAR HIPÓTESES
# ============================================================

def ordenar_hipoteses(
    hipoteses,
):

    return sorted(
        hipoteses,
        key=lambda hipotese: (
            obter_peso_confianca(
                hipotese.confianca
            ),
            len(
                hipotese.evidencias
            ),
        ),
        reverse=True,
    )


# ============================================================
# 5. REMOVER REPETIÇÕES
# ============================================================

def remover_repeticoes(
    itens,
):

    resultado = []

    vistos = set()


    for item in itens:

        chave = str(
            item
        ).strip().lower()


        if not chave:
            continue


        if chave in vistos:
            continue


        vistos.add(
            chave
        )

        resultado.append(
            item
        )


    return resultado


# ============================================================
# 6. CONSTRUIR LEITURA PRINCIPAL
# ============================================================

def construir_leitura_principal(
    dominantes,
    apoio,
):

    if not dominantes:

        return (
            "Ainda não há evidências suficientes "
            "para definir uma identidade consistente."
        )


    if len(dominantes) == 1:

        principal = dominantes[0]


        if apoio:

            return (
                f"{principal.capitalize()} "
                f"com presença de "
                f"{apoio[0]}."
            )


        return (
            f"{principal.capitalize()} "
            f"como característica predominante."
        )


    primeiro = dominantes[0]

    segundo = dominantes[1]


    return (
        f"{primeiro.capitalize()} "
        f"com {segundo}."
    )


# ============================================================
# 7. CONSTRUIR IDENTIDADE
# ============================================================

def construir_identidade(
    hipoteses,
):
    """
    Organiza as hipóteses de significado
    em uma identidade coerente do produto.

    A identidade não cria fatos novos.
    Ela apenas organiza interpretações
    já sustentadas por evidências.
    """

    if not hipoteses:

        return IdentidadeProduto(
            leitura_principal=(
                "Ainda não há evidências suficientes "
                "para definir uma identidade consistente."
            ),
            tracos_dominantes=[],
            tracos_apoio=[],
            evidencias=[],
        )


    ordenadas = ordenar_hipoteses(
        hipoteses
    )


    # --------------------------------------------------------
    # HIPÓTESES DE ALTA CONFIANÇA
    # --------------------------------------------------------

    dominantes = [
        hipotese.significado
        for hipotese in ordenadas
        if obter_peso_confianca(
            hipotese.confianca
        ) >= 3
    ]


    # --------------------------------------------------------
    # HIPÓTESES DE APOIO
    # --------------------------------------------------------

    apoio = [
        hipotese.significado
        for hipotese in ordenadas
        if obter_peso_confianca(
            hipotese.confianca
        ) == 2
    ]


    # --------------------------------------------------------
    # CASO NÃO HAJA ALTA CONFIANÇA
    # --------------------------------------------------------

    if not dominantes:

        dominantes = [
            ordenadas[0].significado
        ]

        apoio = [
            hipotese.significado
            for hipotese in ordenadas[1:]
        ]


    dominantes = remover_repeticoes(
        dominantes
    )

    apoio = remover_repeticoes(
        apoio
    )


    # --------------------------------------------------------
    # EVIDÊNCIAS
    # --------------------------------------------------------

    evidencias = []


    for hipotese in ordenadas:

        for evidencia in hipotese.evidencias:

            evidencias.append(
                evidencia
            )


    evidencias = remover_repeticoes(
        evidencias
    )


    # --------------------------------------------------------
    # LEITURA PRINCIPAL
    # --------------------------------------------------------

    leitura_principal = (
        construir_leitura_principal(
            dominantes,
            apoio,
        )
    )


    return IdentidadeProduto(
        leitura_principal=leitura_principal,
        tracos_dominantes=dominantes,
        tracos_apoio=apoio,
        evidencias=evidencias,
    )


# ============================================================
# 8. FORMATAR IDENTIDADE
# ============================================================

def formatar_identidade(
    identidade,
):

    linhas = [
        "IDENTIDADE DO PRODUTO",
        "",
        "LEITURA PRINCIPAL",
        identidade.leitura_principal,
        "",
    ]


    if identidade.tracos_dominantes:

        linhas.append(
            "TRAÇOS DOMINANTES"
        )


        for traco in (
            identidade.tracos_dominantes
        ):

            linhas.append(
                f"- {traco}"
            )


        linhas.append(
            ""
        )


    if identidade.tracos_apoio:

        linhas.append(
            "TRAÇOS DE APOIO"
        )


        for traco in (
            identidade.tracos_apoio
        ):

            linhas.append(
                f"- {traco}"
            )


        linhas.append(
            ""
        )


    if identidade.evidencias:

        linhas.append(
            "BASE DA LEITURA"
        )


        for evidencia in (
            identidade.evidencias
        ):

            linhas.append(
                f"- {evidencia}"
            )


    return "\n".join(
        linhas
    )