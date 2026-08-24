# ============================================================
# VISUALSELLER FASHION
# TESTE — GENERATOR + IMAGE PROVIDER
# ============================================================

from aura.product_image_generator import (
    gerar_imagem_com_referencias,
    formatar_resultado_geracao,
)


# ============================================================
# 1. CONFIGURAÇÃO
# ============================================================

PROMPT = """
Create a clean commercial product photograph
based on the provided reference image.

Preserve the original garment design,
shape, color, materials and visible details.

Show the garment clearly against a simple
neutral studio background.

Do not add text, logos, accessories or
new design elements.
""".strip()


REFERENCIAS = [
    "imagens/body_frente.jpg.jpeg",
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
    "TESTE — GENERATOR + PROVIDER"
)

print(
    "============================================"
)


# ============================================================
# 3. EXECUTAR
# ============================================================

resultado = gerar_imagem_com_referencias(

    prompt=
        PROMPT,

    referencias=
        REFERENCIAS,

    caminho_saida=
        "outputs/teste_provider.png",

    tamanho=
        "1024x1024",

    qualidade=
        "medium",

    provider=
        "openai",
)


# ============================================================
# 4. MOSTRAR RESULTADO
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
# 5. VERIFICAÇÃO
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


if resultado[
    "sucesso"
]:

    print(
        "A geração foi concluída pelo provider."
    )

else:

    detalhes = (
        resultado.get(
            "detalhes"
        )
        or {}
    )

    if detalhes.get(
        "bloqueio_seguranca"
    ):

        print(
            "O bloqueio de segurança foi capturado "
            "sem derrubar a aplicação."
        )

    else:

        print(
            "Houve uma falha de geração "
            "que não foi classificada "
            "como bloqueio de segurança."
        )


# ============================================================
# 6. FIM
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