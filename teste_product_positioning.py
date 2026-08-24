# ============================================================
# VISUALSELLER FASHION
# TESTE — POSICIONAMENTO DO PRODUTO
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
)

from aura.product_positioning import (
    analisar_posicionamento,
    formatar_posicionamento,
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
# 7. ANALISAR POSICIONAMENTO
# ============================================================

posicionamento = analisar_posicionamento(
    identidade,
    desejos,
    valores,
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
    "TESTE — POSICIONAMENTO DO PRODUTO"
)

print(
    "============================================"
)


# ============================================================
# 9. MOSTRAR IDENTIDADE UTILIZADA
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
# 10. MOSTRAR DESEJOS UTILIZADOS
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
# 11. MOSTRAR VALORES UTILIZADOS
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VALORES UTILIZADOS"
)

print(
    "============================================"
)


for numero, valor in enumerate(
    valores,
    start=1,
):

    print(
        f"\nVALOR {numero}"
    )

    print(
        "VALOR:",
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


# ============================================================
# 12. MOSTRAR POSICIONAMENTO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "AURA — POSICIONAMENTO"
)

print(
    "============================================"
)


print(
    formatar_posicionamento(
        posicionamento
    )
)


# ============================================================
# 13. RESUMO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RESUMO DO POSICIONAMENTO"
)

print(
    "============================================"
)


print(
    "DIREÇÃO PRINCIPAL:",
    posicionamento.direcao_principal
)

print(
    "TERRITÓRIO:",
    posicionamento.territorio_comunicacao
)

print(
    "CONFIANÇA:",
    posicionamento.confianca
)

print(
    "QUANTIDADE DE DESTAQUES:",
    len(
        posicionamento.destacar
    )
)

print(
    "QUANTIDADE DE LIMITES:",
    len(
        posicionamento.evitar
    )
)

print(
    "QUANTIDADE DE EVIDÊNCIAS:",
    len(
        posicionamento.evidencias
    )
)


# ============================================================
# 14. VERIFICAÇÃO
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


if (
    posicionamento.direcao_principal
    and posicionamento.territorio_comunicacao
):

    print(
        "A Aura conseguiu transformar identidade, "
        "desejos e valores percebidos em uma "
        "direção de posicionamento."
    )

else:

    print(
        "A Aura ainda não possui informações "
        "suficientes para definir posicionamento."
    )


# ============================================================
# 15. FINAL
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