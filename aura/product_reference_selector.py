# ============================================================
# VISUALSELLER FASHION
# AURA — SELEÇÃO INTELIGENTE DE REFERÊNCIAS
# ============================================================

from dataclasses import dataclass, field
from typing import Any, List, Dict


# ============================================================
# 1. MODELO DE AVALIAÇÃO DE REFERÊNCIA
# ============================================================

@dataclass
class AvaliacaoReferencia:
    """
    Representa a avaliação de uma fotografia real
    para uma determinada função da campanha.
    """

    caminho: str

    tipo_imagem: str

    funcao_destino: str

    pontuacao: float = 0.0

    campos_relevantes: List[str] = field(
        default_factory=list
    )

    evidencias_relevantes: List[str] = field(
        default_factory=list
    )

    motivos: List[str] = field(
        default_factory=list
    )


# ============================================================
# 2. FUNÇÕES AUXILIARES
# ============================================================

def texto_seguro(
    valor: Any,
) -> str:
    """
    Converte qualquer valor para texto simples.
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
    Adiciona um valor somente uma vez.
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


def normalizar(
    valor,
):
    """
    Normaliza texto para comparação.
    """

    texto = texto_seguro(
        valor
    ).lower()

    texto = (
        texto
        .replace("á", "a")
        .replace("à", "a")
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
# 3. PESO DA CONFIANÇA
# ============================================================

def peso_confianca(
    confianca,
):
    """
    Converte confiança textual em peso numérico.
    """

    confianca = normalizar(
        confianca
    )


    if confianca == "alta":

        return 1.0


    if confianca == "media":

        return 0.65


    if confianca == "baixa":

        return 0.30


    return 0.20


# ============================================================
# 4. PERFIS VISUAIS POR FUNÇÃO
# ============================================================

PERFIS_FUNCAO = {

    # --------------------------------------------------------
    # CAPA
    # --------------------------------------------------------

    "capa": {

        "campos": {

            "decote_frente": 3.0,

            "decote_costas": 1.0,

            "manga": 2.0,

            "transparencia": 2.0,

            "materiais_visuais": 2.0,
        },

        "palavras": {

            "frente": 3.0,

            "silhueta": 3.0,

            "produto inteiro": 4.0,

            "renda": 1.5,

            "transparencia": 1.5,
        },

        "tipos": {

            "frente": 5.0,

            "costas": 1.5,
        },
    },


    # --------------------------------------------------------
    # DETALHES VISUAIS
    # --------------------------------------------------------

    "detalhes visuais": {

        "campos": {

            "materiais_visuais": 5.0,

            "transparencia": 5.0,

            "decote_frente": 1.0,

            "decote_costas": 1.0,

            "acabamento_mangas": 2.0,
        },

        "palavras": {

            "renda": 5.0,

            "floral": 4.0,

            "transpar": 5.0,

            "transluc": 4.0,

            "opac": 2.0,

            "tela": 3.0,
        },

        "tipos": {

            "detalhe": 5.0,

            "composicao": 1.0,

            "frente": 0.5,
        },
    },


    # --------------------------------------------------------
    # CONSTRUÇÃO
    # --------------------------------------------------------

    "construcao": {

        "campos": {

            "decote_frente": 5.0,

            "decote_costas": 5.0,

            "manga": 4.0,

            "acabamento_mangas": 4.0,

            "fechamento": 5.0,
        },

        "palavras": {

            "decote": 5.0,

            "profundo": 3.0,

            "manga": 4.0,

            "punho": 4.0,

            "colchete": 5.0,

            "fechamento": 5.0,
        },

        "tipos": {

            "frente": 4.0,

            "costas": 4.0,

            "detalhe": 3.0,
        },
    },


    # --------------------------------------------------------
    # TEXTURAS E ACABAMENTOS
    # --------------------------------------------------------

    "texturas e acabamentos": {

        "campos": {

            "materiais_visuais": 5.0,

            "acabamento_mangas": 5.0,

            "transparencia": 3.0,
        },

        "palavras": {

            "canelad": 5.0,

            "textura": 5.0,

            "renda": 4.0,

            "trama": 4.0,

            "punho": 4.0,

            "acabamento": 4.0,

            "transpar": 2.0,
        },

        "tipos": {

            "detalhe": 5.0,

            "composicao": 1.0,
        },
    },


    # --------------------------------------------------------
    # INFORMAÇÃO TÉCNICA
    # --------------------------------------------------------

    "informacao tecnica": {

        "campos": {

            "composicao_principal": 8.0,

            "composicao_forro": 8.0,

            "possui_forro": 5.0,

            "tamanho_medido": 4.0,

            "referencia": 4.0,

            "codigo_barras": 4.0,
        },

        "palavras": {

            "poliamida": 7.0,

            "elastano": 7.0,

            "algodao": 7.0,

            "composicao": 7.0,

            "forro": 5.0,

            "etiqueta": 5.0,
        },

        "tipos": {

            "etiqueta": 7.0,

            "composicao": 7.0,
        },
    },


    # --------------------------------------------------------
    # SÍNTESE DE DIFERENCIAIS
    # --------------------------------------------------------

    "sintese de diferenciais": {

        "campos": {

            "materiais_visuais": 4.0,

            "transparencia": 4.0,

            "decote_frente": 3.0,

            "decote_costas": 3.0,

            "acabamento_mangas": 3.0,
        },

        "palavras": {

            "renda": 4.0,

            "transpar": 4.0,

            "canelad": 3.0,

            "decote": 3.0,

            "punho": 2.0,
        },

        "tipos": {

            "frente": 3.0,

            "costas": 2.5,

            "detalhe": 4.0,
        },
    },


    # --------------------------------------------------------
    # FECHAMENTO
    # --------------------------------------------------------

    "fechamento": {

        "campos": {

            "decote_frente": 2.0,

            "manga": 2.0,

            "transparencia": 2.0,

            "materiais_visuais": 2.0,
        },

        "palavras": {

            "renda": 1.5,

            "transpar": 1.5,

            "silhueta": 3.0,

            "produto inteiro": 4.0,
        },

        "tipos": {

            "frente": 5.0,

            "costas": 2.0,
        },
    },
}


# ============================================================
# 5. NORMALIZAR NOME DA FUNÇÃO
# ============================================================

def normalizar_funcao(
    funcao,
):
    """
    Converte o nome da função para a chave usada
    nos perfis da Aura.
    """

    texto = normalizar(
        funcao
    )


    if "detalhes visuais" in texto:

        return "detalhes visuais"


    if "construcao" in texto:

        return "construcao"


    if "texturas" in texto:

        return "texturas e acabamentos"


    if "informacao tecnica" in texto:

        return "informacao tecnica"


    if "sintese" in texto:

        return "sintese de diferenciais"


    if "fechamento" in texto:

        return "fechamento"


    if "capa" in texto:

        return "capa"


    return texto


# ============================================================
# 6. AGRUPAR EVIDÊNCIAS POR FOTO
# ============================================================

def agrupar_evidencias_por_imagem(
    resultado_visao,
):
    """
    Recebe o retorno do vision_product.analisar_produto()
    e organiza as evidências por arquivo.

    Resultado esperado:

    {
        "foto.jpg": {
            "caminho": "...",
            "tipo_imagem": "detalhe",
            "evidencias": [...]
        }
    }
    """

    grupos = {}


    evidencias = resultado_visao.get(
        "evidencias",
        [],
    )


    for evidencia in evidencias:

        caminho = texto_seguro(
            evidencia.get(
                "caminho_imagem"
            )
        )

        tipo = texto_seguro(
            evidencia.get(
                "tipo_imagem"
            )
        )


        if not caminho:

            continue


        if caminho not in grupos:

            grupos[caminho] = {

                "caminho":
                    caminho,

                "tipo_imagem":
                    tipo,

                "evidencias":
                    [],
            }


        grupos[caminho][
            "evidencias"
        ].append(
            evidencia
        )


    # --------------------------------------------------------
    # GARANTIR QUE FOTOS SEM EVIDÊNCIA NÃO SUMAM
    # --------------------------------------------------------

    for analise in resultado_visao.get(
        "analises",
        [],
    ):

        caminho = texto_seguro(
            analise.get(
                "caminho"
            )
        )

        tipo = texto_seguro(
            analise.get(
                "tipo_imagem"
            )
        )


        if (
            caminho
            and caminho not in grupos
        ):

            grupos[caminho] = {

                "caminho":
                    caminho,

                "tipo_imagem":
                    tipo,

                "evidencias":
                    [],
            }


    return grupos


# ============================================================
# 7. CALCULAR PONTUAÇÃO DE UMA FOTO
# ============================================================

def avaliar_referencia(
    caminho,
    tipo_imagem,
    evidencias,
    funcao_destino,
):
    """
    Avalia uma fotografia para uma função específica.

    A pontuação considera:

    - tipo da foto;
    - campos encontrados pela visão;
    - conteúdo textual das evidências;
    - confiança da visão.
    """

    funcao_chave = normalizar_funcao(
        funcao_destino
    )


    perfil = PERFIS_FUNCAO.get(
        funcao_chave,
        {
            "campos": {},
            "palavras": {},
            "tipos": {},
        },
    )


    pontuacao = 0.0

    campos_relevantes = []

    evidencias_relevantes = []

    motivos = []


    # ========================================================
    # PONTUAÇÃO PELO TIPO DA FOTO
    # ========================================================

    tipo_normalizado = normalizar(
        tipo_imagem
    )


    peso_tipo = perfil[
        "tipos"
    ].get(
        tipo_normalizado,
        0.0,
    )


    if peso_tipo:

        pontuacao += peso_tipo

        adicionar_unico(
            motivos,
            (
                f"tipo '{tipo_imagem}' adequado "
                f"à função (+{peso_tipo})"
            ),
        )


    # ========================================================
    # PONTUAÇÃO DAS EVIDÊNCIAS
    # ========================================================

    for evidencia in evidencias:

        campo = texto_seguro(
            evidencia.get(
                "campo"
            )
        )

        valor = texto_seguro(
            evidencia.get(
                "valor"
            )
        )

        observacao = texto_seguro(
            evidencia.get(
                "observacao"
            )
        )

        confianca = texto_seguro(
            evidencia.get(
                "confianca"
            )
        )


        peso_conf = peso_confianca(
            confianca
        )


        # ----------------------------------------------------
        # CAMPO
        # ----------------------------------------------------

        peso_campo = perfil[
            "campos"
        ].get(
            campo,
            0.0,
        )


        if peso_campo:

            pontos = (
                peso_campo
                * peso_conf
            )

            pontuacao += pontos

            adicionar_unico(
                campos_relevantes,
                campo,
            )

            adicionar_unico(
                evidencias_relevantes,
                (
                    f"{campo}: {valor}"
                ),
            )

            adicionar_unico(
                motivos,
                (
                    f"{campo} relevante "
                    f"({confianca}) "
                    f"(+{pontos:.2f})"
                ),
            )


        # ----------------------------------------------------
        # PALAVRAS NO VALOR / OBSERVAÇÃO
        # ----------------------------------------------------

        texto_evidencia = normalizar(
            f"{valor} {observacao}"
        )


        for palavra, peso_palavra in perfil[
            "palavras"
        ].items():

            palavra_normalizada = normalizar(
                palavra
            )


            if (
                palavra_normalizada
                in texto_evidencia
            ):

                pontos = (
                    peso_palavra
                    * peso_conf
                )

                pontuacao += pontos

                adicionar_unico(
                    evidencias_relevantes,
                    (
                        f"{campo}: {valor}"
                    ),
                )

                adicionar_unico(
                    motivos,
                    (
                        f"evidência de '{palavra}' "
                        f"({confianca}) "
                        f"(+{pontos:.2f})"
                    ),
                )


    return AvaliacaoReferencia(

        caminho=
            caminho,

        tipo_imagem=
            tipo_imagem,

        funcao_destino=
            funcao_chave,

        pontuacao=
            round(
                pontuacao,
                2,
            ),

        campos_relevantes=
            campos_relevantes,

        evidencias_relevantes=
            evidencias_relevantes,

        motivos=
            motivos,
    )


# ============================================================
# 8. AVALIAR TODAS AS REFERÊNCIAS
# ============================================================

def avaliar_referencias(
    resultado_visao,
    funcao_destino,
):
    """
    Avalia todas as fotografias reais para
    uma função da campanha.
    """

    grupos = agrupar_evidencias_por_imagem(
        resultado_visao
    )


    avaliacoes = []


    for dados in grupos.values():

        avaliacao = avaliar_referencia(

            caminho=
                dados["caminho"],

            tipo_imagem=
                dados["tipo_imagem"],

            evidencias=
                dados["evidencias"],

            funcao_destino=
                funcao_destino,
        )


        avaliacoes.append(
            avaliacao
        )


    avaliacoes.sort(
        key=lambda item:
            item.pontuacao,
        reverse=True,
    )


    return avaliacoes


# ============================================================
# 9. SELECIONAR MELHORES REFERÊNCIAS
# ============================================================

def selecionar_melhores_referencias(
    resultado_visao,
    funcao_destino,
    limite=3,
    tipos_permitidos=None,
):
    """
    Retorna somente as referências com maior
    relevância visual para a função.

    Pode também respeitar tipos permitidos
    definidos pelo product_image_execution.
    """

    avaliacoes = avaliar_referencias(
        resultado_visao=
            resultado_visao,

        funcao_destino=
            funcao_destino,
    )


    tipos_permitidos_normalizados = None


    if tipos_permitidos:

        tipos_permitidos_normalizados = [

            normalizar(
                tipo
            )

            for tipo in tipos_permitidos
        ]


    selecionadas = []


    for avaliacao in avaliacoes:

        if (
            tipos_permitidos_normalizados
            is not None
        ):

            if normalizar(
                avaliacao.tipo_imagem
            ) not in tipos_permitidos_normalizados:

                continue


        selecionadas.append(
            avaliacao
        )


        if len(
            selecionadas
        ) >= limite:

            break


    return selecionadas


# ============================================================
# 10. GERAR MAPA DE REFERÊNCIAS DA CAMPANHA
# ============================================================

def criar_mapa_referencias(
    resultado_visao,
    funcoes,
):
    """
    Cria um ranking de fotos para cada
    função visual da campanha.
    """

    mapa = {}


    for funcao in funcoes:

        avaliacoes = avaliar_referencias(

            resultado_visao=
                resultado_visao,

            funcao_destino=
                funcao,
        )


        mapa[
            funcao
        ] = avaliacoes


    return mapa


# ============================================================
# 11. FORMATAR AVALIAÇÃO
# ============================================================

def formatar_avaliacao_referencia(
    avaliacao,
):
    """
    Formata uma avaliação individual
    para leitura no terminal.
    """

    linhas = [

        f"ARQUIVO: {avaliacao.caminho}",

        (
            "TIPO: "
            f"{avaliacao.tipo_imagem}"
        ),

        (
            "FUNÇÃO AVALIADA: "
            f"{avaliacao.funcao_destino}"
        ),

        (
            "PONTUAÇÃO: "
            f"{avaliacao.pontuacao}"
        ),

        "",

        "CAMPOS RELEVANTES",
    ]


    if avaliacao.campos_relevantes:

        for campo in avaliacao.campos_relevantes:

            linhas.append(
                f"- {campo}"
            )

    else:

        linhas.append(
            "- nenhum"
        )


    linhas.extend(
        [
            "",
            "EVIDÊNCIAS RELEVANTES",
        ]
    )


    if avaliacao.evidencias_relevantes:

        for evidencia in (
            avaliacao.evidencias_relevantes
        ):

            linhas.append(
                f"- {evidencia}"
            )

    else:

        linhas.append(
            "- nenhuma"
        )


    linhas.extend(
        [
            "",
            "MOTIVOS DA PONTUAÇÃO",
        ]
    )


    if avaliacao.motivos:

        for motivo in avaliacao.motivos:

            linhas.append(
                f"- {motivo}"
            )

    else:

        linhas.append(
            "- nenhuma evidência relevante"
        )


    return "\n".join(
        linhas
    )


# ============================================================
# 12. FORMATAR RANKING
# ============================================================

def formatar_ranking_referencias(
    avaliacoes,
    limite=None,
):
    """
    Exibe o ranking das referências.
    """

    if limite is not None:

        avaliacoes = avaliacoes[
            :limite
        ]


    linhas = []


    for indice, avaliacao in enumerate(
        avaliacoes,
        start=1,
    ):

        linhas.append(
            (
                f"{indice}º — "
                f"{avaliacao.caminho}"
            )
        )

        linhas.append(
            (
                f"TIPO: "
                f"{avaliacao.tipo_imagem}"
            )
        )

        linhas.append(
            (
                f"PONTUAÇÃO: "
                f"{avaliacao.pontuacao}"
            )
        )

        linhas.append(
            ""
        )


    return "\n".join(
        linhas
    )