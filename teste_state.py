from aura_schemas.body import FichaBody

from aura.evidence import FonteEvidencia

from aura.processor import (
    processar_informacao,
    mostrar_resultado_processamento,
)

from aura.state import (
    EstadoProduto,
    mostrar_estado_produto,
)


# ============================================================
# TESTE DO ESTADO / MEMÓRIA DE TRABALHO DA AURA
# PRODUTO 001 — BODY DUBAI
# ============================================================


# ============================================================
# 1. CRIAR UMA FICHA INICIAL VAZIA
# ============================================================

body_dubai = FichaBody(
    marca="Linda Sedução",
    nome_modelo="Body Dubai",
    referencia="277",
    codigo_barras="7002770010015",
)


# ============================================================
# 2. CRIAR O ESTADO DO PRODUTO
# ============================================================

estado = EstadoProduto(
    ficha=body_dubai,
)


# ============================================================
# INÍCIO DO TESTE
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE DE MEMÓRIA DA AURA"
)

print(
    "PRODUTO 001 — BODY DUBAI"
)

print(
    "========================================"
)


# ============================================================
# INFORMAÇÃO 1
# COMPOSIÇÃO — ETIQUETA
# ============================================================

resultado_1 = processar_informacao(
    ficha=estado.ficha,

    campo="composicao_principal",

    valor="85% poliamida + 15% elastano",

    fonte=FonteEvidencia.ETIQUETA,

    descricao=(
        "Composição principal confirmada "
        "pela etiqueta interna da peça."
    ),
)

estado.registrar_resultado(
    resultado_1
)

mostrar_resultado_processamento(
    resultado_1
)


# ============================================================
# INFORMAÇÃO 2
# BOJO — VERIFICAÇÃO FÍSICA
# ============================================================

resultado_2 = processar_informacao(
    ficha=estado.ficha,

    campo="possui_bojo",

    valor=False,

    fonte=FonteEvidencia.VERIFICACAO_FISICA,

    descricao=(
        "Ausência de bojo confirmada "
        "fisicamente na peça."
    ),
)

estado.registrar_resultado(
    resultado_2
)

mostrar_resultado_processamento(
    resultado_2
)


# ============================================================
# INFORMAÇÃO 3
# DECOTE — FOTOGRAFIA
# ============================================================

resultado_3 = processar_informacao(
    ficha=estado.ficha,

    campo="decote_frente",

    valor="V",

    fonte=FonteEvidencia.FOTOGRAFIA,

    descricao=(
        "Decote em V identificado "
        "visualmente na fotografia frontal."
    ),
)

estado.registrar_resultado(
    resultado_3
)

mostrar_resultado_processamento(
    resultado_3
)


# ============================================================
# INFORMAÇÃO 4
# FORRO — HIPÓTESE DA AURA
#
# A AURA acha que não existe forro.
# Como é apenas inferência, deve ficar
# aguardando confirmação.
# ============================================================

resultado_4 = processar_informacao(
    ficha=estado.ficha,

    campo="possui_forro",

    valor=False,

    fonte=FonteEvidencia.INFERENCIA_AURA,

    descricao=(
        "Hipótese criada pela AURA "
        "a partir da aparência da peça."
    ),
)

estado.registrar_resultado(
    resultado_4
)

mostrar_resultado_processamento(
    resultado_4
)


# ============================================================
# INFORMAÇÃO 5
# CAMPO QUE NÃO EXISTE
#
# Deve ser recusado.
# ============================================================

resultado_5 = processar_informacao(
    ficha=estado.ficha,

    campo="produto_maravilhoso",

    valor=True,

    fonte=FonteEvidencia.INFORMACAO_FORNECIDA,

    descricao=(
        "Teste de proteção contra "
        "campos fora da ficha técnica."
    ),
)

estado.registrar_resultado(
    resultado_5
)

mostrar_resultado_processamento(
    resultado_5
)


# ============================================================
# MOSTRAR O ESTADO ATUAL
# ============================================================

mostrar_estado_produto(
    estado
)


# ============================================================
# MOSTRAR O QUE A AURA JÁ SABE
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "O QUE A AURA SABE ATÉ AGORA"
)

print(
    "========================================"
)

print(
    "\n"
    "MARCA:",
    estado.ficha.marca,
)

print(
    "MODELO:",
    estado.ficha.nome_modelo,
)

print(
    "COMPOSIÇÃO:",
    estado.ficha.composicao_principal,
)

print(
    "POSSUI BOJO:",
    estado.ficha.possui_bojo,
)

print(
    "DECOTE FRONTAL:",
    estado.ficha.decote_frente,
)

print(
    "POSSUI FORRO:",
    estado.ficha.possui_forro,
)


# ============================================================
# MOSTRAR CONFIRMAÇÕES PENDENTES
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "AGUARDANDO CONFIRMAÇÃO"
)

print(
    "========================================"
)

confirmacoes = (
    estado.obter_confirmacoes_pendentes()
)

if confirmacoes:

    for item in confirmacoes:

        print(
            "\nCAMPO:",
            item["campo"],
        )

        print(
            "VALOR PROPOSTO:",
            item["valor"],
        )

        print(
            "FONTE:",
            item["fonte"],
        )

        print(
            "CONFIANÇA:",
            item["confianca"],
        )

else:

    print(
        "Nenhuma confirmação pendente."
    )


# ============================================================
# MOSTRAR INFORMAÇÕES RECUSADAS
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "INFORMAÇÕES RECUSADAS"
)

print(
    "========================================"
)

recusadas = (
    estado.obter_informacoes_recusadas()
)

if recusadas:

    for item in recusadas:

        print(
            "\nCAMPO:",
            item["campo"],
        )

        print(
            "AÇÃO:",
            item["acao"],
        )

else:

    print(
        "Nenhuma informação recusada."
    )


# ============================================================
# RESULTADO FINAL
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