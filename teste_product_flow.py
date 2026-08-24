from aura.product_flow import (
    iniciar_produto,
    obter_proxima_interacao,
    receber_resposta,
    produto_concluido,
    obter_status_produto,
    obter_ficha_final,
    mostrar_resumo_produto,
)

from aura_schemas.body import (
    FichaBody,
)


# ============================================================
# VISUALSELLER FASHION
# TESTE — FLUXO PRINCIPAL DO PRODUTO
# ============================================================


# ============================================================
# 1. INICIAR SESSÃO
# ============================================================

sessao = iniciar_produto()


# ============================================================
# 2. SIMULAR RESULTADO DA VISÃO
# ============================================================

sessao[
    "ficha"
] = FichaBody(

    referencia="277",

    codigo_barras=(
        "7002770010015"
    ),

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

    decote_costas="V",

    fechamento="colchetes",

    possui_forro=True,

    transparencia=(
        "Transparência parcial em mangas, "
        "regiões laterais e costas."
    ),

    acabamento_mangas=(
        "Punho largo em malha canelada "
        "e opaca."
    ),

    tamanho_medido="P",
)


sessao[
    "status"
] = "FICHA_PREENCHIDA_PELA_VISAO"


# ============================================================
# 3. INÍCIO DA EXPERIÊNCIA
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "Mostre seu produto para a Aura"
)

print(
    "========================================"
)


print(
    "\nAURA:"
)

print(
    "Já analisei as imagens do produto."
)


# ============================================================
# 4. PRIMEIRA PERGUNTA
# ============================================================

while not produto_concluido(
    sessao
):


    pergunta = obter_proxima_interacao(
        sessao
    )


    if pergunta is None:

        break


    print(
        "\n"
        "----------------------------------------"
    )

    print(
        "\nAURA:"
    )

    print(
        pergunta[
            "mensagem"
        ]
    )


    # ========================================================
    # RESPOSTAS SIMULADAS
    # ========================================================

    grupo = pergunta[
        "grupo"
    ]


    if grupo == "IDENTIDADE_COMERCIAL":

        resposta = (
            "Linda Sedução, "
            "Body Dubai, "
            "preto, "
            "P M G GG"
        )


    elif grupo == "ESTOQUE":

        resposta = (
            "P 8, M 10, G 11, GG 15"
        )


    elif grupo == "ESTRUTURA":

        resposta = "Não"


    else:

        resposta = ""


    print(
        "\nVOCÊ:"
    )

    print(
        resposta
    )


    resultado = receber_resposta(
        sessao=sessao,
        resposta=resposta,
    )


    print(
        "\nAURA:"
    )

    print(
        "Informações registradas:",
        resultado.get(
            "campos_atualizados"
        ),
    )


# ============================================================
# 5. STATUS FINAL
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "RESULTADO FINAL"
)

print(
    "========================================"
)


mostrar_resumo_produto(
    sessao
)


status = obter_status_produto(
    sessao
)


print(
    "\nCONVERSA FINALIZADA:",
    produto_concluido(
        sessao
    )
)


# ============================================================
# 6. FICHA FINAL
# ============================================================

ficha = obter_ficha_final(
    sessao
)


print(
    "\n"
    "========================================"
)

print(
    "FICHA FINAL"
)

print(
    "========================================"
)


print(
    "MARCA:",
    ficha.marca
)

print(
    "MODELO:",
    ficha.nome_modelo
)

print(
    "COR:",
    ficha.cores_disponiveis
)

print(
    "TAMANHOS:",
    ficha.tamanhos_disponiveis
)


print(
    "GRADE:"
)

for item in ficha.grade:

    print(
        "-",
        item.tamanho,
        ":",
        item.quantidade,
    )


print(
    "QUANTIDADE TOTAL:",
    ficha.quantidade_total
)


print(
    "POSSUI BOJO:",
    ficha.possui_bojo
)


print(
    "REFERÊNCIA:",
    ficha.referencia
)


print(
    "COMPOSIÇÃO:",
    ficha.composicao_principal
)


# ============================================================
# FIM
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "FIM DO TESTE"
)

print(
    "========================================"
)