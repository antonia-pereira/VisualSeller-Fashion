# ============================================================
# VISUALSELLER FASHION
# AURA — SIGNIFICADO DO PRODUTO
# ============================================================

from dataclasses import dataclass, field
from typing import List


# ============================================================
# 1. MODELO DE HIPÓTESE
# ============================================================

@dataclass
class HipoteseSignificado:
    """
    Representa uma hipótese de significado percebido
    a partir de evidências reais do produto.
    """

    significado: str
    evidencias: List[str] = field(default_factory=list)
    confianca: str = "baixa"


# ============================================================
# 2. NORMALIZAÇÃO
# ============================================================

def normalizar_texto(valor):
    """
    Converte valores para texto simples e minúsculo
    para facilitar a análise.
    """

    if valor is None:
        return ""

    if isinstance(valor, list):
        return " ".join(str(item) for item in valor).lower()

    return str(valor).lower()


# ============================================================
# 3. COLETAR EVIDÊNCIAS
# ============================================================

def coletar_evidencias_produto(ficha):
    """
    Reúne somente informações presentes na ficha.
    Não cria novas características.
    """

    dados = ficha.model_dump()

    evidencias = []

    campos_observaveis = [
        "materiais_visuais",
        "transparencia",
        "decote_frente",
        "decote_costas",
        "manga",
        "acabamento_mangas",
        "fechamento",
    ]

    for campo in campos_observaveis:

        valor = dados.get(campo)

        if valor is None:
            continue

        if isinstance(valor, list):

            for item in valor:

                if item:
                    evidencias.append(str(item))

        else:

            texto = str(valor).strip()

            if texto:
                evidencias.append(texto)

    return evidencias


# ============================================================
# 4. CRIAR HIPÓTESE
# ============================================================

def criar_hipotese(
    significado,
    evidencias,
):
    """
    Cria uma hipótese e calcula a confiança
    pela quantidade de evidências independentes.
    """

    evidencias_unicas = []

    for evidencia in evidencias:

        if evidencia not in evidencias_unicas:
            evidencias_unicas.append(evidencia)


    quantidade = len(evidencias_unicas)


    if quantidade >= 3:

        confianca = "alta"

    elif quantidade == 2:

        confianca = "media"

    else:

        confianca = "baixa"


    return HipoteseSignificado(
        significado=significado,
        evidencias=evidencias_unicas,
        confianca=confianca,
    )


# ============================================================
# 5. ANALISAR SIGNIFICADOS
# ============================================================

def analisar_significados(ficha):
    """
    Analisa combinações de características observadas
    e produz hipóteses de linguagem visual.

    Importante:
    hipótese não é característica técnica.
    """

    evidencias = coletar_evidencias_produto(ficha)

    texto = " ".join(
        normalizar_texto(item)
        for item in evidencias
    )

    hipoteses = []


    # --------------------------------------------------------
    # SENSUALIDADE
    # --------------------------------------------------------

    sinais_sensualidade = []

    if "transpar" in texto:
        sinais_sensualidade.append(
            "presença de transparência"
        )

    if "renda" in texto:
        sinais_sensualidade.append(
            "presença de renda"
        )

    if "decote v" in texto:
        sinais_sensualidade.append(
            "decote em V"
        )

    if "profundo" in texto:
        sinais_sensualidade.append(
            "decote profundo"
        )


    if len(sinais_sensualidade) >= 2:

        hipoteses.append(
            criar_hipotese(
                "sensualidade",
                sinais_sensualidade,
            )
        )


    # --------------------------------------------------------
    # DELICADEZA
    # --------------------------------------------------------

    sinais_delicadeza = []

    if "renda floral" in texto:
        sinais_delicadeza.append(
            "renda com desenho floral"
        )

    if "transpar" in texto:
        sinais_delicadeza.append(
            "transparência localizada"
        )


    if len(sinais_delicadeza) >= 2:

        hipoteses.append(
            criar_hipotese(
                "delicadeza",
                sinais_delicadeza,
            )
        )


    # --------------------------------------------------------
    # CONTRASTE VISUAL
    # --------------------------------------------------------

    sinais_contraste = []

    if "transpar" in texto:
        sinais_contraste.append(
            "áreas translúcidas"
        )

    if "opac" in texto:
        sinais_contraste.append(
            "áreas opacas"
        )

    if "canelad" in texto:
        sinais_contraste.append(
            "acabamento canelado"
        )


    if len(sinais_contraste) >= 2:

        hipoteses.append(
            criar_hipotese(
                "contraste visual",
                sinais_contraste,
            )
        )


    return hipoteses


# ============================================================
# 6. FORMATAR RESULTADO
# ============================================================

def formatar_significados(hipoteses):
    """
    Cria uma visualização legível das hipóteses.
    """

    if not hipoteses:

        return (
            "Nenhuma hipótese de significado "
            "possui evidência suficiente."
        )


    linhas = [
        "HIPÓTESES DE SIGNIFICADO",
        "",
    ]


    for hipotese in hipoteses:

        linhas.append(
            hipotese.significado.upper()
        )

        linhas.append(
            f"Confiança: {hipotese.confianca}"
        )

        linhas.append(
            "Evidências:"
        )


        for evidencia in hipotese.evidencias:

            linhas.append(
                f"- {evidencia}"
            )


        linhas.append("")


    return "\n".join(linhas)