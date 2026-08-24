from collections import defaultdict
from typing import Any


# ============================================================
# VISUALSELLER FASHION
# AURA — CONSOLIDAÇÃO DE EVIDÊNCIAS
# ============================================================


# ============================================================
# 1. CAMPOS QUE PODEM RECEBER INFORMAÇÕES COMPLEMENTARES
# ============================================================

CAMPOS_COMPLEMENTARES = {
    "materiais_visuais",
    "transparencia",
    "acabamento_mangas",
    "acabamento_pernas",
    "acabamento_decote",
}


# ============================================================
# 2. PESO DA CONFIANÇA
# ============================================================

PESO_CONFIANCA = {
    "alta": 3,
    "media": 2,
    "baixa": 1,
}


# ============================================================
# 3. AGRUPAR EVIDÊNCIAS POR CAMPO
# ============================================================

def agrupar_evidencias_por_campo(
    evidencias: list[dict[str, Any]],
) -> dict[str, list[dict[str, Any]]]:

    grupos = defaultdict(list)

    for evidencia in evidencias:

        campo = evidencia.get(
            "campo"
        )

        if not campo:
            continue

        grupos[campo].append(
            evidencia
        )

    return dict(
        grupos
    )


# ============================================================
# 4. NORMALIZAÇÃO DE TEXTO
# ============================================================

def normalizar_texto(
    valor: str,
) -> str:

    return (
        valor
        .strip()
        .lower()
    )


# ============================================================
# 5. NORMALIZAÇÃO SEMÂNTICA POR CAMPO
# ============================================================

def normalizar_valor_campo(
    campo: str,
    valor: Any,
):
    """
    Converte descrições equivalentes
    para uma representação única.
    """

    if isinstance(
        valor,
        bool,
    ):
        return valor

    if not isinstance(
        valor,
        str,
    ):
        return valor


    texto = normalizar_texto(
        valor
    )


    # --------------------------------------------------------
    # POSSUI FORRO / BOJO
    # --------------------------------------------------------

    if campo in {
        "possui_forro",
        "possui_bojo",
    }:

        if texto in {
            "sim",
            "true",
            "possui",
            "tem",
        }:
            return True

        if texto in {
            "não",
            "nao",
            "false",
            "não possui",
            "nao possui",
            "não tem",
            "nao tem",
        }:
            return False


    # --------------------------------------------------------
    # FECHAMENTO
    # --------------------------------------------------------

    if campo == "fechamento":

        if "colchet" in texto:

            return "colchetes"

        if (
            "ziper" in texto
            or "zíper" in texto
        ):

            return "zíper"

        if (
            "botao" in texto
            or "botão" in texto
        ):

            return "botões"


    # --------------------------------------------------------
    # MANGA
    # --------------------------------------------------------

    if campo == "manga":

        if "longa" in texto:

            return "longa"

        if "curta" in texto:

            return "curta"

        if "sem manga" in texto:

            return "sem manga"


    # --------------------------------------------------------
    # DECOTES
    # --------------------------------------------------------

    if campo in {
        "decote_frente",
        "decote_costas",
    }:

        if "u profundo" in texto:

            return "U profundo"

        if (
            texto == "u"
            or "formato u" in texto
        ):

            return "U"

        if (
            texto == "v"
            or "formato v" in texto
        ):

            return "V"

        if "v profundo" in texto:

            return "V profundo"


    # --------------------------------------------------------
    # REFERÊNCIA
    # --------------------------------------------------------

    if campo == "referencia":

        partes = texto.split()

        if partes:

            primeira_parte = partes[0]

            if primeira_parte.isdigit():

                return primeira_parte


    return texto


# ============================================================
# 6. EXTRAIR TAMANHO DA REFERÊNCIA
# ============================================================

def extrair_tamanho_da_referencia(
    valor: Any,
):
    """
    Exemplo:

    '277 P'
    → retorna 'P'
    """

    if not isinstance(
        valor,
        str,
    ):
        return None

    partes = (
        valor
        .strip()
        .upper()
        .split()
    )

    if len(
        partes
    ) < 2:

        return None

    ultimo = partes[-1]

    tamanhos_validos = {
        "PP",
        "P",
        "M",
        "G",
        "GG",
        "XG",
        "XGG",
    }

    if ultimo in tamanhos_validos:

        return ultimo

    return None


# ============================================================
# 7. OBTER VALORES ÚNICOS ORIGINAIS
# ============================================================

def obter_valores_unicos(
    evidencias: list[dict[str, Any]],
):
    """
    Mantém os valores originais
    para análise e auditoria.
    """

    valores = []

    normalizados = []

    for evidencia in evidencias:

        valor = evidencia.get(
            "valor"
        )

        if isinstance(
            valor,
            str,
        ):

            chave = normalizar_texto(
                valor
            )

        else:

            chave = valor

        if chave not in normalizados:

            normalizados.append(
                chave
            )

            valores.append(
                valor
            )

    return valores


