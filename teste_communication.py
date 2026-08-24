from aura.communication import (
    gerar_pergunta,
    gerar_confirmacao,
    gerar_mensagem_aura,
)


# ============================================================
# TESTE DA CAMADA DE COMUNICAÇÃO DA AURA
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — COMUNICAÇÃO DA AURA"
)

print(
    "========================================"
)


# ============================================================
# TESTE 1
# BUSCAR INFORMAÇÃO
# ============================================================

print(
    "\n"
    "TESTE 1 — BUSCAR INFORMAÇÃO"
)

decisao_1 = {
    "acao": "BUSCAR_INFORMACAO",
    "campo": "possui_bojo",
    "valor_proposto": None,
}

mensagem_1 = gerar_mensagem_aura(
    decisao_1
)

print(
    "INTERNO:"
)

print(
    decisao_1
)

print(
    "\nAURA:"
)

print(
    mensagem_1
)


# ============================================================
# TESTE 2
# OUTRO CAMPO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "TESTE 2 — NOVA INFORMAÇÃO"
)

decisao_2 = {
    "acao": "BUSCAR_INFORMACAO",
    "campo": "possui_forro",
    "valor_proposto": None,
}

mensagem_2 = gerar_mensagem_aura(
    decisao_2
)

print(
    "INTERNO:"
)

print(
    decisao_2
)

print(
    "\nAURA:"
)

print(
    mensagem_2
)


# ============================================================
# TESTE 3
# PEDIR CONFIRMAÇÃO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "TESTE 3 — PEDIR CONFIRMAÇÃO"
)

decisao_3 = {
    "acao": "PEDIR_CONFIRMACAO",
    "campo": "possui_forro",
    "valor_proposto": True,
}

mensagem_3 = gerar_mensagem_aura(
    decisao_3
)

print(
    "INTERNO:"
)

print(
    decisao_3
)

print(
    "\nAURA:"
)

print(
    mensagem_3
)


# ============================================================
# TESTE 4
# ENCERRAR FICHA
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "TESTE 4 — ENCERRAR FICHA"
)

decisao_4 = {
    "acao": "ENCERRAR_FICHA",
    "campo": None,
    "valor_proposto": None,
}

mensagem_4 = gerar_mensagem_aura(
    decisao_4
)

print(
    "INTERNO:"
)

print(
    decisao_4
)

print(
    "\nAURA:"
)

print(
    mensagem_4
)


# ============================================================
# TESTE 5
# PERGUNTA DIRETA POR CAMPO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "TESTE 5 — PERGUNTAS DA FICHA"
)

campos = [
    "possui_bojo",
    "possui_forro",
    "acabamento_mangas",
    "grade",
    "composicao_principal",
    "busto_cm",
    "cintura_cm",
    "quadril_cm",
    "comprimento_cm",
]

for campo in campos:

    pergunta = gerar_pergunta(
        campo
    )

    print(
        "\nCAMPO:",
        campo
    )

    print(
        "AURA:",
        pergunta
    )


# ============================================================
# TESTE 6
# CONFIRMAÇÃO DIRETA
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "TESTE 6 — CONFIRMAÇÃO DIRETA"
)

confirmacao = gerar_confirmacao(
    campo="possui_bojo",
    valor_proposto=False,
)

print(
    "AURA:",
    confirmacao
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