import re
from typing import Any

from aura.question_planner import (
    planejar_perguntas,
)

from aura.gap_analyzer import (
    obter_status_ficha,
)

from aura_schemas.body import (
    FichaBody,
    GradeTamanho,
)


# ============================================================
# VISUALSELLER FASHION
# AURA — GERENCIADOR DE CONVERSA
# ============================================================


# ============================================================
# 1. TAMANHOS RECONHECIDOS
# ============================================================

TAMANHOS_VALIDOS = [
    "PP",
    "P",
    "M",
    "G",
    "GG",
    "XG",
    "XGG",
]


# ============================================================
# 2. LIMPAR TEXTO
# ============================================================

def limpar_texto(
    texto: str,
) -> str:
    """
    Remove espaços desnecessários.
    """

    return (
        texto
        .strip()
    )


# ============================================================
# 3. SEPARAR ITENS
# ============================================================

def separar_itens(
    texto: str,
) -> list[str]:
    """
    Separa uma resposta escrita com
    vírgulas, ponto e vírgula ou barras.
    """

    partes = re.split(
        r"[,;/]+",
        texto,
    )

    return [
        parte.strip()
        for parte in partes
        if parte.strip()
    ]


# ============================================================
# 4. EXTRAIR TAMANHOS
# ============================================================

def extrair_tamanhos(
    texto: str,
) -> list[str]:
    """
    Procura tamanhos conhecidos dentro
    da resposta do usuário.
    """

    texto_upper = texto.upper()

    encontrados = []

    for tamanho in TAMANHOS_VALIDOS:

        padrao = (
            r"\b"
            + re.escape(tamanho)
            + r"\b"
        )

        if re.search(
            padrao,
            texto_upper,
        ):

            encontrados.append(
                tamanho
            )

    return encontrados


# ============================================================
# 5. INTERPRETAR SIM / NÃO
# ============================================================

def interpretar_sim_nao(
    texto: str,
):
    """
    Retorna:

    True  → resposta positiva
    False → resposta negativa
    None  → não foi possível interpretar
    """

    resposta = (
        texto
        .strip()
        .lower()
    )


    negativos = [
        "não",
        "nao",
        "não possui",
        "nao possui",
        "não tem",
        "nao tem",
        "sem bojo",
    ]


    positivos = [
        "sim",
        "possui",
        "tem bojo",
        "com bojo",
    ]


    for termo in negativos:

        if termo in resposta:

            return False


    for termo in positivos:

        if termo in resposta:

            return True


    return None


# ============================================================
# 6. PROCESSAR IDENTIDADE COMERCIAL
# ============================================================

def processar_identidade_comercial(
    ficha: FichaBody,
    resposta: str,
) -> dict[str, Any]:
    """
    Interpreta uma resposta no formato aproximado:

    Linda Sedução, Body Dubai, preto, P M G GG
    """

    partes = separar_itens(
        resposta
    )

    atualizados = []


    # --------------------------------------------------------
    # MARCA
    # --------------------------------------------------------

    if len(partes) >= 1:

        ficha.marca = partes[0]

        atualizados.append(
            "marca"
        )


    # --------------------------------------------------------
    # NOME / MODELO
    # --------------------------------------------------------

    if len(partes) >= 2:

        ficha.nome_modelo = partes[1]

        atualizados.append(
            "nome_modelo"
        )


    # --------------------------------------------------------
    # CORES
    # --------------------------------------------------------

    if len(partes) >= 3:

        cor = partes[2]

        ficha.cores_disponiveis = [
            cor
        ]

        atualizados.append(
            "cores_disponiveis"
        )


    # --------------------------------------------------------
    # TAMANHOS
    # --------------------------------------------------------

    tamanhos = extrair_tamanhos(
        resposta
    )

    if tamanhos:

        ficha.tamanhos_disponiveis = (
            tamanhos
        )

        atualizados.append(
            "tamanhos_disponiveis"
        )


    return {
        "grupo":
            "IDENTIDADE_COMERCIAL",

        "campos_atualizados":
            atualizados,
    }


# ============================================================
# 7. PROCESSAR ESTOQUE
# ============================================================

