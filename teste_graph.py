from aura_schemas.body import (
    FichaBody,
    GradeTamanho,
)

from aura.state import EstadoProduto

from aura.graph import aura_graph


# ============================================================
# TESTE DO GRAFO DA AURA
# PRODUTO 001 — BODY DUBAI
# ============================================================


# ============================================================
# CENÁRIO 1
# FICHA INCOMPLETA
# AURA DEVE BUSCAR INFORMAÇÃO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "CENÁRIO 1 — FICHA INCOMPLETA"
)

print(
    "========================================"
)

ficha_incompleta = FichaBody(
    marca="Linda Sedução",

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
)

estado_incompleto = EstadoProduto(
    ficha=ficha_incompleta
)

resultado_1 = aura_graph.invoke(
    {
        "ficha": estado_incompleto
    }
)

print(
    "AÇÃO:",
    resultado_1.get("acao")
)

print(
    "CAMPO:",
    resultado_1.get("campo")
)

print(
    "MOTIVO:",
    resultado_1.get("motivo")
)

print(
    "RESULTADO:",
    resultado_1.get("resultado")
)


# ============================================================
# CENÁRIO 2
# EXISTE UMA CONFIRMAÇÃO PENDENTE
# AURA DEVE PEDIR CONFIRMAÇÃO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "CENÁRIO 2 — CONFIRMAÇÃO PENDENTE"
)

print(
    "========================================"
)

ficha_confirmacao = FichaBody(
    marca="Linda Sedução",

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
)

estado_confirmacao = EstadoProduto(
    ficha=ficha_confirmacao
)

estado_confirmacao.registrar_resultado(
    {
        "campo": "possui_forro",
        "valor": True,
        "fonte": "inferencia_aura",
        "confianca": "baixa",
        "aceita": False,
        "acao": "PRECISA_CONFIRMACAO",
    }
)

resultado_2 = aura_graph.invoke(
    {
        "ficha": estado_confirmacao
    }
)

print(
    "AÇÃO:",
    resultado_2.get("acao")
)

print(
    "CAMPO:",
    resultado_2.get("campo")
)

print(
    "VALOR PROPOSTO:",
    resultado_2.get("valor_proposto")
)

print(
    "MOTIVO:",
    resultado_2.get("motivo")
)

print(
    "RESULTADO:",
    resultado_2.get("resultado")
)


# ============================================================
# CENÁRIO 3
# FICHA COMPLETA
# AURA DEVE ENCERRAR
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "CENÁRIO 3 — FICHA COMPLETA"
)

print(
    "========================================"
)

ficha_completa = FichaBody(
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

    possui_bojo=False,

    possui_forro=True,

    transparencia=(
        "mangas e regiões em renda"
    ),

    acabamento_mangas=(
        "malha canelada"
    ),

    tamanho_medido="P",
)

estado_completo = EstadoProduto(
    ficha=ficha_completa
)

resultado_3 = aura_graph.invoke(
    {
        "ficha": estado_completo
    }
)

print(
    "AÇÃO:",
    resultado_3.get("acao")
)

print(
    "CAMPO:",
    resultado_3.get("campo")
)

print(
    "MOTIVO:",
    resultado_3.get("motivo")
)

print(
    "RESULTADO:",
    resultado_3.get("resultado")
)


# ============================================================
# FIM
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "FIM DO TESTE DO LANGGRAPH"
)

print(
    "========================================"
)