# ============================================================
# 8. CALCULAR FORÇA DOS VALORES
# ============================================================

def calcular_forca_valores(
    campo: str,
    evidencias: list[dict[str, Any]],
):
    """
    Soma pesos de confiança para cada
    interpretação semântica.
    """

    pontuacao = defaultdict(int)

    detalhes = defaultdict(list)

    for evidencia in evidencias:

        valor_original = evidencia.get(
            "valor"
        )

        valor_normalizado = normalizar_valor_campo(
            campo=campo,
            valor=valor_original,
        )

        confianca = evidencia.get(
            "confianca",
            "baixa",
        )

        peso = PESO_CONFIANCA.get(
            confianca,
            1,
        )

        pontuacao[
            valor_normalizado
        ] += peso

        detalhes[
            valor_normalizado
        ].append(
            evidencia
        )

    return {
        "pontuacao":
            dict(
                pontuacao
            ),

        "detalhes":
            dict(
                detalhes
            ),
    }


# ============================================================
# 9. ESCOLHER VALOR DOMINANTE
# ============================================================

def escolher_valor_dominante(
    campo: str,
    evidencias: list[dict[str, Any]],
):

    resultado = calcular_forca_valores(
        campo=campo,
        evidencias=evidencias,
    )

    pontuacao = resultado[
        "pontuacao"
    ]

    if not pontuacao:

        return None

    return max(
        pontuacao,
        key=pontuacao.get,
    )


# ============================================================
# 10. VERIFICAR DOMINÂNCIA
# ============================================================

def existe_dominancia_clara(
    campo: str,
    evidencias: list[dict[str, Any]],
) -> bool:

    resultado = calcular_forca_valores(
        campo=campo,
        evidencias=evidencias,
    )

    pontuacoes = sorted(
        resultado[
            "pontuacao"
        ].values(),
        reverse=True,
    )

    if len(
        pontuacoes
    ) <= 1:

        return True

    maior = pontuacoes[0]
    segunda = pontuacoes[1]

    return (
        maior >= segunda + 2
    )


# ============================================================
# 11. CLASSIFICAR GRUPO
# ============================================================

def classificar_grupo(
    campo: str,
    evidencias: list[dict[str, Any]],
) -> str:

    if not evidencias:

        return "SEM_EVIDENCIA"


    # --------------------------------------------------------
    # CAMPOS COMPLEMENTARES
    # --------------------------------------------------------

    if campo in CAMPOS_COMPLEMENTARES:

        valores = obter_valores_unicos(
            evidencias
        )

        if len(
            valores
        ) == 1:

            return "CONCORDANCIA"

        return "COMPLEMENTAR"


    # --------------------------------------------------------
    # CAMPOS OBJETIVOS
    # --------------------------------------------------------

    valores_semanticos = []

    for evidencia in evidencias:

        valor = normalizar_valor_campo(
            campo=campo,
            valor=evidencia.get(
                "valor"
            ),
        )

        if valor not in valores_semanticos:

            valores_semanticos.append(
                valor
            )


    if len(
        valores_semanticos
    ) == 1:

        return "CONCORDANCIA"


    if existe_dominancia_clara(
        campo=campo,
        evidencias=evidencias,
    ):

        return "CONCORDANCIA"


    return "CONFLITO"


# ============================================================
# 12. RESUMIR GRUPOS
# ============================================================

def resumir_grupos(
    grupos: dict[str, list[dict[str, Any]]],
) -> list[dict[str, Any]]:

    resumo = []

    for campo, evidencias in grupos.items():

        valores = obter_valores_unicos(
            evidencias
        )

        imagens = []

        confiancas = []

        for evidencia in evidencias:

            imagem = evidencia.get(
                "tipo_imagem"
            )

            confianca = evidencia.get(
                "confianca"
            )

            if (
                imagem is not None
                and imagem not in imagens
            ):
                imagens.append(
                    imagem
                )

            if (
                confianca is not None
                and confianca not in confiancas
            ):
                confiancas.append(
                    confianca
                )


        classificacao = classificar_grupo(
            campo=campo,
            evidencias=evidencias,
        )


        if campo in CAMPOS_COMPLEMENTARES:

            valor_consolidado = None

        else:

            valor_consolidado = escolher_valor_dominante(
                campo=campo,
                evidencias=evidencias,
            )


        resumo.append(
            {
                "campo":
                    campo,

                "classificacao":
                    classificacao,

                "quantidade_evidencias":
                    len(
                        evidencias
                    ),

                "valores":
                    valores,

                "valor_consolidado":
                    valor_consolidado,

                "imagens":
                    imagens,

                "confiancas":
                    confiancas,
            }
        )

    return resumo


# ============================================================
# 13. CONSOLIDAR MATERIAIS VISUAIS
# ============================================================

