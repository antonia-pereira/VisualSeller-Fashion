# ============================================================
# VISUALSELLER FASHION
# AURA — CONEXÃO ENTRE PRODUTO E PESSOA
# ============================================================

from dataclasses import dataclass
from typing import List


# ============================================================
# 1. MODELO DE CONEXÃO
# ============================================================

@dataclass
class HipoteseConexao:

    busca: str

    motivo: str

    evidencias: List[str]

    confianca: str


# ============================================================
# 2. NORMALIZAÇÃO
# ============================================================

def normalizar_texto(
    texto,
):

    if texto is None:
        return ""

    return str(
        texto
    ).strip().lower()


# ============================================================
# 3. VERIFICAR TRAÇO
# ============================================================

def possui_traco(
    identidade,
    termo,
):

    termo = normalizar_texto(
        termo
    )

    tracos = (
        identidade.tracos_dominantes
        + identidade.tracos_apoio
    )


    for traco in tracos:

        if termo in normalizar_texto(
            traco
        ):

            return True


    return False


# ============================================================
# 4. LOCALIZAR EVIDÊNCIAS
# ============================================================

def buscar_evidencias(
    identidade,
    termos,
):

    encontradas = []


    for evidencia in identidade.evidencias:

        evidencia_normalizada = normalizar_texto(
            evidencia
        )


        for termo in termos:

            if normalizar_texto(
                termo
            ) in evidencia_normalizada:

                encontradas.append(
                    evidencia
                )

                break


    return encontradas


# ============================================================
# 5. REMOVER CONEXÕES REPETIDAS
# ============================================================

def remover_conexoes_repetidas(
    conexoes,
):

    resultado = []

    buscas_vistas = set()


    for conexao in conexoes:

        chave = normalizar_texto(
            conexao.busca
        )


        if chave in buscas_vistas:
            continue


        buscas_vistas.add(
            chave
        )

        resultado.append(
            conexao
        )


    return resultado


# ============================================================
# 6. ANALISAR POSSÍVEIS CONEXÕES
# ============================================================

def analisar_conexoes(
    identidade,
):
    """
    Constrói hipóteses sobre o que uma pessoa
    pode buscar ao se conectar com o produto.

    Não define idade, profissão, renda,
    gênero ou perfil demográfico.

    Não transforma hipótese em certeza.

    Toda conexão precisa nascer de uma
    identidade já sustentada por evidências.
    """

    conexoes = []


    # ========================================================
    # SENSUALIDADE
    # ========================================================

    if possui_traco(
        identidade,
        "sensualidade",
    ):

        evidencias = buscar_evidencias(
            identidade,
            [
                "transpar",
                "renda",
                "decote",
            ],
        )


        if evidencias:

            conexoes.append(
                HipoteseConexao(
                    busca=(
                        "expressar sensualidade "
                        "por meio da composição visual"
                    ),

                    motivo=(
                        "A combinação de transparência, "
                        "renda e recortes pode criar uma "
                        "leitura visual associada à "
                        "sensualidade."
                    ),

                    evidencias=evidencias,

                    confianca="alta",
                )
            )


    # ========================================================
    # DELICADEZA
    # ========================================================

    if possui_traco(
        identidade,
        "delicadeza",
    ):

        evidencias = buscar_evidencias(
            identidade,
            [
                "floral",
                "renda",
                "transpar",
            ],
        )


        if evidencias:

            conexoes.append(
                HipoteseConexao(
                    busca=(
                        "combinar sensualidade "
                        "com delicadeza visual"
                    ),

                    motivo=(
                        "Elementos florais e áreas "
                        "translúcidas podem suavizar "
                        "a leitura sensual do produto."
                    ),

                    evidencias=evidencias,

                    confianca="media",
                )
            )


    # ========================================================
    # CONTRASTE VISUAL
    # ========================================================

    if possui_traco(
        identidade,
        "contraste visual",
    ):

        evidencias = buscar_evidencias(
            identidade,
            [
                "translúc",
                "opac",
                "canelado",
            ],
        )


        if evidencias:

            conexoes.append(
                HipoteseConexao(
                    busca=(
                        "uma peça com presença visual "
                        "baseada em contraste de materiais"
                    ),

                    motivo=(
                        "A alternância entre áreas "
                        "translúcidas, opacas e texturizadas "
                        "pode tornar a construção visual "
                        "da peça mais marcante."
                    ),

                    evidencias=evidencias,

                    confianca="alta",
                )
            )


    return remover_conexoes_repetidas(
        conexoes
    )


# ============================================================
# 7. FORMATAR CONEXÕES
# ============================================================

def formatar_conexoes(
    conexoes,
):

    if not conexoes:

        return (
            "POSSÍVEIS CONEXÕES\n\n"
            "Ainda não existem evidências suficientes "
            "para formular hipóteses de conexão."
        )


    linhas = [
        "POSSÍVEIS CONEXÕES",
        "",
    ]


    for numero, conexao in enumerate(
        conexoes,
        start=1,
    ):

        linhas.append(
            f"CONEXÃO {numero}"
        )

        linhas.append(
            f"Busca: {conexao.busca}"
        )

        linhas.append(
            f"Confiança: {conexao.confianca}"
        )

        linhas.append(
            f"Por quê: {conexao.motivo}"
        )

        linhas.append(
            "Evidências:"
        )


        for evidencia in conexao.evidencias:

            linhas.append(
                f"- {evidencia}"
            )


        linhas.append(
            ""
        )


    return "\n".join(
        linhas
    )