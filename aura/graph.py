from typing import TypedDict, Optional, Any

from langgraph.graph import StateGraph, START, END

from aura.decision import decidir_proxima_acao


# ============================================================
# ESTADO DO GRAFO DA AURA
# ============================================================

class AuraGraphState(TypedDict, total=False):
    """
    Representa as informações que circulam
    pelo fluxo do LangGraph.

    O grafo recebe o estado atual da ficha,
    consulta a camada de decisão da AURA
    e escolhe qual será o próximo caminho.
    """

    ficha: Any

    acao: Optional[str]
    campo: Optional[str]
    valor_proposto: Any
    motivo: Optional[str]

    resultado: Optional[str]


# ============================================================
# NÓ 1 — ANALISAR O PRODUTO
# ============================================================

def analisar_produto(
    state: AuraGraphState,
) -> AuraGraphState:
    """
    Consulta a camada de decisão da AURA
    para descobrir qual deve ser
    a próxima ação.
    """

    ficha = state["ficha"]

    decisao = decidir_proxima_acao(
        ficha
    )

    return {
        **state,
        "acao": decisao["acao"],
        "campo": decisao.get("campo"),
        "valor_proposto": decisao.get(
            "valor_proposto"
        ),
        "motivo": decisao.get("motivo"),
    }


# ============================================================
# ROTEADOR
# ============================================================

def escolher_caminho(
    state: AuraGraphState,
) -> str:
    """
    Escolhe qual caminho do grafo
    deve ser executado.
    """

    acao = state["acao"]

    if acao == "PEDIR_CONFIRMACAO":
        return "pedir_confirmacao"

    if acao == "BUSCAR_INFORMACAO":
        return "buscar_informacao"

    if acao == "ENCERRAR_FICHA":
        return "encerrar_ficha"

    return "erro"


# ============================================================
# NÓ 2 — PEDIR CONFIRMAÇÃO
# ============================================================

def pedir_confirmacao(
    state: AuraGraphState,
) -> AuraGraphState:
    """
    Representa uma situação em que
    a AURA encontrou uma informação,
    mas precisa da confirmação humana.
    """

    campo = state.get("campo")

    return {
        **state,
        "resultado": (
            "AGUARDANDO_CONFIRMACAO: "
            f"{campo}"
        ),
    }


# ============================================================
# NÓ 3 — BUSCAR INFORMAÇÃO
# ============================================================

def buscar_informacao(
    state: AuraGraphState,
) -> AuraGraphState:
    """
    Representa uma situação em que
    falta uma informação necessária
    para completar a ficha.
    """

    campo = state.get("campo")

    return {
        **state,
        "resultado": (
            "INFORMACAO_NECESSARIA: "
            f"{campo}"
        ),
    }


# ============================================================
# NÓ 4 — ENCERRAR FICHA
# ============================================================

def encerrar_ficha(
    state: AuraGraphState,
) -> AuraGraphState:
    """
    Finaliza o fluxo quando todos
    os campos necessários já foram
    tratados.
    """

    return {
        **state,
        "resultado": "FICHA_CONCLUIDA",
    }


# ============================================================
# NÓ DE SEGURANÇA — ERRO
# ============================================================

def tratar_erro(
    state: AuraGraphState,
) -> AuraGraphState:
    """
    Impede que uma ação desconhecida
    continue silenciosamente no fluxo.
    """

    return {
        **state,
        "resultado": (
            "ERRO: ACAO_DESCONHECIDA"
        ),
    }


# ============================================================
# CONSTRUÇÃO DO GRAFO
# ============================================================

builder = StateGraph(
    AuraGraphState
)


# ============================================================
# REGISTRO DOS NÓS
# ============================================================

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


# ============================================================
# INÍCIO DO GRAFO
# ============================================================

builder.add_edge(
    START,
    "analisar_produto",
)


# ============================================================
# DECISÃO DE ROTA
# ============================================================

builder.add_conditional_edges(
    "analisar_produto",
    escolher_caminho,
    {
        "pedir_confirmacao": "pedir_confirmacao",
        "buscar_informacao": "buscar_informacao",
        "encerrar_ficha": "encerrar_ficha",
        "erro": "erro",
    },
)


# ============================================================
# FINALIZAÇÃO DOS CAMINHOS
# ============================================================

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


# ============================================================
# COMPILAR A AURA
# ============================================================

aura_graph = builder.compile()