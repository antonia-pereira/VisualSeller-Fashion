# ============================================================
# VISUALSELLER FASHION
# TESTE — DESEJOS ASSOCIADOS AO PRODUTO
# ============================================================

from aura_schemas.body import (
    FichaBody,
    GradeTamanho,
)

from aura.product_meaning import (
    analisar_significados,
)

from aura.product_identity import (
    construir_identidade,
)

from aura.product_connection import (
    analisar_conexoes,
)

from aura.product_desire import (
    analisar_desejos,
    formatar_desejos,
)


# ============================================================
# 1. CRIAR FICHA DO PRODUTO
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
# 2. SIGNIFICADOS
# ============================================================

significados = analisar_significados(
    ficha
)


# ============================================================
# 3. IDENTIDADE
# ============================================================

identidade = construir_identidade(
    significados
)


# ============================================================
# 4. CONEXÕES
# ============================================================

conexoes = analisar_conexoes(
    identidade
)


# ============================================================
# 5. DESEJOS
# ============================================================

desejos = analisar_desejos(
    conexoes
)


# ============================================================
# 6. CABEÇALHO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — DESEJOS ASSOCIADOS AO PRODUTO"
)

print(
    "============================================"
)


# ============================================================
# 7. MOSTRAR IDENTIDADE
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "IDENTIDADE DO PRODUTO"
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


# ============================================================
# 8. MOSTRAR DESEJOS
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "AURA — DESEJOS"
)

print(
    "============================================"
)

print(
    formatar_desejos(
        desejos
    )
)


# ============================================================
# 9. RESUMO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RESUMO DOS DESEJOS"
)

print(
    "============================================"
)

print(
    "TOTAL DE DESEJOS:",
    len(desejos)
)


for numero, desejo in enumerate(
    desejos,
    start=1,
):

    print(
        f"\nDESEJO {numero}"
    )

    print(
        "DESEJO:",
        desejo.desejo
    )

    print(
        "CONFIANÇA:",
        desejo.confianca
    )

    print(
        "QUANTIDADE DE EVIDÊNCIAS:",
        len(
            desejo.evidencias
        )
    )


# ============================================================
# 10. VERIFICAÇÃO
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


if desejos:

    print(
        "A Aura conseguiu formular possíveis "
        "desejos sustentados pelas conexões "
        "com o produto."
    )

else:

    print(
        "A Aura ainda não possui evidências "
        "suficientes para formular desejos."
    )


# ============================================================
# 11. FINAL
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