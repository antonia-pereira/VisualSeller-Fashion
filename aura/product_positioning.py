# ============================================================
# VISUALSELLER FASHION
# AURA — POSICIONAMENTO DO PRODUTO
# ============================================================

from dataclasses import dataclass, field
from typing import List


# ============================================================
# 1. MODELO DE POSICIONAMENTO
# ============================================================

@dataclass
class PosicionamentoProduto:
    """
    Representa a direção estratégica de apresentação
    do produto.

    O posicionamento não inventa atributos.
    Ele organiza identidade, desejos e valores percebidos
    em uma direção de comunicação.
    """

    direcao_principal: str

    territorio_comunicacao: str

    destacar: List[str] = field(
        default_factory=list
    )

    evitar: List[str] = field(
        default_factory=list
    )

    evidencias: List[str] = field(
        default_factory=list
    )

    confianca: str = "baixa"


# ============================================================
# 2. FUNÇÕES AUXILIARES
# ============================================================

def normalizar_texto(
    valor,
):
    """
    Converte valores para texto simples e minúsculo.
    """

    if valor is None:

        return ""


    if isinstance(
        valor,
        list,
    ):

        return " ".join(
            normalizar_texto(
                item
            )
            for item in valor
        )


    return str(
        valor
    ).lower()


def remover_duplicados(
    itens,
):
    """
    Remove duplicados preservando a ordem.
    """

    resultado = []


    for item in itens:

        if (
            item
            and item not in resultado
        ):

            resultado.append(
                item
            )


    return resultado


def obter_valor(
    objeto,
    campo,
    padrao=None,
):
    """
    Permite trabalhar tanto com dataclasses/objetos
    quanto com dicionários.
    """

    if isinstance(
        objeto,
        dict,
    ):

        return objeto.get(
            campo,
            padrao,
        )


    return getattr(
        objeto,
        campo,
        padrao,
    )


# ============================================================
# 3. COLETAR EVIDÊNCIAS
# ============================================================

def coletar_evidencias_posicionamento(
    identidade,
    desejos,
    valores,
):
    """
    Reúne evidências já produzidas pelas etapas anteriores.

    Nenhuma nova característica técnica é criada aqui.
    """

    evidencias = []


    # --------------------------------------------------------
    # IDENTIDADE
    # --------------------------------------------------------

    evidencias_identidade = obter_valor(
        identidade,
        "evidencias",
        [],
    ) or []


    evidencias.extend(
        evidencias_identidade
    )


    # --------------------------------------------------------
    # DESEJOS
    # --------------------------------------------------------

    for desejo in desejos:

        evidencias_desejo = obter_valor(
            desejo,
            "evidencias",
            [],
        ) or []


        evidencias.extend(
            evidencias_desejo
        )


    # --------------------------------------------------------
    # VALORES
    # --------------------------------------------------------

    for valor in valores:

        evidencias_valor = obter_valor(
            valor,
            "evidencias",
            [],
        ) or []


        evidencias.extend(
            evidencias_valor
        )


    return remover_duplicados(
        evidencias
    )


# ============================================================
# 4. IDENTIFICAR TRAÇOS DA IDENTIDADE
# ============================================================

def coletar_tracos_identidade(
    identidade,
):
    """
    Reúne os traços dominantes e de apoio.
    """

    dominantes = obter_valor(
        identidade,
        "tracos_dominantes",
        [],
    ) or []


    apoio = obter_valor(
        identidade,
        "tracos_apoio",
        [],
    ) or []


    return remover_duplicados(
        list(
            dominantes
        )
        +
        list(
            apoio
        )
    )


# ============================================================
# 5. IDENTIFICAR VALORES RELEVANTES
# ============================================================

def coletar_valores_percebidos(
    valores,
):
    """
    Extrai os valores percebidos produzidos
    pela etapa anterior.

    O objeto ValorProduto usa o atributo "valor".
    """

    resultado = []


    for item in valores:

        # ----------------------------------------------------
        # NOME CORRETO DO ATRIBUTO:
        # ValorProduto.valor
        # ----------------------------------------------------

        texto = obter_valor(
            item,
            "valor",
            "",
        )


        if texto:

            resultado.append(
                texto
            )


    return remover_duplicados(
        resultado
    )


