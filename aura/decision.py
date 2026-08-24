from aura.rules import (
    CAMPOS_OBRIGATORIOS,
    CAMPOS_CONDICIONAIS,
    PRIORIDADE_CAMPOS,
    CAMPOS_NAO_BLOQUEANTES,
)

from aura.state import EstadoProduto


# ============================================================
# FUNÇÃO AUXILIAR
# VERIFICAR SE UM CAMPO ESTÁ VAZIO
# ============================================================

def campo_vazio(valor):
    """
    Retorna True quando o campo ainda
    não possui informação útil.
    """

    if valor is None:
        return True

    if isinstance(valor, list) and len(valor) == 0:
        return True

    if isinstance(valor, str) and valor.strip() == "":
        return True

    return False


# ============================================================
# VERIFICAR SE UM CAMPO CONDICIONAL ESTÁ ATIVO
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
            == regra["valor"]
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
# VERIFICAR PENDÊNCIAS REAIS
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
    # 1. CAMPOS OBRIGATÓRIOS
    # ========================================================

    for campo in CAMPOS_OBRIGATORIOS:

        # Segurança:
        # um campo marcado como não bloqueante
        # nunca deve travar a ficha.

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
    # 2. CAMPOS CONDICIONAIS
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
    # 3. REMOVER DUPLICADOS
    # ========================================================

    pendencias_unicas = []

    for campo in pendencias:

        if campo not in pendencias_unicas:

            pendencias_unicas.append(
                campo
            )


    return pendencias_unicas


# ============================================================
# ORDENAR PENDÊNCIAS POR PRIORIDADE
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
# ESCOLHER PRÓXIMA AÇÃO DA AURA
# ============================================================

def decidir_proxima_acao(
    estado: EstadoProduto,
):
    """
    Decide o próximo passo da AURA.

    Nova lógica:

    1. Resolver confirmações pendentes.
    2. Procurar somente lacunas que realmente
       bloqueiam a conclusão.
    3. Respeitar prioridade das perguntas.
    4. Ignorar campos opcionais.
    5. Encerrar quando não houver pendências
       bloqueantes.
    """


    # ========================================================
    # 1. CONFIRMAÇÕES PENDENTES
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
    # 2. PENDÊNCIAS REAIS
    # ========================================================

    pendencias = verificar_pendencias_estado(
        estado
    )


    pendencias = ordenar_pendencias(
        pendencias
    )


    # ========================================================
    # 3. BUSCAR PRÓXIMA INFORMAÇÃO
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
    # 4. ENCERRAR FICHA
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
# MOSTRAR DECISÃO
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