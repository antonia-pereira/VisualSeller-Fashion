from aura.rules import (
    CAMPOS_OBRIGATORIOS,
    CAMPOS_CONDICIONAIS,
    PRIORIDADE_CAMPOS,
    CAMPOS_NAO_BLOQUEANTES,
)

from aura.state import (
    EstadoProduto,
    EstadoProdutoV2,
)

from aura.question_planner import (
    planejar_perguntas_por_objetivo,
)


# ============================================================
# VISUALSELLER FASHION
# AURA — SISTEMA DE DECISÃO
# ============================================================


# ============================================================
# 1. FUNÇÃO AUXILIAR — V1
# VERIFICAR SE UM CAMPO ESTÁ VAZIO
# ============================================================

def campo_vazio(valor):
    """
    Retorna True quando o campo ainda
    não possui informação útil.
    """

    if valor is None:
        return True

    if isinstance(
        valor,
        list,
    ) and len(
        valor
    ) == 0:
        return True

    if isinstance(
        valor,
        str,
    ) and valor.strip() == "":
        return True

    return False


# ============================================================
# 2. VERIFICAR SE UM CAMPO CONDICIONAL ESTÁ ATIVO — V1
# ============================================================

def campo_condicional_ativo(
    campo: str,
    dados: dict,
):
    """
    Verifica se um campo condicional
    deve realmente ser exigido.
    """

    regra = CAMPOS_CONDICIONAIS.get(
        campo
    )

    if regra is None:
        return False

    dependencia = regra.get(
        "depende_de"
    )

    valor_dependencia = dados.get(
        dependencia
    )


    # --------------------------------------------------------
    # REGRA POR VALOR EXATO
    # --------------------------------------------------------

    if "valor" in regra:

        return (
            valor_dependencia
            == regra[
                "valor"
            ]
        )


    # --------------------------------------------------------
    # REGRA POR VALOR DIFERENTE
    # --------------------------------------------------------

    if "valor_diferente_de" in regra:

        return (
            valor_dependencia
            != regra[
                "valor_diferente_de"
            ]
        )

    return False


# ============================================================
# 3. VERIFICAR PENDÊNCIAS REAIS — V1
# ============================================================

def verificar_pendencias_estado(
    estado: EstadoProduto,
):
    """
    Retorna somente campos que realmente
    impedem a conclusão da ficha.

    Campos opcionais não entram aqui.
    """

    dados = estado.ficha.model_dump()

    pendencias = []


    # ========================================================
    # CAMPOS OBRIGATÓRIOS
    # ========================================================

    for campo in CAMPOS_OBRIGATORIOS:

        if campo in CAMPOS_NAO_BLOQUEANTES:
            continue

        valor = dados.get(
            campo
        )

        if campo_vazio(
            valor
        ):

            pendencias.append(
                campo
            )


    # ========================================================
    # CAMPOS CONDICIONAIS
    # ========================================================

    for campo in CAMPOS_CONDICIONAIS:

        if campo in CAMPOS_NAO_BLOQUEANTES:
            continue

        ativo = campo_condicional_ativo(
            campo=campo,
            dados=dados,
        )

        if not ativo:
            continue

        valor = dados.get(
            campo
        )

        if campo_vazio(
            valor
        ):

            pendencias.append(
                campo
            )


    # ========================================================
    # REMOVER DUPLICADOS
    # ========================================================

    pendencias_unicas = []

    for campo in pendencias:

        if campo not in pendencias_unicas:

            pendencias_unicas.append(
                campo
            )

    return pendencias_unicas


# ============================================================
# 4. ORDENAR PENDÊNCIAS POR PRIORIDADE — V1
# ============================================================

def ordenar_pendencias(
    pendencias: list[str],
):
    """
    Coloca as pendências na ordem
    de importância definida pela AURA.
    """

    ordenadas = []


    # --------------------------------------------------------
    # PRIMEIRO: PRIORIDADE EXPLÍCITA
    # --------------------------------------------------------

    for campo in PRIORIDADE_CAMPOS:

        if campo in pendencias:

            ordenadas.append(
                campo
            )


    # --------------------------------------------------------
    # DEPOIS: QUALQUER OUTRA PENDÊNCIA
    # --------------------------------------------------------

    for campo in pendencias:

        if campo not in ordenadas:

            ordenadas.append(
                campo
            )

    return ordenadas


