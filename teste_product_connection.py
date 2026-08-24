# ============================================================
# VISUALSELLER FASHION
# TESTE — CONEXÃO ENTRE PRODUTO E PESSOA
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
    formatar_conexoes,
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
# 5. CABEÇALHO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — CONEXÃO ENTRE PRODUTO E PESSOA"
)

print(
    "============================================"
)


# ============================================================
# 6. MOSTRAR IDENTIDADE BASE
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "IDENTIDADE UTILIZADA"
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
# 7. MOSTRAR CONEXÕES
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "AURA — CONEXÃO COM A PESSOA"
)

print(
    "============================================"
)


print(
    formatar_conexoes(
        conexoes
    )
)


# ============================================================
# 8. RESUMO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RESUMO DAS CONEXÕES"
)

print(
    "============================================"
)


print(
    "TOTAL DE CONEXÕES:",
    len(
        conexoes
    )
)


for numero, conexao in enumerate(
    conexoes,
    start=1,
):

    print(
        f"\nCONEXÃO {numero}"
    )

    print(
        "BUSCA:",
        conexao.busca
    )

    print(
        "CONFIANÇA:",
        conexao.confianca
    )

    print(
        "QUANTIDADE DE EVIDÊNCIAS:",
        len(
            conexao.evidencias
        )
    )


# ============================================================
# 9. VERIFICAÇÃO
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


if conexoes:

    print(
        "A Aura encontrou possíveis conexões "
        "sustentadas pela identidade do produto."
    )

else:

    print(
        "A Aura ainda não encontrou evidências "
        "suficientes para formular conexões."
    )


# ============================================================
# 10. FINAL
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