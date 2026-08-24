from typing import TypedDict, Optional, Any

from langgraph.graph import StateGraph, START, END

from aura.decision import decidir_proxima_acao


# ============================================================
# ESTADO DO GRAFO COM LOOP
# ============================================================

class AuraLoopState(TypedDict, total=False):
    """
    Estado que circula pelo grafo contínuo da AURA.

    Guarda:

    - estado atual do produto;
    - ação escolhida;
    - campo em análise;
    - valor proposto;
    - motivo da decisão;
    - resposta recebida;
    - resultado atual;
    - status do fluxo.
    """

    estado_produto: Any

    acao: Optional[str]
    campo: Optional[str]
    valor_proposto: Any
    motivo: Optional[str]

    resposta: Any

    resultado: Optional[str]
    status_fluxo: Optional[str]


# ============================================================
# NÓ 1 — ANALISAR O ESTADO DO PRODUTO
# ============================================================

def analisar_estado(
    state: AuraLoopState,
) -> AuraLoopState:
    """
    A AURA olha para o estado atual do produto
    e decide o que deve fazer a seguir.
    """

    estado_produto = state[
        "estado_produto"
    ]

    decisao = decidir_proxima_acao(
        estado_produto
    )

    return {
        **state,

        "acao":
            decisao["acao"],

        "campo":
            decisao.get("campo"),

        "valor_proposto":
            decisao.get(
                "valor_proposto"
            ),

        "motivo":
            decisao.get("motivo"),

        "status_fluxo":
            "ANALISADO",
    }


# ============================================================
# ROTEADOR PRINCIPAL
# ============================================================

def escolher_rota(
    state: AuraLoopState,
) -> str:
    """
    Escolhe o próximo nó do grafo
    de acordo com a decisão da AURA.
    """

    acao = state.get(
        "acao"
    )

    if acao == "PEDIR_CONFIRMACAO":

        return "aguardar_confirmacao"

    if acao == "BUSCAR_INFORMACAO":

        return "aguardar_informacao"

    if acao == "ENCERRAR_FICHA":

        return "encerrar"

    return "erro"


# ============================================================
# NÓ 2 — AGUARDAR CONFIRMAÇÃO
# ============================================================

def aguardar_confirmacao(
    state: AuraLoopState,
) -> AuraLoopState:
    """
    Marca que a AURA precisa receber
    uma confirmação antes de continuar.
    """

    campo = state.get(
        "campo"
    )

    valor = state.get(
        "valor_proposto"
    )

    return {
        **state,

        "resultado": (
            "CONFIRMACAO_NECESSARIA: "
            f"{campo} = {valor}"
        ),

        "status_fluxo":
            "AGUARDANDO_RESPOSTA",
    }


# ============================================================
# NÓ 3 — AGUARDAR NOVA INFORMAÇÃO
# ============================================================

def aguardar_informacao(
    state: AuraLoopState,
) -> AuraLoopState:
    """
    Marca que a AURA precisa receber
    uma nova informação sobre um campo.
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

        "status_fluxo":
            "AGUARDANDO_RESPOSTA",
    }


# ============================================================
# NÓ 4 — ENCERRAR FICHA
# ============================================================

def encerrar(
    state: AuraLoopState,
) -> AuraLoopState:
    """
    Finaliza a ficha quando não existem
    mais pendências reais.
    """

    return {
        **state,

        "resultado":
            "FICHA_CONCLUIDA",

        "status_fluxo":
            "CONCLUIDO",
    }


# ============================================================
# NÓ DE SEGURANÇA
# ============================================================

def erro(
    state: AuraLoopState,
) -> AuraLoopState:
    """
    Interrompe o fluxo quando aparece
    uma ação desconhecida.
    """

    return {
        **state,

        "resultado":
            "ERRO: ACAO_DESCONHECIDA",

        "status_fluxo":
            "ERRO",
    }


# ============================================================
# CONSTRUÇÃO DO GRAFO
# ============================================================

builder = StateGraph(
    AuraLoopState
)


# ============================================================
# REGISTRAR NÓS
# ============================================================

builder.add_node(
    "analisar_estado",
    analisar_estado,
)

builder.add_node(
    "aguardar_confirmacao",
    aguardar_confirmacao,
)

builder.add_node(
    "aguardar_informacao",
    aguardar_informacao,
)

builder.add_node(
    "encerrar",
    encerrar,
)

builder.add_node(
    "erro",
    erro,
)


# ============================================================
# INÍCIO
# ============================================================

builder.add_edge(
    START,
    "analisar_estado",
)


# ============================================================
# ROTEAMENTO
# ============================================================

builder.add_conditional_edges(
    "analisar_estado",
    escolher_rota,
    {
        "aguardar_confirmacao":
            "aguardar_confirmacao",

        "aguardar_informacao":
            "aguardar_informacao",

        "encerrar":
            "encerrar",

        "erro":
            "erro",
    },
)


# ============================================================
# PAUSAS DO FLUXO
# ============================================================

builder.add_edge(
    "aguardar_confirmacao",
    END,
)

builder.add_edge(
    "aguardar_informacao",
    END,
)


# ============================================================
# FINALIZAÇÃO
# ============================================================

builder.add_edge(
    "encerrar",
    END,
)

builder.add_edge(
    "erro",
    END,
)


# ============================================================
# COMPILAR O GRAFO
# ============================================================

aura_loop_graph = builder.compile()