# ============================================================
# VISUALSELLER FASHION
# AURA — BRIEFING DE IMAGEM
# ============================================================

from dataclasses import dataclass, field
from typing import List


# ============================================================
# 1. MODELO DE BRIEFING INDIVIDUAL
# ============================================================

@dataclass
class BriefImagem:
    """
    Representa o briefing executável de uma imagem.

    O briefing traduz o plano visual da Aura
    em instruções de produção visual.
    """

    numero: int

    funcao: str

    objetivo: str

    mensagem: str

    enquadramento: str = ""

    foco_principal: str = ""

    composicao: List[str] = field(
        default_factory=list
    )

    iluminacao: List[str] = field(
        default_factory=list
    )

    fundo: List[str] = field(
        default_factory=list
    )

    destacar: List[str] = field(
        default_factory=list
    )

    textos: List[str] = field(
        default_factory=list
    )

    preservar: List[str] = field(
        default_factory=list
    )

    evitar: List[str] = field(
        default_factory=list
    )

    evidencias: List[str] = field(
        default_factory=list
    )

    confianca: str = "media"


# ============================================================
# 2. MODELO DO CONJUNTO DE BRIEFINGS
# ============================================================

@dataclass
class BriefingVisualProduto:
    """
    Representa todos os briefings visuais
    do anúncio.
    """

    conceito_geral: str

    direcao_geral: str

    briefings: List[BriefImagem] = field(
        default_factory=list
    )

    regras_globais: List[str] = field(
        default_factory=list
    )

    confianca: str = "media"


# ============================================================
# 3. FUNÇÕES AUXILIARES
# ============================================================

def texto_seguro(
    valor,
):
    """
    Converte qualquer valor em texto simples.
    """

    if valor is None:
        return ""

    return str(
        valor
    ).strip()


def lista_segura(
    valor,
):
    """
    Garante que um valor seja tratado como lista.
    """

    if valor is None:
        return []

    if isinstance(
        valor,
        list,
    ):
        return valor

    if isinstance(
        valor,
        tuple,
    ):
        return list(
            valor
        )

    return [
        valor
    ]


def adicionar_unico(
    lista,
    valor,
):
    """
    Adiciona um valor apenas uma vez.
    """

    valor = texto_seguro(
        valor
    )

    if (
        valor
        and valor not in lista
    ):
        lista.append(
            valor
        )


def obter_dados_ficha(
    ficha,
):
    """
    Converte a ficha para dicionário.
    """

    if ficha is None:
        return {}

    if hasattr(
        ficha,
        "model_dump",
    ):
        return ficha.model_dump()

    if isinstance(
        ficha,
        dict,
    ):
        return ficha

    return vars(
        ficha
    )


# ============================================================
# 4. IDENTIFICAR COR PRINCIPAL
# ============================================================

def obter_cor_principal(
    ficha,
):
    """
    Retorna a primeira cor confirmada da ficha.
    """

    dados = obter_dados_ficha(
        ficha
    )

    cores = (
        dados.get(
            "cores_disponiveis"
        )
        or []
    )

    if cores:

        return texto_seguro(
            cores[0]
        )

    return ""


# ============================================================
# 5. REGRAS DE PRESERVAÇÃO DO PRODUTO
# ============================================================

