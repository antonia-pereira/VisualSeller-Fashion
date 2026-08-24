# ============================================================
# VISUALSELLER FASHION
# AURA — COMUNICAÇÃO DO PRODUTO
# ============================================================

from dataclasses import dataclass, field
from typing import List


# ============================================================
# 1. MODELO DE COMUNICAÇÃO
# ============================================================

@dataclass
class ComunicacaoProduto:
    """
    Define como a Aura deve comunicar o produto
    a partir do posicionamento já construído.

    Esta camada não cria características novas.
    Ela transforma estratégia em direção de linguagem.
    """

    tom: List[str] = field(default_factory=list)

    linguagem: List[str] = field(default_factory=list)

    palavras_priorizar: List[str] = field(default_factory=list)

    abordagens_evitar: List[str] = field(default_factory=list)

    pilares_comunicacao: List[str] = field(default_factory=list)

    mensagem_central: str = ""

    confianca: str = "baixa"

    evidencias: List[str] = field(default_factory=list)


# ============================================================
# 2. FUNÇÕES AUXILIARES
# ============================================================

def adicionar_unico(lista, valor):
    """
    Adiciona um item somente se ele ainda não existir.
    """

    if valor and valor not in lista:
        lista.append(valor)


def texto_normalizado(valor):
    """
    Converte qualquer valor simples para texto minúsculo.
    """

    if valor is None:
        return ""

    if isinstance(valor, list):
        return " ".join(
            str(item)
            for item in valor
        ).lower()

    return str(valor).lower()


# ============================================================
# 3. ANALISAR COMUNICAÇÃO
# ============================================================

def analisar_comunicacao(
    posicionamento,
):
    """
    Converte o posicionamento do produto em uma
    direção de comunicação.

    A comunicação deve respeitar:

    - identidade do produto;
    - posicionamento;
    - evidências disponíveis;
    - limites definidos pela Aura.

    Não deve inventar benefícios ou promessas.
    """

    tom = []
    linguagem = []
    palavras_priorizar = []
    pilares = []
    evidencias = []

    evitar = list(
        getattr(
            posicionamento,
            "evitar",
            [],
        )
        or []
    )

    base_evidencias = list(
        getattr(
            posicionamento,
            "evidencias",
            [],
        )
        or []
    )

    destaques = list(
        getattr(
            posicionamento,
            "destacar",
            [],
        )
        or []
    )

    direcao = getattr(
        posicionamento,
        "direcao_principal",
        "",
    )

    territorio = getattr(
        posicionamento,
        "territorio_comunicacao",
        "",
    )

    confianca_posicionamento = getattr(
        posicionamento,
        "confianca",
        "baixa",
    )

    texto = " ".join([
        texto_normalizado(direcao),
        texto_normalizado(territorio),
        texto_normalizado(destaques),
        texto_normalizado(base_evidencias),
    ])


    # ========================================================
    # 4. TOM
    # ========================================================

    # A Aura não precisa falar de maneira exagerada.
    # O tom acompanha a leitura do produto.

    adicionar_unico(
        tom,
        "sofisticado",
    )

    adicionar_unico(
        tom,
        "claro",
    )

    adicionar_unico(
        tom,
        "sensorial sem exagero",
    )


    if "sensual" in texto:

        adicionar_unico(
            tom,
            "sensual com elegância",
        )


    if (
        "delicade" in texto
        or "floral" in texto
    ):

        adicionar_unico(
            tom,
            "delicado nos detalhes",
        )


    if (
        "contraste" in texto
        or "marcante" in texto
    ):

        adicionar_unico(
            tom,
            "seguro e visualmente expressivo",
        )


    # ========================================================
    # 5. LINGUAGEM
    # ========================================================

    adicionar_unico(
        linguagem,
        "descrever características visíveis antes de interpretá-las",
    )

    adicionar_unico(
        linguagem,
        "relacionar detalhes do produto à sua presença visual",
    )

    adicionar_unico(
        linguagem,
        "usar interpretação estética como possibilidade, não como fato técnico",
    )


    if "transpar" in texto:

        adicionar_unico(
            linguagem,
            "explorar a transparência como elemento de composição visual",
        )


    if "contraste" in texto:

        adicionar_unico(
            linguagem,
            "destacar o contraste entre superfícies, texturas e níveis de transparência",
        )


    if "renda" in texto:

        adicionar_unico(
            linguagem,
            "valorizar os detalhes visuais da renda",
        )


    if "canelad" in texto:

        adicionar_unico(
            linguagem,
            "mostrar como o acabamento canelado participa da construção visual",
        )


    # ========================================================
    # 6. PALAVRAS A PRIORIZAR
    # ========================================================

    mapa_palavras = {
        "renda": "renda",
        "transpar": "transparência",
        "contraste": "contraste",
        "textura": "textura",
        "canelad": "acabamento canelado",
        "floral": "detalhes florais",
        "decote": "decote",
        "delicade": "delicadeza",
        "sensual": "sensualidade",
        "presença visual": "presença visual",
    }


    for sinal, palavra in mapa_palavras.items():

        if sinal in texto:

            adicionar_unico(
                palavras_priorizar,
                palavra,
            )


    # ========================================================
    # 7. PILARES DE COMUNICAÇÃO
    # ========================================================

    if "sensual" in texto:

        adicionar_unico(
            pilares,
            "sensualidade construída pelos elementos visuais",
        )


    if "contraste" in texto:

        adicionar_unico(
            pilares,
            "contraste entre transparência, opacidade e textura",
        )


    if (
        "delicade" in texto
        or "floral" in texto
    ):

        adicionar_unico(
            pilares,
            "delicadeza presente nos detalhes",
        )


    if (
        "acabamento" in texto
        or "construção" in texto
    ):

        adicionar_unico(
            pilares,
            "detalhes de construção e acabamento",
        )


    # ========================================================
    # 8. EVIDÊNCIAS
    # ========================================================

    for evidencia in base_evidencias:

        adicionar_unico(
            evidencias,
            evidencia,
        )


    # ========================================================
    # 9. MENSAGEM CENTRAL
    # ========================================================

    if (
        "sensual" in texto
        and "contraste" in texto
    ):

        mensagem_central = (
            "Uma peça cuja presença visual nasce da combinação "
            "entre sensualidade, transparência, renda e contrastes "
            "de textura, com detalhes que acrescentam delicadeza "
            "à composição."
        )

    elif "sensual" in texto:

        mensagem_central = (
            "Uma peça construída visualmente a partir de elementos "
            "que sugerem sensualidade, com atenção aos detalhes "
            "que sustentam essa leitura."
        )

    elif "contraste" in texto:

        mensagem_central = (
            "Uma peça marcada pelo contraste entre diferentes "
            "superfícies, texturas e elementos visuais."
        )

    else:

        mensagem_central = (
            "Apresentar o produto a partir de suas características "
            "visuais confirmadas, valorizando os elementos que "
            "sustentam sua identidade."
        )


    # ========================================================
    # 10. CONFIANÇA
    # ========================================================

    if (
        confianca_posicionamento == "alta"
        and len(evidencias) >= 3
    ):

        confianca = "alta"

    elif evidencias:

        confianca = "media"

    else:

        confianca = "baixa"


    # ========================================================
    # 11. RETORNO
    # ========================================================

    return ComunicacaoProduto(

        tom=tom,

        linguagem=linguagem,

        palavras_priorizar=palavras_priorizar,

        abordagens_evitar=evitar,

        pilares_comunicacao=pilares,

        mensagem_central=mensagem_central,

        confianca=confianca,

        evidencias=evidencias,
    )


