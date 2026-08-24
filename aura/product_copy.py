# ============================================================
# VISUALSELLER FASHION
# AURA — COPY COMERCIAL DO PRODUTO
# ============================================================

from dataclasses import dataclass, field
from typing import List


# ============================================================
# 1. MODELO DA COPY
# ============================================================

@dataclass
class CopyProduto:
    """
    Representa a primeira copy comercial estruturada
    produzida pela Aura.
    """

    titulo: str = ""

    descricao_curta: str = ""

    descricao_completa: str = ""

    bullets: List[str] = field(
        default_factory=list
    )

    frases_evitar: List[str] = field(
        default_factory=list
    )

    confianca: str = "baixa"


# ============================================================
# 2. FUNÇÕES AUXILIARES
# ============================================================

def limpar_texto(
    valor,
):
    """
    Converte um valor em texto limpo.
    """

    if valor is None:

        return ""

    return str(
        valor
    ).strip()


# ============================================================
# 3. PLURALIZAR DESCRIÇÃO DA MANGA
# ============================================================

def pluralizar_manga(
    valor,
):
    """
    Ajusta a descrição da manga quando ela é usada
    depois da palavra "mangas".

    Exemplos:

    longa -> longas
    curta -> curtas
    longa bufante -> longas bufantes
    ampla -> amplas
    justa -> justas
    """

    texto = limpar_texto(
        valor
    ).lower()


    if not texto:

        return ""


    palavras = texto.split()


    mapa_plural = {

        "longa":
            "longas",

        "curta":
            "curtas",

        "bufante":
            "bufantes",

        "ampla":
            "amplas",

        "justa":
            "justas",

        "ajustada":
            "ajustadas",

        "transparente":
            "transparentes",

        "canelada":
            "caneladas",

        "larga":
            "largas",

        "estreita":
            "estreitas",
    }


    palavras_pluralizadas = []


    for palavra in palavras:

        palavras_pluralizadas.append(
            mapa_plural.get(
                palavra,
                palavra,
            )
        )


    return " ".join(
        palavras_pluralizadas
    )


# ============================================================
# 4. ADICIONAR ITEM ÚNICO
# ============================================================

def adicionar_unico(
    lista,
    valor,
):
    """
    Adiciona um valor somente se ele ainda
    não estiver presente na lista.
    """

    valor = limpar_texto(
        valor
    )


    if (
        valor
        and valor not in lista
    ):

        lista.append(
            valor
        )


# ============================================================
# 5. REMOVER TIPO REPETIDO
# ============================================================

def remover_tipo_repetido(
    tipo_produto,
    nome_modelo,
):
    """
    Evita títulos como:

    Body Body Dubai

    Se o nome do modelo já começar com o tipo
    do produto, mantém apenas o nome do modelo.
    """

    tipo = limpar_texto(
        tipo_produto
    )

    modelo = limpar_texto(
        nome_modelo
    )


    if not modelo:

        return tipo


    if not tipo:

        return modelo


    if modelo.lower().startswith(
        tipo.lower()
    ):

        return modelo


    return (
        f"{tipo} {modelo}"
    )


# ============================================================
# 6. TÍTULO
# ============================================================

def gerar_titulo(
    ficha,
):
    """
    Gera um título comercial simples
    sem redundância entre tipo e modelo.
    """

    dados = ficha.model_dump()


    tipo_produto = dados.get(
        "tipo_produto"
    )


    nome_modelo = dados.get(
        "nome_modelo"
    )


    marca = limpar_texto(
        dados.get(
            "marca"
        )
    )


    cores = (
        dados.get(
            "cores_disponiveis"
        )
        or []
    )


    produto = remover_tipo_repetido(
        tipo_produto,
        nome_modelo,
    )


    partes = []


    adicionar_unico(
        partes,
        produto,
    )


    if cores:

        adicionar_unico(
            partes,
            limpar_texto(
                cores[0]
            ),
        )


    titulo = " ".join(
        partes
    )


    if marca:

        titulo = (
            f"{titulo} — {marca}"
        )


    return titulo.strip()


# ============================================================
# 7. DESCRIÇÃO CURTA
# ============================================================

