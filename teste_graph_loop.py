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


# ============================================================
# TESTE DO GRAFO CONTÍNUO DA AURA
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
# 2. CRIAR MEMÓRIA DO PRODUTO
# ============================================================

estado = EstadoProduto(
    ficha=ficha
)


# ============================================================
# FUNÇÃO AUXILIAR
# EXECUTAR UMA RODADA DA AURA
# ============================================================

def executar_rodada(
    numero_rodada: int,
):
    print(
        "\n"
        "========================================"
    )

    print(
        f"RODADA {numero_rodada}"
    )

    print(
        "========================================"
    )

    resultado = aura_loop_graph.invoke(
        {
            "estado_produto": estado
        }
    )

    print(
        "AÇÃO:",
        resultado.get("acao")
    )

    print(
        "CAMPO:",
        resultado.get("campo")
    )

    print(
        "VALOR PROPOSTO:",
        resultado.get(
            "valor_proposto"
        )
    )

    print(
        "MOTIVO:",
        resultado.get("motivo")
    )

    print(
        "STATUS:",
        resultado.get(
            "status_fluxo"
        )
    )

    print(
        "RESULTADO:",
        resultado.get(
            "resultado"
        )
    )

    return resultado


# ============================================================
# INÍCIO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — GRAFO CONTÍNUO DA AURA"
)

print(
    "PRODUTO 001 — BODY DUBAI"
)

print(
    "========================================"
)


# ============================================================
# RODADA 1
# AURA DEVE IDENTIFICAR QUE FALTA POSSUI_BOJO
# ============================================================

resultado_1 = executar_rodada(
    1
)


# ============================================================
# SIMULAR RESPOSTA DO USUÁRIO
#
# Usuário responde:
# "Não possui bojo."
# ============================================================

print(
    "\n"
    "USUÁRIO RESPONDE:"
)

print(
    "Não possui bojo."
)

resposta_bojo = processar_informacao(
    ficha=estado.ficha,

    campo="possui_bojo",

    valor=False,

    fonte=(
        FonteEvidencia.VERIFICACAO_FISICA
    ),

    descricao=(
        "Usuário verificou fisicamente "
        "a peça e confirmou ausência de bojo."
    ),
)

estado.registrar_resultado(
    resposta_bojo
)


# ============================================================
# RODADA 2
# AGORA A AURA DEVE IDENTIFICAR POSSUI_FORRO
# ============================================================

resultado_2 = executar_rodada(
    2
)


# ============================================================
# SIMULAR RESPOSTA DO USUÁRIO
#
# Usuário responde:
# "Sim, possui forro."
# ============================================================

print(
    "\n"
    "USUÁRIO RESPONDE:"
)

print(
    "Sim, possui forro."
)

resposta_forro = processar_informacao(
    ficha=estado.ficha,

    campo="possui_forro",

    valor=True,

    fonte=(
        FonteEvidencia.VERIFICACAO_FISICA
    ),

    descricao=(
        "Usuário confirmou fisicamente "
        "que a peça possui forro."
    ),
)

estado.registrar_resultado(
    resposta_forro
)


# ============================================================
# RODADA 3
# AURA DEVE VERIFICAR NOVAMENTE A FICHA
# ============================================================

resultado_3 = executar_rodada(
    3
)


# ============================================================
# ESTADO FINAL DO PRODUTO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "ESTADO FINAL DO PRODUTO"
)

print(
    "========================================"
)

print(
    "POSSUI BOJO:",
    estado.ficha.possui_bojo
)

print(
    "POSSUI FORRO:",
    estado.ficha.possui_forro
)

print(
    "COMPOSIÇÃO DO FORRO:",
    estado.ficha.composicao_forro
)


# ============================================================
# RESUMO DA MEMÓRIA
# ============================================================

resumo = estado.resumo()

print(
    "\n"
    "INFORMAÇÕES ACEITAS:",
    resumo[
        "informacoes_aceitas"
    ]
)

print(
    "AGUARDANDO CONFIRMAÇÃO:",
    resumo[
        "aguardando_confirmacao"
    ]
)

print(
    "INFORMAÇÕES RECUSADAS:",
    resumo[
        "informacoes_recusadas"
    ]
)

print(
    "TOTAL DE DECISÕES:",
    resumo[
        "total_decisoes"
    ]
)


# ============================================================
# FIM
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "FIM DO TESTE"
)

print(
    "========================================"
)