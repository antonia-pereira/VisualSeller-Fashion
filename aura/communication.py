from typing import Any


# ============================================================
# PERGUNTAS NATURAIS DA AURA
# ============================================================

PERGUNTAS_POR_CAMPO = {
    "possui_bojo":
        "Esse body possui bojo?",

    "tipo_bojo":
        "Qual é o tipo de bojo da peça?",

    "possui_forro":
        "A peça possui forro?",

    "composicao_forro":
        "Qual é a composição do forro?",

    "acabamento_mangas":
        "Qual é o acabamento das mangas?",

    "manga":
        "Qual é o tipo ou comprimento da manga?",

    "decote_frente":
        "Qual é o formato do decote frontal?",

    "decote_costas":
        "Qual é o formato do decote nas costas?",

    "fechamento":
        "Qual é o tipo de fechamento da peça?",

    "transparencia":
        (
            "A peça possui transparência? "
            "Se sim, em quais regiões?"
        ),

    "cores_disponiveis":
        "Quais cores estão disponíveis?",

    "tamanhos_disponiveis":
        "Quais tamanhos estão disponíveis?",

    "grade":
        (
            "Qual é a quantidade disponível "
            "em cada tamanho?"
        ),

    "quantidade_total":
        "Qual é a quantidade total disponível?",

    "composicao_principal":
        "Qual é a composição principal da peça?",

    "materiais_visuais":
        (
            "Quais materiais ou tecidos "
            "aparecem visualmente na peça?"
        ),

    "tamanho_medido":
        (
            "Qual tamanho da peça foi usado "
            "para realizar as medições?"
        ),

    "busto_cm":
        "Qual é a medida do busto em centímetros?",

    "cintura_cm":
        "Qual é a medida da cintura em centímetros?",

    "quadril_cm":
        "Qual é a medida do quadril em centímetros?",

    "comprimento_cm":
        "Qual é o comprimento da peça em centímetros?",
}


# ============================================================
# NOMES HUMANOS DOS CAMPOS
# ============================================================

NOMES_POR_CAMPO = {
    "possui_bojo":
        "presença de bojo",

    "tipo_bojo":
        "tipo de bojo",

    "possui_forro":
        "presença de forro",

    "composicao_forro":
        "composição do forro",

    "acabamento_mangas":
        "acabamento das mangas",

    "manga":
        "manga",

    "decote_frente":
        "decote frontal",

    "decote_costas":
        "decote das costas",

    "fechamento":
        "fechamento",

    "transparencia":
        "transparência",

    "cores_disponiveis":
        "cores disponíveis",

    "tamanhos_disponiveis":
        "tamanhos disponíveis",

    "grade":
        "grade de tamanhos",

    "quantidade_total":
        "quantidade total",

    "composicao_principal":
        "composição principal",

    "materiais_visuais":
        "materiais da peça",

    "tamanho_medido":
        "tamanho utilizado na medição",

    "busto_cm":
        "medida do busto",

    "cintura_cm":
        "medida da cintura",

    "quadril_cm":
        "medida do quadril",

    "comprimento_cm":
        "comprimento da peça",
}


# ============================================================
# GERAR PERGUNTA
# ============================================================

def gerar_pergunta(
    campo: str,
) -> str:
    """
    Transforma o nome técnico de um campo
    em uma pergunta natural para o usuário.
    """

    pergunta = PERGUNTAS_POR_CAMPO.get(
        campo
    )

    if pergunta:
        return pergunta

    nome = campo.replace(
        "_",
        " ",
    )

    return (
        "Pode me informar "
        f"{nome}?"
    )


# ============================================================
# GERAR PEDIDO DE CONFIRMAÇÃO
# ============================================================

def gerar_confirmacao(
    campo: str,
    valor_proposto: Any,
) -> str:
    """
    Gera uma pergunta de confirmação
    quando a AURA possui uma hipótese,
    mas ainda não pode tratá-la como fato.
    """

    nome = NOMES_POR_CAMPO.get(
        campo,
        campo.replace("_", " "),
    )

    if isinstance(
        valor_proposto,
        bool,
    ):

        valor_texto = (
            "sim"
            if valor_proposto
            else "não"
        )

    else:

        valor_texto = str(
            valor_proposto
        )

    return (
        f"Pelas informações disponíveis, "
        f"parece que {nome} é "
        f"'{valor_texto}'. "
        "Você consegue confirmar?"
    )


# ============================================================
# GERAR MENSAGEM A PARTIR DA DECISÃO
# ============================================================

def gerar_mensagem_aura(
    decisao: dict,
) -> str:
    """
    Converte a decisão interna da AURA
    em uma mensagem natural para o usuário.
    """

    acao = decisao.get(
        "acao"
    )

    campo = decisao.get(
        "campo"
    )

    valor_proposto = decisao.get(
        "valor_proposto"
    )

    # --------------------------------------------------------
    # BUSCAR NOVA INFORMAÇÃO
    # --------------------------------------------------------

    if acao == "BUSCAR_INFORMACAO":

        return gerar_pergunta(
            campo
        )

    # --------------------------------------------------------
    # CONFIRMAR UMA HIPÓTESE
    # --------------------------------------------------------

    if acao == "PEDIR_CONFIRMACAO":

        return gerar_confirmacao(
            campo,
            valor_proposto,
        )

    # --------------------------------------------------------
    # FICHA CONCLUÍDA
    # --------------------------------------------------------

    if acao == "ENCERRAR_FICHA":

        return (
            "Perfeito. Já tenho as informações "
            "necessárias para concluir a ficha "
            "técnica deste produto."
        )

    # --------------------------------------------------------
    # AÇÃO DESCONHECIDA
    # --------------------------------------------------------

    return (
        "Não consegui determinar a próxima "
        "etapa da análise."
    )