def processar_estoque(
    ficha: FichaBody,
    resposta: str,
) -> dict[str, Any]:
    """
    Interpreta respostas como:

    P 8, M 10, G 11, GG 15

    e gera:

    grade:
        P → 8
        M → 10
        G → 11
        GG → 15

    quantidade_total:
        44
    """

    pares = re.findall(
        r"\b(PP|P|M|G|GG|XG|XGG)\b"
        r"\s*[:=\-]?\s*"
        r"(\d+)",
        resposta.upper(),
    )


    grade = []

    quantidade_total = 0


    for tamanho, quantidade in pares:

        quantidade_int = int(
            quantidade
        )

        grade.append(
            GradeTamanho(
                tamanho=tamanho,
                quantidade=quantidade_int,
            )
        )

        quantidade_total += (
            quantidade_int
        )


    campos_atualizados = []


    if grade:

        ficha.grade = grade

        campos_atualizados.append(
            "grade"
        )


        ficha.quantidade_total = (
            quantidade_total
        )

        campos_atualizados.append(
            "quantidade_total"
        )


        # ----------------------------------------------------
        # SE AINDA NÃO TIVERMOS TAMANHOS,
        # PODEMOS APRENDER PELA GRADE
        # ----------------------------------------------------

        if not ficha.tamanhos_disponiveis:

            ficha.tamanhos_disponiveis = [
                item.tamanho
                for item in grade
            ]


    return {
        "grupo":
            "ESTOQUE",

        "campos_atualizados":
            campos_atualizados,

        "quantidade_total":
            quantidade_total,
    }


# ============================================================
# 8. PROCESSAR ESTRUTURA
# ============================================================

def processar_estrutura(
    ficha: FichaBody,
    resposta: str,
) -> dict[str, Any]:
    """
    Atualmente trata a confirmação
    de possui_bojo.
    """

    possui_bojo = interpretar_sim_nao(
        resposta
    )

    atualizados = []


    if possui_bojo is not None:

        ficha.possui_bojo = (
            possui_bojo
        )

        atualizados.append(
            "possui_bojo"
        )


    return {
        "grupo":
            "ESTRUTURA",

        "campos_atualizados":
            atualizados,

        "possui_bojo":
            possui_bojo,
    }


# ============================================================
# 9. PROCESSAR RESPOSTA DA AURA
# ============================================================

def processar_resposta_usuario(
    ficha: FichaBody,
    grupo: str,
    resposta: str,
) -> dict[str, Any]:
    """
    Direciona a resposta para o
    interpretador correto.
    """

    resposta = limpar_texto(
        resposta
    )


    if grupo == "IDENTIDADE_COMERCIAL":

        return processar_identidade_comercial(
            ficha=ficha,
            resposta=resposta,
        )


    if grupo == "ESTOQUE":

        return processar_estoque(
            ficha=ficha,
            resposta=resposta,
        )


    if grupo == "ESTRUTURA":

        return processar_estrutura(
            ficha=ficha,
            resposta=resposta,
        )


    return {
        "grupo":
            grupo,

        "campos_atualizados":
            [],

        "erro":
            "GRUPO_DESCONHECIDO",
    }


# ============================================================
# 10. OBTER PRÓXIMA PERGUNTA
# ============================================================

def obter_proxima_pergunta(
    ficha: FichaBody,
):
    """
    Retorna somente a próxima pergunta
    realmente necessária.

    Quando não houver mais perguntas,
    retorna None.
    """

    plano = planejar_perguntas(
        ficha
    )


    if not plano:

        return None


    return plano[0]


# ============================================================
# 11. VERIFICAR SE A CONVERSA TERMINOU
# ============================================================

def conversa_concluida(
    ficha: FichaBody,
) -> bool:
    """
    A conversa acaba quando não existem
    mais perguntas essenciais.
    """

    return (
        obter_proxima_pergunta(
            ficha
        )
        is None
    )


# ============================================================
# 12. RESUMO DA CONVERSA
# ============================================================

def obter_resumo_conversa(
    ficha: FichaBody,
) -> dict[str, Any]:
    """
    Retorna a situação atual da conversa.
    """

    proxima = obter_proxima_pergunta(
        ficha
    )

    status = obter_status_ficha(
        ficha
    )


    return {
        "status_ficha":
            status,

        "conversa_concluida":
            proxima is None,

        "proxima_pergunta":
            proxima,
    }