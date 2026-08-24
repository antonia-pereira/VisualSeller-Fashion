from aura.vision_product import analisar_produto

from aura.consolidator import (
    agrupar_evidencias_por_campo,
    gerar_conhecimento_consolidado,
)

from aura.ficha_manager import (
    aplicar_conhecimento_na_ficha,
)

from aura.gap_analyzer import (
    mostrar_analise_lacunas,
)

from aura_schemas.body import FichaBody


# ============================================================
# VISUALSELLER FASHION
# TESTE — ANÁLISE DE LACUNAS
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
# 3. CRIAR FICHA
# ============================================================

ficha = FichaBody()


# ============================================================
# 4. ANALISAR IMAGENS
# ============================================================

resultado_visao = analisar_produto(
    imagens
)


# ============================================================
# 5. AGRUPAR EVIDÊNCIAS
# ============================================================

grupos = agrupar_evidencias_por_campo(
    resultado_visao[
        "evidencias"
    ]
)


# ============================================================
# 6. CONSOLIDAR CONHECIMENTO
# ============================================================

conhecimento = gerar_conhecimento_consolidado(
    grupos
)


# ============================================================
# 7. PREENCHER FICHA
# ============================================================

aplicar_conhecimento_na_ficha(
    ficha=ficha,
    conhecimento=conhecimento,
)


# ============================================================
# 8. ANALISAR O QUE AINDA FALTA
# ============================================================

mostrar_analise_lacunas(
    ficha
)


# ============================================================
# 9. FIM
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