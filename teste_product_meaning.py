# ============================================================
# VISUALSELLER FASHION
# TESTE — SIGNIFICADO DO PRODUTO
# ============================================================

from aura.product_meaning import (
    analisar_significados,
    formatar_significados,
)

from aura_schemas.body import (
    FichaBody,
    GradeTamanho,
)


# ============================================================
# 1. CRIAR FICHA JÁ COMPREENDIDA PELA AURA
# ============================================================

ficha = FichaBody(

    categoria="Moda íntima",

    tipo_produto="Body",

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
        "85% poliamida, 15% elastano"
    ),

    composicao_forro=(
        "100% algodão"
    ),

    materiais_visuais=[
        "renda floral",
        "malha/tela fina translúcida",
        "malha canelada",
    ],

    manga="longa",

    decote_frente="V",

    decote_costas="V profundo",

    fechamento="colchetes",

    possui_bojo=False,

    possui_forro=True,

    transparencia=(
        "Transparência parcial em mangas, "
        "costas e áreas em renda."
    ),

    acabamento_mangas=(
        "Punho largo em malha canelada e opaca."
    ),

    tamanho_medido="P",
)


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
    "TESTE — SIGNIFICADO DO PRODUTO"
)

print(
    "============================================"
)


# ============================================================
# 3. ANALISAR SIGNIFICADOS
# ============================================================

hipoteses = analisar_significados(
    ficha
)


# ============================================================
# 4. MOSTRAR RESULTADO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "AURA — SIGNIFICADO DO PRODUTO"
)

print(
    "============================================"
)


resultado_formatado = formatar_significados(
    hipoteses
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
    "RESUMO DAS HIPÓTESES"
)

print(
    "============================================"
)


print(
    "TOTAL DE HIPÓTESES:",
    len(
        hipoteses
    )
)


for hipotese in hipoteses:

    print(
        "\nSIGNIFICADO:",
        hipotese.significado
    )

    print(
        "CONFIANÇA:",
        hipotese.confianca
    )

    print(
        "QUANTIDADE DE EVIDÊNCIAS:",
        len(
            hipotese.evidencias
        )
    )


# ============================================================
# 6. VERIFICAÇÃO DA REGRA DE SEGURANÇA
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


if hipoteses:

    print(
        "A Aura encontrou hipóteses sustentadas "
        "por evidências do produto."
    )

else:

    print(
        "A Aura não encontrou evidências suficientes "
        "para criar hipóteses."
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