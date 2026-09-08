from typing import TypedDict, Optional, Any

from langgraph.graph import StateGraph, START, END

from aura.decision import decidir_proxima_acao


# ============================================================
# VISUALSELLER FASHION
# AURA — GRAPH LOOP V1
# ============================================================
#
# A V1 original permanece preservada.
# ============================================================


# ============================================================
# 1. ESTADO DO GRAFO COM LOOP — V1
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
# 2. NÓ — ANALISAR O ESTADO DO PRODUTO — V1
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

        "status_fluxo":
            "ANALISADO",
    }


# ============================================================
# 3. ROTEADOR PRINCIPAL — V1
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
# 4. NÓ — AGUARDAR CONFIRMAÇÃO — V1
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
# 5. NÓ — AGUARDAR NOVA INFORMAÇÃO — V1
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
# 6. NÓ — ENCERRAR FICHA — V1
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
# 7. NÓ DE SEGURANÇA — V1
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
# 8. CONSTRUÇÃO DO GRAFO — V1
# ============================================================

builder = StateGraph(
    AuraLoopState
)


# ============================================================
# 9. REGISTRAR NÓS — V1
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
# 10. INÍCIO — V1
# ============================================================

builder.add_edge(
    START,
    "analisar_estado",
)


# ============================================================
# 11. ROTEAMENTO — V1
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
# 12. PAUSAS DO FLUXO — V1
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
# 13. FINALIZAÇÃO — V1
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
# 14. COMPILAR O GRAFO — V1
# ============================================================

aura_loop_graph = builder.compile()


# ============================================================
# VISUALSELLER FASHION
# AURA — CONTROLADOR DE FLUXO V2
# ============================================================
#
# Responsabilidades:
#
# - iniciar uma rodada;
# - executar o LangGraph V2;
# - identificar pausa para resposta humana;
# - entregar a resposta ao conversation_manager;
# - registrar a resposta na memória operacional;
# - executar novamente o grafo;
# - retornar a nova decisão.
#
# ============================================================


from aura.graph import aura_graph_v2
from aura.state import EstadoProdutoV2
from aura.conversation_manager import (
    processar_resposta_usuario_v2,
)


# ============================================================
# 15. EXECUTAR UMA RODADA DO FLUXO V2
# ============================================================

def executar_fluxo_v2(
    estado: EstadoProdutoV2,
) -> dict:
    """
    Executa uma rodada do LangGraph V2.

    O EstadoProdutoV2 é mantido fora do grafo
    e reutilizado entre as interações.
    """

    resultado = aura_graph_v2.invoke(
        {
            "estado_produto":
                estado,
        }
    )

    return resultado


# ============================================================
# 16. INICIAR O FLUXO V2
# ============================================================

def iniciar_fluxo_v2(
    estado: EstadoProdutoV2,
) -> dict:
    """
    Inicia o fluxo da AURA para o objetivo
    armazenado no EstadoProdutoV2.
    """

    return executar_fluxo_v2(
        estado
    )


# ============================================================
# 17. OBTER CAMPO QUE AGUARDA RESPOSTA
# ============================================================

def obter_campo_aguardando_v2(
    resultado_fluxo: dict,
) -> Optional[str]:
    """
    Retorna o campo associado à pergunta
    que aguarda resposta do usuário.
    """

    if (
        resultado_fluxo.get("acao")
        != "PERGUNTAR_USUARIO"
    ):
        return None

    return resultado_fluxo.get(
        "campo"
    )


# ============================================================
# 18. VERIFICAR SE AGUARDA O USUÁRIO
# ============================================================

def aguardando_usuario_v2(
    resultado_fluxo: dict,
) -> bool:
    """
    Retorna True quando a rodada terminou
    aguardando uma resposta humana.
    """

    return (
        resultado_fluxo.get("acao")
        == "PERGUNTAR_USUARIO"
    )


# ============================================================
# 19. VERIFICAR SE O OBJETIVO FOI LIBERADO
# ============================================================

def objetivo_liberado_v2(
    resultado_fluxo: dict,
) -> bool:
    """
    Retorna True quando não existem mais
    bloqueadores para o objetivo atual.
    """

    return (
        resultado_fluxo.get("acao")
        == "CONTINUAR_OBJETIVO"
    )


# ============================================================
# 20. CRIAR RESULTADO DE ERRO DO FLUXO
# ============================================================

def criar_erro_fluxo_v2(
    estado: EstadoProdutoV2,
    motivo: str,
    resultado: str,
    campo: Optional[str] = None,
) -> dict:
    """
    Padroniza erros operacionais do controlador
    sem alterar a ficha técnica.
    """

    return {
        "estado_produto":
            estado,

        "acao":
            "ERRO_FLUXO",

        "campo":
            campo,

        "pergunta":
            None,

        "status":
            None,

        "motivo":
            motivo,

        "resultado":
            resultado,
    }


# ============================================================
# 21. PROCESSAR RESPOSTA E CONTINUAR O FLUXO
# ============================================================

