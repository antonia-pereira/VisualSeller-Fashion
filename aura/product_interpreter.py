from typing import Any

from aura_schemas.body import FichaBody


# ============================================================
# VISUALSELLER FASHION
# AURA — INTERPRETAÇÃO DO PRODUTO
# ============================================================


# ============================================================
# 1. VERIFICAR SE EXISTE VALOR
# ============================================================

def possui_valor(
    valor: Any,
) -> bool:
    """
    Retorna True quando existe
    informação útil no campo.
    """

    if valor is None:
        return False

    if isinstance(
        valor,
        str,
    ):

        if not valor.strip():
            return False

    if isinstance(
        valor,
        list,
    ):

        if len(valor) == 0:
            return False

    return True


# ============================================================
# 2. TEXTO PARA LISTA
# ============================================================

def lista_texto(
    valores,
) -> str:
    """
    Converte uma lista simples
    em texto legível.
    """

    if not valores:
        return ""

    return ", ".join(
        str(valor)
        for valor in valores
    )


# ============================================================
# 3. IDENTIDADE OBJETIVA
# ============================================================

def interpretar_identidade_objetiva(
    ficha: FichaBody,
) -> dict[str, Any]:
    """
    Cria uma leitura objetiva do produto
    usando apenas fatos já registrados
    na ficha.

    Não inventa posicionamento,
    público ou estilo.
    """

    elementos = []


    if possui_valor(
        ficha.tipo_produto
    ):

        elementos.append(
            ficha.tipo_produto
        )


    if possui_valor(
        ficha.manga
    ):

        elementos.append(
            f"manga {ficha.manga}"
        )


    if possui_valor(
        ficha.decote_frente
    ):

        elementos.append(
            f"decote frontal {ficha.decote_frente}"
        )


    if possui_valor(
        ficha.transparencia
    ):

        elementos.append(
            str(
                ficha.transparencia
            )
        )


    if possui_valor(
        ficha.materiais_visuais
    ):

        materiais = lista_texto(
            ficha.materiais_visuais
        )

        elementos.append(
            materiais
        )


    descricao = ". ".join(
        elementos
    )


    return {
        "tipo_produto":
            ficha.tipo_produto,

        "elementos_identificados":
            elementos,

        "descricao_objetiva":
            descricao,
    }


# ============================================================
# 4. ELEMENTOS DE DESTAQUE
# ============================================================

def identificar_elementos_destaque(
    ficha: FichaBody,
) -> list[str]:
    """
    Identifica características que podem
    merecer atenção visual ou comercial.

    Aqui ainda não estamos dizendo
    que são diferenciais competitivos.
    Apenas que são elementos perceptíveis.
    """

    destaques = []


    # --------------------------------------------------------
    # MATERIAIS VISUAIS
    # --------------------------------------------------------

    if ficha.materiais_visuais:

        for material in ficha.materiais_visuais:

            if material not in destaques:

                destaques.append(
                    str(material)
                )


    # --------------------------------------------------------
    # TRANSPARÊNCIA
    # --------------------------------------------------------

    if possui_valor(
        ficha.transparencia
    ):

        destaques.append(
            f"Transparência: {ficha.transparencia}"
        )


    # --------------------------------------------------------
    # DECOTE
    # --------------------------------------------------------

    if possui_valor(
        ficha.decote_frente
    ):

        destaques.append(
            f"Decote frontal: {ficha.decote_frente}"
        )


    if possui_valor(
        ficha.decote_costas
    ):

        destaques.append(
            f"Decote das costas: {ficha.decote_costas}"
        )


    # --------------------------------------------------------
    # MANGAS
    # --------------------------------------------------------

    if possui_valor(
        ficha.manga
    ):

        destaques.append(
            f"Manga: {ficha.manga}"
        )


    if possui_valor(
        ficha.acabamento_mangas
    ):

        destaques.append(
            f"Acabamento das mangas: "
            f"{ficha.acabamento_mangas}"
        )


    # --------------------------------------------------------
    # FECHAMENTO
    # --------------------------------------------------------

    if possui_valor(
        ficha.fechamento
    ):

        destaques.append(
            f"Fechamento: {ficha.fechamento}"
        )


    return destaques


# ============================================================
# 5. SINAIS VISUAIS
# ============================================================

