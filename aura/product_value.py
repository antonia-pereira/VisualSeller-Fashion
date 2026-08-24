# ============================================================
# VISUALSELLER FASHION
# AURA — VALOR PERCEBIDO DO PRODUTO
# ============================================================

from dataclasses import dataclass
from typing import List


# ============================================================
# 1. MODELO DE VALOR
# ============================================================

@dataclass
class ValorProduto:
    valor: str
    tipo: str
    confianca: str
    motivo: str
    evidencias: List[str]


# ============================================================
# 2. NORMALIZAR TEXTO
# ============================================================

def normalizar_texto(
    valor,
):

    if valor is None:
        return ""

    return str(
        valor
    ).strip().lower()


# ============================================================
# 3. VERIFICAR TEXTO
# ============================================================

def contem_algum(
    texto,
    termos,
):

    texto_normalizado = normalizar_texto(
        texto
    )


    for termo in termos:

        if normalizar_texto(
            termo
        ) in texto_normalizado:

            return True


    return False


# ============================================================
# 4. BUSCAR EVIDÊNCIAS NA FICHA
# ============================================================

def coletar_evidencias_ficha(
    ficha,
):

    dados = ficha.model_dump()

    evidencias = []


    campos = [
        "composicao_principal",
        "composicao_forro",
        "materiais_visuais",
        "manga",
        "decote_frente",
        "decote_costas",
        "fechamento",
        "possui_bojo",
        "possui_forro",
        "transparencia",
        "acabamento_mangas",
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

                if item is not None:

                    evidencias.append(
                        str(item)
                    )

        else:

            evidencias.append(
                f"{campo}: {valor}"
            )


    return evidencias


# ============================================================
# 5. REMOVER REPETIÇÕES
# ============================================================

def remover_repeticoes(
    itens,
):

    resultado = []

    vistos = set()


    for item in itens:

        chave = normalizar_texto(
            item
        )


        if not chave:
            continue


        if chave in vistos:
            continue


        vistos.add(
            chave
        )

        resultado.append(
            item
        )


    return resultado


# ============================================================
# 6. IDENTIFICAR VALORES PERCEBIDOS
# ============================================================

def analisar_valor_produto(
    ficha,
    identidade,
    desejos,
):
    """
    Identifica possíveis fontes de valor percebido.

    A Aura só pode usar:
    - fatos presentes na ficha;
    - identidade já sustentada;
    - desejos já formulados.

    Não transforma hipótese em promessa comercial.
    """

    valores = []

    evidencias_ficha = coletar_evidencias_ficha(
        ficha
    )


    texto_evidencias = " ".join(
        normalizar_texto(
            evidencia
        )
        for evidencia in evidencias_ficha
    )


    # ========================================================
    # VALOR 1 — RIQUEZA VISUAL
    # ========================================================

    sinais_visuais = []


    if "renda" in texto_evidencias:

        sinais_visuais.append(
            "presença de renda"
        )


    if (
        "transpar" in texto_evidencias
        or "translúc" in texto_evidencias
    ):

        sinais_visuais.append(
            "presença de transparência"
        )


    if (
        "canelad" in texto_evidencias
        or "textura" in texto_evidencias
    ):

        sinais_visuais.append(
            "variação de textura"
        )


    if len(
        sinais_visuais
    ) >= 2:

        valores.append(
            ValorProduto(
                valor=(
                    "riqueza visual pela combinação "
                    "de materiais, transparências e texturas"
                ),

                tipo="estetico",

                confianca="alta",

                motivo=(
                    "A peça apresenta diferentes elementos "
                    "visuais que trabalham em conjunto e "
                    "aumentam a complexidade percebida "
                    "da construção."
                ),

                evidencias=sinais_visuais,
            )
        )


    # ========================================================
    # VALOR 2 — CONSTRUÇÃO VISUAL MARCANTE
    # ========================================================

    if "contraste visual" in [
        normalizar_texto(
            item
        )
        for item in identidade.tracos_dominantes
    ]:

        evidencias = []


        for evidencia in identidade.evidencias:

            if contem_algum(
                evidencia,
                [
                    "translúc",
                    "opac",
                    "canelad",
                    "transpar",
                ],
            ):

                evidencias.append(
                    evidencia
                )


        evidencias = remover_repeticoes(
            evidencias
        )


        if evidencias:

            valores.append(
                ValorProduto(
                    valor=(
                        "presença visual construída "
                        "pelo contraste entre áreas "
                        "translúcidas, opacas e texturizadas"
                    ),

                    tipo="estetico",

                    confianca="alta",

                    motivo=(
                        "O contraste entre diferentes "
                        "superfícies pode tornar a peça "
                        "visualmente mais marcante."
                    ),

                    evidencias=evidencias,
                )
            )


    # ========================================================
    # VALOR 3 — COMPOSIÇÃO INFORMADA
    # ========================================================

    dados = ficha.model_dump()


    composicao = dados.get(
        "composicao_principal"
    )


    if composicao:

        valores.append(
            ValorProduto(
                valor=(
                    "composição têxtil informada"
                ),

                tipo="informacional",

                confianca="alta",

                motivo=(
                    "A presença da composição oficial "
                    "reduz incerteza sobre os materiais "
                    "declarados do produto."
                ),

                evidencias=[
                    str(
                        composicao
                    )
                ],
            )
        )


    # ========================================================
    # VALOR 4 — FORRO IDENTIFICADO
    # ========================================================

    possui_forro = dados.get(
        "possui_forro"
    )


    composicao_forro = dados.get(
        "composicao_forro"
    )


    if possui_forro is True:

        evidencias = [
            "possui forro"
        ]


        if composicao_forro:

            evidencias.append(
                f"composição do forro: {composicao_forro}"
            )


        valores.append(
            ValorProduto(
                valor=(
                    "estrutura interna identificada "
                    "e descrita"
                ),

                tipo="tecnico",

                confianca="alta",

                motivo=(
                    "A existência do forro e, quando "
                    "disponível, sua composição tornam "
                    "a ficha do produto mais completa."
                ),

                evidencias=evidencias,
            )
        )


    # ========================================================
    # VALOR 5 — DETALHAMENTO DO ACABAMENTO
    # ========================================================

    acabamento = dados.get(
        "acabamento_mangas"
    )


    if acabamento:

        valores.append(
            ValorProduto(
                valor=(
                    "acabamento construtivo identificado"
                ),

                tipo="construtivo",

                confianca="alta",

                motivo=(
                    "Detalhes de acabamento ajudam "
                    "a demonstrar como a peça foi "
                    "visualmente construída."
                ),

                evidencias=[
                    str(
                        acabamento
                    )
                ],
            )
        )


    # ========================================================
    # VALOR 6 — COERÊNCIA COM OS DESEJOS
    # ========================================================

    for desejo in desejos:

        texto_desejo = normalizar_texto(
            desejo.desejo
        )


        if (
            "presença visual" in texto_desejo
            or "visualmente marcante" in texto_desejo
        ):

            valores.append(
                ValorProduto(
                    valor=(
                        "coerência entre a identidade "
                        "visual do produto e a busca "
                        "por presença estética"
                    ),

                    tipo="conexao",

                    confianca=desejo.confianca,

                    motivo=(
                        "A leitura visual do produto "
                        "é compatível com uma possível "
                        "busca por maior presença "
                        "na própria expressão."
                    ),

                    evidencias=(
                        desejo.evidencias.copy()
                    ),
                )
            )

            break


    return valores


# ============================================================
# 7. PROMESSAS QUE A AURA NÃO DEVE FAZER
# ============================================================

def identificar_promessas_nao_sustentadas(
    ficha,
):
    """
    Lista alegações que não devem ser usadas
    como argumentos de venda sem evidência.
    """

    return [
        (
            "Não afirmar conforto sem teste, "
            "avaliação ou informação do fabricante."
        ),

        (
            "Não afirmar alta durabilidade "
            "sem evidência específica."
        ),

        (
            "Não afirmar qualidade premium "
            "apenas pela aparência."
        ),

        (
            "Não afirmar que a peça modela, "
            "afina ou valoriza o corpo sem evidência."
        ),

        (
            "Não afirmar ajuste perfeito "
            "para diferentes corpos."
        ),

        (
            "Não afirmar que os materiais visuais "
            "percebidos correspondem à composição "
            "oficial, salvo quando confirmados "
            "pela etiqueta."
        ),
    ]


# ============================================================
# 8. FORMATAR RESULTADO
# ============================================================

def formatar_valores(
    valores,
    limites,
):

    linhas = [
        "VALOR PERCEBIDO DO PRODUTO",
        "",
    ]


    if valores:

        for numero, valor in enumerate(
            valores,
            start=1,
        ):

            linhas.append(
                f"VALOR {numero}"
            )

            linhas.append(
                f"Valor percebido: {valor.valor}"
            )

            linhas.append(
                f"Tipo: {valor.tipo}"
            )

            linhas.append(
                f"Confiança: {valor.confianca}"
            )

            linhas.append(
                f"Por quê: {valor.motivo}"
            )

            linhas.append(
                "Evidências:"
            )


            for evidencia in valor.evidencias:

                linhas.append(
                    f"- {evidencia}"
                )


            linhas.append(
                ""
            )

    else:

        linhas.append(
            "Ainda não existem evidências "
            "suficientes para formular "
            "valor percebido."
        )

        linhas.append(
            ""
        )


    linhas.append(
        "O QUE A AURA NÃO DEVE PROMETER"
    )

    linhas.append(
        ""
    )


    for limite in limites:

        linhas.append(
            f"- {limite}"
        )


    return "\n".join(
        linhas
    )