def gerar_descricao_curta(
    ficha,
    posicionamento,
    comunicacao,
):
    """
    Cria uma descrição curta comercial.

    A descrição usa apenas características
    sustentadas pela ficha e pela estratégia
    já construída pela Aura.
    """

    dados = ficha.model_dump()


    materiais = (
        dados.get(
            "materiais_visuais"
        )
        or []
    )


    transparencia = limpar_texto(
        dados.get(
            "transparencia"
        )
    )


    elementos = []


    # --------------------------------------------------------
    # RENDA
    # --------------------------------------------------------

    for material in materiais:

        material_texto = limpar_texto(
            material
        )


        if (
            "renda"
            in material_texto.lower()
        ):

            adicionar_unico(
                elementos,
                material_texto,
            )


    # --------------------------------------------------------
    # TRANSPARÊNCIA
    # --------------------------------------------------------

    if transparencia:

        adicionar_unico(
            elementos,
            "transparência localizada",
        )


    # --------------------------------------------------------
    # TEXTURAS
    # --------------------------------------------------------

    possui_texturas = any(

        (
            "canelad"
            in limpar_texto(
                material
            ).lower()
        )

        for material in materiais
    )


    if possui_texturas:

        adicionar_unico(
            elementos,
            "contrastes de textura",
        )


    # --------------------------------------------------------
    # CONSTRUIR FRASE
    # --------------------------------------------------------

    if len(
        elementos
    ) >= 3:

        descricao = (

            "Peça de presença visual marcante, "
            f"com {elementos[0]}, "
            f"{elementos[1]} e "
            f"{elementos[2]}, equilibrando "
            "sensualidade e delicadeza na "
            "composição visual."
        )


    elif len(
        elementos
    ) == 2:

        descricao = (

            "Peça de presença visual marcante, "
            f"com {elementos[0]} e "
            f"{elementos[1]}, em uma composição "
            "que combina sensualidade e "
            "delicadeza."
        )


    elif len(
        elementos
    ) == 1:

        descricao = (

            "Peça com presença visual marcada "
            f"por {elementos[0]}."
        )


    else:

        mensagem = limpar_texto(
            getattr(
                comunicacao,
                "mensagem_central",
                "",
            )
        )


        if mensagem:

            descricao = mensagem


        else:

            descricao = (

                "Peça com construção visual "
                "marcante e detalhes de destaque."
            )


    return descricao


# ============================================================
# 8. BULLETS
# ============================================================

def gerar_bullets(
    ficha,
):
    """
    Seleciona informações concretas e úteis
    para uma apresentação comercial.

    Mantém a lista curta e evita repetir toda
    a estratégia interna da Aura.
    """

    dados = ficha.model_dump()

    bullets = []


    # --------------------------------------------------------
    # MATERIAIS VISUAIS
    # --------------------------------------------------------

    materiais = (
        dados.get(
            "materiais_visuais"
        )
        or []
    )


    renda = ""


    for material in materiais:

        material_texto = limpar_texto(
            material
        )


        if (
            "renda"
            in material_texto.lower()
        ):

            renda = material_texto

            break


    transparencia = limpar_texto(
        dados.get(
            "transparencia"
        )
    )


    if (
        renda
        and transparencia
    ):

        adicionar_unico(
            bullets,
            (
                f"{renda.capitalize()} "
                "com transparência localizada"
            ),
        )


    elif renda:

        adicionar_unico(
            bullets,
            renda.capitalize(),
        )


    # --------------------------------------------------------
    # MANGAS
    # --------------------------------------------------------

    manga = limpar_texto(
        dados.get(
            "manga"
        )
    )


    acabamento_mangas = limpar_texto(
        dados.get(
            "acabamento_mangas"
        )
    )


    if (
        manga
        and acabamento_mangas
    ):

        if (
            "punho"
            in acabamento_mangas.lower()
        ):

            adicionar_unico(
                bullets,
                (
                    f"Mangas "
                    f"{pluralizar_manga(manga)} "
                    f"com "
                    f"{acabamento_mangas.lower().rstrip('.')}"
                ),
            )


        else:

            adicionar_unico(
                bullets,
                (
                    f"Mangas "
                    f"{pluralizar_manga(manga)} — "
                    f"{acabamento_mangas.rstrip('.')}"
                ),
            )


    elif manga:

        adicionar_unico(
            bullets,
            (
                f"Mangas "
                f"{pluralizar_manga(manga)}"
            ),
        )


    # --------------------------------------------------------
    # DECOTES
    # --------------------------------------------------------

    decote_frente = limpar_texto(
        dados.get(
            "decote_frente"
        )
    )


    decote_costas = limpar_texto(
        dados.get(
            "decote_costas"
        )
    )


    if (
        decote_frente
        and decote_costas
    ):

        adicionar_unico(
            bullets,
            (
                f"Decote frontal "
                f"{decote_frente} "
                f"e decote nas costas "
                f"{decote_costas}"
            ),
        )


    elif decote_frente:

        adicionar_unico(
            bullets,
            (
                f"Decote frontal "
                f"{decote_frente}"
            ),
        )


    # --------------------------------------------------------
    # FECHAMENTO
    # --------------------------------------------------------

    fechamento = limpar_texto(
        dados.get(
            "fechamento"
        )
    )


    if fechamento:

        adicionar_unico(
            bullets,
            (
                f"Fechamento por "
                f"{fechamento.lower()}"
            ),
        )


    # --------------------------------------------------------
    # FORRO
    # --------------------------------------------------------

    possui_forro = dados.get(
        "possui_forro"
    )


    composicao_forro = limpar_texto(
        dados.get(
            "composicao_forro"
        )
    )


    if (
        possui_forro
        and composicao_forro
    ):

        adicionar_unico(
            bullets,
            (
                f"Forro "
                f"{composicao_forro}"
            ),
        )


    elif possui_forro:

        adicionar_unico(
            bullets,
            "Possui forro",
        )


    # --------------------------------------------------------
    # COMPOSIÇÃO
    # --------------------------------------------------------

    composicao = limpar_texto(
        dados.get(
            "composicao_principal"
        )
    )


    if composicao:

        adicionar_unico(
            bullets,
            (
                f"Composição: "
                f"{composicao}"
            ),
        )


    # --------------------------------------------------------
    # LIMITE COMERCIAL
    # --------------------------------------------------------

    return bullets[
        :6
    ]


