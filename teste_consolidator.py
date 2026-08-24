from aura.vision_product import analisar_produto

from aura.consolidator import (
    agrupar_evidencias_por_campo,
    resumir_grupos,
    gerar_conhecimento_consolidado,
)


# ============================================================
# VISUALSELLER FASHION
# TESTE — CONSOLIDAÇÃO DE EVIDÊNCIAS
# ============================================================


# ============================================================
# 1. IMAGENS DO PRODUTO
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
    {
        "caminho": "imagens/body_composição.jpeg",
        "tipo": "composicao",
    },
    {
        "caminho": "imagens/body_etiqueta.jpeg",
        "tipo": "etiqueta",
    },
]


# ============================================================
# 2. CABEÇALHO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — CONSOLIDAÇÃO DE EVIDÊNCIAS"
)

print(
    "========================================"
)


# ============================================================
# 3. ANALISAR TODAS AS IMAGENS
# ============================================================

resultado_visao = analisar_produto(
    imagens
)

evidencias = resultado_visao[
    "evidencias"
]


# ============================================================
# 4. AGRUPAR EVIDÊNCIAS
# ============================================================

grupos = agrupar_evidencias_por_campo(
    evidencias
)


# ============================================================
# 5. CRIAR RESUMO
# ============================================================

resumo = resumir_grupos(
    grupos
)


# ============================================================
# 6. GERAR CONHECIMENTO CONSOLIDADO
# ============================================================

conhecimento = gerar_conhecimento_consolidado(
    grupos
)


# ============================================================
# 7. RESULTADO GERAL
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "RESULTADO GERAL"
)

print(
    "========================================"
)

print(
    "IMAGENS ANALISADAS:",
    resultado_visao[
        "quantidade_imagens"
    ]
)

print(
    "EVIDÊNCIAS BRUTAS:",
    resultado_visao[
        "quantidade_evidencias"
    ]
)

print(
    "CAMPOS DIFERENTES:",
    len(
        grupos
    )
)


# ============================================================
# 8. EVIDÊNCIAS AGRUPADAS
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "EVIDÊNCIAS AGRUPADAS POR CAMPO"
)

print(
    "========================================"
)


for item in resumo:

    print(
        "\nCAMPO:",
        item[
            "campo"
        ]
    )

    print(
        "CLASSIFICAÇÃO:",
        item[
            "classificacao"
        ]
    )

    print(
        "QUANTIDADE DE EVIDÊNCIAS:",
        item[
            "quantidade_evidencias"
        ]
    )

    print(
        "VALORES:"
    )

    for valor in item[
        "valores"
    ]:

        print(
            " -",
            valor
        )

    print(
        "VALOR CONSOLIDADO:",
        item.get(
            "valor_consolidado"
        )
    )

    print(
        "IMAGENS:",
        item[
            "imagens"
        ]
    )

    print(
        "CONFIANÇAS:",
        item[
            "confiancas"
        ]
    )


# ============================================================
# 9. RESUMO DAS CLASSIFICAÇÕES
# ============================================================

quantidade_concordancia = 0
quantidade_complementar = 0
quantidade_conflito = 0
quantidade_sem_evidencia = 0


for item in resumo:

    classificacao = item[
        "classificacao"
    ]

    if classificacao == "CONCORDANCIA":

        quantidade_concordancia += 1

    elif classificacao == "COMPLEMENTAR":

        quantidade_complementar += 1

    elif classificacao == "CONFLITO":

        quantidade_conflito += 1

    elif classificacao == "SEM_EVIDENCIA":

        quantidade_sem_evidencia += 1


print(
    "\n"
    "========================================"
)

print(
    "RESUMO DAS CLASSIFICAÇÕES"
)

print(
    "========================================"
)

print(
    "CONCORDÂNCIA:",
    quantidade_concordancia
)

print(
    "COMPLEMENTAR:",
    quantidade_complementar
)

print(
    "CONFLITO:",
    quantidade_conflito
)

print(
    "SEM EVIDÊNCIA:",
    quantidade_sem_evidencia
)


# ============================================================
# 10. CONHECIMENTO CONSOLIDADO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "CONHECIMENTO CONSOLIDADO"
)

print(
    "========================================"
)


for campo, valor in conhecimento.items():

    print(
        "\n",
        campo,
        "=",
        valor
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