# ============================================================
# 6. CALCULAR CONFIANÇA
# ============================================================

def calcular_confianca(
    evidencias,
):
    """
    Calcula a confiança do posicionamento
    pela quantidade de evidências disponíveis.
    """

    quantidade = len(
        remover_duplicados(
            evidencias
        )
    )


    if quantidade >= 5:

        return "alta"


    if quantidade >= 3:

        return "media"


    return "baixa"


# ============================================================
# 7. CRIAR DIREÇÃO PRINCIPAL
# ============================================================

def criar_direcao_principal(
    identidade,
):
    """
    Usa a leitura principal da identidade
    como base para a direção estratégica.
    """

    leitura = obter_valor(
        identidade,
        "leitura_principal",
        "",
    )


    if leitura:

        leitura = (
            leitura
            .strip()
            .rstrip(".")
        )


        return (
            "Apresentar o produto a partir de "
            f"{leitura.lower()}, destacando os elementos "
            "visuais que sustentam essa leitura."
        )


    return (
        "Apresentar o produto a partir de suas "
        "características visuais confirmadas."
    )


# ============================================================
# 8. CRIAR TERRITÓRIO DE COMUNICAÇÃO
# ============================================================

def criar_territorio_comunicacao(
    identidade,
):
    """
    Organiza os traços da identidade em um território
    de comunicação sem transformá-los em promessa.
    """

    dominantes = obter_valor(
        identidade,
        "tracos_dominantes",
        [],
    ) or []


    apoio = obter_valor(
        identidade,
        "tracos_apoio",
        [],
    ) or []


    if (
        dominantes
        and apoio
    ):

        principais = " + ".join(
            dominantes
        )

        secundarios = " + ".join(
            apoio
        )


        return (
            f"{principais}, com apoio de "
            f"{secundarios}."
        )


    if dominantes:

        return (
            " + ".join(
                dominantes
            )
            + "."
        )


    return (
        "Comunicação baseada nas características "
        "visuais observadas do produto."
    )


# ============================================================
# 9. DEFINIR O QUE DESTACAR
# ============================================================

def definir_destaques(
    identidade,
    valores,
    evidencias,
):
    """
    Seleciona elementos relevantes para a comunicação.

    O objetivo não é repetir toda a ficha técnica,
    mas identificar os pontos com maior potencial
    de apresentação.
    """

    destaques = []


    texto = normalizar_texto(
        evidencias
    )


    # --------------------------------------------------------
    # ELEMENTOS VISUAIS
    # --------------------------------------------------------

    if "renda" in texto:

        destaques.append(
            "renda e seus detalhes visuais"
        )


    if (
        "transpar" in texto
        or "translúc" in texto
    ):

        destaques.append(
            "transparência e contraste entre "
            "áreas translúcidas e opacas"
        )


    if "canelad" in texto:

        destaques.append(
            "contraste de textura criado "
            "pelo acabamento canelado"
        )


    if "decote" in texto:

        destaques.append(
            "construção visual dos decotes"
        )


    if "punho" in texto:

        destaques.append(
            "acabamento das mangas"
        )


    # --------------------------------------------------------
    # VALORES JÁ IDENTIFICADOS
    # --------------------------------------------------------

    valores_percebidos = (
        coletar_valores_percebidos(
            valores
        )
    )


    texto_valores = normalizar_texto(
        valores_percebidos
    )


    # --------------------------------------------------------
    # COMPOSIÇÃO
    # --------------------------------------------------------

    if (
        "composição têxtil"
        in texto_valores
    ):

        destaques.append(
            "composição têxtil informada"
        )


    # --------------------------------------------------------
    # FORRO / ESTRUTURA INTERNA
    # --------------------------------------------------------

    if (
        "estrutura interna"
        in texto_valores
    ):

        destaques.append(
            "presença e composição do forro"
        )


    # --------------------------------------------------------
    # ACABAMENTO CONSTRUTIVO
    # --------------------------------------------------------

    if (
        "acabamento construtivo"
        in texto_valores
    ):

        destaques.append(
            "detalhes construtivos e acabamentos"
        )


    # --------------------------------------------------------
    # RIQUEZA VISUAL
    # --------------------------------------------------------

    if (
        "riqueza visual"
        in texto_valores
    ):

        destaques.append(
            "riqueza visual da combinação "
            "entre materiais e texturas"
        )


    # --------------------------------------------------------
    # PRESENÇA VISUAL
    # --------------------------------------------------------

    if (
        "presença visual"
        in texto_valores
    ):

        destaques.append(
            "presença visual criada pelo "
            "contraste de materiais"
        )


    return remover_duplicados(
        destaques
    )


