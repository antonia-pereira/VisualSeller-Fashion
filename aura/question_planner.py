from typing import Any

from aura.gap_analyzer import (
    analisar_lacunas,
)

from aura_schemas.body import (
    FichaBody,
)


# ============================================================
# VISUALSELLER FASHION
# AURA — PLANEJADOR DE PERGUNTAS
# ============================================================


# ============================================================
# 1. GRUPOS DE PERGUNTAS
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
# 2. VERIFICAR CAMPOS PENDENTES DE UM GRUPO
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
# 3. PLANEJAR PERGUNTAS
# ============================================================

def planejar_perguntas(
    ficha: FichaBody,
) -> list[dict[str, Any]]:
    """
    Analisa as lacunas essenciais da ficha
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
# 4. CONTAR INTERAÇÕES
# ============================================================

def contar_interacoes(
    ficha: FichaBody,
) -> int:
    """
    Retorna quantas perguntas agrupadas
    serão necessárias.
    """

    plano = planejar_perguntas(
        ficha
    )

    return len(
        plano
    )


# ============================================================
# 5. MOSTRAR PLANO
# ============================================================

def mostrar_plano_perguntas(
    ficha: FichaBody,
):
    """
    Mostra como a AURA pretende conversar
    com o usuário.
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