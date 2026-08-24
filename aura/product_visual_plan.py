# ============================================================
# VISUALSELLER FASHION
# AURA — PLANO VISUAL DO PRODUTO
# ============================================================

from dataclasses import dataclass, field
from typing import List


# ============================================================
# 1. MODELO DE IMAGEM DO PLANO VISUAL
# ============================================================

@dataclass
class ImagemPlanoVisual:
    """
    Representa uma imagem planejada para o anúncio.

    A imagem ainda não é gerada aqui.
    Este objeto define sua função estratégica.
    """

    numero: int
    funcao: str
    objetivo: str
    mensagem: str

    destacar: List[str] = field(
        default_factory=list
    )

    textos_sugeridos: List[str] = field(
        default_factory=list
    )

    evidencias: List[str] = field(
        default_factory=list
    )

    confianca: str = "media"


# ============================================================
# 2. MODELO DO PLANO VISUAL COMPLETO
# ============================================================

@dataclass
class PlanoVisualProduto:
    """
    Representa a direção visual completa do anúncio.
    """

    conceito_visual: str
    direcao_visual: str

    imagens: List[ImagemPlanoVisual] = field(
        default_factory=list
    )

    evitar: List[str] = field(
        default_factory=list
    )

    confianca: str = "media"


# ============================================================
# 3. FUNÇÕES AUXILIARES
# ============================================================

def obter_valor(
    objeto,
    nome,
    padrao=None,
):
    """
    Permite trabalhar com objeto,
    dataclass ou dicionário.
    """

    if objeto is None:
        return padrao

    if isinstance(
        objeto,
        dict,
    ):
        return objeto.get(
            nome,
            padrao,
        )

    return getattr(
        objeto,
        nome,
        padrao,
    )


