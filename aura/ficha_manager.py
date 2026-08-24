from typing import Any

from aura_schemas.body import FichaBody


# ============================================================
# VISUALSELLER FASHION
# AURA — GERENCIADOR DA FICHA TÉCNICA
# ============================================================


# ============================================================
# 1. CAMPOS BOOLEANOS
# ============================================================

CAMPOS_BOOLEANOS = {
    "possui_forro",
    "possui_bojo",
}


# ============================================================
# 2. VERIFICAR SE O CAMPO EXISTE NA FICHA
# ============================================================

def campo_existe_na_ficha(
    ficha: FichaBody,
    campo: str,
) -> bool:
    """
    Verifica se o campo produzido pela AURA
    existe realmente na FichaBody.
    """

    return (
        campo
        in ficha.__class__.model_fields
    )


# ============================================================
# 3. VERIFICAR SE O VALOR É UMA PENDÊNCIA
# ============================================================

def valor_e_pendencia(
    valor: Any,
) -> bool:
    """
    Detecta estruturas explicitamente marcadas
    como pendentes pelo consolidador.
    """

    if not isinstance(
        valor,
        dict,
    ):
        return False

    return (
        valor.get("status")
        == "PENDENTE"
    )


# ============================================================
# 4. INTERPRETAR BOOLEANO
# ============================================================

def interpretar_booleano(
    valor: Any,
):
    """
    Converte respostas conhecidas em bool.

    Retorna:
    - True
    - False
    - None quando não é possível determinar
    """

    if isinstance(
        valor,
        bool,
    ):
        return valor


    if not isinstance(
        valor,
        str,
    ):
        return None


    texto = (
        valor
        .strip()
        .lower()
    )


    # --------------------------------------------------------
    # POSITIVOS
    # --------------------------------------------------------

    positivos = {
        "sim",
        "true",
        "possui",
        "tem",
        "presente",
    }

    if texto in positivos:

        return True


    # --------------------------------------------------------
    # NEGATIVOS
    # --------------------------------------------------------

    negativos = {
        "não",
        "nao",
        "false",
        "não possui",
        "nao possui",
        "não tem",
        "nao tem",
        "ausente",
    }

    if texto in negativos:

        return False


    # --------------------------------------------------------
    # INCERTOS
    # --------------------------------------------------------

    termos_incertos = {
        "não identificável",
        "nao identificavel",
        "não identificavel",
        "nao identificável",
        "não é possível identificar",
        "nao e possivel identificar",
        "não foi possível identificar",
        "nao foi possivel identificar",
        "indeterminado",
        "indeterminável",
        "indeterminavel",
        "incerto",
        "não visível",
        "nao visivel",
        "não é visível",
        "nao e visivel",
    }

    if texto in termos_incertos:

        return None


    # --------------------------------------------------------
    # QUALQUER RESPOSTA DESCONHECIDA
    # --------------------------------------------------------

    return None


# ============================================================
# 5. NORMALIZAR VALOR PARA A FICHA
# ============================================================

def normalizar_valor_para_ficha(
    campo: str,
    valor: Any,
):
    """
    Ajusta valores consolidados antes
    de inseri-los na FichaBody.
    """


    # --------------------------------------------------------
    # BOOLEANOS
    # --------------------------------------------------------

    if campo in CAMPOS_BOOLEANOS:

        return interpretar_booleano(
            valor
        )


    # --------------------------------------------------------
    # MATERIAIS VISUAIS
    # --------------------------------------------------------

    if campo == "materiais_visuais":

        if isinstance(
            valor,
            list,
        ):
            return valor

        if isinstance(
            valor,
            str,
        ):
            return [
                valor
            ]


    # --------------------------------------------------------
    # INSTRUÇÕES DE CONSERVAÇÃO
    # --------------------------------------------------------

    if campo == "instrucoes_conservacao":

        if isinstance(
            valor,
            list,
        ):
            return valor

        if isinstance(
            valor,
            str,
        ):
            return [
                valor
            ]


    return valor


# ============================================================
# 6. APLICAR CONHECIMENTO À FICHA
# ============================================================

