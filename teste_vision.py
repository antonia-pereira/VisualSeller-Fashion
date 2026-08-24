from aura.vision import (
    criar_evidencia_visual,
    classificar_tipo_imagem,
)


print("=" * 60)
print("TESTE DA CAMADA DE VISÃO DA AURA")
print("=" * 60)


# ============================================================
# TESTE 1 — FOTO FRONTAL
# ============================================================

print("\nTESTE 1 — FOTO FRONTAL")

tipo_imagem = classificar_tipo_imagem(
    "frente"
)

evidencia_1 = criar_evidencia_visual(
    campo="decote_frente",
    valor="V",
    confianca="alta",
    origem=tipo_imagem,
    observacao=(
        "O formato em V está claramente "
        "visível na fotografia frontal."
    ),
)

print(evidencia_1)


# ============================================================
# TESTE 2 — MANGA
# ============================================================

print("\nTESTE 2 — MANGA")

evidencia_2 = criar_evidencia_visual(
    campo="manga",
    valor="longa",
    confianca="alta",
    origem="frente",
    observacao=(
        "As mangas aparecem completas "
        "na imagem da peça."
    ),
)

print(evidencia_2)


# ============================================================
# TESTE 3 — FORRO INCERTO
# ============================================================

print("\nTESTE 3 — POSSÍVEL FORRO")

evidencia_3 = criar_evidencia_visual(
    campo="possui_forro",
    valor=True,
    confianca="baixa",
    origem="detalhe",
    observacao=(
        "A imagem sugere uma camada interna, "
        "mas não permite confirmação visual segura."
    ),
)

print(evidencia_3)


# ============================================================
# TESTE 4 — FOTO DE ETIQUETA
# ============================================================

print("\nTESTE 4 — FOTO DE ETIQUETA")

tipo_imagem = classificar_tipo_imagem(
    "etiqueta"
)

evidencia_4 = criar_evidencia_visual(
    campo="composicao_principal",
    valor="85% poliamida + 15% elastano",
    confianca="alta",
    origem=tipo_imagem,
    observacao=(
        "Composição legível na fotografia "
        "da etiqueta interna."
    ),
)

print(evidencia_4)


# ============================================================
# TESTE 5 — TIPO DE IMAGEM DESCONHECIDO
# ============================================================

print("\nTESTE 5 — TIPO DESCONHECIDO")

tipo_imagem = classificar_tipo_imagem(
    "foto qualquer"
)

print(
    "TIPO NORMALIZADO:",
    tipo_imagem
)


# ============================================================
# TESTE 6 — PROTEÇÃO DE CONFIANÇA
# ============================================================

print("\nTESTE 6 — CONFIANÇA INVÁLIDA")

try:

    criar_evidencia_visual(
        campo="possui_bojo",
        valor=True,
        confianca="certeza_absoluta",
        origem="frente",
    )

except ValueError as erro:

    print(
        "ERRO CONTROLADO:",
        erro
    )


# ============================================================
# FIM
# ============================================================

print("\n" + "=" * 60)
print("FIM DO TESTE")
print("=" * 60)