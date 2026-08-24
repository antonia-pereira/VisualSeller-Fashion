from pprint import pprint

from aura.vision_ai import analisar_imagem


# ============================================================
# VISUALSELLER FASHION
# TESTE DE VISÃO REAL DA AURA
# ============================================================


CAMINHO_IMAGEM = (
    "imagens/body_frente.jpg.jpeg"
)


print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — VISÃO REAL DA AURA"
)

print(
    "========================================"
)


# ============================================================
# ANALISAR FOTO REAL
# ============================================================

try:

    resultado = analisar_imagem(
        CAMINHO_IMAGEM
    )

    print(
        "\nANÁLISE CONCLUÍDA.\n"
    )

    pprint(
        resultado,
        sort_dicts=False,
    )


# ============================================================
# TRATAMENTO DE ERRO
# ============================================================

except FileNotFoundError as erro:

    print(
        "\nERRO:"
    )

    print(
        erro
    )


except Exception as erro:

    print(
        "\nERRO DURANTE A ANÁLISE:"
    )

    print(
        type(erro).__name__
    )

    print(
        erro
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