from typing import TypedDict, Optional, Any

from langgraph.graph import StateGraph, START, END

from aura.decision import (
    decidir_proxima_acao,
    decidir_proxima_acao_v2,
)

from aura.state import EstadoProdutoV2


# ============================================================
# VISUALSELLER FASHION
# AURA — GRAFOS DE ORQUESTRAÇÃO
# ============================================================


# ============================================================
# 1. ESTADO DO GRAFO DA AURA — V1
# ============================================================

class AuraGraphState(TypedDict, total=False):
    """
    Representa as informações que circulam
    pelo fluxo V1 do LangGraph.
    """

    ficha: Any

    acao: Optional[str]
    campo: Optional[str]
    valor_proposto: Any
    motivo: Optional[str]

    resultado: Optional[str]


# ============================================================
# 2. NÓ — ANALISAR PRODUTO — V1
# ============================================================

def analisar_produto(
    state: AuraGraphState,
) -> AuraGraphState:
    """
    Consulta a camada de decisão V1.
    """

    ficha = state[
        "ficha"
    ]

    decisao = decidir_proxima_acao(
        ficha
    )

    return {
        **state,

        "acao":
            decisao[
                "acao"
            ],

        "campo":
            decisao.get(
                "campo"
            ),

        "valor_proposto":
            decisao.get(
                "valor_proposto"
            ),

        "motivo":
            decisao.get(
                "motivo"
            ),
    }


# ============================================================
# 3. ROTEADOR — V1
# ============================================================

def escolher_caminho(
    state: AuraGraphState,
) -> str:
    """
    Escolhe o caminho do grafo V1.
    """

    acao = state[
        "acao"
    ]

    if acao == "PEDIR_CONFIRMACAO":
        return "pedir_confirmacao"

    if acao == "BUSCAR_INFORMACAO":
        return "buscar_informacao"

    if acao == "ENCERRAR_FICHA":
        return "encerrar_ficha"

    return "erro"


# ============================================================
# 4. NÓ — PEDIR CONFIRMAÇÃO — V1
# ============================================================

def pedir_confirmacao(
    state: AuraGraphState,
) -> AuraGraphState:
    """
    AURA encontrou uma informação,
    mas precisa de confirmação humana.
    """

    campo = state.get(
        "campo"
    )

    return {
        **state,

        "resultado": (
            "AGUARDANDO_CONFIRMACAO: "
            f"{campo}"
        ),
    }


# ============================================================
# 5. NÓ — BUSCAR INFORMAÇÃO — V1
# ============================================================

def buscar_informacao(
    state: AuraGraphState,
) -> AuraGraphState:
    """
    Falta uma informação necessária
    para completar a ficha V1.
    """

    campo = state.get(
        "campo"
    )

    return {
        **state,

        "resultado": (
            "INFORMACAO_NECESSARIA: "
            f"{campo}"
        ),
    }


# ============================================================
# 6. NÓ — ENCERRAR FICHA — V1
# ============================================================

def encerrar_ficha(
    state: AuraGraphState,
) -> AuraGraphState:
    """
    Finaliza o fluxo V1.
    """

    return {
        **state,

        "resultado":
            "FICHA_CONCLUIDA",
    }


# ============================================================
# 7. NÓ DE SEGURANÇA — V1
# ============================================================

def tratar_erro(
    state: AuraGraphState,
) -> AuraGraphState:
    """
    Impede que uma ação desconhecida
    continue silenciosamente.
    """

    return {
        **state,

        "resultado":
            "ERRO: ACAO_DESCONHECIDA",
    }


# ============================================================
# 8. CONSTRUÇÃO DO GRAFO — V1
# ============================================================

builder = StateGraph(
    AuraGraphState
)

builder.add_node(
    "analisar_produto",
    analisar_produto,
)

builder.add_node(
    "pedir_confirmacao",
    pedir_confirmacao,
)

builder.add_node(
    "buscar_informacao",
    buscar_informacao,
)

builder.add_node(
    "encerrar_ficha",
    encerrar_ficha,
)

builder.add_node(
    "erro",
    tratar_erro,
)

builder.add_edge(
    START,
    "analisar_produto",
)

builder.add_conditional_edges(
    "analisar_produto",
    escolher_caminho,
    {
        "pedir_confirmacao":
            "pedir_confirmacao",

        "buscar_informacao":
            "buscar_informacao",

        "encerrar_ficha":
            "encerrar_ficha",

        "erro":
            "erro",
    },
)

builder.add_edge(
    "pedir_confirmacao",
    END,
)

builder.add_edge(
    "buscar_informacao",
    END,
)

builder.add_edge(
    "encerrar_ficha",
    END,
)

builder.add_edge(
    "erro",
    END,
)

aura_graph = builder.compile()


# ============================================================
# ============================================================
# AURA GRAPH — V2
# ============================================================
# ============================================================


# ============================================================
# 9. ESTADO DO GRAFO — V2
# ============================================================

class AuraGraphStateV2(
    TypedDict,
    total=False,
):
    """
    Estado que circula pelo LangGraph V2.

    O objeto EstadoProdutoV2 carrega:

    - ficha técnica;
    - objetivo atual;
    - histórico;
    - bloqueios;
    - perguntas;
    - respostas;
    - decisões.

    O restante representa a decisão
    operacional atual do grafo.
    """

    estado_produto: EstadoProdutoV2

    acao: Optional[str]
    campo: Optional[str]
    pergunta: Optional[str]
    status: Optional[str]
    motivo: Optional[str]

    quantidade_bloqueadores: int
    quantidade_perguntas: int

    resultado: Optional[str]