def aplicar_conhecimento_na_ficha(
    ficha: FichaBody,
    conhecimento: dict[str, Any],
) -> dict[str, Any]:
    """
    Aplica o conhecimento consolidado à ficha.

    Informações incertas não são registradas
    como se fossem fatos.
    """

    preenchidos = []

    ignorados = []

    pendentes = []

    erros = []


    for campo, valor in conhecimento.items():


        # ----------------------------------------------------
        # CAMPO NÃO EXISTE
        # ----------------------------------------------------

        if not campo_existe_na_ficha(
            ficha,
            campo,
        ):

            ignorados.append(
                {
                    "campo":
                        campo,

                    "valor":
                        valor,

                    "motivo":
                        "CAMPO_NAO_EXISTE_NA_FICHA",
                }
            )

            continue


        # ----------------------------------------------------
        # PENDÊNCIA EXPLÍCITA
        # ----------------------------------------------------

        if valor_e_pendencia(
            valor
        ):

            pendentes.append(
                {
                    "campo":
                        campo,

                    "valor":
                        valor,

                    "motivo":
                        "EVIDENCIAS_CONFLITANTES",
                }
            )

            continue


        # ----------------------------------------------------
        # NORMALIZAR
        # ----------------------------------------------------

        valor_normalizado = normalizar_valor_para_ficha(
            campo=campo,
            valor=valor,
        )


        # ----------------------------------------------------
        # BOOLEANO NÃO DETERMINÁVEL
        # ----------------------------------------------------

        if (
            campo in CAMPOS_BOOLEANOS
            and valor_normalizado is None
        ):

            pendentes.append(
                {
                    "campo":
                        campo,

                    "valor":
                        valor,

                    "motivo":
                        "NAO_FOI_POSSIVEL_DETERMINAR",
                }
            )

            continue


        # ----------------------------------------------------
        # REGISTRAR NA FICHA
        # ----------------------------------------------------

        try:

            setattr(
                ficha,
                campo,
                valor_normalizado,
            )

            preenchidos.append(
                {
                    "campo":
                        campo,

                    "valor":
                        valor_normalizado,
                }
            )


        except Exception as erro:

            erros.append(
                {
                    "campo":
                        campo,

                    "valor":
                        valor_normalizado,

                    "erro":
                        str(
                            erro
                        ),
                }
            )


    return {
        "ficha":
            ficha,

        "preenchidos":
            preenchidos,

        "ignorados":
            ignorados,

        "pendentes":
            pendentes,

        "erros":
            erros,

        "quantidade_preenchidos":
            len(
                preenchidos
            ),

        "quantidade_ignorados":
            len(
                ignorados
            ),

        "quantidade_pendentes":
            len(
                pendentes
            ),

        "quantidade_erros":
            len(
                erros
            ),
    }


# ============================================================
# 7. MOSTRAR FICHA
# ============================================================

def mostrar_ficha(
    ficha: FichaBody,
):
    """
    Exibe apenas informações úteis
    atualmente registradas na ficha.
    """

    dados = ficha.model_dump()


    print(
        "\n"
        "========================================"
    )

    print(
        "FICHA TÉCNICA AURA"
    )

    print(
        "========================================"
    )


    for campo, valor in dados.items():

        if valor is None:
            continue

        if (
            isinstance(
                valor,
                list,
            )
            and len(valor) == 0
        ):
            continue

        print(
            f"{campo}: {valor}"
        )


# ============================================================
# 8. MOSTRAR RESULTADO DO PREENCHIMENTO
# ============================================================

def mostrar_resultado_preenchimento(
    resultado: dict[str, Any],
):
    """
    Exibe um resumo do preenchimento
    realizado pela AURA.
    """

    print(
        "\n"
        "========================================"
    )

    print(
        "RESULTADO DO PREENCHIMENTO"
    )

    print(
        "========================================"
    )

    print(
        "CAMPOS PREENCHIDOS:",
        resultado[
            "quantidade_preenchidos"
        ],
    )

    print(
        "CAMPOS PENDENTES:",
        resultado[
            "quantidade_pendentes"
        ],
    )

    print(
        "CAMPOS IGNORADOS:",
        resultado[
            "quantidade_ignorados"
        ],
    )

    print(
        "ERROS:",
        resultado[
            "quantidade_erros"
        ],
    )


    # --------------------------------------------------------
    # MOSTRAR PENDÊNCIAS
    # --------------------------------------------------------

    if resultado[
        "pendentes"
    ]:

        print(
            "\n"
            "PENDÊNCIAS:"
        )

        for pendencia in resultado[
            "pendentes"
        ]:

            print(
                "-",
                pendencia[
                    "campo"
                ],
                ":",
                pendencia[
                    "motivo"
                ],
            )