# ============================================================
# 12. FORMATAR COMUNICAÇÃO
# ============================================================

def formatar_comunicacao(
    comunicacao,
):
    """
    Formata a estratégia de comunicação
    para leitura humana.
    """

    linhas = [
        "COMUNICAÇÃO DO PRODUTO",
        "",
        "MENSAGEM CENTRAL",
        comunicacao.mensagem_central,
        "",
        f"CONFIANÇA: {comunicacao.confianca}",
        "",
        "TOM",
        "",
    ]


    for item in comunicacao.tom:

        linhas.append(
            f"- {item}"
        )


    linhas.extend([
        "",
        "LINGUAGEM",
        "",
    ])


    for item in comunicacao.linguagem:

        linhas.append(
            f"- {item}"
        )


    linhas.extend([
        "",
        "PILARES DE COMUNICAÇÃO",
        "",
    ])


    for item in comunicacao.pilares_comunicacao:

        linhas.append(
            f"- {item}"
        )


    linhas.extend([
        "",
        "PALAVRAS A PRIORIZAR",
        "",
    ])


    for item in comunicacao.palavras_priorizar:

        linhas.append(
            f"- {item}"
        )


    linhas.extend([
        "",
        "ABORDAGENS A EVITAR",
        "",
    ])


    for item in comunicacao.abordagens_evitar:

        linhas.append(
            f"- {item}"
        )


    linhas.extend([
        "",
        "BASE DA COMUNICAÇÃO",
        "",
    ])


    for evidencia in comunicacao.evidencias:

        linhas.append(
            f"- {evidencia}"
        )


    return "\n".join(
        linhas
    )