# ============================================================
# 10. NÓ — ANALISAR ESTADO — V2
# ============================================================

def analisar_estado_v2(
    state: AuraGraphStateV2,
) -> AuraGraphStateV2:
    """
    Entrega o EstadoProdutoV2 para
    a camada de decisão.

    O grafo não decide regras técnicas.
    Ele apenas recebe a decisão e
    prepara o roteamento.
    """

    estado_produto = state[
        "estado_produto"
    ]

    decisao = decidir_proxima_acao_v2(
        estado_produto
    )

    return {
        **state,

        "acao":
            decisao.get(
                "acao"
            ),

        "campo":
            decisao.get(
                "campo"
            ),

        "pergunta":
            decisao.get(
                "pergunta"
            ),

        "status":
            decisao.get(
                "status"
            ),

        "motivo":
            decisao.get(
                "motivo"
            ),

        "quantidade_bloqueadores":
            decisao.get(
                "quantidade_bloqueadores",
                0,
            ),

        "quantidade_perguntas":
            decisao.get(
                "quantidade_perguntas",
                0,
            ),
    }


# ============================================================
# 11. ROTEADOR — V2
# ============================================================

def escolher_caminho_v2(
    state: AuraGraphStateV2,
) -> str:
    """
    Converte a decisão da AURA
    em uma rota do LangGraph.
    """

    acao = state.get(
        "acao"
    )

    if acao == "PERGUNTAR_USUARIO":

        return "aguardar_usuario"

    if acao == "CONTINUAR_OBJETIVO":

        return "objetivo_liberado"

    if acao == "BLOQUEADO_SEM_PERGUNTA":

        return "bloqueio_tecnico"

    return "erro_v2"


# ============================================================
# 12. NÓ — AGUARDAR USUÁRIO — V2
# ============================================================

def aguardar_usuario_v2(
    state: AuraGraphStateV2,
) -> AuraGraphStateV2:
    """
    Finaliza esta execução do grafo
    informando que a AURA precisa
    de uma resposta humana.

    A próxima execução poderá continuar
    depois que a resposta for incorporada
    à ficha.
    """

    campo = state.get(
        "campo"
    )

    return {
        **state,

        "resultado": (
            "AGUARDANDO_USUARIO: "
            f"{campo}"
        ),
    }


# ============================================================
# 13. NÓ — OBJETIVO LIBERADO — V2
# ============================================================

def objetivo_liberado_v2(
    state: AuraGraphStateV2,
) -> AuraGraphStateV2:
    """
    Indica que a ficha possui evidência
    suficiente para o objetivo atual.
    """

    return {
        **state,

        "resultado":
            "OBJETIVO_LIBERADO",
    }


# ============================================================
# 14. NÓ — BLOQUEIO TÉCNICO — V2
# ============================================================

def bloqueio_tecnico_v2(
    state: AuraGraphStateV2,
) -> AuraGraphStateV2:
    """
    Interrompe o fluxo quando existe
    um bloqueador, mas nenhuma pergunta
    utilizável foi planejada.

    Isso impede a AURA de ignorar
    silenciosamente uma lacuna técnica.
    """

    campo = state.get(
        "campo"
    )

    return {
        **state,

        "resultado": (
            "BLOQUEIO_TECNICO: "
            f"{campo}"
        ),
    }


# ============================================================
# 15. NÓ DE SEGURANÇA — V2
# ============================================================

def tratar_erro_v2(
    state: AuraGraphStateV2,
) -> AuraGraphStateV2:
    """
    Interrompe o fluxo caso apareça
    uma ação ainda não reconhecida
    pelo grafo V2.
    """

    return {
        **state,

        "resultado":
            "ERRO_V2: ACAO_DESCONHECIDA",
    }


# ============================================================
# 16. CONSTRUÇÃO DO GRAFO — V2
# ============================================================

builder_v2 = StateGraph(
    AuraGraphStateV2
)


# ============================================================
# 17. REGISTRO DOS NÓS — V2
# ============================================================

builder_v2.add_node(
    "analisar_estado_v2",
    analisar_estado_v2,
)

builder_v2.add_node(
    "aguardar_usuario",
    aguardar_usuario_v2,
)

builder_v2.add_node(
    "objetivo_liberado",
    objetivo_liberado_v2,
)

builder_v2.add_node(
    "bloqueio_tecnico",
    bloqueio_tecnico_v2,
)

builder_v2.add_node(
    "erro_v2",
    tratar_erro_v2,
)


# ============================================================
# 18. INÍCIO DO GRAFO — V2
# ============================================================

builder_v2.add_edge(
    START,
    "analisar_estado_v2",
)


# ============================================================
# 19. ROTEAMENTO — V2
# ============================================================

builder_v2.add_conditional_edges(
    "analisar_estado_v2",
    escolher_caminho_v2,
    {
        "aguardar_usuario":
            "aguardar_usuario",

        "objetivo_liberado":
            "objetivo_liberado",

        "bloqueio_tecnico":
            "bloqueio_tecnico",

        "erro_v2":
            "erro_v2",
    },
)


# ============================================================
# 20. FINALIZAÇÃO — V2
# ============================================================

builder_v2.add_edge(
    "aguardar_usuario",
    END,
)

builder_v2.add_edge(
    "objetivo_liberado",
    END,
)

builder_v2.add_edge(
    "bloqueio_tecnico",
    END,
)

builder_v2.add_edge(
    "erro_v2",
    END,
)


# ============================================================
# 21. COMPILAR AURA V2
# ============================================================

aura_graph_v2 = builder_v2.compile()