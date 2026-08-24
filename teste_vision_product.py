from aura.vision_product import analisar_produto


# ============================================================
# TESTE — VISÃO COMPLETA DO PRODUTO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "TESTE — VISÃO COMPLETA DO PRODUTO"
)

print(
    "========================================"
)


# ============================================================
# IMAGENS DO MESMO PRODUTO
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
# ANALISAR O PRODUTO
# ============================================================

resultado = analisar_produto(
    imagens
)


# ============================================================
# RESUMO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "RESUMO DA ANÁLISE"
)

print(
    "========================================"
)

print(
    "QUANTIDADE DE IMAGENS:",
    resultado["quantidade_imagens"],
)

print(
    "QUANTIDADE DE EVIDÊNCIAS:",
    resultado["quantidade_evidencias"],
)


# ============================================================
# EVIDÊNCIAS ENCONTRADAS
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "EVIDÊNCIAS ENCONTRADAS"
)

print(
    "========================================"
)

for evidencia in resultado["evidencias"]:

    print(
        "\nCAMPO:",
        evidencia.get("campo"),
    )

    print(
        "VALOR:",
        evidencia.get("valor"),
    )

    print(
        "CONFIANÇA:",
        evidencia.get("confianca"),
    )

    print(
        "IMAGEM:",
        evidencia.get("tipo_imagem"),
    )


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