def responder_fluxo_v2(
    estado: EstadoProdutoV2,
    resultado_fluxo: dict,
    resposta_usuario: Any,
) -> dict:
    """
    Recebe a resposta humana e continua
    o ciclo da AURA.

    Fluxo:

    1. identifica o campo pendente;
    2. valida se realmente existe uma pergunta;
    3. envia ficha, campo, resposta e objetivo
       ao conversation_manager;
    4. o conversation_manager interpreta
       a resposta;
    5. evidence.py classifica a evidência;
    6. ficha_manager atualiza a ficha;
    7. registra a resposta na memória operacional;
    8. executa novamente o LangGraph;
    9. retorna a próxima decisão.
    """

    campo = obter_campo_aguardando_v2(
        resultado_fluxo
    )

    if campo is None:

        return criar_erro_fluxo_v2(
            estado=estado,
            motivo=(
                "Não existe uma pergunta "
                "pendente para receber resposta."
            ),
            resultado=(
                "ERRO: NENHUMA_PERGUNTA_PENDENTE"
            ),
        )

    # --------------------------------------------------------
    # NORMALIZAR RESPOSTA
    # --------------------------------------------------------

    if resposta_usuario is None:

        resposta_texto = ""

    elif isinstance(
        resposta_usuario,
        str,
    ):

        resposta_texto = resposta_usuario

    else:

        resposta_texto = str(
            resposta_usuario
        )

    # --------------------------------------------------------
    # PROCESSAR RESPOSTA NO CONVERSATION MANAGER
    # --------------------------------------------------------
    #
    # A assinatura real da função V2 é:
    #
    # processar_resposta_usuario_v2(
    #     ficha,
    #     campo,
    #     resposta,
    #     objetivo,
    # )
    #
    # --------------------------------------------------------

    processamento = (
        processar_resposta_usuario_v2(
            ficha=estado.ficha,
            campo=campo,
            resposta=resposta_texto,
            objetivo=estado.objetivo,
        )
    )

    # --------------------------------------------------------
    # VERIFICAR SE A RESPOSTA FOI ACEITA
    # --------------------------------------------------------

    if not processamento.get(
        "sucesso",
        False,
    ):

        return criar_erro_fluxo_v2(
            estado=estado,
            campo=campo,
            motivo=processamento.get(
                "motivo",
                "RESPOSTA_NAO_PROCESSADA",
            ),
            resultado=(
                "ERRO: RESPOSTA_NAO_PROCESSADA"
            ),
        )

    # --------------------------------------------------------
    # REGISTRAR RESPOSTA NA MEMÓRIA OPERACIONAL
    # --------------------------------------------------------
    #
    # A ficha já foi atualizada pelo
    # conversation_manager.
    #
    # Aqui registramos apenas o acontecimento
    # no EstadoProdutoV2.
    #
    # --------------------------------------------------------

    estado.registrar_resposta(
        campo=campo,
        resposta=resposta_texto,
    )

    # --------------------------------------------------------
    # EXECUTAR NOVAMENTE O GRAFO
    # --------------------------------------------------------

    novo_resultado = executar_fluxo_v2(
        estado
    )

    return novo_resultado


# ============================================================
# 22. RESUMIR O FLUXO V2
# ============================================================

def resumir_fluxo_v2(
    resultado_fluxo: dict,
) -> dict:
    """
    Cria uma representação simples do estado
    atual do fluxo.

    Essa estrutura pode ser utilizada por:

    - terminal;
    - Gradio;
    - FastAPI;
    - frontend;
    - testes.
    """

    estado = resultado_fluxo.get(
        "estado_produto"
    )

    resumo_memoria = None

    if estado is not None:

        resumo_memoria = estado.resumo()

    return {
        "acao":
            resultado_fluxo.get(
                "acao"
            ),

        "campo":
            resultado_fluxo.get(
                "campo"
            ),

        "pergunta":
            resultado_fluxo.get(
                "pergunta"
            ),

        "status":
            resultado_fluxo.get(
                "status"
            ),

        "resultado":
            resultado_fluxo.get(
                "resultado"
            ),

        "motivo":
            resultado_fluxo.get(
                "motivo"
            ),

        "memoria":
            resumo_memoria,
    }


# ============================================================
# 23. MOSTRAR O FLUXO V2
# ============================================================

def mostrar_fluxo_v2(
    resultado_fluxo: dict,
):
    """
    Exibe no terminal o estado atual
    da conversa da AURA V2.
    """

    resumo = resumir_fluxo_v2(
        resultado_fluxo
    )

    print(
        "\n"
        "========================================"
    )

    print(
        "AURA — FLUXO V2"
    )

    print(
        "========================================"
    )

    print(
        "AÇÃO:",
        resumo[
            "acao"
        ],
    )

    print(
        "CAMPO:",
        resumo[
            "campo"
        ],
    )

    print(
        "STATUS:",
        resumo[
            "status"
        ],
    )

    print(
        "RESULTADO:",
        resumo[
            "resultado"
        ],
    )

    if resumo[
        "pergunta"
    ]:

        print(
            "\n"
            "AURA:"
        )

        print(
            resumo[
                "pergunta"
            ]
        )

    print(
        "\n"
        "MOTIVO:",
        resumo[
            "motivo"
        ],
    )

    print(
        "\n"
        "MEMÓRIA:"
    )

    print(
        resumo[
            "memoria"
        ]
    )