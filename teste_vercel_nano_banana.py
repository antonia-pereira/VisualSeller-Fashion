# ============================================================
# VISUALSELLER FASHION
# TESTE MÍNIMO — VERCEL + NANO BANANA 2
# ============================================================

from aura.product_image_generator import (
    gerar_imagem_com_referencias,
    formatar_resultado_geracao,
)


# ============================================================
# 1. PROMPT MÍNIMO
# ============================================================

PROMPT = """
Create a clean commercial fashion product image
based on the provided reference.

Preserve the garment's real design, shape, color,
materials, transparency, lace, sleeves, neckline,
cuffs and proportions.

Place the garment against a simple neutral
studio background.

Do not add text, logos, accessories or new
design elements.
""".strip()


# ============================================================
# 2. UMA ÚNICA REFERÊNCIA
# ============================================================

REFERENCIAS = [
    "imagens/body_frente.jpg.jpeg",
]


# ============================================================
# 3. CABEÇALHO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — VERCEL + NANO BANANA 2"
)

print(
    "============================================"
)


# ============================================================
# 4. GERAR
# ============================================================

resultado = gerar_imagem_com_referencias(

    prompt=
        PROMPT,

    referencias=
        REFERENCIAS,

    caminho_saida=
        "outputs/teste_nano_banana.png",

    tamanho=
        "1024x1024",

    qualidade=
        "medium",

    provider=
        "vercel",
)


# ============================================================
# 5. RESULTADO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RESULTADO"
)

print(
    "============================================"
)

print(
    formatar_resultado_geracao(
        resultado
    )
)


# ============================================================
# 6. DETALHES DO ERRO, SE HOUVER
# ============================================================

if not resultado.get(
    "sucesso"
):

    print(
        "\n"
        "============================================"
    )

    print(
        "DETALHES"
    )

    print(
        "============================================"
    )

    print(
        resultado.get(
            "erro"
        )
    )

    print()

    print(
        resultado.get(
            "detalhes"
        )
    )


# ============================================================
# 7. FIM
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