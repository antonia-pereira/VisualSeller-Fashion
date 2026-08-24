from aura_schemas.body import (
    FichaBody,
    GradeTamanho,
)

from aura.state import EstadoProduto

from aura.decision import (
    decidir_proxima_acao,
    mostrar_decisao,
)


# ============================================================
# TESTE DO SISTEMA DE DECISÃO DA AURA
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — SISTEMA DE DECISÃO DA AURA"
)

print(
    "========================================"
)


# ============================================================
# CENÁRIO 1
# EXISTE UMA INFORMAÇÃO AGUARDANDO CONFIRMAÇÃO
# ============================================================

print(
    "\n"
    "CENÁRIO 1 — CONFIRMAÇÃO PENDENTE"
)

ficha_1 = FichaBody(
    marca="Linda Sedução",

    cores_disponiveis=[
        "Preto",
    ],

    tamanhos_disponiveis=[
        "P",
    ],

    grade=[
        GradeTamanho(
            tamanho="P",
            quantidade=1,
        ),
    ],

    quantidade_total=1,

    composicao_principal=(
        "85% poliamida + 15% elastano"
    ),

    materiais_visuais=[
        "renda floral",
    ],

    manga="longa",

    decote_frente="V",

    fechamento=(
        "colchetes na entreperna"
    ),

    transparencia=(
        "mangas e regiões em renda"
    ),
)

estado_1 = EstadoProduto(
    ficha_1
)

estado_1.registrar_resultado(
    {
        "campo": "possui_forro",
        "valor": True,
        "confianca": "baixa",
        "aceita": False,
        "acao": "PRECISA_CONFIRMACAO",
    }
)

decisao_1 = decidir_proxima_acao(
    estado_1
)

mostrar_decisao(
    decisao_1
)


# ============================================================
# CENÁRIO 2
# NÃO HÁ CONFIRMAÇÃO,
# MAS EXISTE CAMPO PENDENTE
# ============================================================

print(
    "\n"
    "CENÁRIO 2 — BUSCAR INFORMAÇÃO"
)

ficha_2 = FichaBody(
    marca="Linda Sedução",

    cores_disponiveis=[
        "Preto",
    ],

    tamanhos_disponiveis=[
        "P",
    ],

    grade=[
        GradeTamanho(
            tamanho="P",
            quantidade=1,
        ),
    ],

    quantidade_total=1,

    composicao_principal=(
        "85% poliamida + 15% elastano"
    ),

    materiais_visuais=[
        "renda floral",
    ],

    manga="longa",

    decote_frente="V",

    fechamento=(
        "colchetes na entreperna"
    ),

    transparencia=(
        "mangas e regiões em renda"
    ),
)

estado_2 = EstadoProduto(
    ficha_2
)

decisao_2 = decidir_proxima_acao(
    estado_2
)

mostrar_decisao(
    decisao_2
)


# ============================================================
# CENÁRIO 3
# FICHA COMPLETA — BODY DUBAI
# ============================================================

print(
    "\n"
    "CENÁRIO 3 — FICHA COMPLETA"
)

ficha_3 = FichaBody(
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

    possui_bojo=False,

    possui_forro=True,

    acabamento_mangas=(
        "malha canelada"
    ),

    tamanho_medido="P",

    observacoes=[
        "Produto fabricado no Brasil",
        (
            "Composição confirmada "
            "pela etiqueta"
        ),
    ],
)

estado_3 = EstadoProduto(
    ficha_3
)

decisao_3 = decidir_proxima_acao(
    estado_3
)

mostrar_decisao(
    decisao_3
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