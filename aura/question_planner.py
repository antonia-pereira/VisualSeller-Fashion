from typing import Any

from aura.gap_analyzer import (
    analisar_lacunas,
    analisar_lacunas_por_objetivo,
)

from aura_schemas.body import FichaBody
from aura_schemas.body_v2 import FichaBodyV2


# ============================================================
# VISUALSELLER FASHION
# AURA — PLANEJADOR DE PERGUNTAS
# ============================================================


# ============================================================
# 1. GRUPOS DE PERGUNTAS — V1
# ============================================================
#
# Mantidos para compatibilidade com a arquitetura antiga.
# ============================================================

GRUPOS_PERGUNTAS = {

    "IDENTIDADE_COMERCIAL": {
        "campos": [
            "marca",
            "nome_modelo",
            "cores_disponiveis",
            "tamanhos_disponiveis",
        ],

        "mensagem": (
            "Já consegui entender boa parte do produto "
            "pelas imagens.\n\n"
            "Para completar as informações comerciais, "
            "me informe a marca, o nome ou modelo, "
            "as cores disponíveis e os tamanhos disponíveis."
        ),
    },


    "ESTOQUE": {
        "campos": [
            "grade",
            "quantidade_total",
        ],

        "mensagem": (
            "Agora preciso entender o estoque.\n\n"
            "Qual é a quantidade disponível de cada tamanho?"
        ),
    },


    "ESTRUTURA": {
        "campos": [
            "possui_bojo",
        ],

        "mensagem": (
            "Só falta confirmar uma informação da estrutura: "
            "essa peça possui bojo?"
        ),
    },
}


# ============================================================
# 2. VERIFICAR CAMPOS PENDENTES DE UM GRUPO — V1
# ============================================================

def obter_campos_pendentes_grupo(
    campos_grupo: list[str],
    campos_essenciais: list[str],
) -> list[str]:
    """
    Retorna somente os campos do grupo
    que realmente continuam faltando.
    """

    pendentes = []

    for campo in campos_grupo:

        if campo in campos_essenciais:

            pendentes.append(
                campo
            )

    return pendentes


# ============================================================
# 3. PLANEJAR PERGUNTAS — V1
# ============================================================

def planejar_perguntas(
    ficha: FichaBody,
) -> list[dict[str, Any]]:
    """
    Analisa as lacunas essenciais da ficha antiga
    e transforma vários campos em poucas
    perguntas agrupadas.
    """

    analise = analisar_lacunas(
        ficha
    )

    campos_essenciais = analise[
        "essenciais"
    ]

    plano = []

    for nome_grupo, configuracao in GRUPOS_PERGUNTAS.items():

        campos_grupo = configuracao[
            "campos"
        ]

        campos_pendentes = obter_campos_pendentes_grupo(
            campos_grupo=campos_grupo,
            campos_essenciais=campos_essenciais,
        )

        if not campos_pendentes:

            continue

        plano.append(
            {
                "grupo":
                    nome_grupo,

                "campos":
                    campos_pendentes,

                "mensagem":
                    configuracao[
                        "mensagem"
                    ],

                "quantidade_campos":
                    len(
                        campos_pendentes
                    ),
            }
        )

    return plano


# ============================================================
# 4. CONTAR INTERAÇÕES — V1
# ============================================================

def contar_interacoes(
    ficha: FichaBody,
) -> int:
    """
    Retorna quantas perguntas agrupadas
    serão necessárias na arquitetura V1.
    """

    plano = planejar_perguntas(
        ficha
    )

    return len(
        plano
    )


# ============================================================
# 5. MOSTRAR PLANO — V1
# ============================================================

def mostrar_plano_perguntas(
    ficha: FichaBody,
):
    """
    Mostra como a AURA pretende conversar
    com o usuário na arquitetura antiga.
    """

    plano = planejar_perguntas(
        ficha
    )

    print(
        "\n"
        "========================================"
    )

    print(
        "PLANO DE CONVERSA DA AURA"
    )

    print(
        "========================================"
    )

    if not plano:

        print(
            "Nenhuma pergunta essencial necessária."
        )

        return

    print(
        "INTERAÇÕES NECESSÁRIAS:",
        len(
            plano
        )
    )

    for numero, pergunta in enumerate(
        plano,
        start=1,
    ):

        print(
            "\n----------------------------------------"
        )

        print(
            f"PERGUNTA {numero}"
        )

        print(
            "GRUPO:",
            pergunta[
                "grupo"
            ]
        )

        print(
            "CAMPOS:",
            pergunta[
                "campos"
            ]
        )

        print(
            "\nAURA:"
        )

        print(
            pergunta[
                "mensagem"
            ]
        )