def criar_regras_preservacao(
    ficha,
):
    """
    Define quais características confirmadas
    nunca devem ser modificadas durante
    a produção das imagens.
    """

    dados = obter_dados_ficha(
        ficha
    )

    preservar = []


    # --------------------------------------------------------
    # COR
    # --------------------------------------------------------

    cor = obter_cor_principal(
        ficha
    )

    if cor:

        adicionar_unico(
            preservar,
            f"cor real da peça: {cor}",
        )


    # --------------------------------------------------------
    # MATERIAIS VISUAIS
    # --------------------------------------------------------

    materiais = (
        dados.get(
            "materiais_visuais"
        )
        or []
    )

    for material in materiais:

        adicionar_unico(
            preservar,
            f"material visual identificado: {material}",
        )


    # --------------------------------------------------------
    # MANGA
    # --------------------------------------------------------

    manga = texto_seguro(
        dados.get(
            "manga"
        )
    )

    if manga:

        adicionar_unico(
            preservar,
            f"comprimento e formato das mangas: {manga}",
        )


    # --------------------------------------------------------
    # ACABAMENTO DE MANGA
    # --------------------------------------------------------

    acabamento_mangas = texto_seguro(
        dados.get(
            "acabamento_mangas"
        )
    )

    if acabamento_mangas:

        adicionar_unico(
            preservar,
            f"acabamento das mangas: {acabamento_mangas}",
        )


    # --------------------------------------------------------
    # DECOTE FRONTAL
    # --------------------------------------------------------

    decote_frente = texto_seguro(
        dados.get(
            "decote_frente"
        )
    )

    if decote_frente:

        adicionar_unico(
            preservar,
            f"formato do decote frontal: {decote_frente}",
        )


    # --------------------------------------------------------
    # DECOTE COSTAS
    # --------------------------------------------------------

    decote_costas = texto_seguro(
        dados.get(
            "decote_costas"
        )
    )

    if decote_costas:

        adicionar_unico(
            preservar,
            f"formato do decote das costas: {decote_costas}",
        )


    # --------------------------------------------------------
    # FECHAMENTO
    # --------------------------------------------------------

    fechamento = texto_seguro(
        dados.get(
            "fechamento"
        )
    )

    if fechamento:

        adicionar_unico(
            preservar,
            f"tipo de fechamento: {fechamento}",
        )


    # --------------------------------------------------------
    # TRANSPARÊNCIA
    # --------------------------------------------------------

    transparencia = texto_seguro(
        dados.get(
            "transparencia"
        )
    )

    if transparencia:

        adicionar_unico(
            preservar,
            (
                "nível e localização da transparência "
                f"conforme observado: {transparencia}"
            ),
        )


    return preservar


# ============================================================
# 6. REGRAS GLOBAIS
# ============================================================

def criar_regras_globais(
    plano_visual,
):
    """
    Define regras que todas as imagens
    da campanha devem seguir.
    """

    regras = [

        (
            "O produto deve permanecer visualmente "
            "consistente em toda a sequência."
        ),

        (
            "Cor, modelagem, renda, transparência, "
            "texturas e acabamentos não podem ser "
            "alterados para fins estéticos."
        ),

        (
            "A iluminação deve revelar o produto "
            "sem modificar visualmente sua cor real."
        ),

        (
            "O fundo deve apoiar a leitura do produto "
            "e não competir com ele."
        ),

        (
            "A hierarquia visual deve manter "
            "o produto como protagonista."
        ),

        (
            "Os textos devem ser curtos e coerentes "
            "com a função específica de cada imagem."
        ),

        (
            "Não adicionar acessórios, elementos ou "
            "características que possam ser confundidos "
            "com partes do produto."
        ),

        (
            "Todas as imagens devem parecer parte "
            "da mesma campanha visual."
        ),
    ]


    for regra in lista_segura(
        getattr(
            plano_visual,
            "evitar",
            [],
        )
    ):

        adicionar_unico(
            regras,
            regra,
        )


    return regras


# ============================================================
# 7. ENQUADRAMENTO POR FUNÇÃO
# ============================================================

def definir_enquadramento(
    funcao,
):
    """
    Define um enquadramento inicial
    de acordo com a função da imagem.
    """

    funcao = texto_seguro(
        funcao
    ).lower()


    if funcao == "capa":

        return (
            "Plano aberto ou médio mostrando "
            "o produto inteiro com leitura imediata."
        )


    if "detalhes visuais" in funcao:

        return (
            "Close ou plano de detalhe, aproximando "
            "renda, transparência e superfícies."
        )


    if "construção" in funcao:

        return (
            "Enquadramentos médios e detalhes técnicos, "
            "permitindo visualizar frente, costas, "
            "mangas e fechamento."
        )


    if "texturas" in funcao:

        return (
            "Close de alta definição para revelar "
            "textura, trama, renda e acabamento."
        )


    if "informação técnica" in funcao:

        return (
            "Composição limpa e organizada, "
            "com espaço visual para informações técnicas."
        )


    if "síntese" in funcao:

        return (
            "Composição editorial com produto "
            "e detalhes principais em hierarquia visual."
        )


    if "fechamento" in funcao:

        return (
            "Plano de impacto com o produto novamente "
            "como protagonista da composição."
        )


    return (
        "Enquadramento adequado ao elemento "
        "principal definido no plano visual."
    )


# ============================================================
# 8. FOCO PRINCIPAL POR FUNÇÃO
# ============================================================

def definir_foco_principal(
    imagem_plano,
):
    """
    Define o foco principal a partir dos elementos
    que o plano visual mandou destacar.
    """

    destaques = lista_segura(
        getattr(
            imagem_plano,
            "destacar",
            [],
        )
    )


    if not destaques:

        return (
            "produto como elemento principal"
        )


    if len(
        destaques
    ) == 1:

        return texto_seguro(
            destaques[0]
        )


    return (
        texto_seguro(
            destaques[0]
        )
        +
        " + "
        +
        texto_seguro(
            destaques[1]
        )
    )


