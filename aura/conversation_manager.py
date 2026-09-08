import re
from typing import Any

from aura.question_planner import (
    planejar_perguntas,
    planejar_perguntas_por_objetivo,
)

from aura.gap_analyzer import (
    obter_status_ficha,
)

from aura.evidence import (
    FonteEvidencia,
    criar_evidencia,
    converter_evidencia_para_ficha,
)

from aura.ficha_manager import (
    aplicar_conhecimento_na_ficha_v2,
)

from aura_schemas.body import (
    FichaBody,
    GradeTamanho,
)

from aura_schemas.body_v2 import (
    FichaBodyV2,
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
# 6. PROCESSAR IDENTIDADE COMERCIAL — V1
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
# 7. PROCESSAR ESTOQUE — V1
# ============================================================

def processar_estoque(
    ficha: FichaBody,
    resposta: str,
) -> dict[str, Any]:
    """
    Interpreta respostas como:

    P 8, M 10, G 11, GG 15

    e gera uma grade e a quantidade total.
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
# 8. PROCESSAR ESTRUTURA — V1
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
# 9. PROCESSAR RESPOSTA DO USUÁRIO — V1
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
# 10. OBTER PRÓXIMA PERGUNTA — V1
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
# 11. VERIFICAR SE A CONVERSA TERMINOU — V1
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
# 12. RESUMO DA CONVERSA — V1
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


# ============================================================
# 13. CAMPOS BOOLEANOS — V2
# ============================================================
#
# Quando a pergunta técnica exigir uma resposta booleana,
# a conversa pode reutilizar interpretar_sim_nao().
#
# Os demais campos permanecem como texto informado
# pelo usuário.
# ============================================================

CAMPOS_BOOLEANOS_V2 = {
    "possui_bojo",
    "possui_aro",
    "possui_forro",
    "possui_fechamento_entrepernas",
}


# ============================================================
# 14. INTERPRETAR VALOR DA RESPOSTA — V2
# ============================================================

def interpretar_valor_resposta_v2(
    campo: str,
    resposta: str,
) -> dict[str, Any]:
    """
    Interpreta o valor informado pelo usuário
    antes da criação da evidência.

    O conversation_manager pode interpretar
    a linguagem da resposta, mas não decide
    o status da evidência.

    Essa responsabilidade permanece no
    evidence.py.
    """

    resposta_limpa = limpar_texto(
        resposta
    )


    # --------------------------------------------------------
    # RESPOSTA VAZIA
    # --------------------------------------------------------

    if not resposta_limpa:

        return {
            "sucesso": False,
            "campo": campo,
            "valor": None,
            "motivo": "RESPOSTA_VAZIA",
        }


    # --------------------------------------------------------
    # CAMPOS BOOLEANOS
    # --------------------------------------------------------

    if campo in CAMPOS_BOOLEANOS_V2:

        valor_booleano = interpretar_sim_nao(
            resposta_limpa
        )

        if valor_booleano is None:

            return {
                "sucesso": False,
                "campo": campo,
                "valor": None,
                "motivo": "RESPOSTA_NAO_INTERPRETADA",
            }

        return {
            "sucesso": True,
            "campo": campo,
            "valor": valor_booleano,
            "motivo": None,
        }


    # --------------------------------------------------------
    # CAMPOS TEXTUAIS
    # --------------------------------------------------------

    return {
        "sucesso": True,
        "campo": campo,
        "valor": resposta_limpa,
        "motivo": None,
    }


# ============================================================
# 15. PROCESSAR RESPOSTA DO USUÁRIO — V2
# ============================================================

def processar_resposta_usuario_v2(
    ficha: FichaBodyV2,
    campo: str,
    resposta: str,
    objetivo: str,
) -> dict[str, Any]:
    """
    Processa a resposta do usuário para um
    bloqueador específico da FichaBodyV2.

    Fluxo:

    resposta do usuário
        ↓
    interpretação
        ↓
    Evidencia
        ↓
    INFORMACAO_FORNECIDA
        ↓
    evidence.py determina o status
        ↓
    ficha_manager registra
        ↓
    objetivo é reavaliado
    """

    # --------------------------------------------------------
    # CAMPO EXISTE?
    # --------------------------------------------------------

    if campo not in ficha.__class__.model_fields:

        return {
            "sucesso": False,
            "campo": campo,
            "objetivo": objetivo,
            "motivo": "CAMPO_NAO_EXISTE_NA_FICHA",
        }


    # --------------------------------------------------------
    # INTERPRETAR RESPOSTA
    # --------------------------------------------------------

    interpretacao = interpretar_valor_resposta_v2(
        campo=campo,
        resposta=resposta,
    )


    if not interpretacao[
        "sucesso"
    ]:

        return {
            "sucesso": False,
            "campo": campo,
            "objetivo": objetivo,
            "motivo": interpretacao[
                "motivo"
            ],
        }


    valor = interpretacao[
        "valor"
    ]


    # --------------------------------------------------------
    # CRIAR EVIDÊNCIA
    # --------------------------------------------------------
    #
    # A resposta veio diretamente do usuário.
    #
    # Não marcamos CONFIRMADO manualmente.
    # O evidence.py determinará:
    #
    # INFORMADO_PELO_USUARIO
    # --------------------------------------------------------

    evidencia = criar_evidencia(
        campo=campo,
        valor=valor,
        fonte=FonteEvidencia.INFORMACAO_FORNECIDA,
        descricao=(
            "Informação fornecida pelo usuário "
            "durante a conversa com a AURA."
        ),
    )


    # --------------------------------------------------------
    # CONVERTER PARA O FORMATO DA FICHA V2
    # --------------------------------------------------------

    conhecimento_campo = (
        converter_evidencia_para_ficha(
            evidencia
        )
    )


    conhecimento = {
        campo:
            conhecimento_campo
    }


    # --------------------------------------------------------
    # ATUALIZAR FICHA
    # --------------------------------------------------------

    resultado_preenchimento = (
        aplicar_conhecimento_na_ficha_v2(
            ficha=ficha,
            conhecimento=conhecimento,
        )
    )


    if resultado_preenchimento[
        "quantidade_erros"
    ] > 0:

        return {
            "sucesso": False,
            "campo": campo,
            "objetivo": objetivo,
            "motivo": "ERRO_AO_ATUALIZAR_FICHA",
            "erros": resultado_preenchimento[
                "erros"
            ],
        }


    # --------------------------------------------------------
    # REAVALIAR OBJETIVO
    # --------------------------------------------------------

    plano_atualizado = (
        planejar_perguntas_por_objetivo(
            ficha=ficha,
            objetivo=objetivo,
        )
    )


    # --------------------------------------------------------
    # RETORNAR RESULTADO
    # --------------------------------------------------------

    return {
        "sucesso": True,

        "campo":
            campo,

        "valor":
            valor,

        "fonte":
            conhecimento_campo[
                "fonte"
            ],

        "status":
            conhecimento_campo[
                "status"
            ].value,

        "objetivo":
            objetivo,

        "pode_continuar":
            plano_atualizado[
                "pode_continuar"
            ],

        "quantidade_bloqueadores":
            len(
                plano_atualizado[
                    "bloqueadores"
                ]
            ),

        "quantidade_perguntas":
            plano_atualizado[
                "quantidade_perguntas"
            ],

        "proxima_pergunta":
            (
                plano_atualizado[
                    "perguntas"
                ][0]
                if plano_atualizado[
                    "perguntas"
                ]
                else None
            ),

        "plano":
            plano_atualizado,
    }


# ============================================================
# 16. OBTER PRÓXIMA PERGUNTA — V2
# ============================================================

def obter_proxima_pergunta_v2(
    ficha: FichaBodyV2,
    objetivo: str,
):
    """
    Retorna somente a próxima pergunta
    necessária para o objetivo atual.

    Quando não houver bloqueadores que
    exijam perguntas, retorna None.
    """

    plano = planejar_perguntas_por_objetivo(
        ficha=ficha,
        objetivo=objetivo,
    )

    perguntas = plano[
        "perguntas"
    ]

    if not perguntas:

        return None

    return perguntas[0]


# ============================================================
# 17. VERIFICAR SE A CONVERSA TERMINOU — V2
# ============================================================

def conversa_concluida_v2(
    ficha: FichaBodyV2,
    objetivo: str,
) -> bool:
    """
    Na V2, a conversa termina quando
    o objetivo atual não possui mais
    bloqueadores.
    """

    plano = planejar_perguntas_por_objetivo(
        ficha=ficha,
        objetivo=objetivo,
    )

    return plano[
        "pode_continuar"
    ]


# ============================================================
# 18. RESUMO DA CONVERSA — V2
# ============================================================

def obter_resumo_conversa_v2(
    ficha: FichaBodyV2,
    objetivo: str,
) -> dict[str, Any]:
    """
    Retorna a situação atual da conversa
    orientada por objetivo.
    """

    plano = planejar_perguntas_por_objetivo(
        ficha=ficha,
        objetivo=objetivo,
    )

    proxima_pergunta = None

    if plano[
        "perguntas"
    ]:

        proxima_pergunta = plano[
            "perguntas"
        ][0]


    return {
        "objetivo":
            objetivo,

        "pode_continuar":
            plano[
                "pode_continuar"
            ],

        "conversa_concluida":
            plano[
                "pode_continuar"
            ],

        "quantidade_bloqueadores":
            len(
                plano[
                    "bloqueadores"
                ]
            ),

        "quantidade_perguntas":
            plano[
                "quantidade_perguntas"
            ],

        "proxima_pergunta":
            proxima_pergunta,
    }


# ============================================================
# 19. MOSTRAR RESUMO DA CONVERSA — V2
# ============================================================

def mostrar_resumo_conversa_v2(
    ficha: FichaBodyV2,
    objetivo: str,
):
    """
    Exibe de forma simples o estado atual
    da conversa da AURA para um objetivo.
    """

    resumo = obter_resumo_conversa_v2(
        ficha=ficha,
        objetivo=objetivo,
    )


    print(
        "\n"
        "========================================"
    )

    print(
        "CONVERSA DA AURA — V2"
    )

    print(
        "========================================"
    )

    print(
        "OBJETIVO:",
        resumo[
            "objetivo"
        ]
    )

    print(
        "PODE CONTINUAR:",
        resumo[
            "pode_continuar"
        ]
    )

    print(
        "BLOQUEADORES:",
        resumo[
            "quantidade_bloqueadores"
        ]
    )

    print(
        "PERGUNTAS:",
        resumo[
            "quantidade_perguntas"
        ]
    )


    if resumo[
        "proxima_pergunta"
    ]:

        pergunta = resumo[
            "proxima_pergunta"
        ]

        print(
            "\n"
            "PRÓXIMA PERGUNTA:"
        )

        print(
            "CAMPO:",
            pergunta[
                "campo"
            ]
        )

        print(
            "AURA:"
        )

        print(
            pergunta[
                "pergunta"
            ]
        )

    else:

        print(
            "\n"
            "Nenhuma pergunta necessária."
        )