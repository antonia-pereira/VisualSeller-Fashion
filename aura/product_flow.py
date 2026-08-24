from typing import Any

from aura.vision_product import (
    analisar_produto,
)

from aura.consolidator import (
    agrupar_evidencias_por_campo,
    gerar_conhecimento_consolidado,
)

from aura.ficha_manager import (
    aplicar_conhecimento_na_ficha,
)

from aura.gap_analyzer import (
    analisar_lacunas,
    obter_status_ficha,
)

from aura.conversation_manager import (
    obter_proxima_pergunta,
    processar_resposta_usuario,
    conversa_concluida,
)

from aura_schemas.body import (
    FichaBody,
)


# ============================================================
# VISUALSELLER FASHION
# AURA — FLUXO PRINCIPAL DO PRODUTO
# ============================================================


# ============================================================
# 1. CRIAR SESSÃO DO PRODUTO
# ============================================================

def iniciar_produto() -> dict[str, Any]:
    """
    Cria uma nova sessão de análise.

    A ficha começa vazia e será preenchida
    primeiro pela visão e depois pelas
    respostas do usuário.
    """

    ficha = FichaBody()

    return {
        "ficha":
            ficha,

        "imagens":
            [],

        "resultado_visao":
            None,

        "grupos_evidencias":
            {},

        "conhecimento":
            {},

        "resultado_preenchimento":
            None,

        "status":
            "AGUARDANDO_IMAGENS",

        "historico":
            [],
    }


# ============================================================
# 2. REGISTRAR EVENTO NO HISTÓRICO
# ============================================================

def registrar_evento(
    sessao: dict[str, Any],
    tipo: str,
    dados: Any = None,
):
    """
    Guarda acontecimentos importantes
    durante o fluxo do produto.
    """

    sessao[
        "historico"
    ].append(
        {
            "tipo":
                tipo,

            "dados":
                dados,
        }
    )


# ============================================================
# 3. RECEBER IMAGENS
# ============================================================

def receber_imagens(
    sessao: dict[str, Any],
    imagens: list[dict[str, str]],
) -> dict[str, Any]:
    """
    Registra as imagens enviadas pelo usuário.
    """

    sessao[
        "imagens"
    ] = imagens

    sessao[
        "status"
    ] = "IMAGENS_RECEBIDAS"

    registrar_evento(
        sessao=sessao,
        tipo="IMAGENS_RECEBIDAS",
        dados={
            "quantidade":
                len(
                    imagens
                )
        },
    )

    return sessao


# ============================================================
# 4. ANALISAR IMAGENS
# ============================================================

def executar_visao(
    sessao: dict[str, Any],
) -> dict[str, Any]:
    """
    Envia todas as imagens para
    a visão da Aura.
    """

    imagens = sessao[
        "imagens"
    ]

    if not imagens:

        raise ValueError(
            "Nenhuma imagem foi enviada para a Aura."
        )


    resultado_visao = analisar_produto(
        imagens
    )


    sessao[
        "resultado_visao"
    ] = resultado_visao


    sessao[
        "status"
    ] = "VISAO_CONCLUIDA"


    registrar_evento(
        sessao=sessao,
        tipo="VISAO_CONCLUIDA",
        dados={
            "quantidade_imagens":
                resultado_visao.get(
                    "quantidade_imagens"
                ),

            "quantidade_evidencias":
                resultado_visao.get(
                    "quantidade_evidencias"
                ),
        },
    )


    return sessao


# ============================================================
# 5. CONSOLIDAR EVIDÊNCIAS
# ============================================================