# ============================================================
# 6. PERGUNTAS TÉCNICAS REGISTRADAS — V2
# ============================================================
#
# A AURA não deve inventar livremente uma pergunta técnica
# quando já existe uma pergunta controlada para o campo.
#
# Esta estrutura poderá crescer conforme novas fichas
# especializadas forem sendo criadas.
# ============================================================

PERGUNTAS_POR_CAMPO = {

    "acabamento_pernas": (
        "Como é o acabamento da abertura das pernas? "
        "Observe a borda da peça e descreva como ela é finalizada."
    ),

    "possui_bojo": (
        "O body possui bojo?"
    ),

    "tipo_bojo": (
        "Qual é o tipo de bojo utilizado na peça?"
    ),

    "possui_aro": (
        "O body possui aro na região do busto?"
    ),

    "possui_forro": (
        "O body possui forro?"
    ),

    "regiao_forrada": (
        "Em quais regiões da peça existe forro?"
    ),

    "decote_frente": (
        "Qual é o formato do decote da frente?"
    ),

    "decote_costas": (
        "Qual é o formato do decote das costas?"
    ),

    "construcao_mangas": (
        "De qual material é feita a manga e existem "
        "outros materiais ou detalhes aplicados nela?"
    ),
}


# ============================================================
# 7. GERAR PERGUNTA PARA UM BLOQUEADOR — V2
# ============================================================

def gerar_pergunta_para_bloqueador(
    bloqueador: dict[str, Any],
) -> dict[str, Any]:
    """
    Transforma um bloqueador técnico em uma pergunta.

    Quando existe uma pergunta registrada para o campo,
    ela é utilizada.

    Caso contrário, utiliza uma pergunta neutra de
    confirmação sem inventar conteúdo técnico.
    """

    campo = bloqueador[
        "campo"
    ]

    pergunta = PERGUNTAS_POR_CAMPO.get(
        campo
    )

    if pergunta is None:

        pergunta = (
            "Preciso confirmar a informação técnica "
            f"referente ao campo '{campo}'."
        )

    return {
        "campo":
            campo,

        "status":
            bloqueador[
                "status"
            ],

        "motivo":
            bloqueador[
                "motivo"
            ],

        "pergunta":
            pergunta,
    }


# ============================================================
# 8. PLANEJAR PERGUNTAS POR OBJETIVO — V2
# ============================================================

def planejar_perguntas_por_objetivo(
    ficha: FichaBodyV2,
    objetivo: str,
) -> dict[str, Any]:
    """
    Planeja perguntas somente para os campos
    que realmente bloqueiam o objetivo atual.

    Se não existem bloqueadores, nenhuma pergunta
    é produzida.
    """

    analise = analisar_lacunas_por_objetivo(
        ficha=ficha,
        objetivo=objetivo,
    )

    perguntas = []

    for bloqueador in analise[
        "bloqueadores"
    ]:

        perguntas.append(
            gerar_pergunta_para_bloqueador(
                bloqueador
            )
        )

    return {
        "objetivo":
            objetivo,

        "pode_continuar":
            analise[
                "pode_continuar"
            ],

        "bloqueadores":
            analise[
                "bloqueadores"
            ],

        "perguntas":
            perguntas,

        "quantidade_perguntas":
            len(
                perguntas
            ),
    }


# ============================================================
# 9. MOSTRAR PLANO DE PERGUNTAS — V2
# ============================================================

def mostrar_plano_perguntas_por_objetivo(
    ficha: FichaBodyV2,
    objetivo: str,
):
    """
    Exibe o plano de perguntas da arquitetura V2.
    """

    plano = planejar_perguntas_por_objetivo(
        ficha=ficha,
        objetivo=objetivo,
    )

    print(
        "\n"
        "========================================"
    )

    print(
        "PLANO DE PERGUNTAS DA AURA — V2"
    )

    print(
        "========================================"
    )

    print(
        "OBJETIVO:",
        plano[
            "objetivo"
        ]
    )

    print(
        "PERGUNTAS NECESSÁRIAS:",
        plano[
            "quantidade_perguntas"
        ]
    )

    if not plano[
        "perguntas"
    ]:

        print(
            "\nNenhuma pergunta necessária."
        )

        return

    for numero, item in enumerate(
        plano[
            "perguntas"
        ],
        start=1,
    ):

        print(
            "\n----------------------------------------"
        )

        print(
            f"PERGUNTA {numero}"
        )

        print(
            "CAMPO:",
            item[
                "campo"
            ]
        )

        print(
            "STATUS:",
            item[
                "status"
            ]
        )

        print(
            "\nAURA:"
        )

        print(
            item[
                "pergunta"
            ]
        )