# ============================================================
# 9. COMPOSIÇÃO POR FUNÇÃO
# ============================================================

def definir_composicao(
    imagem_plano,
):
    """
    Define princípios de composição.
    """

    funcao = texto_seguro(
        getattr(
            imagem_plano,
            "funcao",
            "",
        )
    ).lower()

    composicao = []


    if funcao == "capa":

        adicionar_unico(
            composicao,
            "produto central ou em posição de forte protagonismo",
        )

        adicionar_unico(
            composicao,
            "silhueta completa claramente visível",
        )

        adicionar_unico(
            composicao,
            "espaço negativo suficiente para título e marca",
        )

        adicionar_unico(
            composicao,
            "evitar excesso de elementos gráficos",
        )


    elif "detalhes visuais" in funcao:

        adicionar_unico(
            composicao,
            "aproximação suficiente para revelar a renda",
        )

        adicionar_unico(
            composicao,
            "mostrar simultaneamente áreas translúcidas e opacas quando possível",
        )

        adicionar_unico(
            composicao,
            "priorizar leitura do material antes do texto",
        )


    elif "construção" in funcao:

        adicionar_unico(
            composicao,
            "organizar frente, costas e detalhes de forma comparável",
        )

        adicionar_unico(
            composicao,
            "destacar decotes, mangas e fechamento",
        )

        adicionar_unico(
            composicao,
            "evitar cortes que escondam elementos estruturais importantes",
        )


    elif "texturas" in funcao:

        adicionar_unico(
            composicao,
            "macro ou close dos materiais",
        )

        adicionar_unico(
            composicao,
            "mostrar diferenças entre renda, transparência e malha canelada",
        )

        adicionar_unico(
            composicao,
            "usar profundidade visual sem perder nitidez do produto",
        )


    elif "informação técnica" in funcao:

        adicionar_unico(
            composicao,
            "layout limpo e informativo",
        )

        adicionar_unico(
            composicao,
            "produto ou detalhe ocupando uma área secundária da composição",
        )

        adicionar_unico(
            composicao,
            "informações técnicas organizadas em hierarquia clara",
        )


    elif "síntese" in funcao:

        adicionar_unico(
            composicao,
            "reunir os principais diferenciais sem repetir a capa",
        )

        adicionar_unico(
            composicao,
            "usar detalhes selecionados como apoio ao produto",
        )

        adicionar_unico(
            composicao,
            "criar hierarquia visual entre produto e diferenciais",
        )


    elif "fechamento" in funcao:

        adicionar_unico(
            composicao,
            "retomar o produto inteiro ou sua leitura mais reconhecível",
        )

        adicionar_unico(
            composicao,
            "usar composição mais limpa que as imagens intermediárias",
        )

        adicionar_unico(
            composicao,
            "encerrar a sequência com forte unidade visual",
        )


    else:

        adicionar_unico(
            composicao,
            "produto como protagonista",
        )


    return composicao


# ============================================================
# 10. ILUMINAÇÃO
# ============================================================

def definir_iluminacao(
    imagem_plano,
):
    """
    Define como a luz deve colaborar
    com a função da imagem.
    """

    funcao = texto_seguro(
        getattr(
            imagem_plano,
            "funcao",
            "",
        )
    ).lower()

    iluminacao = []


    adicionar_unico(
        iluminacao,
        (
            "luz controlada que preserve "
            "a cor real do produto"
        ),
    )


    if (
        "detalhes"
        in funcao
        or "texturas"
        in funcao
    ):

        adicionar_unico(
            iluminacao,
            (
                "luz lateral ou suave suficiente "
                "para revelar textura e relevo"
            ),
        )


    if (
        "transpar"
        in texto_seguro(
            getattr(
                imagem_plano,
                "mensagem",
                "",
            )
        ).lower()
    ):

        adicionar_unico(
            iluminacao,
            (
                "iluminação que permita perceber "
                "a transparência sem exagerá-la"
            ),
        )


    if funcao == "capa":

        adicionar_unico(
            iluminacao,
            (
                "iluminação equilibrada sobre "
                "todo o produto"
            ),
        )


    if "informação técnica" in funcao:

        adicionar_unico(
            iluminacao,
            (
                "luz uniforme e neutra para "
                "facilitar leitura objetiva"
            ),
        )


    return iluminacao


# ============================================================
# 11. FUNDO
# ============================================================