# ============================================================
# 9. DESCRIÇÃO COMPLETA
# ============================================================

def gerar_descricao_completa(
    ficha,
    posicionamento,
    comunicacao,
):
    """
    Cria uma descrição comercial mais fluida,
    separando interpretação estética de
    características técnicas.
    """

    dados = ficha.model_dump()


    tipo_produto = limpar_texto(
        dados.get(
            "tipo_produto"
        )
    )


    nome_modelo = limpar_texto(
        dados.get(
            "nome_modelo"
        )
    )


    marca = limpar_texto(
        dados.get(
            "marca"
        )
    )


    produto = remover_tipo_repetido(
        tipo_produto,
        nome_modelo,
    )


    # --------------------------------------------------------
    # PARÁGRAFO 1 — IDENTIDADE VISUAL
    # --------------------------------------------------------

    materiais = (
        dados.get(
            "materiais_visuais"
        )
        or []
    )


    renda = ""


    for material in materiais:

        material_texto = limpar_texto(
            material
        )


        if (
            "renda"
            in material_texto.lower()
        ):

            renda = material_texto

            break


    transparencia = limpar_texto(
        dados.get(
            "transparencia"
        )
    )


    abertura = (
        f"O {produto}"
    )


    if marca:

        abertura += (
            f", da {marca},"
        )


    if (
        renda
        and transparencia
    ):

        paragrafo_1 = (

            f"{abertura} combina "
            f"{renda}, transparência localizada "
            "e diferentes texturas em uma "
            "construção visual marcada pelo "
            "contraste entre áreas translúcidas "
            "e opacas."
        )


    elif renda:

        paragrafo_1 = (

            f"{abertura} apresenta "
            f"{renda} como um dos principais "
            "elementos de sua construção visual."
        )


    else:

        mensagem = limpar_texto(
            getattr(
                comunicacao,
                "mensagem_central",
                "",
            )
        )


        if mensagem:

            mensagem = (
                mensagem[0].lower()
                + mensagem[1:]
            )


            paragrafo_1 = (

                f"{abertura} apresenta "
                f"{mensagem}"
            )


        else:

            paragrafo_1 = (

                f"{abertura} apresenta uma "
                "construção visual marcada "
                "pelos detalhes do produto."
            )


    # --------------------------------------------------------
    # PARÁGRAFO 2 — CONSTRUÇÃO
    # --------------------------------------------------------

    manga = limpar_texto(
        dados.get(
            "manga"
        )
    )


    acabamento_mangas = limpar_texto(
        dados.get(
            "acabamento_mangas"
        )
    )


    decote_frente = limpar_texto(
        dados.get(
            "decote_frente"
        )
    )


    decote_costas = limpar_texto(
        dados.get(
            "decote_costas"
        )
    )


    fechamento = limpar_texto(
        dados.get(
            "fechamento"
        )
    )


    detalhes = []


    if manga:

        detalhe_manga = (

            f"mangas "
            f"{pluralizar_manga(manga)}"
        )


        if acabamento_mangas:

            if (
                "punho"
                in acabamento_mangas.lower()
            ):

                detalhe_manga += (

                    f" com "
                    f"{acabamento_mangas.lower().rstrip('.')}"
                )


        adicionar_unico(
            detalhes,
            detalhe_manga,
        )


    if decote_frente:

        adicionar_unico(
            detalhes,
            (
                f"decote frontal "
                f"{decote_frente}"
            ),
        )


    if decote_costas:

        adicionar_unico(
            detalhes,
            (
                f"decote nas costas "
                f"{decote_costas}"
            ),
        )


    if detalhes:

        if len(
            detalhes
        ) == 1:

            texto_detalhes = (
                detalhes[0]
            )


        else:

            texto_detalhes = (

                ", ".join(
                    detalhes[:-1]
                )

                + " e "

                + detalhes[-1]
            )


        paragrafo_2 = (

            "A construção da peça inclui "
            f"{texto_detalhes}."
        )


    else:

        paragrafo_2 = ""


    if fechamento:

        frase_fechamento = (

            f"O fechamento é feito por "
            f"{fechamento.lower()}."
        )


        if paragrafo_2:

            paragrafo_2 += (

                " "
                + frase_fechamento
            )


        else:

            paragrafo_2 = (
                frase_fechamento
            )


    # --------------------------------------------------------
    # PARÁGRAFO 3 — COMPOSIÇÃO
    # --------------------------------------------------------

    composicao = limpar_texto(
        dados.get(
            "composicao_principal"
        )
    )


    possui_forro = dados.get(
        "possui_forro"
    )


    composicao_forro = limpar_texto(
        dados.get(
            "composicao_forro"
        )
    )


    composicoes = []


    if composicao:

        adicionar_unico(
            composicoes,
            (
                f"Composição principal: "
                f"{composicao}."
            ),
        )


    if (
        possui_forro
        and composicao_forro
    ):

        adicionar_unico(
            composicoes,
            (
                f"Possui forro "
                f"{composicao_forro}."
            ),
        )


    elif possui_forro:

        adicionar_unico(
            composicoes,
            "Possui forro.",
        )


    paragrafo_3 = " ".join(
        composicoes
    )


    # --------------------------------------------------------
    # JUNTAR PARÁGRAFOS
    # --------------------------------------------------------

    paragrafos = [

        paragrafo_1,

        paragrafo_2,

        paragrafo_3,
    ]


    paragrafos = [

        paragrafo

        for paragrafo in paragrafos

        if paragrafo
    ]


    return "\n\n".join(
        paragrafos
    )