# ============================================================
# 5. ESCOLHER PRÓXIMA AÇÃO DA AURA — V1
# ============================================================

def decidir_proxima_acao(
    estado: EstadoProduto,
):
    """
    Decide o próximo passo da AURA V1.

    1. Resolver confirmações pendentes.
    2. Procurar somente lacunas que realmente
       bloqueiam a conclusão.
    3. Respeitar prioridade das perguntas.
    4. Ignorar campos opcionais.
    5. Encerrar quando não houver pendências
       bloqueantes.
    """


    # ========================================================
    # CONFIRMAÇÕES PENDENTES
    # ========================================================

    confirmacoes = (
        estado.obter_confirmacoes_pendentes()
    )


    if confirmacoes:

        proxima = confirmacoes[0]

        return {
            "acao":
                "PEDIR_CONFIRMACAO",

            "campo":
                proxima.get(
                    "campo"
                ),

            "valor_proposto":
                proxima.get(
                    "valor"
                ),

            "motivo": (
                "Existe uma informação relevante "
                "que ainda precisa ser confirmada."
            ),
        }


    # ========================================================
    # PENDÊNCIAS REAIS
    # ========================================================

    pendencias = verificar_pendencias_estado(
        estado
    )

    pendencias = ordenar_pendencias(
        pendencias
    )


    # ========================================================
    # BUSCAR PRÓXIMA INFORMAÇÃO
    # ========================================================

    if pendencias:

        proximo_campo = pendencias[0]

        return {
            "acao":
                "BUSCAR_INFORMACAO",

            "campo":
                proximo_campo,

            "valor_proposto":
                None,

            "motivo": (
                "Esta informação ainda é necessária "
                "para concluir a ficha essencial "
                "do produto."
            ),
        }


    # ========================================================
    # ENCERRAR FICHA
    # ========================================================

    return {
        "acao":
            "ENCERRAR_FICHA",

        "campo":
            None,

        "valor_proposto":
            None,

        "motivo": (
            "Não existem mais pendências "
            "obrigatórias ou condicionais ativas."
        ),
    }


# ============================================================
# 6. MOSTRAR DECISÃO — V1
# ============================================================

def mostrar_decisao(
    decisao: dict,
):
    """
    Exibe no terminal a decisão
    escolhida pela AURA.
    """

    print(
        "\n"
        "========================================"
    )

    print(
        "PRÓXIMA DECISÃO DA AURA"
    )

    print(
        "========================================"
    )

    print(
        "AÇÃO:",
        decisao.get(
            "acao"
        ),
    )

    print(
        "CAMPO:",
        decisao.get(
            "campo"
        ),
    )

    print(
        "VALOR PROPOSTO:",
        decisao.get(
            "valor_proposto"
        ),
    )

    print(
        "MOTIVO:",
        decisao.get(
            "motivo"
        ),
    )


# ============================================================
# 7. ESCOLHER PRÓXIMA AÇÃO DA AURA — V2
# ============================================================

