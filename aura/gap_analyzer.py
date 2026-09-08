from typing import Any

from aura.rules import (
    STATUS_V2_ACEITOS,
    obter_campos_por_objetivo,
)

from aura_schemas.body import FichaBody
from aura_schemas.body_v2 import FichaBodyV2


# ============================================================
# VISUALSELLER FASHION
# AURA — ANALISADOR DE LACUNAS DA FICHA
# ============================================================


# ============================================================
# 1. PRIORIDADE DOS CAMPOS — ARQUITETURA LEGADA
# ============================================================
#
# Estas regras continuam disponíveis enquanto componentes
# antigos da AURA ainda utilizarem FichaBody.
# ============================================================

CAMPOS_ESSENCIAIS = {
    "marca",
    "nome_modelo",
    "cores_disponiveis",
    "tamanhos_disponiveis",
    "grade",
    "quantidade_total",
    "possui_bojo",
}


CAMPOS_QUE_PODEM_VIR_DE_OUTRA_FOTO = {
    "codigo_barras",
    "composicao_principal",
    "composicao_forro",
    "instrucoes_conservacao",
}


CAMPOS_OPCIONAIS = {
    "referencia",
    "tipo_bojo",
    "acabamento_pernas",
    "acabamento_decote",
    "busto_cm",
    "cintura_cm",
    "quadril_cm",
    "comprimento_cm",
}


# ============================================================
# 2. VERIFICAR SE UM VALOR ESTÁ VAZIO
# ============================================================

def valor_vazio(
    valor: Any,
) -> bool:
    """
    Retorna True quando o campo ainda
    não possui informação útil.
    """

    if valor is None:
        return True

    if isinstance(
        valor,
        str,
    ):

        if not valor.strip():
            return True

    if isinstance(
        valor,
        list,
    ):

        if len(
            valor
        ) == 0:
            return True

    return False


# ============================================================
# 3. DESCOBRIR TODOS OS CAMPOS VAZIOS — V1
# ============================================================

def obter_campos_vazios(
    ficha: FichaBody,
) -> list[str]:
    """
    Percorre a ficha antiga e retorna
    somente os campos ainda vazios.
    """

    dados = ficha.model_dump()

    vazios = []

    for campo, valor in dados.items():

        if valor_vazio(
            valor
        ):

            vazios.append(
                campo
            )

    return vazios


# ============================================================
# 4. CLASSIFICAR UMA LACUNA — V1
# ============================================================

def classificar_lacuna(
    campo: str,
) -> str:
    """
    Classifica um campo vazio conforme
    a importância para o fluxo legado da AURA.
    """

    if campo in CAMPOS_ESSENCIAIS:

        return "ESSENCIAL"

    if campo in CAMPOS_QUE_PODEM_VIR_DE_OUTRA_FOTO:

        return "OUTRA_FOTO"

    if campo in CAMPOS_OPCIONAIS:

        return "OPCIONAL"

    return "PODE_PULAR"


# ============================================================
# 5. ANALISAR LACUNAS DA FICHA — V1
# ============================================================

def analisar_lacunas(
    ficha: FichaBody,
) -> dict[str, Any]:
    """
    Analisa os campos ainda vazios da ficha antiga
    e organiza por prioridade.

    Esta função é mantida para compatibilidade
    com os componentes existentes da AURA.
    """

    campos_vazios = obter_campos_vazios(
        ficha
    )

    essenciais = []
    outra_foto = []
    opcionais = []
    pode_pular = []

    for campo in campos_vazios:

        classificacao = classificar_lacuna(
            campo
        )

        if classificacao == "ESSENCIAL":

            essenciais.append(
                campo
            )

        elif classificacao == "OUTRA_FOTO":

            outra_foto.append(
                campo
            )

        elif classificacao == "OPCIONAL":

            opcionais.append(
                campo
            )

        else:

            pode_pular.append(
                campo
            )

    return {
        "campos_vazios":
            campos_vazios,

        "essenciais":
            essenciais,

        "outra_foto":
            outra_foto,

        "opcionais":
            opcionais,

        "pode_pular":
            pode_pular,

        "quantidade_vazios":
            len(
                campos_vazios
            ),

        "quantidade_essenciais":
            len(
                essenciais
            ),

        "quantidade_outra_foto":
            len(
                outra_foto
            ),

        "quantidade_opcionais":
            len(
                opcionais
            ),

        "quantidade_pode_pular":
            len(
                pode_pular
            ),
    }


