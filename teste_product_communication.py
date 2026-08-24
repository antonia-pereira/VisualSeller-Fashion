# ============================================================
# VISUALSELLER FASHION
# TESTE — COMUNICAÇÃO DO PRODUTO
# ============================================================

from aura_schemas.body import (
    FichaBody,
    GradeTamanho,
)

from aura.product_meaning import analisar_significados
from aura.product_identity import construir_identidade
from aura.product_connection import analisar_conexoes
from aura.product_desire import analisar_desejos
from aura.product_value import analisar_valor_produto

from aura.product_positioning import (
    analisar_posicionamento,
)

from aura.product_communication import (
    analisar_comunicacao,
    formatar_comunicacao,
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
# 9. CABEÇALHO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — COMUNICAÇÃO DO PRODUTO"
)

print(
    "============================================"
)


# ============================================================
# 10. POSICIONAMENTO UTILIZADO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "POSICIONAMENTO UTILIZADO"
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


# ============================================================
# 11. COMUNICAÇÃO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "AURA — COMUNICAÇÃO"
)

print(
    "============================================"
)

print(
    formatar_comunicacao(
        comunicacao
    )
)


# ============================================================
# 12. RESUMO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RESUMO DA COMUNICAÇÃO"
)

print(
    "============================================"
)

print(
    "MENSAGEM CENTRAL:",
    comunicacao.mensagem_central
)

print(
    "CONFIANÇA:",
    comunicacao.confianca
)

print(
    "QUANTIDADE DE TONS:",
    len(comunicacao.tom)
)

print(
    "QUANTIDADE DE DIRETRIZES DE LINGUAGEM:",
    len(comunicacao.linguagem)
)

print(
    "QUANTIDADE DE PILARES:",
    len(comunicacao.pilares_comunicacao)
)

print(
    "QUANTIDADE DE PALAVRAS PRIORITÁRIAS:",
    len(comunicacao.palavras_priorizar)
)

print(
    "QUANTIDADE DE LIMITES:",
    len(comunicacao.abordagens_evitar)
)

print(
    "QUANTIDADE DE EVIDÊNCIAS:",
    len(comunicacao.evidencias)
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

if (
    comunicacao.mensagem_central
    and comunicacao.tom
    and comunicacao.linguagem
):

    print(
        "A Aura conseguiu transformar o posicionamento "
        "do produto em uma direção de comunicação."
    )

else:

    print(
        "A Aura ainda não possui informações "
        "suficientes para definir a comunicação."
    )


# ============================================================
# 14. FIM
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