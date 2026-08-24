from typing import Any

from aura.evidence import (
    FonteEvidencia,
    NivelConfianca,
    criar_evidencia,
    aura_pode_aceitar,
)

from aura_schemas.body import FichaBody


# ============================================================
# RESULTADO DO PROCESSAMENTO
# ============================================================

def processar_informacao(
    ficha: FichaBody,
    campo: str,
    valor: Any,
    fonte: FonteEvidencia,
    descricao: str | None = None,
    confianca: NivelConfianca | None = None,
):
    """
    Recebe uma informação sobre o produto,
    cria sua evidência e decide se a AURA
    pode aceitar essa informação na ficha.

    Quando uma confiança explícita é fornecida,
    ela é preservada.

    Quando não é fornecida, a confiança padrão
    da fonte é utilizada.
    """

    # --------------------------------------------------------
    # 1. CRIAR A EVIDÊNCIA
    # --------------------------------------------------------

    evidencia = criar_evidencia(
        campo=campo,
        valor=valor,
        fonte=fonte,
        descricao=descricao,
        confianca=confianca,
    )

    # --------------------------------------------------------
    # 2. VERIFICAR SE O CAMPO EXISTE NA FICHA
    # --------------------------------------------------------

    if campo not in ficha.model_fields:

        return {
            "aceita": False,
            "campo": campo,
            "valor": valor,
            "fonte": evidencia.fonte.value,
            "confianca": evidencia.confianca.value,
            "acao": "CAMPO_NAO_EXISTE_NA_FICHA",
        }

    # --------------------------------------------------------
    # 3. VERIFICAR SE A EVIDÊNCIA PODE SER ACEITA
    # --------------------------------------------------------

    if not aura_pode_aceitar(
        evidencia
    ):

        return {
            "aceita": False,
            "campo": campo,
            "valor": valor,
            "fonte": evidencia.fonte.value,
            "confianca": evidencia.confianca.value,
            "acao": "PRECISA_CONFIRMACAO",
        }

    # --------------------------------------------------------
    # 4. CAMPOS DO TIPO LISTA
    # --------------------------------------------------------

    valor_atual = getattr(
        ficha,
        campo,
    )

    if isinstance(
        valor_atual,
        list,
    ):

        if isinstance(
            valor,
            list,
        ):

            for item in valor:

                if item not in valor_atual:

                    valor_atual.append(
                        item
                    )

        else:

            if valor not in valor_atual:

                valor_atual.append(
                    valor
                )

    # --------------------------------------------------------
    # 5. CAMPOS SIMPLES
    # --------------------------------------------------------

    else:

        setattr(
            ficha,
            campo,
            valor,
        )

    # --------------------------------------------------------
    # 6. RETORNAR RESULTADO
    # --------------------------------------------------------

    return {
        "aceita": True,
        "campo": campo,
        "valor": valor,
        "fonte": evidencia.fonte.value,
        "confianca": evidencia.confianca.value,
        "acao": "INFORMACAO_REGISTRADA",
    }


# ============================================================
# FUNÇÃO PARA EXIBIR O RESULTADO
# ============================================================

def mostrar_resultado_processamento(
    resultado: dict,
):
    """
    Exibe no terminal o resultado de uma decisão da AURA.
    """

    print(
        "\n----------------------------------------"
    )

    print(
        "CAMPO:",
        resultado["campo"],
    )

    print(
        "VALOR:",
        resultado["valor"],
    )

    print(
        "FONTE:",
        resultado["fonte"],
    )

    print(
        "CONFIANÇA:",
        resultado["confianca"],
    )

    print(
        "ACEITA:",
        resultado["aceita"],
    )

    print(
        "AÇÃO:",
        resultado["acao"],
    )