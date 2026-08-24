# ============================================================
# VISUALSELLER FASHION
# TESTE — PLANO VISUAL DO PRODUTO
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

from aura.product_visual_plan import (
    criar_plano_visual,
    formatar_plano_visual,
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
    "TESTE — PLANO VISUAL DO PRODUTO"
)

print(
    "============================================"
)


# ============================================================
# 3. SIGNIFICADOS
# ============================================================

significados = analisar_significados(
    ficha
)


# ============================================================
# 4. IDENTIDADE
# ============================================================

identidade = construir_identidade(
    significados
)


# ============================================================
# 5. CONEXÕES
# ============================================================

conexoes = analisar_conexoes(
    identidade
)


# ============================================================
# 6. DESEJOS
# ============================================================

desejos = analisar_desejos(
    conexoes
)


# ============================================================
# 7. VALOR PERCEBIDO
# ============================================================

valores = analisar_valor_produto(
    ficha,
    identidade,
    desejos,
)


# ============================================================
# 8. POSICIONAMENTO
# ============================================================

posicionamento = analisar_posicionamento(
    identidade,
    desejos,
    valores,
)


# ============================================================
# 9. COMUNICAÇÃO
# ============================================================

comunicacao = analisar_comunicacao(
    posicionamento
)


# ============================================================
# 10. MOSTRAR ESTRATÉGIA UTILIZADA
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "ESTRATÉGIA UTILIZADA"
)

print(
    "============================================"
)


print(
    "IDENTIDADE:",
    identidade.leitura_principal
)


print(
    "POSICIONAMENTO:",
    posicionamento.direcao_principal
)


print(
    "TERRITÓRIO:",
    posicionamento.territorio_comunicacao
)


print(
    "MENSAGEM CENTRAL:",
    comunicacao.mensagem_central
)


# ============================================================
# 11. CRIAR PLANO VISUAL
# ============================================================

plano = criar_plano_visual(
    ficha=ficha,
    identidade=identidade,
    posicionamento=posicionamento,
    comunicacao=comunicacao,
)


# ============================================================
# 12. MOSTRAR PLANO VISUAL
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "AURA — PLANO VISUAL"
)

print(
    "============================================"
)


print(
    formatar_plano_visual(
        plano
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
    "RESUMO DO PLANO VISUAL"
)

print(
    "============================================"
)


print(
    "CONCEITO VISUAL:",
    plano.conceito_visual
)


print(
    "DIREÇÃO VISUAL:",
    plano.direcao_visual
)


print(
    "CONFIANÇA:",
    plano.confianca
)


print(
    "QUANTIDADE DE IMAGENS:",
    len(
        plano.imagens
    )
)


print(
    "QUANTIDADE DE LIMITES:",
    len(
        plano.evitar
    )
)


# ============================================================
# 14. RESUMO DAS IMAGENS
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "SEQUÊNCIA VISUAL"
)

print(
    "============================================"
)


for imagem in plano.imagens:

    print(
        f"\nIMAGEM {imagem.numero}"
    )

    print(
        "FUNÇÃO:",
        imagem.funcao
    )

    print(
        "CONFIANÇA:",
        imagem.confianca
    )

    print(
        "QUANTIDADE DE EVIDÊNCIAS:",
        len(
            imagem.evidencias
        )
    )


# ============================================================
# 15. VERIFICAÇÃO
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
    plano.imagens
    and len(
        plano.imagens
    ) == 7
):

    print(
        "A Aura conseguiu transformar a estratégia "
        "do produto em uma sequência visual "
        "estruturada para marketplace."
    )

else:

    print(
        "O plano visual foi criado parcialmente."
    )

    print(
        "QUANTIDADE DE IMAGENS:",
        len(
            plano.imagens
        )
    )


# ============================================================
# 16. FIM
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