def executar_consolidacao(
    sessao: dict[str, Any],
) -> dict[str, Any]:
    """
    Agrupa e consolida as evidências
    produzidas pela visão.
    """

    resultado_visao = sessao.get(
        "resultado_visao"
    )


    if not resultado_visao:

        raise ValueError(
            "A visão precisa ser executada "
            "antes da consolidação."
        )


    evidencias = resultado_visao.get(
        "evidencias",
        [],
    )


    grupos = agrupar_evidencias_por_campo(
        evidencias
    )


    conhecimento = gerar_conhecimento_consolidado(
        grupos
    )


    sessao[
        "grupos_evidencias"
    ] = grupos


    sessao[
        "conhecimento"
    ] = conhecimento


    sessao[
        "status"
    ] = "CONHECIMENTO_CONSOLIDADO"


    registrar_evento(
        sessao=sessao,
        tipo="CONHECIMENTO_CONSOLIDADO",
        dados={
            "quantidade_campos":
                len(
                    conhecimento
                )
        },
    )


    return sessao


# ============================================================
# 6. PREENCHER FICHA COM A VISÃO
# ============================================================

def preencher_ficha_com_visao(
    sessao: dict[str, Any],
) -> dict[str, Any]:
    """
    Aplica o conhecimento consolidado
    diretamente à ficha técnica.
    """

    ficha = sessao[
        "ficha"
    ]


    conhecimento = sessao.get(
        "conhecimento",
        {},
    )


    if not conhecimento:

        raise ValueError(
            "Não existe conhecimento consolidado "
            "para aplicar à ficha."
        )


    resultado = aplicar_conhecimento_na_ficha(
        ficha=ficha,
        conhecimento=conhecimento,
    )


    sessao[
        "resultado_preenchimento"
    ] = resultado


    sessao[
        "status"
    ] = "FICHA_PREENCHIDA_PELA_VISAO"


    registrar_evento(
        sessao=sessao,
        tipo="FICHA_PREENCHIDA_PELA_VISAO",
        dados={
            "campos_preenchidos":
                resultado.get(
                    "quantidade_preenchidos"
                ),

            "campos_pendentes":
                resultado.get(
                    "quantidade_pendentes"
                ),

            "erros":
                resultado.get(
                    "quantidade_erros"
                ),
        },
    )


    return sessao


# ============================================================
# 7. PREPARAR PRODUTO
# ============================================================

def preparar_produto(
    imagens: list[dict[str, str]],
) -> dict[str, Any]:
    """
    Executa toda a primeira etapa:

    1. cria sessão;
    2. recebe imagens;
    3. executa visão;
    4. consolida;
    5. preenche ficha.
    """

    sessao = iniciar_produto()


    receber_imagens(
        sessao=sessao,
        imagens=imagens,
    )


    executar_visao(
        sessao
    )


    executar_consolidacao(
        sessao
    )


    preencher_ficha_com_visao(
        sessao
    )


    atualizar_status_fluxo(
        sessao
    )


    return sessao


# ============================================================
# 8. ANALISAR SITUAÇÃO ATUAL DA FICHA
# ============================================================

def analisar_ficha_atual(
    sessao: dict[str, Any],
) -> dict[str, Any]:
    """
    Retorna as lacunas atuais da ficha.
    """

    ficha = sessao[
        "ficha"
    ]

    return analisar_lacunas(
        ficha
    )


# ============================================================
# 9. OBTER PRÓXIMA INTERAÇÃO
# ============================================================

def obter_proxima_interacao(
    sessao: dict[str, Any],
):
    """
    Retorna a próxima pergunta necessária.

    Se não houver mais nenhuma,
    retorna None.
    """

    ficha = sessao[
        "ficha"
    ]

    return obter_proxima_pergunta(
        ficha
    )


# ============================================================
# 10. RECEBER RESPOSTA DO USUÁRIO
# ============================================================

