from typing import Any

from aura_schemas.body import FichaBody


# ============================================================
# VISUALSELLER FASHION
# AURA — ANALISADOR DE LACUNAS DA FICHA
# ============================================================


# ============================================================
# 1. PRIORIDADE DOS CAMPOS
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
# 3. DESCOBRIR TODOS OS CAMPOS VAZIOS
# ============================================================

def obter_campos_vazios(
    ficha: FichaBody,
) -> list[str]:
    """
    Percorre a ficha inteira e retorna
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
# 4. CLASSIFICAR UMA LACUNA
# ============================================================

def classificar_lacuna(
    campo: str,
) -> str:
    """
    Classifica um campo vazio conforme
    a importância para o fluxo da Aura.
    """

    if campo in CAMPOS_ESSENCIAIS:

        return "ESSENCIAL"

    if campo in CAMPOS_QUE_PODEM_VIR_DE_OUTRA_FOTO:

        return "OUTRA_FOTO"

    if campo in CAMPOS_OPCIONAIS:

        return "OPCIONAL"

    return "PODE_PULAR"


# ============================================================
# 5. ANALISAR LACUNAS DA FICHA
# ============================================================

def analisar_lacunas(
    ficha: FichaBody,
) -> dict[str, Any]:
    """
    Analisa os campos ainda vazios e
    organiza por prioridade.
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
# 6. PRÓXIMAS PERGUNTAS RECOMENDADAS
# ============================================================

def obter_perguntas_prioritarias(
    ficha: FichaBody,
    limite: int = 4,
) -> list[str]:
    """
    Retorna somente os campos essenciais
    que realmente justificam pergunta.

    Limita a quantidade para evitar
    interrogatório infinito.
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
# 7. STATUS DA FICHA
# ============================================================

def obter_status_ficha(
    ficha: FichaBody,
) -> str:
    """
    Define o status da ficha com base
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
# 8. MOSTRAR ANÁLISE
# ============================================================

def mostrar_analise_lacunas(
    ficha: FichaBody,
):
    """
    Exibe um resumo simples das lacunas.
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