# ============================================================
# 6. PRÓXIMAS PERGUNTAS RECOMENDADAS — V1
# ============================================================

def obter_perguntas_prioritarias(
    ficha: FichaBody,
    limite: int = 4,
) -> list[str]:
    """
    Retorna somente os campos essenciais
    que realmente justificam pergunta.

    Mantido para compatibilidade com a V1.
    """

    analise = analisar_lacunas(
        ficha
    )

    essenciais = analise[
        "essenciais"
    ]

    return essenciais[
        :limite
    ]


# ============================================================
# 7. STATUS DA FICHA — V1
# ============================================================

def obter_status_ficha(
    ficha: FichaBody,
) -> str:
    """
    Define o status da ficha antiga com base
    nas lacunas essenciais.
    """

    analise = analisar_lacunas(
        ficha
    )

    if not analise[
        "essenciais"
    ]:

        return "COMPLETA"

    return "PARCIAL"


# ============================================================
# 8. MOSTRAR ANÁLISE — V1
# ============================================================

def mostrar_analise_lacunas(
    ficha: FichaBody,
):
    """
    Exibe um resumo simples das lacunas
    da arquitetura antiga.
    """

    analise = analisar_lacunas(
        ficha
    )

    status = obter_status_ficha(
        ficha
    )

    perguntas = obter_perguntas_prioritarias(
        ficha
    )

    print(
        "\n"
        "========================================"
    )

    print(
        "ANÁLISE DE LACUNAS DA AURA"
    )

    print(
        "========================================"
    )

    print(
        "STATUS DA FICHA:",
        status
    )

    print(
        "CAMPOS VAZIOS:",
        analise[
            "quantidade_vazios"
        ]
    )

    print(
        "ESSENCIAIS:",
        analise[
            "quantidade_essenciais"
        ]
    )

    print(
        "PODEM VIR DE OUTRA FOTO:",
        analise[
            "quantidade_outra_foto"
        ]
    )

    print(
        "OPCIONAIS:",
        analise[
            "quantidade_opcionais"
        ]
    )

    print(
        "PODEM SER PULADOS:",
        analise[
            "quantidade_pode_pular"
        ]
    )

    print(
        "\n"
        "CAMPOS ESSENCIAIS AINDA FALTANDO:"
    )

    if analise[
        "essenciais"
    ]:

        for campo in analise[
            "essenciais"
        ]:

            print(
                "-",
                campo
            )

    else:

        print(
            "Nenhum."
        )

    print(
        "\n"
        "PRÓXIMAS PERGUNTAS RECOMENDADAS:"
    )

    if perguntas:

        for campo in perguntas:

            print(
                "-",
                campo
            )

    else:

        print(
            "Nenhuma pergunta necessária."
        )


# ============================================================
# 9. NORMALIZAR STATUS DE EVIDÊNCIA — V2
# ============================================================

def normalizar_status_v2(
    status: Any,
) -> str | None:
    """
    Converte o status recebido para seu valor textual.

    Funciona tanto com StatusEvidencia quanto com strings.
    """

    if status is None:
        return None

    if hasattr(
        status,
        "value",
    ):

        return str(
            status.value
        )

    return str(
        status
    )


# ============================================================
# 10. ANALISAR UM CAMPO — V2
# ============================================================

