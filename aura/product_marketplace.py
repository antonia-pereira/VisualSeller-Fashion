# ============================================================
# VISUALSELLER FASHION
# AURA — ADAPTAÇÃO PARA MARKETPLACE
# ============================================================

from dataclasses import dataclass, field
from typing import List


# ============================================================
# 1. MODELO DE MARKETPLACE
# ============================================================

@dataclass
class MarketplaceProduto:
    """
    Representa uma versão da comunicação adaptada
    para um anúncio de marketplace.

    Esta camada não cria novos fatos.
    Ela reorganiza a copy já validada pela Aura.
    """

    titulo: str = ""

    descricao: str = ""

    bullets: List[str] = field(
        default_factory=list
    )

    termos_busca: List[str] = field(
        default_factory=list
    )

    ficha_resumida: List[str] = field(
        default_factory=list
    )

    faq: List[dict] = field(
        default_factory=list
    )

    confianca: str = "baixa"


# ============================================================
# 2. FUNÇÕES AUXILIARES
# ============================================================

def limpar_texto(valor):
    """
    Converte qualquer valor em texto limpo.
    """

    if valor is None:
        return ""

    return str(valor).strip()


def adicionar_unico(lista, valor):
    """
    Adiciona um item somente se ele ainda
    não estiver presente.
    """

    valor = limpar_texto(valor)

    if (
        valor
        and valor not in lista
    ):
        lista.append(valor)


def normalizar_termo(valor):
    """
    Normaliza um termo para busca.
    """

    return limpar_texto(
        valor
    ).lower()


# ============================================================
# 3. TÍTULO PARA MARKETPLACE
# ============================================================

def gerar_titulo_marketplace(
    ficha,
    copy,
):
    """
    Usa a copy como base e mantém o título objetivo.

    Não adiciona atributos que não estejam confirmados.
    """

    titulo_copy = limpar_texto(
        getattr(
            copy,
            "titulo",
            "",
        )
    )

    if titulo_copy:
        return titulo_copy

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

    cores = (
        dados.get(
            "cores_disponiveis"
        )
        or []
    )

    partes = []

    adicionar_unico(
        partes,
        nome_modelo or tipo_produto,
    )

    if cores:

        adicionar_unico(
            partes,
            cores[0],
        )

    titulo = " ".join(
        partes
    )

    if marca:

        titulo = (
            f"{titulo} — {marca}"
        )

    return titulo


# ============================================================
# 4. DESCRIÇÃO PARA MARKETPLACE
# ============================================================

def gerar_descricao_marketplace(
    ficha,
    copy,
):
    """
    Adapta a descrição completa da copy
    para uma leitura clara de marketplace.
    """

    descricao_copy = limpar_texto(
        getattr(
            copy,
            "descricao_completa",
            "",
        )
    )

    if descricao_copy:
        return descricao_copy

    return (
        "Produto apresentado com base nas "
        "características confirmadas pela Aura."
    )


# ============================================================
# 5. BULLETS PARA MARKETPLACE
# ============================================================

def gerar_bullets_marketplace(
    copy,
):
    """
    Reutiliza os bullets já selecionados
    pela camada de copy.
    """

    bullets_copy = list(
        getattr(
            copy,
            "bullets",
            [],
        )
        or []
    )

    resultado = []

    for bullet in bullets_copy:

        adicionar_unico(
            resultado,
            bullet,
        )

    return resultado[:6]


# ============================================================
# 6. TERMOS DE BUSCA
# ============================================================