def consolidar_materiais_visuais(
    valores: list[Any],
) -> list[str]:
    """
    Reduz descrições repetitivas
    a categorias visuais úteis.
    """

    texto_total = " ".join(
        str(valor).lower()
        for valor in valores
    )

    materiais = []


    if "renda" in texto_total:

        materiais.append(
            "renda floral"
        )


    if (
        "tela" in texto_total
        or "tule" in texto_total
        or "translúcid" in texto_total
        or "transparente" in texto_total
    ):

        materiais.append(
            "malha/tela fina translúcida"
        )


    if (
        "canelad" in texto_total
        or "plissad" in texto_total
    ):

        materiais.append(
            "malha canelada"
        )


    if (
        "liso" in texto_total
        or "brilho" in texto_total
        or "acetinado" in texto_total
    ):

        materiais.append(
            "tecido liso com leve brilho"
        )


    if not materiais:

        materiais = [
            str(valor)
            for valor in valores
        ]


    return materiais


# ============================================================
# 14. CONSOLIDAR TRANSPARÊNCIA
# ============================================================

def consolidar_transparencia(
    valores: list[Any],
) -> str:
    """
    Resume as regiões em que há transparência.
    """

    texto_total = " ".join(
        str(valor).lower()
        for valor in valores
    )

    regioes = []


    if "manga" in texto_total:

        regioes.append(
            "mangas"
        )


    if (
        "lateral" in texto_total
        or "cintura" in texto_total
    ):

        regioes.append(
            "regiões laterais"
        )


    if "costas" in texto_total:

        regioes.append(
            "costas"
        )


    if "renda" in texto_total:

        regioes.append(
            "áreas em renda"
        )


    regioes_unicas = []

    for regiao in regioes:

        if regiao not in regioes_unicas:

            regioes_unicas.append(
                regiao
            )


    if regioes_unicas:

        return (
            "Transparência parcial em "
            + ", ".join(
                regioes_unicas
            )
            + "."
        )


    return "Transparência parcial."


# ============================================================
# 15. CONSOLIDAR ACABAMENTO DAS MANGAS
# ============================================================

def consolidar_acabamento_mangas(
    valores: list[Any],
) -> str:

    texto_total = " ".join(
        str(valor).lower()
        for valor in valores
    )


    if (
        "punho" in texto_total
        and "canelad" in texto_total
    ):

        return (
            "Punho largo em malha "
            "canelada e opaca."
        )


    if "punho" in texto_total:

        return "Punho largo e opaco."


    return "Acabamento simples nas mangas."


# ============================================================
# 16. GERAR CONHECIMENTO CONSOLIDADO
# ============================================================

def gerar_conhecimento_consolidado(
    grupos: dict[str, list[dict[str, Any]]],
) -> dict[str, Any]:
    """
    Produz conhecimento final limpo,
    pronto para alimentar a ficha técnica.
    """

    conhecimento = {}

    resumo = resumir_grupos(
        grupos
    )


    for item in resumo:

        campo = item[
            "campo"
        ]

        classificacao = item[
            "classificacao"
        ]

        valor_consolidado = item.get(
            "valor_consolidado"
        )

        valores = item.get(
            "valores",
            [],
        )


        # ----------------------------------------------------
        # CONCORDÂNCIA
        # ----------------------------------------------------

        if classificacao == "CONCORDANCIA":

            conhecimento[
                campo
            ] = valor_consolidado

            continue


        # ----------------------------------------------------
        # COMPLEMENTARES ESPECIAIS
        # ----------------------------------------------------

        if classificacao == "COMPLEMENTAR":

            if campo == "materiais_visuais":

                conhecimento[
                    campo
                ] = consolidar_materiais_visuais(
                    valores
                )

                continue


            if campo == "transparencia":

                conhecimento[
                    campo
                ] = consolidar_transparencia(
                    valores
                )

                continue


            if campo == "acabamento_mangas":

                conhecimento[
                    campo
                ] = consolidar_acabamento_mangas(
                    valores
                )

                continue


            conhecimento[
                campo
            ] = valores

            continue


        # ----------------------------------------------------
        # CONFLITO REAL
        # ----------------------------------------------------

        if classificacao == "CONFLITO":

            conhecimento[
                campo
            ] = {
                "status":
                    "PENDENTE",

                "valores":
                    valores,

                "motivo":
                    (
                        "Existem evidências "
                        "conflitantes para este campo."
                    ),
            }


    # ========================================================
    # 17. TRATAR REFERÊNCIA + TAMANHO
    # ========================================================

    if "referencia" in grupos:

        evidencias_referencia = grupos[
            "referencia"
        ]

        for evidencia in evidencias_referencia:

            valor_original = evidencia.get(
                "valor"
            )

            tamanho = extrair_tamanho_da_referencia(
                valor_original
            )

            if tamanho:

                conhecimento[
                    "tamanho_medido"
                ] = tamanho

                break


    return conhecimento