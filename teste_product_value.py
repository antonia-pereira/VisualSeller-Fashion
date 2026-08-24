# ============================================================
# VISUALSELLER FASHION
# TESTE — VALOR PERCEBIDO DO PRODUTO
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
)

from aura.product_value import (
    analisar_valor_produto,
    identificar_promessas_nao_sustentadas,
    formatar_valores,
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
# 2. GERAR SIGNIFICADOS
# ============================================================

significados = analisar_significados(
    ficha
)


# ============================================================
# 3. CONSTRUIR IDENTIDADE
# ============================================================

identidade = construir_identidade(
    significados
)


# ============================================================
# 4. ANALISAR CONEXÕES
# ============================================================

conexoes = analisar_conexoes(
    identidade
)


# ============================================================
# 5. ANALISAR DESEJOS
# ============================================================

desejos = analisar_desejos(
    conexoes
)


# ============================================================
# 6. ANALISAR VALOR PERCEBIDO
# ============================================================

valores = analisar_valor_produto(
    ficha,
    identidade,
    desejos,
)


# ============================================================
# 7. IDENTIFICAR LIMITES DE PROMESSA
# ============================================================

limites = identificar_promessas_nao_sustentadas(
    ficha
)


# ============================================================
# 8. CABEÇALHO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — VALOR PERCEBIDO DO PRODUTO"
)

print(
    "============================================"
)


# ============================================================
# 9. MOSTRAR IDENTIDADE
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
# 10. MOSTRAR DESEJOS
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "DESEJOS UTILIZADOS"
)

print(
    "============================================"
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


# ============================================================
# 11. MOSTRAR VALORES
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "AURA — VALOR PERCEBIDO"
)

print(
    "============================================"
)


print(
    formatar_valores(
        valores,
        limites,
    )
)


# ============================================================
# 12. RESUMO DOS VALORES
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RESUMO DOS VALORES"
)

print(
    "============================================"
)

print(
    "TOTAL DE VALORES:",
    len(
        valores
    )
)


for numero, valor in enumerate(
    valores,
    start=1,
):

    print(
        f"\nVALOR {numero}"
    )

    print(
        "VALOR PERCEBIDO:",
        valor.valor
    )

    print(
        "TIPO:",
        valor.tipo
    )

    print(
        "CONFIANÇA:",
        valor.confianca
    )

    print(
        "QUANTIDADE DE EVIDÊNCIAS:",
        len(
            valor.evidencias
        )
    )


# ============================================================
# 13. VERIFICAÇÃO
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


if valores:

    print(
        "A Aura conseguiu identificar fontes "
        "de valor percebido sustentadas pelas "
        "características do produto."
    )

else:

    print(
        "A Aura ainda não encontrou evidências "
        "suficientes para formular valor percebido."
    )


# ============================================================
# 14. FINAL
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