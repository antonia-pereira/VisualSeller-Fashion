from aura.vision_ai import analisar_imagem

from aura.evidence import (
    FonteEvidencia,
    NivelConfianca,
)

from aura.processor import (
    processar_informacao,
    mostrar_resultado_processamento,
)

from aura.state import (
    EstadoProduto,
    mostrar_estado_produto,
)

from aura_schemas.body import (
    FichaBody,
)


# ============================================================
# VISUALSELLER FASHION
# TESTE — FOTO → PROCESSOR → STATE → FICHA
# ============================================================


# ============================================================
# 1. IMAGEM REAL
# ============================================================

CAMINHO_IMAGEM = (
    "imagens/body_frente.jpg.jpeg"
)


# ============================================================
# 2. CRIAR FICHA INICIAL
# ============================================================

ficha = FichaBody()


# ============================================================
# 3. CRIAR MEMÓRIA DO PRODUTO
# ============================================================

estado = EstadoProduto(
    ficha=ficha
)


# ============================================================
# 4. CABEÇALHO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "VISÃO → PROCESSOR → STATE → FICHA"
)

print(
    "========================================"
)


# ============================================================
# 5. MOSTRAR FICHA ANTES
# ============================================================

print(
    "\nFICHA ANTES DA ANÁLISE:\n"
)

print(
    estado.ficha.model_dump_json(
        indent=2
    )
)


# ============================================================
# 6. ANALISAR FOTO REAL
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "AURA ESTÁ ANALISANDO A FOTO..."
)

print(
    "========================================"
)


resultado_visao = analisar_imagem(
    CAMINHO_IMAGEM
)


tipo_imagem = resultado_visao.get(
    "tipo_imagem"
)


evidencias_visuais = resultado_visao.get(
    "evidencias",
    [],
)


print(
    "\nTIPO DE IMAGEM:",
    tipo_imagem
)


print(
    "EVIDÊNCIAS ENCONTRADAS:",
    len(
        evidencias_visuais
    )
)


# ============================================================
# 7. PROCESSAR CADA EVIDÊNCIA
# ============================================================

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

    descricao = item.get(
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
            "CAMPO:",
            campo
        )

        print(
            "MOTIVO: confiança inválida."
        )

        continue


    # --------------------------------------------------------
    # ENVIAR AO PROCESSOR OFICIAL
    # --------------------------------------------------------

    resultado = processar_informacao(
        ficha=estado.ficha,
        campo=campo,
        valor=valor,
        fonte=FonteEvidencia.FOTOGRAFIA,
        descricao=descricao,
        confianca=confianca,
    )


    # --------------------------------------------------------
    # REGISTRAR NA MEMÓRIA
    # --------------------------------------------------------

    estado.registrar_resultado(
        resultado
    )


    # --------------------------------------------------------
    # MOSTRAR RESULTADO
    # --------------------------------------------------------

    mostrar_resultado_processamento(
        resultado
    )


# ============================================================
# 8. MOSTRAR MEMÓRIA DA AURA
# ============================================================

mostrar_estado_produto(
    estado
)


# ============================================================
# 9. MOSTRAR FICHA DEPOIS
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "FICHA DEPOIS DA ANÁLISE"
)

print(
    "========================================"
)


print(
    "\n"
)

print(
    estado.ficha.model_dump_json(
        indent=2
    )
)


# ============================================================
# 10. MOSTRAR INFORMAÇÕES ACEITAS
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "INFORMAÇÕES ACEITAS PELA AURA"
)

print(
    "========================================"
)


informacoes_aceitas = (
    estado.obter_informacoes_aceitas()
)


if informacoes_aceitas:

    for informacao in informacoes_aceitas:

        print(
            "\nCAMPO:",
            informacao.get(
                "campo"
            )
        )

        print(
            "VALOR:",
            informacao.get(
                "valor"
            )
        )

        print(
            "CONFIANÇA:",
            informacao.get(
                "confianca"
            )
        )

else:

    print(
        "\nNenhuma informação aceita."
    )


# ============================================================
# 11. MOSTRAR CONFIRMAÇÕES PENDENTES
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

    for informacao in confirmacoes:

        print(
            "\nCAMPO:",
            informacao.get(
                "campo"
            )
        )

        print(
            "VALOR PROPOSTO:",
            informacao.get(
                "valor"
            )
        )

        print(
            "CONFIANÇA:",
            informacao.get(
                "confianca"
            )
        )

else:

    print(
        "\nNenhuma confirmação pendente."
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