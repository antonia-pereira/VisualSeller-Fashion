from aura.vision_ai import analisar_imagem

from aura.evidence import (
    criar_evidencia,
    FonteEvidencia,
    NivelConfianca,
    aura_pode_aceitar,
)


# ============================================================
# VISUALSELLER FASHION
# TESTE — VISÃO REAL + EVIDÊNCIAS
# ============================================================


# ============================================================
# 1. IMAGEM REAL DO PRODUTO
# ============================================================

CAMINHO_IMAGEM = (
    "imagens/body_frente.jpg.jpeg"
)


# ============================================================
# 2. CABEÇALHO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "AURA — VISÃO + EVIDÊNCIAS"
)

print(
    "========================================"
)


# ============================================================
# 3. ANALISAR FOTO REAL
# ============================================================

print(
    "\nAnalisando imagem..."
)

resultado_visao = analisar_imagem(
    CAMINHO_IMAGEM
)


print(
    "\nAnálise visual concluída."
)


# ============================================================
# 4. MOSTRAR TIPO DA IMAGEM
# ============================================================

tipo_imagem = resultado_visao.get(
    "tipo_imagem"
)


print(
    "\nTIPO DE IMAGEM:",
    tipo_imagem
)


# ============================================================
# 5. PEGAR EVIDÊNCIAS DA VISÃO
# ============================================================

evidencias_visuais = resultado_visao.get(
    "evidencias",
    [],
)


# ============================================================
# 6. CONVERTER EM EVIDÊNCIAS OFICIAIS DA AURA
# ============================================================

evidencias_aura = []


for item in evidencias_visuais:

    campo = item.get(
        "campo"
    )

    valor = item.get(
        "valor"
    )

    confianca_texto = item.get(
        "confianca"
    )

    observacao = item.get(
        "observacao"
    )


    # --------------------------------------------------------
    # VALIDAR CONFIANÇA
    # --------------------------------------------------------

    try:

        confianca = NivelConfianca(
            confianca_texto
        )

    except ValueError:

        print(
            "\nEVIDÊNCIA IGNORADA:"
        )

        print(
            "Campo:",
            campo
        )

        print(
            "Motivo: nível de confiança inválido."
        )

        continue


    # --------------------------------------------------------
    # CRIAR EVIDÊNCIA OFICIAL
    # --------------------------------------------------------

    evidencia = criar_evidencia(
        campo=campo,
        valor=valor,
        fonte=FonteEvidencia.FOTOGRAFIA,
        descricao=observacao,
        confianca=confianca,
    )


    evidencias_aura.append(
        evidencia
    )


# ============================================================
# 7. MOSTRAR EVIDÊNCIAS
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "EVIDÊNCIAS CRIADAS"
)

print(
    "========================================"
)


for evidencia in evidencias_aura:

    pode_aceitar = aura_pode_aceitar(
        evidencia
    )


    print(
        "\nCAMPO:",
        evidencia.campo
    )

    print(
        "VALOR:",
        evidencia.valor
    )

    print(
        "FONTE:",
        evidencia.fonte.value
    )

    print(
        "CONFIANÇA:",
        evidencia.confianca.value
    )

    print(
        "AURA PODE ACEITAR:",
        pode_aceitar
    )


    if evidencia.descricao:

        print(
            "OBSERVAÇÃO:",
            evidencia.descricao
        )


# ============================================================
# 8. SEPARAR ACEITAS E PENDENTES
# ============================================================

aceitas = []

precisam_confirmacao = []


for evidencia in evidencias_aura:

    if aura_pode_aceitar(
        evidencia
    ):

        aceitas.append(
            evidencia
        )

    else:

        precisam_confirmacao.append(
            evidencia
        )


# ============================================================
# 9. RESUMO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "RESUMO DA AURA"
)

print(
    "========================================"
)


print(
    "\nEVIDÊNCIAS RECEBIDAS:",
    len(
        evidencias_aura
    )
)


print(
    "ACEITAS AUTOMATICAMENTE:",
    len(
        aceitas
    )
)


print(
    "PRECISAM DE CONFIRMAÇÃO:",
    len(
        precisam_confirmacao
    )
)


# ============================================================
# 10. MOSTRAR AS QUE PRECISAM DE CONFIRMAÇÃO
# ============================================================

if precisam_confirmacao:

    print(
        "\n"
        "========================================"
    )

    print(
        "CONFIRMAÇÕES NECESSÁRIAS"
    )

    print(
        "========================================"
    )


    for evidencia in precisam_confirmacao:

        print(
            "\nCAMPO:",
            evidencia.campo
        )

        print(
            "VALOR PROPOSTO:",
            evidencia.valor
        )

        print(
            "CONFIANÇA:",
            evidencia.confianca.value
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