def analisar_campo_v2(
    ficha: FichaBodyV2,
    campo: str,
) -> dict[str, Any]:
    """
    Analisa um campo individual da FichaBodyV2.

    Um campo só é considerado aprovado quando:

    - existe no schema;
    - possui informação;
    - possui status aceito pelas regras V2.

    Campos simples do schema, como tipo_produto,
    continuam válidos quando possuem valor.
    """

    if campo not in ficha.__class__.model_fields:

        return {
            "campo": campo,
            "aprovado": False,
            "status": "CAMPO_INEXISTENTE",
            "valor": None,
            "motivo": "CAMPO_NAO_EXISTE_NA_FICHA",
        }

    valor = getattr(
        ficha,
        campo,
    )

    if valor_vazio(
        valor
    ):

        return {
            "campo": campo,
            "aprovado": False,
            "status": "SEM_INFORMACAO",
            "valor": None,
            "motivo": "SEM_INFORMACAO",
        }

    # --------------------------------------------------------
    # CAMPO SIMPLES
    # --------------------------------------------------------
    #
    # Alguns campos estruturais do schema ainda são valores
    # simples e não EvidenciaCampo.
    # --------------------------------------------------------

    if not hasattr(
        valor,
        "status",
    ):

        return {
            "campo": campo,
            "aprovado": True,
            "status": "VALOR_ESTRUTURAL",
            "valor": valor,
            "motivo": None,
        }

    # --------------------------------------------------------
    # CAMPO COM EVIDÊNCIA
    # --------------------------------------------------------

    status = normalizar_status_v2(
        valor.status
    )

    valor_campo = getattr(
        valor,
        "valor",
        None,
    )

    if valor_vazio(
        valor_campo
    ):

        return {
            "campo": campo,
            "aprovado": False,
            "status": status or "SEM_INFORMACAO",
            "valor": valor_campo,
            "motivo": "SEM_INFORMACAO",
        }

    if status in STATUS_V2_ACEITOS:

        return {
            "campo": campo,
            "aprovado": True,
            "status": status,
            "valor": valor_campo,
            "motivo": None,
        }

    return {
        "campo": campo,
        "aprovado": False,
        "status": status or "SEM_STATUS",
        "valor": valor_campo,
        "motivo": "EVIDENCIA_NAO_ACEITA",
    }


# ============================================================
# 11. ANALISAR LACUNAS POR OBJETIVO — V2
# ============================================================

def analisar_lacunas_por_objetivo(
    ficha: FichaBodyV2,
    objetivo: str,
) -> dict[str, Any]:
    """
    Analisa somente os campos necessários
    para o objetivo atual da AURA.

    Diferentemente da V1, um campo preenchido
    pode continuar sendo uma lacuna quando
    sua evidência ainda não foi aceita.
    """

    campos_necessarios = obter_campos_por_objetivo(
        objetivo
    )

    aprovados = []
    bloqueadores = []

    for campo in campos_necessarios:

        resultado = analisar_campo_v2(
            ficha=ficha,
            campo=campo,
        )

        if resultado[
            "aprovado"
        ]:

            aprovados.append(
                resultado
            )

        else:

            bloqueadores.append(
                resultado
            )

    return {
        "objetivo":
            objetivo,

        "pode_continuar":
            len(
                bloqueadores
            ) == 0,

        "campos_necessarios":
            campos_necessarios,

        "aprovados":
            aprovados,

        "bloqueadores":
            bloqueadores,

        "quantidade_necessarios":
            len(
                campos_necessarios
            ),

        "quantidade_aprovados":
            len(
                aprovados
            ),

        "quantidade_bloqueadores":
            len(
                bloqueadores
            ),
    }


# ============================================================
# 12. MOSTRAR ANÁLISE POR OBJETIVO — V2
# ============================================================

def mostrar_analise_por_objetivo(
    ficha: FichaBodyV2,
    objetivo: str,
):
    """
    Exibe o resultado da análise V2
    para um objetivo específico.
    """

    analise = analisar_lacunas_por_objetivo(
        ficha=ficha,
        objetivo=objetivo,
    )

    print(
        "\n"
        "========================================"
    )

    print(
        "ANÁLISE DE LACUNAS DA AURA — V2"
    )

    print(
        "========================================"
    )

    print(
        "OBJETIVO:",
        analise[
            "objetivo"
        ]
    )

    print(
        "CAMPOS NECESSÁRIOS:",
        analise[
            "quantidade_necessarios"
        ]
    )

    print(
        "CAMPOS APROVADOS:",
        analise[
            "quantidade_aprovados"
        ]
    )

    print(
        "BLOQUEADORES:",
        analise[
            "quantidade_bloqueadores"
        ]
    )

    print(
        "\n"
        "DECISÃO:"
    )

    if analise[
        "pode_continuar"
    ]:

        print(
            "AURA PODE CONTINUAR"
        )

    else:

        print(
            "AURA NÃO DEVE CONTINUAR"
        )

    print(
        "\n"
        "CAMPOS BLOQUEADORES:"
    )

    if not analise[
        "bloqueadores"
    ]:

        print(
            "Nenhum."
        )

        return

    for bloqueador in analise[
        "bloqueadores"
    ]:

        print(
            "-",
            bloqueador[
                "campo"
            ],
            "("
            + bloqueador[
                "status"
            ]
            + ")"
        )