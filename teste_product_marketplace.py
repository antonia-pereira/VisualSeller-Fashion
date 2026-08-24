# ============================================================
# VISUALSELLER FASHION
# TESTE — MARKETPLACE
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
)

from aura.product_communication import (
    analisar_comunicacao,
)

from aura.product_copy import (
    gerar_copy,
)

from aura.product_marketplace import (
    gerar_marketplace,
    formatar_marketplace,
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
# 6. VALOR PERCEBIDO
# ============================================================

valores = analisar_valor_produto(
    ficha,
    identidade,
    desejos,
)


# ============================================================
# 7. POSICIONAMENTO
# ============================================================

posicionamento = analisar_posicionamento(
    identidade,
    desejos,
    valores,
)


# ============================================================
# 8. COMUNICAÇÃO
# ============================================================

comunicacao = analisar_comunicacao(
    posicionamento
)


# ============================================================
# 9. COPY-MÃE
# ============================================================

copy = gerar_copy(
    ficha,
    posicionamento,
    comunicacao,
)


# ============================================================
# 10. ADAPTAÇÃO PARA MARKETPLACE
# ============================================================

marketplace = gerar_marketplace(
    ficha,
    copy,
)


# ============================================================
# 11. CABEÇALHO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — MARKETPLACE"
)

print(
    "============================================"
)


# ============================================================
# 12. ESTRATÉGIA DE ORIGEM
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "COPY-MÃE UTILIZADA"
)

print(
    "============================================"
)


print(
    "TÍTULO:",
    copy.titulo
)


print(
    "CONFIANÇA DA COPY:",
    copy.confianca
)


print(
    "BULLETS DA COPY:",
    len(
        copy.bullets
    )
)


# ============================================================
# 13. MOSTRAR MARKETPLACE
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "AURA — MARKETPLACE"
)

print(
    "============================================"
)


print(
    formatar_marketplace(
        marketplace
    )
)


# ============================================================
# 14. RESUMO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RESUMO DO MARKETPLACE"
)

print(
    "============================================"
)


print(
    "TÍTULO:",
    marketplace.titulo
)


print(
    "CONFIANÇA:",
    marketplace.confianca
)


print(
    "QUANTIDADE DE BULLETS:",
    len(
        marketplace.bullets
    )
)


print(
    "QUANTIDADE DE TERMOS DE BUSCA:",
    len(
        marketplace.termos_busca
    )
)


print(
    "QUANTIDADE DE ITENS NA FICHA RESUMIDA:",
    len(
        marketplace.ficha_resumida
    )
)


print(
    "QUANTIDADE DE PERGUNTAS NO FAQ:",
    len(
        marketplace.faq
    )
)


# ============================================================
# 15. VERIFICAÇÕES
# ============================================================

tem_titulo = bool(
    marketplace.titulo.strip()
)

tem_descricao = bool(
    marketplace.descricao.strip()
)

tem_bullets = bool(
    marketplace.bullets
)

tem_termos = bool(
    marketplace.termos_busca
)

tem_ficha = bool(
    marketplace.ficha_resumida
)

tem_faq = bool(
    marketplace.faq
)


# ============================================================
# 16. RESULTADO DA VERIFICAÇÃO
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
    tem_titulo
    and tem_descricao
    and tem_bullets
    and tem_termos
    and tem_ficha
    and tem_faq
):

    print(
        "A Aura conseguiu adaptar a copy-mãe "
        "para uma estrutura completa de marketplace."
    )

else:

    print(
        "A adaptação para marketplace "
        "foi criada parcialmente."
    )

    print(
        "TÍTULO:",
        tem_titulo
    )

    print(
        "DESCRIÇÃO:",
        tem_descricao
    )

    print(
        "BULLETS:",
        tem_bullets
    )

    print(
        "TERMOS DE BUSCA:",
        tem_termos
    )

    print(
        "FICHA RESUMIDA:",
        tem_ficha
    )

    print(
        "FAQ:",
        tem_faq
    )


# ============================================================
# 17. FIM
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