def interpretar_sinais_visuais(
    ficha: FichaBody,
) -> list[str]:
    """
    Registra sinais visuais que poderão
    ser usados posteriormente pela Aura
    para interpretar estilo e comunicação.

    Nesta etapa ainda preservamos
    separação entre fato e interpretação.
    """

    sinais = []


    if ficha.materiais_visuais:

        for material in ficha.materiais_visuais:

            sinais.append(
                f"Material visual identificado: {material}"
            )


    if possui_valor(
        ficha.transparencia
    ):

        sinais.append(
            f"Uso de transparência: {ficha.transparencia}"
        )


    if possui_valor(
        ficha.decote_frente
    ):

        sinais.append(
            f"Construção frontal: "
            f"decote {ficha.decote_frente}"
        )


    if possui_valor(
        ficha.decote_costas
    ):

        sinais.append(
            f"Construção das costas: "
            f"decote {ficha.decote_costas}"
        )


    if possui_valor(
        ficha.acabamento_mangas
    ):

        sinais.append(
            f"Acabamento perceptível: "
            f"{ficha.acabamento_mangas}"
        )


    return sinais


# ============================================================
# 6. LIMITES DO CONHECIMENTO
# ============================================================

def identificar_limites(
    ficha: FichaBody,
) -> list[str]:
    """
    Registra aquilo que NÃO deve ser
    afirmado automaticamente apenas
    com base na ficha atual.
    """

    limites = [
        (
            "Não afirmar conforto, durabilidade ou qualidade "
            "sem evidência específica."
        ),

        (
            "Não afirmar que o produto valoriza determinado "
            "tipo de corpo sem validação."
        ),

        (
            "Não definir público-alvo apenas pela aparência."
        ),

        (
            "Não afirmar ocasião de uso como fato "
            "sem contexto adicional."
        ),

        (
            "Não transformar materiais visualmente percebidos "
            "em composição têxtil oficial."
        ),

        (
            "Não tratar interpretação estética "
            "como característica técnica confirmada."
        ),
    ]


    return limites


# ============================================================
# 7. GERAR INTERPRETAÇÃO BASE
# ============================================================

def interpretar_produto(
    ficha: FichaBody,
) -> dict[str, Any]:
    """
    Gera a primeira camada de interpretação
    do produto pela Aura.

    Esta etapa separa:

    - fatos;
    - destaques;
    - sinais visuais;
    - limites de interpretação.

    Ainda não cria campanha,
    público-alvo ou texto de venda.
    """

    identidade = interpretar_identidade_objetiva(
        ficha
    )


    destaques = identificar_elementos_destaque(
        ficha
    )


    sinais = interpretar_sinais_visuais(
        ficha
    )


    limites = identificar_limites(
        ficha
    )


    return {
        "identidade_objetiva":
            identidade,

        "elementos_de_destaque":
            destaques,

        "sinais_visuais":
            sinais,

        "limites":
            limites,
    }


# ============================================================
# 8. MOSTRAR INTERPRETAÇÃO
# ============================================================

def mostrar_interpretacao_produto(
    ficha: FichaBody,
):
    """
    Exibe a interpretação base da Aura.
    """

    interpretacao = interpretar_produto(
        ficha
    )


    print(
        "\n"
        "========================================"
    )

    print(
        "AURA — INTERPRETAÇÃO DO PRODUTO"
    )

    print(
        "========================================"
    )


    # --------------------------------------------------------
    # IDENTIDADE OBJETIVA
    # --------------------------------------------------------

    print(
        "\nIDENTIDADE OBJETIVA"
    )

    print(
        "----------------------------------------"
    )


    descricao = (
        interpretacao[
            "identidade_objetiva"
        ][
            "descricao_objetiva"
        ]
    )


    if descricao:

        print(
            descricao
        )

    else:

        print(
            "Ainda não existem informações suficientes."
        )


    # --------------------------------------------------------
    # DESTAQUES
    # --------------------------------------------------------

    print(
        "\nELEMENTOS DE DESTAQUE"
    )

    print(
        "----------------------------------------"
    )


    for item in interpretacao[
        "elementos_de_destaque"
    ]:

        print(
            "-",
            item
        )


    # --------------------------------------------------------
    # SINAIS VISUAIS
    # --------------------------------------------------------

    print(
        "\nSINAIS VISUAIS"
    )

    print(
        "----------------------------------------"
    )


    for item in interpretacao[
        "sinais_visuais"
    ]:

        print(
            "-",
            item
        )


    # --------------------------------------------------------
    # LIMITES
    # --------------------------------------------------------

    print(
        "\nO QUE A AURA AINDA NÃO DEVE AFIRMAR"
    )

    print(
        "----------------------------------------"
    )


    for item in interpretacao[
        "limites"
    ]:

        print(
            "-",
            item
        )


    return interpretacao