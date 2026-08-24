from aura.vision_ai import analisar_imagem

from aura.evidence import (
    criar_evidencia,
    FonteEvidencia,
    NivelConfianca,
    aura_pode_aceitar,
)

from aura_schemas.body import (
    FichaBody,
)


# ============================================================
# VISUALSELLER FASHION
# TESTE — VISÃO REAL → EVIDÊNCIA → FICHA BODY
# ============================================================


# ============================================================
# 1. IMAGEM REAL
# ============================================================

CAMINHO_IMAGEM = (
    "imagens/body_frente.jpg.jpeg"
)


# ============================================================
# 2. CRIAR FICHA VAZIA
# ============================================================

ficha = FichaBody()


# ============================================================
# 3. CAMPOS DA FICHA
# ============================================================

CAMPOS_LISTA = {
    "cores_disponiveis",
    "tamanhos_disponiveis",
    "grade",
    "materiais_visuais",
    "instrucoes_conservacao",
    "observacoes",
}


# ============================================================
# 4. FUNÇÃO PARA APLICAR EVIDÊNCIA NA FICHA
# ============================================================

def aplicar_evidencia_na_ficha(
    ficha: FichaBody,
    evidencia,
):
    """
    Aplica uma evidência aceita à ficha técnica.

    Não cria campos novos.
    Só trabalha com campos já existentes
    no modelo FichaBody.
    """

    campo = evidencia.campo
    valor = evidencia.valor

    # --------------------------------------------------------
    # VERIFICAR SE O CAMPO EXISTE
    # --------------------------------------------------------

    if campo not in ficha.model_fields:

        return {
            "aplicada": False,
            "campo": campo,
            "motivo": "CAMPO_NAO_EXISTE_NA_FICHA",
        }

    # --------------------------------------------------------
    # CAMPOS DO TIPO LISTA
    # --------------------------------------------------------

    if campo in CAMPOS_LISTA:

        lista_atual = getattr(
            ficha,
            campo,
        )

        if isinstance(valor, list):

            for item in valor:

                if item not in lista_atual:

                    lista_atual.append(
                        item
                    )

        else:

            if valor not in lista_atual:

                lista_atual.append(
                    valor
                )

        return {
            "aplicada": True,
            "campo": campo,
            "valor": valor,
        }

    # --------------------------------------------------------
    # CAMPOS SIMPLES
    # --------------------------------------------------------

    setattr(
        ficha,
        campo,
        valor,
    )

    return {
        "aplicada": True,
        "campo": campo,
        "valor": valor,
    }


# ============================================================
# 5. CABEÇALHO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "VISÃO → EVIDÊNCIA → FICHA BODY"
)

print(
    "========================================"
)


# ============================================================
# 6. MOSTRAR FICHA ANTES
# ============================================================

print(
    "\nFICHA ANTES DA ANÁLISE:\n"
)

print(
    ficha.model_dump_json(
        indent=2
    )
)


# ============================================================
# 7. ANALISAR FOTO REAL
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "ANALISANDO FOTO..."
)

print(
    "========================================"
)


resultado_visao = analisar_imagem(
    CAMINHO_IMAGEM
)


evidencias_visuais = resultado_visao.get(
    "evidencias",
    [],
)


# ============================================================
# 8. CONVERTER E AVALIAR EVIDÊNCIAS
# ============================================================

evidencias_aceitas = []

evidencias_pendentes = []


for item in evidencias_visuais:

    campo = item.get(
        "campo"
    )

    valor = item.get(
        "valor"
    )

    observacao = item.get(
        "observacao"
    )

    confianca_texto = item.get(
        "confianca"
    )


    try:

        confianca = NivelConfianca(
            confianca_texto
        )

    except ValueError:

        print(
            "\nEVIDÊNCIA IGNORADA:"
        )

        print(
            campo
        )

        print(
            "Motivo: confiança inválida."
        )

        continue


    evidencia = criar_evidencia(
        campo=campo,
        valor=valor,
        fonte=FonteEvidencia.FOTOGRAFIA,
        descricao=observacao,
        confianca=confianca,
    )


    if aura_pode_aceitar(
        evidencia
    ):

        evidencias_aceitas.append(
            evidencia
        )

    else:

        evidencias_pendentes.append(
            evidencia
        )


# ============================================================
# 9. APLICAR EVIDÊNCIAS ACEITAS
# ============================================================

resultados_aplicacao = []


for evidencia in evidencias_aceitas:

    resultado = aplicar_evidencia_na_ficha(
        ficha,
        evidencia,
    )

    resultados_aplicacao.append(
        resultado
    )


# ============================================================
# 10. MOSTRAR O QUE FOI APLICADO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "EVIDÊNCIAS APLICADAS À FICHA"
)

print(
    "========================================"
)


for resultado in resultados_aplicacao:

    print(
        "\nCAMPO:",
        resultado.get(
            "campo"
        )
    )

    print(
        "APLICADA:",
        resultado.get(
            "aplicada"
        )
    )

    if resultado.get(
        "aplicada"
    ):

        print(
            "VALOR:",
            resultado.get(
                "valor"
            )
        )

    else:

        print(
            "MOTIVO:",
            resultado.get(
                "motivo"
            )
        )


# ============================================================
# 11. PENDÊNCIAS DE CONFIANÇA
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "EVIDÊNCIAS QUE PRECISAM DE CONFIRMAÇÃO"
)

print(
    "========================================"
)


if evidencias_pendentes:

    for evidencia in evidencias_pendentes:

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

else:

    print(
        "\nNenhuma evidência pendente."
    )


# ============================================================
# 12. MOSTRAR FICHA DEPOIS
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
    ficha.model_dump_json(
        indent=2
    )
)


# ============================================================
# 13. RESUMO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "RESUMO"
)

print(
    "========================================"
)


print(
    "\nEVIDÊNCIAS VISUAIS:",
    len(
        evidencias_visuais
    )
)


print(
    "ACEITAS:",
    len(
        evidencias_aceitas
    )
)


print(
    "PENDENTES:",
    len(
        evidencias_pendentes
    )
)


print(
    "APLICADAS À FICHA:",
    len(
        [
            resultado
            for resultado in resultados_aplicacao
            if resultado.get("aplicada")
        ]
    )
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