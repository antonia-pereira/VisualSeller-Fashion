from aura_schemas.body import (
    FichaBody,
    GradeTamanho,
)

from aura.state import EstadoProduto

from aura.evidence import FonteEvidencia

from aura.processor import (
    processar_informacao,
)

from aura.graph_loop import (
    aura_loop_graph,
)

from aura.communication import (
    gerar_mensagem_aura,
)


# ============================================================
# TESTE DE CONVERSA COMPLETA DA AURA
# PRODUTO 001 — BODY DUBAI
# ============================================================


# ============================================================
# 1. CRIAR FICHA INICIAL
# ============================================================

ficha = FichaBody(
    marca="Linda Sedução",

    nome_modelo="Body Dubai",

    referencia="277",

    codigo_barras="7002770010015",

    cores_disponiveis=[
        "Preto",
    ],

    tamanhos_disponiveis=[
        "P",
        "M",
        "G",
        "GG",
    ],

    grade=[
        GradeTamanho(
            tamanho="P",
            quantidade=8,
        ),

        GradeTamanho(
            tamanho="M",
            quantidade=10,
        ),

        GradeTamanho(
            tamanho="G",
            quantidade=11,
        ),

        GradeTamanho(
            tamanho="GG",
            quantidade=15,
        ),
    ],

    quantidade_total=44,

    composicao_principal=(
        "85% poliamida + 15% elastano"
    ),

    composicao_forro=(
        "100% algodão"
    ),

    materiais_visuais=[
        "renda floral",
        "material transparente nas mangas",
        "malha canelada",
        "malha lisa",
    ],

    manga="longa",

    decote_frente="V",

    decote_costas="V",

    fechamento=(
        "colchetes na entreperna "
        "com 2 posições de ajuste"
    ),

    transparencia=(
        "mangas e regiões em renda"
    ),

    acabamento_mangas=(
        "malha canelada"
    ),

    tamanho_medido="P",
)


# ============================================================
# 2. CRIAR ESTADO DO PRODUTO
# ============================================================

estado = EstadoProduto(
    ficha=ficha
)


# ============================================================
# FUNÇÃO
# AURA ANALISA E FALA COM O USUÁRIO
# ============================================================

def aura_falar():
    """
    Executa uma rodada do grafo
    e transforma a decisão interna
    em linguagem natural.
    """

    resultado = aura_loop_graph.invoke(
        {
            "estado_produto": estado
        }
    )

    mensagem = gerar_mensagem_aura(
        resultado
    )

    print(
        "\nAURA:"
    )

    print(
        mensagem
    )

    return resultado


# ============================================================
# CABEÇALHO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "SIMULAÇÃO DE CONVERSA COM A AURA"
)

print(
    "PRODUTO 001 — BODY DUBAI"
)

print(
    "========================================"
)


# ============================================================
# RODADA 1
# ============================================================

resultado_1 = aura_falar()


# ============================================================
# SIMULAR RESPOSTA DO USUÁRIO
# ============================================================

print(
    "\nUSUÁRIO:"
)

print(
    "Não."
)


# ============================================================
# PROCESSAR A RESPOSTA
# ============================================================

resposta_1 = processar_informacao(
    ficha=estado.ficha,

    campo=resultado_1["campo"],

    valor=False,

    fonte=(
        FonteEvidencia.VERIFICACAO_FISICA
    ),

    descricao=(
        "Usuário verificou fisicamente "
        "a peça e respondeu que não "
        "possui bojo."
    ),
)

estado.registrar_resultado(
    resposta_1
)


# ============================================================
# RODADA 2
# ============================================================

resultado_2 = aura_falar()


# ============================================================
# SIMULAR RESPOSTA DO USUÁRIO
# ============================================================

print(
    "\nUSUÁRIO:"
)

print(
    "Sim."
)


# ============================================================
# PROCESSAR SEGUNDA RESPOSTA
# ============================================================

resposta_2 = processar_informacao(
    ficha=estado.ficha,

    campo=resultado_2["campo"],

    valor=True,

    fonte=(
        FonteEvidencia.VERIFICACAO_FISICA
    ),

    descricao=(
        "Usuário verificou fisicamente "
        "a peça e confirmou que "
        "possui forro."
    ),
)

estado.registrar_resultado(
    resposta_2
)


# ============================================================
# RODADA 3
# ============================================================

resultado_3 = aura_falar()


# ============================================================
# MOSTRAR RESULTADO INTERNO FINAL
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "RESULTADO INTERNO FINAL"
)

print(
    "========================================"
)

print(
    "STATUS:",
    resultado_3.get(
        "status_fluxo"
    )
)

print(
    "RESULTADO:",
    resultado_3.get(
        "resultado"
    )
)

print(
    "POSSUI BOJO:",
    estado.ficha.possui_bojo
)

print(
    "POSSUI FORRO:",
    estado.ficha.possui_forro
)


# ============================================================
# MEMÓRIA DA AURA
# ============================================================

resumo = estado.resumo()

print(
    "\n"
    "========================================"
)

print(
    "MEMÓRIA DA AURA"
)

print(
    "========================================"
)

print(
    "INFORMAÇÕES ACEITAS:",
    resumo["informacoes_aceitas"]
)

print(
    "AGUARDANDO CONFIRMAÇÃO:",
    resumo["aguardando_confirmacao"]
)

print(
    "INFORMAÇÕES RECUSADAS:",
    resumo["informacoes_recusadas"]
)

print(
    "TOTAL DE DECISÕES:",
    resumo["total_decisoes"]
)


# ============================================================
# FIM
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "FIM DA SIMULAÇÃO"
)

print(
    "========================================"
)