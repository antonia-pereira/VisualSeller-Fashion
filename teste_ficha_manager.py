from aura.vision_product import analisar_produto

from aura.consolidator import (
    agrupar_evidencias_por_campo,
    gerar_conhecimento_consolidado,
)

from aura.ficha_manager import (
    aplicar_conhecimento_na_ficha,
    mostrar_ficha,
    mostrar_resultado_preenchimento,
)

from aura_schemas.body import FichaBody


# ============================================================
# VISUALSELLER FASHION
# TESTE — PREENCHIMENTO AUTOMÁTICO DA FICHA
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
# 2. INÍCIO
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


# ============================================================
# 3. CRIAR FICHA VAZIA
# ============================================================

ficha = FichaBody()


# ============================================================
# 4. AURA ANALISA AS IMAGENS
# ============================================================

resultado_visao = analisar_produto(
    imagens
)


print(
    "\n"
    "IMAGENS ANALISADAS:",
    resultado_visao[
        "quantidade_imagens"
    ]
)

print(
    "EVIDÊNCIAS ENCONTRADAS:",
    resultado_visao[
        "quantidade_evidencias"
    ]
)


# ============================================================
# 5. AGRUPAR AS EVIDÊNCIAS
# ============================================================

grupos = agrupar_evidencias_por_campo(
    resultado_visao[
        "evidencias"
    ]
)


# ============================================================
# 6. GERAR CONHECIMENTO CONSOLIDADO
# ============================================================

conhecimento = gerar_conhecimento_consolidado(
    grupos
)


# ============================================================
# 7. APLICAR CONHECIMENTO À FICHA
# ============================================================

resultado_preenchimento = aplicar_conhecimento_na_ficha(
    ficha=ficha,
    conhecimento=conhecimento,
)


# ============================================================
# 8. MOSTRAR RESULTADO
# ============================================================

mostrar_resultado_preenchimento(
    resultado_preenchimento
)


# ============================================================
# 9. MOSTRAR A FICHA PREENCHIDA
# ============================================================

mostrar_ficha(
    ficha
)


# ============================================================
# 10. FIM
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