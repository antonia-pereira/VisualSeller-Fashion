from aura.evidence import (
    FonteEvidencia,
    criar_evidencia,
    evidencia_forte,
    aura_pode_aceitar,
)


# ============================================================
# TESTE DO SISTEMA DE EVIDÊNCIAS DA AURA
# PRODUTO 001 — BODY DUBAI
# ============================================================


# ============================================================
# EVIDÊNCIA 1
# COMPOSIÇÃO CONFIRMADA PELA ETIQUETA
# ============================================================

evidencia_composicao = criar_evidencia(
    campo="composicao_principal",
    valor="85% poliamida + 15% elastano",
    fonte=FonteEvidencia.ETIQUETA,
    descricao=(
        "Composição confirmada diretamente "
        "pela etiqueta da peça."
    ),
)


# ============================================================
# EVIDÊNCIA 2
# BOJO VERIFICADO FISICAMENTE
# ============================================================

evidencia_bojo = criar_evidencia(
    campo="possui_bojo",
    valor=False,
    fonte=FonteEvidencia.VERIFICACAO_FISICA,
    descricao=(
        "Peça verificada fisicamente. "
        "Não possui bojo."
    ),
)


# ============================================================
# EVIDÊNCIA 3
# DECOTE IDENTIFICADO PELA FOTOGRAFIA
# ============================================================

evidencia_decote = criar_evidencia(
    campo="decote_frente",
    valor="V",
    fonte=FonteEvidencia.FOTOGRAFIA,
    descricao=(
        "Formato do decote identificado "
        "visualmente nas fotografias."
    ),
)


# ============================================================
# EVIDÊNCIA 4
# HIPÓTESE CRIADA PELA PRÓPRIA AURA
# ============================================================

evidencia_inferencia = criar_evidencia(
    campo="estilo",
    valor="sensual",
    fonte=FonteEvidencia.INFERENCIA_AURA,
    descricao=(
        "Hipótese criada pela AURA "
        "a partir das características visuais."
    ),
)


# ============================================================
# LISTA DE EVIDÊNCIAS
# ============================================================

evidencias = [
    evidencia_composicao,
    evidencia_bojo,
    evidencia_decote,
    evidencia_inferencia,
]


# ============================================================
# MOSTRAR RESULTADOS
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "AURA — SISTEMA DE EVIDÊNCIAS"
)

print(
    "PRODUTO 001 — BODY DUBAI"
)

print(
    "========================================"
)


for evidencia in evidencias:

    print(
        "\n----------------------------------------"
    )

    print(
        "CAMPO:",
        evidencia.campo,
    )

    print(
        "VALOR:",
        evidencia.valor,
    )

    print(
        "FONTE:",
        evidencia.fonte.value,
    )

    print(
        "CONFIANÇA:",
        evidencia.confianca.value,
    )

    print(
        "DESCRIÇÃO:",
        evidencia.descricao,
    )

    print(
        "EVIDÊNCIA FORTE:",
        evidencia_forte(
            evidencia
        ),
    )

    print(
        "AURA PODE ACEITAR:",
        aura_pode_aceitar(
            evidencia
        ),
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