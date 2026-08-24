# ============================================================
# VISUALSELLER FASHION
# TESTE — SELEÇÃO INTELIGENTE DE REFERÊNCIAS
# ============================================================

from aura.vision_product import (
    analisar_produto,
)

from aura.product_reference_selector import (
    avaliar_referencias,
    selecionar_melhores_referencias,
    formatar_ranking_referencias,
    formatar_avaliacao_referencia,
)


# ============================================================
# 1. IMAGENS REAIS DO BODY DUBAI
# ============================================================

imagens = [

    {
        "caminho": "imagens/body_frente.jpg.jpeg",
        "tipo": "frente",
    },

    {
        "caminho": "imagens/body_costa.jpeg",
        "tipo": "costas",
    },

    {
        "caminho": "imagens/body_composição.jpeg",
        "tipo": "composicao",
    },

    {
        "caminho": "imagens/body_etiqueta.jpeg",
        "tipo": "etiqueta",
    },

    {
        "caminho": "imagens/body_detalhe (1).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (2).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (3).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (4).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (5).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (6).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (7).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (8).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (9).jpeg",
        "tipo": "detalhe",
    },
]


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
    "TESTE — SELEÇÃO INTELIGENTE DE REFERÊNCIAS"
)

print(
    "============================================"
)


# ============================================================
# 3. VISÃO DA AURA
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "ETAPA 1 — AURA OBSERVANDO AS FOTOGRAFIAS"
)

print(
    "============================================"
)


resultado_visao = analisar_produto(
    imagens
)


print(
    "\nQUANTIDADE DE IMAGENS ANALISADAS:",
    resultado_visao["quantidade_imagens"]
)


print(
    "QUANTIDADE DE EVIDÊNCIAS ENCONTRADAS:",
    resultado_visao["quantidade_evidencias"]
)


# ============================================================
# 4. RANKING — DETALHES VISUAIS
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RANKING — DETALHES VISUAIS"
)

print(
    "============================================"
)


ranking_detalhes = avaliar_referencias(
    resultado_visao=
        resultado_visao,

    funcao_destino=
        "detalhes visuais",
)


print(
    formatar_ranking_referencias(
        ranking_detalhes,
        limite=8,
    )
)


# ============================================================
# 5. RANKING — TEXTURAS E ACABAMENTOS
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RANKING — TEXTURAS E ACABAMENTOS"
)

print(
    "============================================"
)


ranking_texturas = avaliar_referencias(
    resultado_visao=
        resultado_visao,

    funcao_destino=
        "texturas e acabamentos",
)


print(
    formatar_ranking_referencias(
        ranking_texturas,
        limite=8,
    )
)


# ============================================================
# 6. RANKING — CONSTRUÇÃO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RANKING — CONSTRUÇÃO"
)

print(
    "============================================"
)


ranking_construcao = avaliar_referencias(
    resultado_visao=
        resultado_visao,

    funcao_destino=
        "construção",
)


print(
    formatar_ranking_referencias(
        ranking_construcao,
        limite=8,
    )
)


# ============================================================
# 7. RANKING — INFORMAÇÃO TÉCNICA
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RANKING — INFORMAÇÃO TÉCNICA"
)

print(
    "============================================"
)


ranking_tecnico = avaliar_referencias(
    resultado_visao=
        resultado_visao,

    funcao_destino=
        "informação técnica",
)


print(
    formatar_ranking_referencias(
        ranking_tecnico,
        limite=8,
    )
)


# ============================================================
# 8. MELHORES REFERÊNCIAS — DETALHES
# ============================================================

melhores_detalhes = selecionar_melhores_referencias(
    resultado_visao=
        resultado_visao,

    funcao_destino=
        "detalhes visuais",

    limite=3,

    tipos_permitidos=[
        "detalhe",
        "composicao",
    ],
)


print(
    "\n"
    "============================================"
)

print(
    "SELEÇÃO FINAL — DETALHES VISUAIS"
)

print(
    "============================================"
)


for indice, avaliacao in enumerate(
    melhores_detalhes,
    start=1,
):

    print(
        f"\n{indice}º LUGAR"
    )

    print(
        formatar_avaliacao_referencia(
            avaliacao
        )
    )


# ============================================================
# 9. MELHORES REFERÊNCIAS — TEXTURAS
# ============================================================

melhores_texturas = selecionar_melhores_referencias(
    resultado_visao=
        resultado_visao,

    funcao_destino=
        "texturas e acabamentos",

    limite=3,

    tipos_permitidos=[
        "detalhe",
        "composicao",
    ],
)


print(
    "\n"
    "============================================"
)

print(
    "SELEÇÃO FINAL — TEXTURAS E ACABAMENTOS"
)

print(
    "============================================"
)


for indice, avaliacao in enumerate(
    melhores_texturas,
    start=1,
):

    print(
        f"\n{indice}º LUGAR"
    )

    print(
        formatar_avaliacao_referencia(
            avaliacao
        )
    )


# ============================================================
# 10. COMPARAÇÃO ENTRE AS DUAS FUNÇÕES
# ============================================================

arquivos_detalhes = [
    item.caminho
    for item in melhores_detalhes
]


arquivos_texturas = [
    item.caminho
    for item in melhores_texturas
]


print(
    "\n"
    "============================================"
)

print(
    "COMPARAÇÃO"
)

print(
    "============================================"
)


print(
    "\nREFERÊNCIAS ESCOLHIDAS PARA DETALHES:"
)

for caminho in arquivos_detalhes:

    print(
        "-",
        caminho
    )


print(
    "\nREFERÊNCIAS ESCOLHIDAS PARA TEXTURAS:"
)

for caminho in arquivos_texturas:

    print(
        "-",
        caminho
    )


# ============================================================
# 11. VERIFICAÇÃO
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


if not melhores_detalhes:

    print(
        "ERRO: nenhuma referência foi selecionada "
        "para detalhes visuais."
    )


elif not melhores_texturas:

    print(
        "ERRO: nenhuma referência foi selecionada "
        "para texturas e acabamentos."
    )


else:

    print(
        "A Aura conseguiu avaliar visualmente "
        "as fotografias e criar rankings "
        "por finalidade."
    )


    if (
        arquivos_detalhes
        != arquivos_texturas
    ):

        print(
            "Os rankings finais são diferentes."
        )

        print(
            "Isso indica que a seleção está "
            "considerando a finalidade visual "
            "da imagem."
        )

    else:

        print(
            "ATENÇÃO: as duas funções escolheram "
            "exatamente as mesmas referências."
        )

        print(
            "Precisamos analisar as pontuações "
            "antes de integrar o seletor "
            "ao plano de execução."
        )


# ============================================================
# 12. FIM
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