# ============================================================
# 10. DEFINIR O QUE EVITAR
# ============================================================

def definir_limites():
    """
    Regras de segurança da comunicação.

    Impede que posicionamento seja confundido
    com promessa comercial sem evidência.
    """

    return [

        (
            "Não prometer conforto sem teste, "
            "avaliação ou informação do fabricante."
        ),

        (
            "Não afirmar alta durabilidade "
            "sem evidência específica."
        ),

        (
            "Não classificar o produto como premium "
            "apenas pela aparência."
        ),

        (
            "Não afirmar que o produto modela, "
            "afina ou valoriza o corpo sem evidência."
        ),

        (
            "Não definir público-alvo apenas "
            "pela aparência do produto."
        ),

        (
            "Não afirmar ocasião de uso como fato "
            "sem contexto adicional."
        ),

        (
            "Não transformar interpretação estética "
            "em característica técnica confirmada."
        ),
    ]


# ============================================================
# 11. ANALISAR POSICIONAMENTO
# ============================================================

def analisar_posicionamento(
    identidade,
    desejos,
    valores,
):
    """
    Constrói o posicionamento estratégico do produto
    a partir das análises anteriores da Aura.
    """

    evidencias = (
        coletar_evidencias_posicionamento(
            identidade,
            desejos,
            valores,
        )
    )


    direcao_principal = (
        criar_direcao_principal(
            identidade
        )
    )


    territorio = (
        criar_territorio_comunicacao(
            identidade
        )
    )


    destacar = definir_destaques(
        identidade,
        valores,
        evidencias,
    )


    evitar = definir_limites()


    confianca = calcular_confianca(
        evidencias
    )


    return PosicionamentoProduto(

        direcao_principal=
            direcao_principal,

        territorio_comunicacao=
            territorio,

        destacar=
            destacar,

        evitar=
            evitar,

        evidencias=
            evidencias,

        confianca=
            confianca,
    )


# ============================================================
# 12. FORMATAR POSICIONAMENTO
# ============================================================

def formatar_posicionamento(
    posicionamento,
):
    """
    Gera uma visualização legível do posicionamento.
    """

    linhas = [

        "POSICIONAMENTO DO PRODUTO",

        "",

        "DIREÇÃO PRINCIPAL",

        posicionamento.direcao_principal,

        "",

        "TERRITÓRIO DE COMUNICAÇÃO",

        posicionamento.territorio_comunicacao,

        "",

        (
            f"CONFIANÇA: "
            f"{posicionamento.confianca}"
        ),

        "",

        "O QUE DESTACAR",

        "",
    ]


    if posicionamento.destacar:

        for item in (
            posicionamento.destacar
        ):

            linhas.append(
                f"- {item}"
            )


    else:

        linhas.append(
            "- Nenhum destaque adicional identificado."
        )


    linhas.extend([
        "",
        "O QUE EVITAR",
        "",
    ])


    for item in (
        posicionamento.evitar
    ):

        linhas.append(
            f"- {item}"
        )


    linhas.extend([
        "",
        "BASE DA LEITURA",
        "",
    ])


    if posicionamento.evidencias:

        for evidencia in (
            posicionamento.evidencias
        ):

            linhas.append(
                f"- {evidencia}"
            )


    else:

        linhas.append(
            "- Nenhuma evidência disponível."
        )


    return "\n".join(
        linhas
    )