def receber_resposta(
    sessao: dict[str, Any],
    resposta: str,
) -> dict[str, Any]:
    """
    Recebe a resposta do usuário para
    a pergunta atual da Aura.
    """

    ficha = sessao[
        "ficha"
    ]


    pergunta = obter_proxima_pergunta(
        ficha
    )


    if pergunta is None:

        return {
            "aceita":
                False,

            "motivo":
                "CONVERSA_JA_CONCLUIDA",

            "campos_atualizados":
                [],
        }


    grupo = pergunta[
        "grupo"
    ]


    resultado = processar_resposta_usuario(
        ficha=ficha,
        grupo=grupo,
        resposta=resposta,
    )


    registrar_evento(
        sessao=sessao,
        tipo="RESPOSTA_USUARIO",
        dados={
            "grupo":
                grupo,

            "resposta":
                resposta,

            "campos_atualizados":
                resultado.get(
                    "campos_atualizados",
                    [],
                ),
        },
    )


    atualizar_status_fluxo(
        sessao
    )


    return {
        "aceita":
            True,

        "grupo":
            grupo,

        "campos_atualizados":
            resultado.get(
                "campos_atualizados",
                [],
            ),

        "resultado":
            resultado,
    }


# ============================================================
# 11. ATUALIZAR STATUS DO FLUXO
# ============================================================

def atualizar_status_fluxo(
    sessao: dict[str, Any],
):
    """
    Atualiza o estado principal da sessão.
    """

    ficha = sessao[
        "ficha"
    ]


    if conversa_concluida(
        ficha
    ):

        sessao[
            "status"
        ] = "CONCLUIDO"


        registrar_evento(
            sessao=sessao,
            tipo="FLUXO_CONCLUIDO",
            dados=None,
        )


        return


    sessao[
        "status"
    ] = "AGUARDANDO_USUARIO"


# ============================================================
# 12. VERIFICAR SE O PRODUTO FOI CONCLUÍDO
# ============================================================

def produto_concluido(
    sessao: dict[str, Any],
) -> bool:
    """
    Retorna True quando a Aura não precisa
    mais fazer perguntas essenciais.
    """

    ficha = sessao[
        "ficha"
    ]

    return conversa_concluida(
        ficha
    )


# ============================================================
# 13. OBTER STATUS COMPLETO
# ============================================================

def obter_status_produto(
    sessao: dict[str, Any],
) -> dict[str, Any]:
    """
    Resume a situação atual do produto.
    """

    ficha = sessao[
        "ficha"
    ]


    lacunas = analisar_lacunas(
        ficha
    )


    proxima_pergunta = obter_proxima_pergunta(
        ficha
    )


    return {
        "status_fluxo":
            sessao.get(
                "status"
            ),

        "status_ficha":
            obter_status_ficha(
                ficha
            ),

        "concluido":
            produto_concluido(
                sessao
            ),

        "campos_essenciais_faltando":
            lacunas.get(
                "essenciais",
                [],
            ),

        "quantidade_essenciais_faltando":
            lacunas.get(
                "quantidade_essenciais",
                0,
            ),

        "proxima_pergunta":
            proxima_pergunta,
    }


# ============================================================
# 14. OBTER FICHA FINAL
# ============================================================

def obter_ficha_final(
    sessao: dict[str, Any],
) -> FichaBody:
    """
    Retorna a ficha atual do produto.
    """

    return sessao[
        "ficha"
    ]


# ============================================================
# 15. MOSTRAR RESUMO DO PRODUTO
# ============================================================

def mostrar_resumo_produto(
    sessao: dict[str, Any],
):
    """
    Mostra um resumo simples do fluxo.
    """

    status = obter_status_produto(
        sessao
    )


    print(
        "\n"
        "========================================"
    )

    print(
        "STATUS DO PRODUTO"
    )

    print(
        "========================================"
    )


    print(
        "STATUS DO FLUXO:",
        status[
            "status_fluxo"
        ]
    )


    print(
        "STATUS DA FICHA:",
        status[
            "status_ficha"
        ]
    )


    print(
        "CONCLUÍDO:",
        status[
            "concluido"
        ]
    )


    print(
        "ESSENCIAIS FALTANDO:",
        status[
            "quantidade_essenciais_faltando"
        ]
    )


    if status[
        "campos_essenciais_faltando"
    ]:

        print(
            "CAMPOS:"
        )

        for campo in status[
            "campos_essenciais_faltando"
        ]:

            print(
                "-",
                campo
            )