def definir_fundo(
    imagem_plano,
    ficha,
):
    """
    Define princípios de fundo sem impor
    uma estética que altere o produto.
    """

    funcao = texto_seguro(
        getattr(
            imagem_plano,
            "funcao",
            "",
        )
    ).lower()

    cor = obter_cor_principal(
        ficha
    ).lower()

    fundo = []


    adicionar_unico(
        fundo,
        "fundo sem elementos que confundam a leitura do produto",
    )


    if cor == "preto":

        adicionar_unico(
            fundo,
            (
                "evitar fundo preto puro quando "
                "isso fizer a peça perder contorno"
            ),
        )

        adicionar_unico(
            fundo,
            (
                "usar contraste suficiente para "
                "separar visualmente a peça do fundo"
            ),
        )


    if funcao == "capa":

        adicionar_unico(
            fundo,
            "fundo limpo e visualmente sofisticado",
        )


    elif "detalhes" in funcao:

        adicionar_unico(
            fundo,
            (
                "fundo discreto para manter "
                "atenção sobre textura e renda"
            ),
        )


    elif "informação técnica" in funcao:

        adicionar_unico(
            fundo,
            (
                "fundo neutro com alta legibilidade "
                "para textos informativos"
            ),
        )


    elif "fechamento" in funcao:

        adicionar_unico(
            fundo,
            (
                "retomar a linguagem visual "
                "estabelecida na capa"
            ),
        )


    else:

        adicionar_unico(
            fundo,
            "manter coerência com a identidade visual da campanha",
        )


    return fundo


# ============================================================
# 12. CRIAR BRIEFING INDIVIDUAL
# ============================================================

def criar_brief_imagem(
    imagem_plano,
    ficha,
    regras_preservacao,
    regras_globais,
):
    """
    Transforma uma imagem do plano visual
    em um briefing de produção.
    """

    numero = getattr(
        imagem_plano,
        "numero",
        0,
    )

    funcao = texto_seguro(
        getattr(
            imagem_plano,
            "funcao",
            "",
        )
    )

    objetivo = texto_seguro(
        getattr(
            imagem_plano,
            "objetivo",
            "",
        )
    )

    mensagem = texto_seguro(
        getattr(
            imagem_plano,
            "mensagem",
            "",
        )
    )

    destacar = lista_segura(
        getattr(
            imagem_plano,
            "destacar",
            [],
        )
    )

    textos = lista_segura(
        getattr(
            imagem_plano,
            "textos_sugeridos",
            [],
        )
    )

    evidencias = lista_segura(
        getattr(
            imagem_plano,
            "evidencias",
            [],
        )
    )

    confianca = texto_seguro(
        getattr(
            imagem_plano,
            "confianca",
            "media",
        )
    )


    # --------------------------------------------------------
    # O QUE EVITAR
    # --------------------------------------------------------

    evitar = []

    for regra in regras_globais:

        adicionar_unico(
            evitar,
            regra,
        )


    # --------------------------------------------------------
    # CRIAR BRIEF
    # --------------------------------------------------------

    return BriefImagem(

        numero=
            numero,

        funcao=
            funcao,

        objetivo=
            objetivo,

        mensagem=
            mensagem,

        enquadramento=
            definir_enquadramento(
                funcao
            ),

        foco_principal=
            definir_foco_principal(
                imagem_plano
            ),

        composicao=
            definir_composicao(
                imagem_plano
            ),

        iluminacao=
            definir_iluminacao(
                imagem_plano
            ),

        fundo=
            definir_fundo(
                imagem_plano,
                ficha,
            ),

        destacar=
            destacar,

        textos=
            [
                texto
                for texto in textos
                if texto_seguro(texto)
            ],

        preservar=
            list(
                regras_preservacao
            ),

        evitar=
            evitar,

        evidencias=
            [
                evidencia
                for evidencia in evidencias
                if texto_seguro(evidencia)
            ],

        confianca=
            confianca,
    )


# ============================================================
# 13. GERAR TODOS OS BRIEFINGS
# ============================================================