def decidir_proxima_acao_v2(
    estado: EstadoProdutoV2,
) -> dict:
    """
    Decide o próximo passo da AURA V2.

    A função não recria regras técnicas.

    Ela consulta o question_planner,
    que já utiliza a análise de lacunas
    orientada pelo objetivo.

    Decisões atuais:

    PERGUNTAR_USUARIO
        existe pelo menos um bloqueador
        que exige uma pergunta.

    CONTINUAR_OBJETIVO
        não existem mais bloqueadores
        para o objetivo atual.
    """

    plano = planejar_perguntas_por_objetivo(
        ficha=estado.ficha,
        objetivo=estado.objetivo,
    )


    # ========================================================
    # EXISTEM BLOQUEADORES
    # ========================================================

    if not plano[
        "pode_continuar"
    ]:

        perguntas = plano[
            "perguntas"
        ]

        bloqueadores = plano[
            "bloqueadores"
        ]


        # ----------------------------------------------------
        # REGISTRAR BLOQUEADORES NO ESTADO
        # ----------------------------------------------------

        for bloqueador in bloqueadores:

            estado.registrar_bloqueio(
                bloqueador
            )


        # ----------------------------------------------------
        # EXISTE PERGUNTA PLANEJADA
        # ----------------------------------------------------

        if perguntas:

            proxima_pergunta = perguntas[
                0
            ]

            decisao = {
                "acao":
                    "PERGUNTAR_USUARIO",

                "objetivo":
                    estado.objetivo,

                "campo":
                    proxima_pergunta[
                        "campo"
                    ],

                "pergunta":
                    proxima_pergunta[
                        "pergunta"
                    ],

                "status":
                    proxima_pergunta.get(
                        "status"
                    ),

                "motivo":
                    proxima_pergunta.get(
                        "motivo"
                    ),

                "quantidade_bloqueadores":
                    len(
                        bloqueadores
                    ),

                "quantidade_perguntas":
                    len(
                        perguntas
                    ),
            }

            estado.registrar_pergunta(
                proxima_pergunta
            )

            estado.registrar_decisao(
                decisao
            )

            return decisao


        # ----------------------------------------------------
        # BLOQUEIO SEM PERGUNTA CADASTRADA
        # ----------------------------------------------------
        #
        # Esse caso não deve ser tratado como
        # CONTINUAR_OBJETIVO.
        #
        # Existe um bloqueio real, mas o sistema
        # ainda não possui uma pergunta utilizável.
        # ----------------------------------------------------

        primeiro_bloqueador = (
            bloqueadores[0]
            if bloqueadores
            else None
        )

        decisao = {
            "acao":
                "BLOQUEADO_SEM_PERGUNTA",

            "objetivo":
                estado.objetivo,

            "campo":
                (
                    primeiro_bloqueador.get(
                        "campo"
                    )
                    if primeiro_bloqueador
                    else None
                ),

            "pergunta":
                None,

            "status":
                (
                    primeiro_bloqueador.get(
                        "status"
                    )
                    if primeiro_bloqueador
                    else None
                ),

            "motivo":
                (
                    "Existe um bloqueio para o objetivo, "
                    "mas nenhuma pergunta utilizável "
                    "foi planejada."
                ),

            "quantidade_bloqueadores":
                len(
                    bloqueadores
                ),

            "quantidade_perguntas":
                0,
        }

        estado.registrar_decisao(
            decisao
        )

        return decisao


    # ========================================================
    # OBJETIVO LIBERADO
    # ========================================================

    decisao = {
        "acao":
            "CONTINUAR_OBJETIVO",

        "objetivo":
            estado.objetivo,

        "campo":
            None,

        "pergunta":
            None,

        "status":
            None,

        "motivo":
            (
                "Não existem bloqueadores para "
                "o objetivo atual."
            ),

        "quantidade_bloqueadores":
            0,

        "quantidade_perguntas":
            0,
    }

    estado.registrar_decisao(
        decisao
    )

    return decisao


# ============================================================
# 8. MOSTRAR DECISÃO — V2
# ============================================================

def mostrar_decisao_v2(
    decisao: dict,
):
    """
    Exibe a decisão tomada pela AURA V2.
    """

    print(
        "\n"
        "========================================"
    )

    print(
        "PRÓXIMA DECISÃO DA AURA — V2"
    )

    print(
        "========================================"
    )

    print(
        "AÇÃO:",
        decisao.get(
            "acao"
        ),
    )

    print(
        "OBJETIVO:",
        decisao.get(
            "objetivo"
        ),
    )

    print(
        "CAMPO:",
        decisao.get(
            "campo"
        ),
    )

    print(
        "STATUS:",
        decisao.get(
            "status"
        ),
    )

    print(
        "BLOQUEADORES:",
        decisao.get(
            "quantidade_bloqueadores"
        ),
    )

    print(
        "PERGUNTAS:",
        decisao.get(
            "quantidade_perguntas"
        ),
    )


    if decisao.get(
        "pergunta"
    ):

        print(
            "\n"
            "AURA:"
        )

        print(
            decisao[
                "pergunta"
            ]
        )


    print(
        "\n"
        "MOTIVO:",
        decisao.get(
            "motivo"
        ),
    )