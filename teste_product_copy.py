# ============================================================
# VISUALSELLER FASHION
# TESTE — COPY COMERCIAL DO PRODUTO
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
    formatar_copy,
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
# 9. GERAR COPY
# ============================================================

copy = gerar_copy(
    ficha,
    posicionamento,
    comunicacao,
)


# ============================================================
# 10. CABEÇALHO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — COPY COMERCIAL DO PRODUTO"
)

print(
    "============================================"
)


# ============================================================
# 11. ESTRATÉGIA UTILIZADA
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
# 12. MOSTRAR COPY
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "AURA — COPY COMERCIAL"
)

print(
    "============================================"
)


print(
    formatar_copy(
        copy
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
    "RESUMO DA COPY"
)

print(
    "============================================"
)


print(
    "TÍTULO:",
    copy.titulo
)


print(
    "CONFIANÇA:",
    copy.confianca
)


print(
    "QUANTIDADE DE BULLETS:",
    len(
        copy.bullets
    )
)


print(
    "QUANTIDADE DE LIMITES:",
    len(
        copy.frases_evitar
    )
)


# ============================================================
# 14. VERIFICAR CONTEÚDO MÍNIMO
# ============================================================

tem_titulo = bool(
    copy.titulo.strip()
)

tem_descricao_curta = bool(
    copy.descricao_curta.strip()
)

tem_descricao_completa = bool(
    copy.descricao_completa.strip()
)

tem_bullets = bool(
    copy.bullets
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
    tem_titulo
    and tem_descricao_curta
    and tem_descricao_completa
    and tem_bullets
):

    print(
        "A Aura conseguiu transformar toda a "
        "estratégia do produto em uma primeira "
        "copy comercial estruturada."
    )

else:

    print(
        "A copy foi criada parcialmente."
    )

    print(
        "TÍTULO:",
        tem_titulo
    )

    print(
        "DESCRIÇÃO CURTA:",
        tem_descricao_curta
    )

    print(
        "DESCRIÇÃO COMPLETA:",
        tem_descricao_completa
    )

    print(
        "BULLETS:",
        tem_bullets
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