def criar_briefings_imagem(
    ficha,
    plano_visual,
):
    """
    Transforma todo o plano visual
    em briefings executáveis de imagem.
    """

    preservar = criar_regras_preservacao(
        ficha
    )

    regras_globais = criar_regras_globais(
        plano_visual
    )

    briefings = []


    for imagem in lista_segura(
        getattr(
            plano_visual,
            "imagens",
            [],
        )
    ):

        briefing = criar_brief_imagem(
            imagem_plano=imagem,
            ficha=ficha,
            regras_preservacao=preservar,
            regras_globais=regras_globais,
        )

        briefings.append(
            briefing
        )


    # --------------------------------------------------------
    # CONFIANÇA GERAL
    # --------------------------------------------------------

    confiancas_altas = sum(

        1

        for briefing in briefings

        if (
            briefing.confianca.lower()
            == "alta"
        )
    )


    if (
        briefings
        and confiancas_altas
        == len(
            briefings
        )
    ):

        confianca = "alta"


    elif briefings:

        confianca = "media"


    else:

        confianca = "baixa"


    return BriefingVisualProduto(

        conceito_geral=
            texto_seguro(
                getattr(
                    plano_visual,
                    "conceito_visual",
                    "",
                )
            ),

        direcao_geral=
            texto_seguro(
                getattr(
                    plano_visual,
                    "direcao_visual",
                    "",
                )
            ),

        briefings=
            briefings,

        regras_globais=
            regras_globais,

        confianca=
            confianca,
    )


# ============================================================
# 14. ALIAS
# ============================================================

def gerar_briefings_imagem(
    ficha,
    plano_visual,
):
    """
    Alias para uso futuro no fluxo principal.
    """

    return criar_briefings_imagem(
        ficha=ficha,
        plano_visual=plano_visual,
    )


# ============================================================
# 15. FORMATAR BRIEFING INDIVIDUAL
# ============================================================

def formatar_brief_imagem(
    briefing,
):
    """
    Formata um briefing individual.
    """

    linhas = [

        f"IMAGEM {briefing.numero}",

        "",

        f"FUNÇÃO: {briefing.funcao}",

        f"CONFIANÇA: {briefing.confianca}",

        "",

        "OBJETIVO",

        briefing.objetivo,

        "",

        "MENSAGEM",

        briefing.mensagem,

        "",

        "ENQUADRAMENTO",

        briefing.enquadramento,

        "",

        "FOCO PRINCIPAL",

        briefing.foco_principal,

        "",

        "COMPOSIÇÃO",

    ]


    for item in briefing.composicao:

        linhas.append(
            f"- {item}"
        )


    linhas.extend(
        [
            "",
            "ILUMINAÇÃO",
        ]
    )


    for item in briefing.iluminacao:

        linhas.append(
            f"- {item}"
        )


    linhas.extend(
        [
            "",
            "FUNDO",
        ]
    )


    for item in briefing.fundo:

        linhas.append(
            f"- {item}"
        )


    linhas.extend(
        [
            "",
            "DESTACAR",
        ]
    )


    for item in briefing.destacar:

        linhas.append(
            f"- {item}"
        )


    linhas.extend(
        [
            "",
            "TEXTOS SUGERIDOS",
        ]
    )


    if briefing.textos:

        for item in briefing.textos:

            linhas.append(
                f"- {item}"
            )

    else:

        linhas.append(
            "- Sem texto obrigatório."
        )


    linhas.extend(
        [
            "",
            "PRESERVAR NO PRODUTO",
        ]
    )


    for item in briefing.preservar:

        linhas.append(
            f"- {item}"
        )


    linhas.extend(
        [
            "",
            "EVIDÊNCIAS",
        ]
    )


    if briefing.evidencias:

        for item in briefing.evidencias:

            linhas.append(
                f"- {item}"
            )

    else:

        linhas.append(
            "- Nenhuma evidência específica."
        )


    return "\n".join(
        linhas
    )


# ============================================================
# 16. FORMATAR TODOS OS BRIEFINGS
# ============================================================

def formatar_briefings_imagem(
    resultado,
):
    """
    Formata todo o pacote de briefings.
    """

    linhas = [

        "BRIEFING VISUAL DO PRODUTO",

        "",

        "CONCEITO GERAL",

        resultado.conceito_geral,

        "",

        "DIREÇÃO GERAL",

        resultado.direcao_geral,

        "",

        (
            f"CONFIANÇA: "
            f"{resultado.confianca}"
        ),

        "",

        "============================================",

        "",
    ]


    for indice, briefing in enumerate(
        resultado.briefings
    ):

        linhas.append(
            formatar_brief_imagem(
                briefing
            )
        )


        if (
            indice
            < len(
                resultado.briefings
            ) - 1
        ):

            linhas.extend(
                [
                    "",
                    "--------------------------------------------",
                    "",
                ]
            )


    linhas.extend(
        [
            "",
            "============================================",
            "",
            "REGRAS GLOBAIS DA CAMPANHA",
            "",
        ]
    )


    for regra in resultado.regras_globais:

        linhas.append(
            f"- {regra}"
        )


    return "\n".join(
        linhas
    )