# ============================================================
# 10. GERAR COPY COMPLETA
# ============================================================

def gerar_copy(
    ficha,
    posicionamento,
    comunicacao,
):
    """
    Transforma a estratégia construída pela Aura
    em uma copy comercial estruturada.
    """

    titulo = gerar_titulo(
        ficha
    )


    descricao_curta = gerar_descricao_curta(
        ficha,
        posicionamento,
        comunicacao,
    )


    descricao_completa = gerar_descricao_completa(
        ficha,
        posicionamento,
        comunicacao,
    )


    bullets = gerar_bullets(
        ficha
    )


    frases_evitar = list(

        getattr(
            comunicacao,
            "abordagens_evitar",
            [],
        )

        or

        getattr(
            posicionamento,
            "evitar",
            [],
        )

        or []
    )


    # --------------------------------------------------------
    # CONFIANÇA
    # --------------------------------------------------------

    confianca_posicionamento = limpar_texto(

        getattr(
            posicionamento,
            "confianca",
            "",
        )

    ).lower()


    confianca_comunicacao = limpar_texto(

        getattr(
            comunicacao,
            "confianca",
            "",
        )

    ).lower()


    if (
        confianca_posicionamento
        == "alta"

        and

        confianca_comunicacao
        == "alta"

        and titulo

        and descricao_completa

        and len(
            bullets
        ) >= 3
    ):

        confianca = "alta"


    elif (
        titulo
        and descricao_completa
    ):

        confianca = "media"


    else:

        confianca = "baixa"


    return CopyProduto(

        titulo=
            titulo,

        descricao_curta=
            descricao_curta,

        descricao_completa=
            descricao_completa,

        bullets=
            bullets,

        frases_evitar=
            frases_evitar,

        confianca=
            confianca,
    )


# ============================================================
# 11. FORMATAR COPY
# ============================================================

def formatar_copy(
    copy,
):
    """
    Formata a copy para leitura no terminal.
    """

    linhas = [

        "COPY COMERCIAL DO PRODUTO",

        "",

        "TÍTULO",

        copy.titulo,

        "",

        "DESCRIÇÃO CURTA",

        copy.descricao_curta,

        "",

        "DESCRIÇÃO COMPLETA",

        copy.descricao_completa,

        "",

        (
            f"CONFIANÇA: "
            f"{copy.confianca}"
        ),

        "",

        "BULLETS PRINCIPAIS",

        "",
    ]


    for bullet in copy.bullets:

        linhas.append(
            f"- {bullet}"
        )


    if copy.frases_evitar:

        linhas.extend(
            [

                "",

                "FRASES / ABORDAGENS QUE NÃO DEVEM SER USADAS",

                "",
            ]
        )


        for frase in (
            copy.frases_evitar
        ):

            linhas.append(
                f"- {frase}"
            )


    return "\n".join(
        linhas
    )