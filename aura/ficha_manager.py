from typing import Any, Optional

from aura_schemas.body import FichaBody

from aura_schemas.body_v2 import (
    EvidenciaCampo,
    FichaBodyV2,
    StatusEvidencia,
)


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


# ============================================================
# 9. APLICAR EVIDÊNCIA A UM CAMPO — V2
# ============================================================

def aplicar_evidencia_na_ficha_v2(
    ficha: FichaBodyV2,
    campo: str,
    valor: Any,
    fonte: Optional[str],
    status: StatusEvidencia,
) -> dict[str, Any]:
    """
    Registra uma informação na FichaBodyV2
    preservando valor, fonte e status da evidência.

    A função não decide se a informação é verdadeira.

    Ela apenas registra uma informação que já chegou
    classificada pelo fluxo anterior da AURA.
    """

    # --------------------------------------------------------
    # CAMPO NÃO EXISTE
    # --------------------------------------------------------

    if campo not in ficha.__class__.model_fields:

        return {
            "sucesso": False,
            "campo": campo,
            "motivo": "CAMPO_NAO_EXISTE_NA_FICHA",
        }


    # --------------------------------------------------------
    # CAMPOS ESTRUTURAIS
    # --------------------------------------------------------
    #
    # categoria e tipo_produto são campos estruturais
    # simples da FichaBodyV2.
    #
    # Eles não recebem EvidenciaCampo.
    # --------------------------------------------------------

    if campo in {
        "categoria",
        "tipo_produto",
    }:

        try:

            setattr(
                ficha,
                campo,
                valor,
            )

        except Exception as erro:

            return {
                "sucesso": False,
                "campo": campo,
                "motivo": "ERRO_AO_REGISTRAR",
                "erro": str(
                    erro
                ),
            }

        return {
            "sucesso": True,
            "campo": campo,
            "valor": valor,
            "fonte": None,
            "status": "VALOR_ESTRUTURAL",
            "motivo": None,
        }


    # --------------------------------------------------------
    # CAMPO COM EVIDÊNCIA
    # --------------------------------------------------------

    evidencia_campo = EvidenciaCampo(
        valor=(
            None
            if valor is None
            else str(
                valor
            )
        ),
        fonte=fonte,
        status=status,
    )


    try:

        setattr(
            ficha,
            campo,
            evidencia_campo,
        )

    except Exception as erro:

        return {
            "sucesso": False,
            "campo": campo,
            "motivo": "ERRO_AO_REGISTRAR",
            "erro": str(
                erro
            ),
        }


    return {
        "sucesso": True,
        "campo": campo,
        "valor": evidencia_campo.valor,
        "fonte": evidencia_campo.fonte,
        "status": evidencia_campo.status.value,
        "motivo": None,
    }


# ============================================================
# 10. APLICAR CONHECIMENTO À FICHA — V2
# ============================================================

def aplicar_conhecimento_na_ficha_v2(
    ficha: FichaBodyV2,
    conhecimento: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """
    Aplica várias informações estruturadas
    à FichaBodyV2.

    Formato esperado:

    {
        "marca": {
            "valor": "Linda Sedução Lingerie",
            "fonte": "etiqueta",
            "status": StatusEvidencia.CONFIRMADO,
        }
    }

    Informações inválidas são registradas no relatório
    sem interromper os outros campos.
    """

    preenchidos = []

    ignorados = []

    erros = []


    for campo, dados in conhecimento.items():


        # ----------------------------------------------------
        # CAMPO NÃO EXISTE
        # ----------------------------------------------------

        if campo not in ficha.__class__.model_fields:

            ignorados.append(
                {
                    "campo":
                        campo,

                    "motivo":
                        "CAMPO_NAO_EXISTE_NA_FICHA",
                }
            )

            continue


        # ----------------------------------------------------
        # ESTRUTURA INVÁLIDA
        # ----------------------------------------------------

        if not isinstance(
            dados,
            dict,
        ):

            erros.append(
                {
                    "campo":
                        campo,

                    "motivo":
                        "ESTRUTURA_DE_EVIDENCIA_INVALIDA",
                }
            )

            continue


        valor = dados.get(
            "valor"
        )

        fonte = dados.get(
            "fonte"
        )

        status = dados.get(
            "status"
        )


        # ----------------------------------------------------
        # STATUS AUSENTE
        # ----------------------------------------------------

        if status is None:

            erros.append(
                {
                    "campo":
                        campo,

                    "motivo":
                        "STATUS_NAO_INFORMADO",
                }
            )

            continue


        # ----------------------------------------------------
        # NORMALIZAR STATUS
        # ----------------------------------------------------

        if isinstance(
            status,
            str,
        ):

            try:

                status = StatusEvidencia(
                    status
                )

            except ValueError:

                erros.append(
                    {
                        "campo":
                            campo,

                        "motivo":
                            "STATUS_INVALIDO",

                        "status":
                            status,
                    }
                )

                continue


        # ----------------------------------------------------
        # VALIDAR TIPO DO STATUS
        # ----------------------------------------------------

        if not isinstance(
            status,
            StatusEvidencia,
        ):

            erros.append(
                {
                    "campo":
                        campo,

                    "motivo":
                        "STATUS_INVALIDO",

                    "status":
                        str(
                            status
                        ),
                }
            )

            continue


        # ----------------------------------------------------
        # APLICAR À FICHA
        # ----------------------------------------------------

        resultado = aplicar_evidencia_na_ficha_v2(
            ficha=ficha,
            campo=campo,
            valor=valor,
            fonte=fonte,
            status=status,
        )


        if resultado[
            "sucesso"
        ]:

            preenchidos.append(
                resultado
            )

        else:

            erros.append(
                resultado
            )


    return {
        "ficha":
            ficha,

        "preenchidos":
            preenchidos,

        "ignorados":
            ignorados,

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

        "quantidade_erros":
            len(
                erros
            ),
    }


# ============================================================
# 11. MOSTRAR RESULTADO DO PREENCHIMENTO — V2
# ============================================================

def mostrar_resultado_preenchimento_v2(
    resultado: dict[str, Any],
):
    """
    Exibe um resumo do preenchimento
    realizado na FichaBodyV2.
    """

    print(
        "\n"
        "========================================"
    )

    print(
        "RESULTADO DO PREENCHIMENTO — V2"
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
    # MOSTRAR CAMPOS PREENCHIDOS
    # --------------------------------------------------------

    if resultado[
        "preenchidos"
    ]:

        print(
            "\n"
            "CAMPOS PREENCHIDOS:"
        )

        for item in resultado[
            "preenchidos"
        ]:

            print(
                "-",
                item[
                    "campo"
                ],
                ":",
                item[
                    "status"
                ],
            )


    # --------------------------------------------------------
    # MOSTRAR CAMPOS IGNORADOS
    # --------------------------------------------------------

    if resultado[
        "ignorados"
    ]:

        print(
            "\n"
            "CAMPOS IGNORADOS:"
        )

        for item in resultado[
            "ignorados"
        ]:

            print(
                "-",
                item[
                    "campo"
                ],
                ":",
                item[
                    "motivo"
                ],
            )


    # --------------------------------------------------------
    # MOSTRAR ERROS
    # --------------------------------------------------------

    if resultado[
        "erros"
    ]:

        print(
            "\n"
            "ERROS:"
        )

        for erro in resultado[
            "erros"
        ]:

            print(
                "-",
                erro[
                    "campo"
                ],
                ":",
                erro[
                    "motivo"
                ],
            )