def gerar_termos_busca(
    ficha,
):
    """
    Gera termos descritivos de busca a partir
    de informações confirmadas na ficha.

    Não inventa tendência, ocasião ou público.
    """

    dados = ficha.model_dump()

    termos = []


    # --------------------------------------------------------
    # TIPO
    # --------------------------------------------------------

    tipo_produto = limpar_texto(
        dados.get(
            "tipo_produto"
        )
    )

    adicionar_unico(
        termos,
        tipo_produto,
    )


    # --------------------------------------------------------
    # MODELO
    # --------------------------------------------------------

    nome_modelo = limpar_texto(
        dados.get(
            "nome_modelo"
        )
    )

    adicionar_unico(
        termos,
        nome_modelo,
    )


    # --------------------------------------------------------
    # MARCA
    # --------------------------------------------------------

    marca = limpar_texto(
        dados.get(
            "marca"
        )
    )

    adicionar_unico(
        termos,
        marca,
    )


    # --------------------------------------------------------
    # CORES
    # --------------------------------------------------------

    cores = (
        dados.get(
            "cores_disponiveis"
        )
        or []
    )

    for cor in cores:

        adicionar_unico(
            termos,
            cor,
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

        texto = limpar_texto(
            material
        )

        adicionar_unico(
            termos,
            texto,
        )


    # --------------------------------------------------------
    # MANGA
    # --------------------------------------------------------

    manga = limpar_texto(
        dados.get(
            "manga"
        )
    )

    if manga:

        adicionar_unico(
            termos,
            f"manga {manga.lower()}",
        )


    # --------------------------------------------------------
    # DECOTE
    # --------------------------------------------------------

    decote_frente = limpar_texto(
        dados.get(
            "decote_frente"
        )
    )

    if decote_frente:

        adicionar_unico(
            termos,
            f"decote {decote_frente}",
        )


    # --------------------------------------------------------
    # TRANSPARÊNCIA
    # --------------------------------------------------------

    transparencia = limpar_texto(
        dados.get(
            "transparencia"
        )
    )

    if transparencia:

        adicionar_unico(
            termos,
            "transparência",
        )


    # --------------------------------------------------------
    # LIMPAR E NORMALIZAR
    # --------------------------------------------------------

    resultado = []

    for termo in termos:

        termo_normalizado = normalizar_termo(
            termo
        )

        if termo_normalizado:

            adicionar_unico(
                resultado,
                termo_normalizado,
            )

    return resultado


# ============================================================
# 7. FICHA RESUMIDA
# ============================================================

def gerar_ficha_resumida(
    ficha,
):
    """
    Seleciona os principais dados objetivos
    para o anúncio.
    """

    dados = ficha.model_dump()

    itens = []


    campos = [
        (
            "Marca",
            "marca",
        ),
        (
            "Modelo",
            "nome_modelo",
        ),
        (
            "Produto",
            "tipo_produto",
        ),
        (
            "Referência",
            "referencia",
        ),
        (
            "Composição",
            "composicao_principal",
        ),
        (
            "Forro",
            "composicao_forro",
        ),
        (
            "Manga",
            "manga",
        ),
        (
            "Decote frontal",
            "decote_frente",
        ),
        (
            "Decote costas",
            "decote_costas",
        ),
        (
            "Fechamento",
            "fechamento",
        ),
    ]


    for rotulo, campo in campos:

        valor = dados.get(
            campo
        )

        texto = limpar_texto(
            valor
        )

        if texto:

            adicionar_unico(
                itens,
                f"{rotulo}: {texto}",
            )


    # --------------------------------------------------------
    # CORES
    # --------------------------------------------------------

    cores = (
        dados.get(
            "cores_disponiveis"
        )
        or []
    )

    if cores:

        adicionar_unico(
            itens,
            "Cores: "
            + ", ".join(
                str(cor)
                for cor in cores
            ),
        )


    # --------------------------------------------------------
    # TAMANHOS
    # --------------------------------------------------------

    tamanhos = (
        dados.get(
            "tamanhos_disponiveis"
        )
        or []
    )

    if tamanhos:

        adicionar_unico(
            itens,
            "Tamanhos: "
            + ", ".join(
                str(tamanho)
                for tamanho in tamanhos
            ),
        )


    # --------------------------------------------------------
    # BOJO
    # --------------------------------------------------------

    possui_bojo = dados.get(
        "possui_bojo"
    )

    if possui_bojo is True:

        adicionar_unico(
            itens,
            "Possui bojo: Sim",
        )

    elif possui_bojo is False:

        adicionar_unico(
            itens,
            "Possui bojo: Não",
        )


    return itens


# ============================================================
# 8. FAQ
# ============================================================

def gerar_faq(
    ficha,
):
    """
    Gera perguntas frequentes apenas para
    informações que a Aura realmente conhece.
    """

    dados = ficha.model_dump()

    faq = []


    # --------------------------------------------------------
    # BOJO
    # --------------------------------------------------------

    possui_bojo = dados.get(
        "possui_bojo"
    )

    if possui_bojo is not None:

        resposta = (
            "Sim."
            if possui_bojo
            else "Não."
        )

        faq.append(
            {
                "pergunta":
                    "A peça possui bojo?",

                "resposta":
                    resposta,
            }
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

    if possui_forro is not None:

        if (
            possui_forro
            and composicao_forro
        ):

            resposta = (
                "Sim. O forro informado é "
                f"{composicao_forro}."
            )

        elif possui_forro:

            resposta = (
                "Sim, a peça possui forro."
            )

        else:

            resposta = (
                "Não."
            )

        faq.append(
            {
                "pergunta":
                    "A peça possui forro?",

                "resposta":
                    resposta,
            }
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

        faq.append(
            {
                "pergunta":
                    "Qual é a composição da peça?",

                "resposta":
                    composicao,
            }
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

        faq.append(
            {
                "pergunta":
                    "Qual é o tipo de fechamento?",

                "resposta":
                    (
                        f"O fechamento é por "
                        f"{fechamento.lower()}."
                    ),
            }
        )


    # --------------------------------------------------------
    # TAMANHOS
    # --------------------------------------------------------

    tamanhos = (
        dados.get(
            "tamanhos_disponiveis"
        )
        or []
    )

    if tamanhos:

        faq.append(
            {
                "pergunta":
                    "Quais tamanhos estão disponíveis?",

                "resposta":
                    ", ".join(
                        str(tamanho)
                        for tamanho in tamanhos
                    ),
            }
        )


    # --------------------------------------------------------
    # CORES
    # --------------------------------------------------------

    cores = (
        dados.get(
            "cores_disponiveis"
        )
        or []
    )

    if cores:

        faq.append(
            {
                "pergunta":
                    "Quais cores estão disponíveis?",

                "resposta":
                    ", ".join(
                        str(cor)
                        for cor in cores
                    ),
            }
        )


    return faq


# ============================================================
# 9. CALCULAR CONFIANÇA
# ============================================================

def calcular_confianca_marketplace(
    copy,
    ficha_resumida,
):
    """
    Define a confiança da adaptação.
    """

    confianca_copy = limpar_texto(
        getattr(
            copy,
            "confianca",
            "",
        )
    ).lower()


    if (
        confianca_copy == "alta"
        and len(
            ficha_resumida
        ) >= 5
    ):

        return "alta"


    if ficha_resumida:

        return "media"


    return "baixa"


# ============================================================
# 10. GERAR MARKETPLACE
# ============================================================

def gerar_marketplace(
    ficha,
    copy,
):
    """
    Gera uma versão completa da copy
    adaptada para marketplace.
    """

    titulo = gerar_titulo_marketplace(
        ficha,
        copy,
    )

    descricao = gerar_descricao_marketplace(
        ficha,
        copy,
    )

    bullets = gerar_bullets_marketplace(
        copy
    )

    termos_busca = gerar_termos_busca(
        ficha
    )

    ficha_resumida = gerar_ficha_resumida(
        ficha
    )

    faq = gerar_faq(
        ficha
    )

    confianca = calcular_confianca_marketplace(
        copy,
        ficha_resumida,
    )


    return MarketplaceProduto(

        titulo=
            titulo,

        descricao=
            descricao,

        bullets=
            bullets,

        termos_busca=
            termos_busca,

        ficha_resumida=
            ficha_resumida,

        faq=
            faq,

        confianca=
            confianca,
    )


# ============================================================
# 11. FORMATAR MARKETPLACE
# ============================================================

def formatar_marketplace(
    marketplace,
):
    """
    Formata a saída para leitura no terminal.
    """

    linhas = [

        "ANÚNCIO PARA MARKETPLACE",

        "",

        "TÍTULO",

        marketplace.titulo,

        "",

        "DESCRIÇÃO",

        marketplace.descricao,

        "",

        (
            f"CONFIANÇA: "
            f"{marketplace.confianca}"
        ),

        "",

        "BULLETS",

        "",
    ]


    for bullet in marketplace.bullets:

        linhas.append(
            f"- {bullet}"
        )


    linhas.extend(
        [
            "",
            "TERMOS DE BUSCA",
            "",
        ]
    )


    for termo in marketplace.termos_busca:

        linhas.append(
            f"- {termo}"
        )


    linhas.extend(
        [
            "",
            "FICHA RESUMIDA",
            "",
        ]
    )


    for item in marketplace.ficha_resumida:

        linhas.append(
            f"- {item}"
        )


    linhas.extend(
        [
            "",
            "FAQ",
            "",
        ]
    )


    for item in marketplace.faq:

        linhas.append(
            f"PERGUNTA: {item['pergunta']}"
        )

        linhas.append(
            f"RESPOSTA: {item['resposta']}"
        )

        linhas.append(
            ""
        )


    return "\n".join(
        linhas
    )