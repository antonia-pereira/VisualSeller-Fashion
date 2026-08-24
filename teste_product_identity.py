# ============================================================
# VISUALSELLER FASHION
# TESTE — IDENTIDADE DO PRODUTO
# ============================================================

from aura.product_meaning import (
    HipoteseSignificado,
)

from aura.product_identity import (
    construir_identidade,
    formatar_identidade,
)


# ============================================================
# 1. HIPÓTESES JÁ VALIDADAS
# ============================================================

hipoteses = [

    HipoteseSignificado(
        significado="sensualidade",
        evidencias=[
            "presença de transparência",
            "presença de renda",
            "decote profundo",
        ],
        confianca="alta",
    ),

    HipoteseSignificado(
        significado="delicadeza",
        evidencias=[
            "renda com desenho floral",
            "transparência localizada",
        ],
        confianca="media",
    ),

    HipoteseSignificado(
        significado="contraste visual",
        evidencias=[
            "áreas translúcidas",
            "áreas opacas",
            "acabamento canelado",
        ],
        confianca="alta",
    ),
]


# ============================================================
# 2. CABEÇALHO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — IDENTIDADE DO PRODUTO"
)

print(
    "============================================"
)


# ============================================================
# 3. CONSTRUIR IDENTIDADE
# ============================================================

identidade = construir_identidade(
    hipoteses
)


# ============================================================
# 4. MOSTRAR IDENTIDADE
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "AURA — IDENTIDADE DO PRODUTO"
)

print(
    "============================================"
)


resultado_formatado = formatar_identidade(
    identidade
)


print(
    resultado_formatado
)


# ============================================================
# 5. RESUMO TÉCNICO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RESUMO DA IDENTIDADE"
)

print(
    "============================================"
)


print(
    "LEITURA PRINCIPAL:",
    identidade.leitura_principal
)


print(
    "TRAÇOS DOMINANTES:",
    identidade.tracos_dominantes
)


print(
    "TRAÇOS DE APOIO:",
    identidade.tracos_apoio
)


print(
    "QUANTIDADE DE EVIDÊNCIAS:",
    len(
        identidade.evidencias
    )
)


# ============================================================
# 6. VERIFICAÇÃO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VERIFICAÇÃO"
)

print(
    "============================================"
)


if identidade.tracos_dominantes:

    print(
        "A Aura conseguiu organizar as hipóteses "
        "em uma identidade do produto."
    )

else:

    print(
        "Ainda não existem evidências suficientes "
        "para definir a identidade do produto."
    )


# ============================================================
# 7. FIM
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "FIM DO TESTE"
)

print(
    "============================================"
)