def lista_segura(
    valor,
):
    """
    Garante que o valor seja uma lista.
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


def texto_seguro(
    valor,
):
    """
    Converte valores para texto.
    """

    if valor is None:
        return ""

    return str(
        valor
    ).strip()


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


# ============================================================
# 4. LIMPAR PONTUAÇÃO
# ============================================================

def limpar_pontuacao_final(
    texto,
):
    """
    Remove pontuação repetida no final
    antes de reutilizar um texto em outra frase.

    Exemplo:
    'Sensualidade com contraste visual.'
    vira
    'Sensualidade com contraste visual'
    """

    texto = texto_seguro(
        texto
    )

    while texto.endswith(
        (
            ".",
            ",",
            ";",
            ":",
        )
    ):
        texto = texto[:-1].rstrip()

    return texto


# ============================================================
# 5. NORMALIZAÇÃO DE EVIDÊNCIAS
# ============================================================

def normalizar_evidencia(
    evidencia,
):
    """
    Cria uma versão simples para comparação
    sem alterar o texto original apresentado.
    """

    texto = texto_seguro(
        evidencia
    ).lower()

    texto = (
        texto
        .replace("á", "a")
        .replace("ã", "a")
        .replace("â", "a")
        .replace("é", "e")
        .replace("ê", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ô", "o")
        .replace("õ", "o")
        .replace("ú", "u")
        .replace("ç", "c")
    )

    return texto


# ============================================================
# 6. CONSOLIDAR EVIDÊNCIAS SEMELHANTES
# ============================================================

def consolidar_evidencias(
    evidencias,
):
    """
    Reduz evidências muito parecidas semanticamente.

    Exemplo:
    - presença de renda
    - renda com desenho floral
    - renda floral

    pode manter apenas as versões mais informativas.
    """

    resultado = []

    grupos = {
        "renda": [],
        "transparencia": [],
        "opacidade": [],
        "textura": [],
        "decote": [],
        "manga": [],
        "fechamento": [],
        "forro": [],
        "composicao": [],
        "outros": [],
    }

    for evidencia in evidencias:

        texto_original = texto_seguro(
            evidencia
        )

        texto = normalizar_evidencia(
            evidencia
        )

        if not texto_original:
            continue

        if "renda" in texto:

            grupos["renda"].append(
                texto_original
            )

        elif (
            "transpar"
            in texto
            or "transluc"
            in texto
        ):

            grupos["transparencia"].append(
                texto_original
            )

        elif "opac" in texto:

            grupos["opacidade"].append(
                texto_original
            )

        elif (
            "textura"
            in texto
            or "canelad"
            in texto
            or "punho"
            in texto
        ):

            grupos["textura"].append(
                texto_original
            )

        elif (
            "decote"
            in texto
            or "profundo"
            in texto
        ):

            grupos["decote"].append(
                texto_original
            )

        elif "manga" in texto:

            grupos["manga"].append(
                texto_original
            )

        elif (
            "colchete"
            in texto
            or "fechamento"
            in texto
        ):

            grupos["fechamento"].append(
                texto_original
            )

        elif "forro" in texto:

            grupos["forro"].append(
                texto_original
            )

        elif (
            "poliamida"
            in texto
            or "elastano"
            in texto
            or "algodao"
            in texto
            or "composicao"
            in texto
        ):

            grupos["composicao"].append(
                texto_original
            )

        else:

            grupos["outros"].append(
                texto_original
            )

    # --------------------------------------------------------
    # ESCOLHER EVIDÊNCIA MAIS INFORMATIVA
    # --------------------------------------------------------

    for nome_grupo, itens in grupos.items():

        if not itens:
            continue

        if nome_grupo == "outros":

            for item in itens:
                adicionar_unico(
                    resultado,
                    item,
                )

            continue

        # Preferimos a descrição mais longa,
        # porque normalmente carrega mais contexto.
        item_escolhido = max(
            itens,
            key=len,
        )

        adicionar_unico(
            resultado,
            item_escolhido,
        )

    return resultado


# ============================================================
# 7. COLETAR BASE VISUAL
# ============================================================

def coletar_base_visual(
    ficha,
    identidade=None,
    posicionamento=None,
    comunicacao=None,
):
    """
    Reúne somente informações que já existem
    nas etapas anteriores da Aura.

    O plano visual não deve inventar
    características do produto.
    """

    evidencias = []

    # --------------------------------------------------------
    # IDENTIDADE
    # --------------------------------------------------------

    if identidade is not None:

        for evidencia in lista_segura(
            obter_valor(
                identidade,
                "evidencias",
                [],
            )
        ):

            adicionar_unico(
                evidencias,
                evidencia,
            )

    # --------------------------------------------------------
    # POSICIONAMENTO
    # --------------------------------------------------------

    if posicionamento is not None:

        for evidencia in lista_segura(
            obter_valor(
                posicionamento,
                "evidencias",
                [],
            )
        ):

            adicionar_unico(
                evidencias,
                evidencia,
            )

    # --------------------------------------------------------
    # COMUNICAÇÃO
    # --------------------------------------------------------

    if comunicacao is not None:

        for evidencia in lista_segura(
            obter_valor(
                comunicacao,
                "evidencias",
                [],
            )
        ):

            adicionar_unico(
                evidencias,
                evidencia,
            )

    # --------------------------------------------------------
    # FICHA
    # --------------------------------------------------------

    if ficha is not None:

        if hasattr(
            ficha,
            "model_dump",
        ):

            dados = ficha.model_dump()

        elif isinstance(
            ficha,
            dict,
        ):

            dados = ficha

        else:

            dados = vars(
                ficha
            )

        campos = [
            "tipo_produto",
            "nome_modelo",
            "marca",
            "cores_disponiveis",
            "materiais_visuais",
            "transparencia",
            "manga",
            "acabamento_mangas",
            "decote_frente",
            "decote_costas",
            "fechamento",
            "composicao_principal",
            "possui_forro",
            "composicao_forro",
        ]

        for campo in campos:

            valor = dados.get(
                campo
            )

            if valor is None:
                continue

            if isinstance(
                valor,
                list,
            ):

                for item in valor:

                    adicionar_unico(
                        evidencias,
                        item,
                    )

            else:

                adicionar_unico(
                    evidencias,
                    valor,
                )

    return consolidar_evidencias(
        evidencias
    )


# ============================================================
# 8. BUSCAR EVIDÊNCIAS
# ============================================================

def buscar_evidencias(
    evidencias,
    palavras,
):
    """
    Localiza evidências relacionadas
    a determinadas palavras.
    """

    encontradas = []

    for evidencia in evidencias:

        texto = normalizar_evidencia(
            evidencia
        )

        for palavra in palavras:

            palavra_normalizada = (
                normalizar_evidencia(
                    palavra
                )
            )

            if (
                palavra_normalizada
                in texto
            ):

                adicionar_unico(
                    encontradas,
                    evidencia,
                )

                break

    return encontradas


# ============================================================
# 9. CRIAR IMAGEM DO PLANO
# ============================================================

def criar_imagem(
    numero,
    funcao,
    objetivo,
    mensagem,
    destacar=None,
    textos_sugeridos=None,
    evidencias=None,
):
    """
    Cria uma etapa visual e calcula
    a confiança a partir das evidências.
    """

    destacar = lista_segura(
        destacar
    )

    textos_sugeridos = lista_segura(
        textos_sugeridos
    )

    evidencias = consolidar_evidencias(
        lista_segura(
            evidencias
        )
    )

    quantidade = len(
        evidencias
    )

    if quantidade >= 2:

        confianca = "alta"

    elif quantidade == 1:

        confianca = "media"

    else:

        confianca = "baixa"

    return ImagemPlanoVisual(
        numero=numero,
        funcao=funcao,
        objetivo=objetivo,
        mensagem=mensagem,
        destacar=destacar,
        textos_sugeridos=textos_sugeridos,
        evidencias=evidencias,
        confianca=confianca,
    )


# ============================================================
# 10. GERAR PLANO VISUAL
# ============================================================

def criar_plano_visual(
    ficha,
    identidade,
    posicionamento,
    comunicacao,
):
    """
    Transforma a estratégia da Aura em uma
    sequência visual estruturada para marketplace.
    """

    evidencias = coletar_base_visual(
        ficha=ficha,
        identidade=identidade,
        posicionamento=posicionamento,
        comunicacao=comunicacao,
    )

    # --------------------------------------------------------
    # LEITURA ESTRATÉGICA
    # --------------------------------------------------------

    leitura_principal = limpar_pontuacao_final(
        obter_valor(
            identidade,
            "leitura_principal",
            "",
        )
    )

    territorio = limpar_pontuacao_final(
        obter_valor(
            posicionamento,
            "territorio_comunicacao",
            "",
        )
    )

    mensagem_central = texto_seguro(
        obter_valor(
            comunicacao,
            "mensagem_central",
            "",
        )
    )

    # --------------------------------------------------------
    # EVIDÊNCIAS POR TEMA
    # --------------------------------------------------------

    evidencias_renda = buscar_evidencias(
        evidencias,
        [
            "renda",
            "floral",
        ],
    )

    evidencias_transparencia = buscar_evidencias(
        evidencias,
        [
            "transpar",
            "translúc",
            "transluc",
            "opac",
        ],
    )

    evidencias_textura = buscar_evidencias(
        evidencias,
        [
            "canelad",
            "textura",
            "punho",
        ],
    )

    evidencias_decote = buscar_evidencias(
        evidencias,
        [
            "decote",
            "profundo",
        ],
    )

    evidencias_manga = buscar_evidencias(
        evidencias,
        [
            "manga",
            "punho",
        ],
    )

    evidencias_composicao = buscar_evidencias(
        evidencias,
        [
            "poliamida",
            "elastano",
            "algodão",
            "algodao",
            "composição",
            "composicao",
            "forro",
        ],
    )

    evidencias_fechamento = buscar_evidencias(
        evidencias,
        [
            "colchete",
            "fechamento",
        ],
    )

    # ========================================================
    # CONCEITO VISUAL
    # ========================================================

    if leitura_principal:

        conceito_visual = (
            "Construir a apresentação visual do produto "
            f"a partir de {leitura_principal.lower()}, "
            "mantendo as características reais da peça "
            "como centro da comunicação."
        )

    else:

        conceito_visual = (
            "Construir a apresentação visual a partir "
            "das características observáveis do produto."
        )

    # ========================================================
    # DIREÇÃO VISUAL
    # ========================================================

    if territorio:

        direcao_visual = (
            "A direção visual deve trabalhar "
            f"{territorio.lower()}, "
            "priorizando renda, transparência localizada, "
            "contraste de texturas e detalhes construtivos, "
            "sem alterar as características reais da peça."
        )

    else:

        direcao_visual = (
            "A direção visual deve priorizar "
            "as características confirmadas do produto, "
            "mantendo coerência entre todas as imagens."
        )

    imagens = []

    # ========================================================
    # IMAGEM 1 — CAPA
    # ========================================================

    evidencias_capa = (
        evidencias_renda
        + evidencias_transparencia
        + evidencias_textura
    )

    imagens.append(
        criar_imagem(
            numero=1,
            funcao="capa",
            objetivo=(
                "Apresentar o produto com clareza "
                "e criar reconhecimento imediato."
            ),
            mensagem=(
                mensagem_central
                if mensagem_central
                else
                "Apresentar a identidade visual principal da peça."
            ),
            destacar=[
                "produto inteiro",
                "silhueta geral da peça",
                "contraste visual dos materiais",
                "principais elementos da identidade",
            ],
            textos_sugeridos=[
                "Nome do produto",
                "Marca",
                leitura_principal,
            ],
            evidencias=evidencias_capa,
        )
    )

    # ========================================================
    # IMAGEM 2 — DETALHES VISUAIS
    # ========================================================

    imagens.append(
        criar_imagem(
            numero=2,
            funcao="detalhes visuais",
            objetivo=(
                "Mostrar de perto os elementos que "
                "constroem a identidade visual da peça."
            ),
            mensagem=(
                "Renda, transparência e contraste "
                "participam diretamente da presença visual do produto."
            ),
            destacar=[
                "detalhes da renda",
                "desenho floral",
                "áreas translúcidas",
                "contraste entre transparência e opacidade",
            ],
            textos_sugeridos=[
                "Renda floral",
                "Transparência localizada",
                "Contraste visual",
            ],
            evidencias=(
                evidencias_renda
                + evidencias_transparencia
            ),
        )
    )

    # ========================================================
    # IMAGEM 3 — CONSTRUÇÃO
    # ========================================================

    imagens.append(
        criar_imagem(
            numero=3,
            funcao="construção",
            objetivo=(
                "Explicar visualmente como "
                "a peça foi construída."
            ),
            mensagem=(
                "Decotes, mangas e fechamento "
                "fazem parte da construção do produto."
            ),
            destacar=[
                "decote frontal",
                "decote das costas",
                "mangas",
                "punhos",
                "fechamento",
            ],
            textos_sugeridos=[
                "Detalhes de construção",
                "Frente e costas",
                "Acabamentos",
            ],
            evidencias=(
                evidencias_decote
                + evidencias_manga
                + evidencias_fechamento
            ),
        )
    )

    # ========================================================
    # IMAGEM 4 — TEXTURAS E ACABAMENTOS
    # ========================================================

    imagens.append(
        criar_imagem(
            numero=4,
            funcao="texturas e acabamentos",
            objetivo=(
                "Evidenciar diferenças de superfície "
                "e detalhes construtivos."
            ),
            mensagem=(
                "A combinação de diferentes superfícies "
                "cria contraste e riqueza visual."
            ),
            destacar=[
                "malha canelada",
                "renda",
                "textura dos materiais",
                "acabamento das mangas",
            ],
            textos_sugeridos=[
                "Contraste de texturas",
                "Detalhes que constroem a peça",
            ],
            evidencias=(
                evidencias_textura
                + evidencias_renda
            ),
        )
    )

    # ========================================================
    # IMAGEM 5 — INFORMAÇÃO TÉCNICA
    # ========================================================

    imagens.append(
        criar_imagem(
            numero=5,
            funcao="informação técnica",
            objetivo=(
                "Apresentar informações objetivas "
                "sobre composição e estrutura."
            ),
            mensagem=(
                "Informações técnicas confirmadas "
                "ajudam a reduzir dúvidas sobre o produto."
            ),
            destacar=[
                "composição principal",
                "presença de forro",
                "composição do forro",
            ],
            textos_sugeridos=[
                "Composição",
                "Informações do produto",
            ],
            evidencias=evidencias_composicao,
        )
    )

    # ========================================================
    # IMAGEM 6 — DIFERENCIAIS
    # ========================================================

    imagens.append(
        criar_imagem(
            numero=6,
            funcao="síntese de diferenciais",
            objetivo=(
                "Reunir os principais elementos "
                "que diferenciam visualmente a peça."
            ),
            mensagem=(
                "A identidade do produto nasce da "
                "combinação entre renda, transparência, "
                "contraste e detalhes de construção."
            ),
            destacar=[
                "renda floral",
                "transparência",
                "contraste de materiais",
                "acabamento canelado",
                "construção dos decotes",
            ],
            textos_sugeridos=[
                "Detalhes em destaque",
                "Renda + transparência + textura",
            ],
            evidencias=(
                evidencias_renda
                + evidencias_transparencia
                + evidencias_textura
                + evidencias_decote
            ),
        )
    )

    # ========================================================
    # IMAGEM 7 — FECHAMENTO
    # ========================================================

    imagens.append(
        criar_imagem(
            numero=7,
            funcao="fechamento",
            objetivo=(
                "Encerrar a sequência retomando "
                "a identidade principal do produto."
            ),
            mensagem=(
                mensagem_central
                if mensagem_central
                else
                "Síntese da identidade visual do produto."
            ),
            destacar=[
                "produto como protagonista",
                "identidade visual principal",
                "elementos mais reconhecíveis da peça",
            ],
            textos_sugeridos=[
                leitura_principal,
                "Conheça os detalhes da peça",
            ],
            evidencias=evidencias_capa,
        )
    )

    # ========================================================
    # LIMITES VISUAIS
    # ========================================================

    evitar = [
        (
            "Não alterar visualmente características "
            "estruturais do produto."
        ),
        (
            "Não adicionar materiais, detalhes ou "
            "acabamentos que não estejam confirmados."
        ),
        (
            "Não representar transparência, renda ou "
            "textura de forma incompatível com o produto."
        ),
        (
            "Não usar textos que prometam conforto, "
            "durabilidade ou modelagem sem evidência."
        ),
        (
            "Não transformar interpretação estética "
            "em característica técnica."
        ),
        (
            "Não esconder detalhes importantes apenas "
            "para tornar a imagem mais estética."
        ),
        (
            "Manter coerência visual entre todas "
            "as imagens da sequência."
        ),
    ]

    # ========================================================
    # CONFIANÇA GERAL
    # ========================================================

    imagens_com_evidencia = sum(
        1
        for imagem in imagens
        if imagem.evidencias
    )

    if imagens_com_evidencia >= 6:

        confianca = "alta"

    elif imagens_com_evidencia >= 4:

        confianca = "media"

    else:

        confianca = "baixa"

    return PlanoVisualProduto(
        conceito_visual=conceito_visual,
        direcao_visual=direcao_visual,
        imagens=imagens,
        evitar=evitar,
        confianca=confianca,
    )


# ============================================================
# 11. ALIAS
# ============================================================

def planejar_visual(
    ficha,
    identidade,
    posicionamento,
    comunicacao,
):
    """
    Alias curto para uso futuro
    no fluxo principal da Aura.
    """

    return criar_plano_visual(
        ficha=ficha,
        identidade=identidade,
        posicionamento=posicionamento,
        comunicacao=comunicacao,
    )


# ============================================================
# 12. FORMATAR PLANO VISUAL
# ============================================================

def formatar_plano_visual(
    plano,
):
    """
    Formata o plano visual
    para leitura no terminal.
    """

    linhas = [
        "PLANO VISUAL DO PRODUTO",
        "",
        "CONCEITO VISUAL",
        plano.conceito_visual,
        "",
        "DIREÇÃO VISUAL",
        plano.direcao_visual,
        "",
        f"CONFIANÇA: {plano.confianca}",
        "",
        "SEQUÊNCIA DE IMAGENS",
        "",
    ]

    for imagem in plano.imagens:

        linhas.append(
            f"IMAGEM {imagem.numero}"
        )

        linhas.append(
            f"Função: {imagem.funcao}"
        )

        linhas.append(
            f"Confiança: {imagem.confianca}"
        )

        linhas.append("")

        linhas.append(
            "OBJETIVO"
        )

        linhas.append(
            imagem.objetivo
        )

        linhas.append("")

        linhas.append(
            "MENSAGEM"
        )

        linhas.append(
            imagem.mensagem
        )

        linhas.append("")

        linhas.append(
            "O QUE DESTACAR"
        )

        for item in imagem.destacar:

            if item:

                linhas.append(
                    f"- {item}"
                )

        linhas.append("")

        linhas.append(
            "TEXTOS SUGERIDOS"
        )

        for texto in imagem.textos_sugeridos:

            if texto:

                linhas.append(
                    f"- {texto}"
                )

        linhas.append("")

        linhas.append(
            "EVIDÊNCIAS"
        )

        if imagem.evidencias:

            for evidencia in imagem.evidencias:

                linhas.append(
                    f"- {evidencia}"
                )

        else:

            linhas.append(
                "- Nenhuma evidência específica encontrada."
            )

        linhas.append("")

    linhas.append(
        "O QUE EVITAR"
    )

    linhas.append("")

    for item in plano.evitar:

        linhas.append(
            f"- {item}"
        )

    return "\n".join(
        linhas
    )