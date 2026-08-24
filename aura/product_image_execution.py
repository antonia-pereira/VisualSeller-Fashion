# ============================================================
# VISUALSELLER FASHION
# AURA — EXECUÇÃO DE IMAGEM
# ============================================================

from dataclasses import dataclass, field
from typing import Any, List

from aura.product_reference_selector import (
    selecionar_melhores_referencias,
)


# ============================================================
# 1. MODELO DE EXECUÇÃO
# ============================================================

@dataclass
class ExecucaoImagem:
    """
    Representa a estratégia de execução de uma imagem.

    Esta camada não gera a imagem.
    Ela decide como o prompt deve ser executado.
    """

    numero_imagem: int

    funcao: str

    modo_execucao: str

    prompt: str

    usar_referencia: bool = True

    tipos_referencia: List[str] = field(
        default_factory=list
    )

    referencias_sugeridas: List[str] = field(
        default_factory=list
    )

    preservar: List[str] = field(
        default_factory=list
    )

    restricoes: List[str] = field(
        default_factory=list
    )

    justificativa: str = ""

    confianca: str = "media"

    limite_referencias: int = 0

    selecao_visual_inteligente: bool = False


# ============================================================
# 2. MODELO DO PACOTE DE EXECUÇÃO
# ============================================================

@dataclass
class PlanoExecucaoImagens:
    """
    Representa a estratégia de execução
    das imagens da campanha.
    """

    execucoes: List[ExecucaoImagem] = field(
        default_factory=list
    )

    regras_gerais: List[str] = field(
        default_factory=list
    )

    confianca: str = "media"


# ============================================================
# 3. FUNÇÕES AUXILIARES
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


def lista_segura(
    valor: Any,
) -> list:
    """
    Garante que o valor seja tratado como lista.
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


def obter_valor(
    objeto,
    nome,
    padrao=None,
):
    """
    Busca um valor em dicionário
    ou objeto.
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


# ============================================================
# 4. IDENTIFICAR TIPOS DE REFERÊNCIA
# ============================================================

def definir_tipos_referencia(
    funcao,
):
    """
    Define quais tipos de fotos reais
    são úteis para cada imagem.

    A ordem representa prioridade.
    """

    funcao = texto_seguro(
        funcao
    ).lower()


    if funcao == "capa":

        return [
            "frente",
            "costas",
        ]


    if "detalhes visuais" in funcao:

        return [
            "detalhe",
            "composicao",
        ]


    if "construção" in funcao:

        return [
            "frente",
            "costas",
            "detalhe",
        ]


    if "texturas" in funcao:

        return [
            "detalhe",
            "composicao",
        ]


    if "informação técnica" in funcao:

        return [
            "etiqueta",
            "composicao",
        ]


    if "síntese" in funcao:

        return [
            "frente",
            "costas",
            "detalhe",
        ]


    if "fechamento" in funcao:

        return [
            "frente",
            "costas",
        ]


    return [
        "frente",
        "detalhe",
    ]


# ============================================================
# 5. LIMITE DE REFERÊNCIAS POR FUNÇÃO
# ============================================================

def definir_limite_referencias(
    funcao,
):
    """
    Define o máximo de referências
    necessárias para cada imagem.
    """

    funcao = texto_seguro(
        funcao
    ).lower()


    if funcao == "capa":
        return 2


    if "detalhes visuais" in funcao:
        return 3


    if "construção" in funcao:
        return 4


    if "texturas" in funcao:
        return 3


    if "informação técnica" in funcao:
        return 2


    if "síntese" in funcao:
        return 4


    if "fechamento" in funcao:
        return 2


    return 2


# ============================================================
# 6. COTAS DE REFERÊNCIA POR FUNÇÃO
# ============================================================

def definir_cotas_referencia(
    funcao,
):
    """
    Define quantas imagens de cada tipo
    devem ser utilizadas no fallback estrutural.
    """

    funcao = texto_seguro(
        funcao
    ).lower()


    if funcao == "capa":

        return {
            "frente": 1,
            "costas": 1,
        }


    if "detalhes visuais" in funcao:

        return {
            "detalhe": 2,
            "composicao": 1,
        }


    if "construção" in funcao:

        return {
            "frente": 1,
            "costas": 1,
            "detalhe": 2,
        }


    if "texturas" in funcao:

        return {
            "detalhe": 2,
            "composicao": 1,
        }


    if "informação técnica" in funcao:

        return {
            "etiqueta": 1,
            "composicao": 1,
        }


    if "síntese" in funcao:

        return {
            "frente": 1,
            "costas": 1,
            "detalhe": 2,
        }


    if "fechamento" in funcao:

        return {
            "frente": 1,
            "costas": 1,
        }


    return {
        "frente": 1,
        "detalhe": 1,
    }


# ============================================================
# 7. MODO DE EXECUÇÃO
# ============================================================

def definir_modo_execucao(
    funcao,
):
    """
    Decide como o modelo de imagem
    deverá trabalhar.

    reference_edit:
        usa uma foto real como base principal.

    reference_composition:
        combina referências reais
        em uma nova composição.

    technical_layout:
        organiza informação técnica.
    """

    funcao = texto_seguro(
        funcao
    ).lower()


    if funcao == "capa":

        return "reference_composition"


    if "detalhes visuais" in funcao:

        return "reference_edit"


    if "construção" in funcao:

        return "reference_composition"


    if "texturas" in funcao:

        return "reference_edit"


    if "informação técnica" in funcao:

        return "technical_layout"


    if "síntese" in funcao:

        return "reference_composition"


    if "fechamento" in funcao:

        return "reference_composition"


    return "reference_edit"


# ============================================================
# 8. ORGANIZAR IMAGENS POR TIPO
# ============================================================

def organizar_imagens_por_tipo(
    imagens_disponiveis,
):
    """
    Agrupa imagens disponíveis pelo tipo.
    """

    grupos = {}


    for imagem in lista_segura(
        imagens_disponiveis
    ):

        tipo = texto_seguro(
            obter_valor(
                imagem,
                "tipo",
                "",
            )
        ).lower()

        caminho = texto_seguro(
            obter_valor(
                imagem,
                "caminho",
                "",
            )
        )


        if (
            not tipo
            or not caminho
        ):
            continue


        if tipo not in grupos:

            grupos[
                tipo
            ] = []


        adicionar_unico(
            grupos[tipo],
            caminho,
        )


    return grupos


# ============================================================
# 9. SELEÇÃO ESTRUTURAL — FALLBACK
# ============================================================

def selecionar_referencias_estruturais(
    funcao,
    tipos_referencia,
    imagens_disponiveis=None,
):
    """
    Seleção antiga da Aura.

    É utilizada somente quando ainda
    não existe resultado visual disponível.
    """

    if not imagens_disponiveis:

        return []


    limite = definir_limite_referencias(
        funcao
    )

    cotas = definir_cotas_referencia(
        funcao
    )

    grupos = organizar_imagens_por_tipo(
        imagens_disponiveis
    )

    selecionadas = []


    # --------------------------------------------------------
    # PRIMEIRA PASSAGEM — RESPEITAR COTAS
    # --------------------------------------------------------

    for tipo in tipos_referencia:

        quantidade_desejada = (
            cotas.get(
                tipo,
                0,
            )
        )


        if quantidade_desejada <= 0:

            continue


        candidatas = grupos.get(
            tipo,
            [],
        )


        for caminho in candidatas[
            :quantidade_desejada
        ]:

            if len(
                selecionadas
            ) >= limite:

                break


            adicionar_unico(
                selecionadas,
                caminho,
            )


        if len(
            selecionadas
        ) >= limite:

            break


    # --------------------------------------------------------
    # SEGUNDA PASSAGEM — COMPLETAR SE NECESSÁRIO
    # --------------------------------------------------------

    if len(
        selecionadas
    ) < limite:

        for tipo in tipos_referencia:

            candidatas = grupos.get(
                tipo,
                [],
            )


            for caminho in candidatas:

                if len(
                    selecionadas
                ) >= limite:

                    break


                adicionar_unico(
                    selecionadas,
                    caminho,
                )


            if len(
                selecionadas
            ) >= limite:

                break


    return selecionadas


# ============================================================
# 10. SELEÇÃO VISUAL INTELIGENTE
# ============================================================

def selecionar_referencias_visuais(
    funcao,
    tipos_referencia,
    resultado_visao,
):
    """
    Usa as evidências produzidas pela visão
    da Aura para selecionar as fotografias
    mais adequadas para cada função.

    Não escolhe pelo nome ou ordem do arquivo.

    Escolhe pelo ranking visual.
    """

    if not resultado_visao:

        return []


    limite = definir_limite_referencias(
        funcao
    )


    melhores = selecionar_melhores_referencias(

        resultado_visao=
            resultado_visao,

        funcao_destino=
            funcao,

        limite=
            limite,

        tipos_permitidos=
            tipos_referencia,
    )


    referencias = []


    for avaliacao in melhores:

        caminho = texto_seguro(
            avaliacao.caminho
        )


        if caminho:

            adicionar_unico(
                referencias,
                caminho,
            )


    return referencias


# ============================================================
# 11. SELEÇÃO FINAL DE REFERÊNCIAS
# ============================================================

def selecionar_referencias_sugeridas(
    funcao,
    tipos_referencia,
    imagens_disponiveis=None,
    resultado_visao=None,
):
    """
    Decide qual sistema de seleção será usado.

    PRIORIDADE:

    1. seleção visual inteligente;
    2. fallback estrutural.
    """

    # ========================================================
    # TENTAR PRIMEIRO A VISÃO
    # ========================================================

    if resultado_visao:

        try:

            referencias_visuais = (
                selecionar_referencias_visuais(

                    funcao=
                        funcao,

                    tipos_referencia=
                        tipos_referencia,

                    resultado_visao=
                        resultado_visao,
                )
            )


            if referencias_visuais:

                return (
                    referencias_visuais,
                    True,
                )


        except Exception as erro:

            print(
                "\n"
                "ATENÇÃO — SELEÇÃO VISUAL"
            )

            print(
                "Não foi possível utilizar "
                "o ranking visual inteligente."
            )

            print(
                "A Aura utilizará o fallback "
                "estrutural."
            )

            print(
                f"Motivo: {erro}"
            )


    # ========================================================
    # FALLBACK
    # ========================================================

    referencias_estruturais = (
        selecionar_referencias_estruturais(

            funcao=
                funcao,

            tipos_referencia=
                tipos_referencia,

            imagens_disponiveis=
                imagens_disponiveis,
        )
    )


    return (
        referencias_estruturais,
        False,
    )


# ============================================================
# 12. JUSTIFICATIVA
# ============================================================

def criar_justificativa(
    funcao,
    modo_execucao,
    referencias_sugeridas=None,
    selecao_visual_inteligente=False,
):
    """
    Explica como as referências foram escolhidas.
    """

    quantidade = len(
        referencias_sugeridas
        or []
    )


    if selecao_visual_inteligente:

        origem = (
            "As referências foram escolhidas "
            "a partir do ranking visual da Aura, "
            "considerando as evidências observadas "
            "em cada fotografia."
        )

    else:

        origem = (
            "As referências foram escolhidas "
            "pela lógica estrutural de tipos e cotas, "
            "pois não havia ranking visual disponível."
        )


    if modo_execucao == "reference_edit":

        return (
            "Esta imagem depende de fidelidade visual "
            "a detalhes reais do produto. "
            f"Foram selecionadas {quantidade} referência(s). "
            f"{origem}"
        )


    if modo_execucao == "reference_composition":

        return (
            "Esta imagem pode reorganizar visualmente "
            "o produto em uma nova composição, "
            f"utilizando {quantidade} referência(s) "
            "para preservar estrutura e identidade. "
            f"{origem}"
        )


    if modo_execucao == "technical_layout":

        return (
            "Esta imagem tem função informativa. "
            f"Foram selecionadas {quantidade} referência(s) "
            "relacionadas aos dados técnicos. "
            f"{origem}"
        )


    return (
        "A execução deve manter fidelidade "
        "ao produto real. "
        f"{origem}"
    )


# ============================================================
# 13. REGRAS GERAIS DE EXECUÇÃO
# ============================================================

def criar_regras_gerais():
    """
    Regras que valem para toda a campanha.
    """

    return [

        (
            "Toda imagem deve partir das "
            "características reais do produto."
        ),

        (
            "Fotos reais do produto devem ser usadas "
            "como referência sempre que disponíveis."
        ),

        (
            "Quando existir análise visual, "
            "as referências devem ser selecionadas "
            "pela relevância das evidências observadas."
        ),

        (
            "Usar somente as referências necessárias "
            "para a função de cada imagem."
        ),

        (
            "Evitar enviar ao modelo várias imagens "
            "redundantes do mesmo detalhe."
        ),

        (
            "A IA pode alterar fundo, enquadramento, "
            "composição e iluminação, mas não pode "
            "redesenhar o produto."
        ),

        (
            "Cor, modelagem, transparência, renda, "
            "texturas, decotes, mangas, punhos e "
            "fechamento devem permanecer fiéis."
        ),

        (
            "Quando várias referências forem usadas, "
            "elas devem representar o mesmo produto."
        ),

        (
            "Nenhum detalhe visual pode ser criado "
            "apenas para tornar a imagem mais bonita."
        ),

        (
            "A execução deve preservar coerência "
            "visual entre todas as imagens da campanha."
        ),
    ]


# ============================================================
# 14. CRIAR EXECUÇÃO DE UMA IMAGEM
# ============================================================

def criar_execucao_imagem(
    prompt_imagem,
    imagens_disponiveis=None,
    resultado_visao=None,
):
    """
    Transforma um prompt pronto
    em uma estratégia de execução.
    """

    numero = obter_valor(
        prompt_imagem,
        "numero_imagem",
        0,
    )

    funcao = texto_seguro(
        obter_valor(
            prompt_imagem,
            "funcao",
            "",
        )
    )

    prompt = texto_seguro(
        obter_valor(
            prompt_imagem,
            "prompt_principal",
            "",
        )
    )

    preservar = lista_segura(
        obter_valor(
            prompt_imagem,
            "preservar",
            [],
        )
    )

    restricoes = lista_segura(
        obter_valor(
            prompt_imagem,
            "evitar",
            [],
        )
    )

    confianca = texto_seguro(
        obter_valor(
            prompt_imagem,
            "confianca",
            "media",
        )
    )


    # --------------------------------------------------------
    # DECISÕES DE EXECUÇÃO
    # --------------------------------------------------------

    modo_execucao = definir_modo_execucao(
        funcao
    )

    tipos_referencia = definir_tipos_referencia(
        funcao
    )

    limite_referencias = definir_limite_referencias(
        funcao
    )


    (
        referencias_sugeridas,
        selecao_visual_inteligente,
    ) = selecionar_referencias_sugeridas(

        funcao=
            funcao,

        tipos_referencia=
            tipos_referencia,

        imagens_disponiveis=
            imagens_disponiveis,

        resultado_visao=
            resultado_visao,
    )


    # --------------------------------------------------------
    # PRODUTO REAL DEVE USAR REFERÊNCIA
    # --------------------------------------------------------

    usar_referencia = True


    justificativa = criar_justificativa(

        funcao=
            funcao,

        modo_execucao=
            modo_execucao,

        referencias_sugeridas=
            referencias_sugeridas,

        selecao_visual_inteligente=
            selecao_visual_inteligente,
    )


    return ExecucaoImagem(

        numero_imagem=
            numero,

        funcao=
            funcao,

        modo_execucao=
            modo_execucao,

        prompt=
            prompt,

        usar_referencia=
            usar_referencia,

        tipos_referencia=
            tipos_referencia,

        referencias_sugeridas=
            referencias_sugeridas,

        preservar=
            preservar,

        restricoes=
            restricoes,

        justificativa=
            justificativa,

        confianca=
            confianca,

        limite_referencias=
            limite_referencias,

        selecao_visual_inteligente=
            selecao_visual_inteligente,
    )


# ============================================================
# 15. CRIAR PLANO DE EXECUÇÃO
# ============================================================

def criar_plano_execucao(
    prompts,
    imagens_disponiveis=None,
    resultado_visao=None,
):
    """
    Cria o plano completo de execução
    para todos os prompts da campanha.
    """

    execucoes = []


    for prompt in lista_segura(
        prompts
    ):

        execucao = criar_execucao_imagem(

            prompt_imagem=
                prompt,

            imagens_disponiveis=
                imagens_disponiveis,

            resultado_visao=
                resultado_visao,
        )


        execucoes.append(
            execucao
        )


    # --------------------------------------------------------
    # CONFIANÇA
    # --------------------------------------------------------

    if not execucoes:

        confianca = "baixa"


    elif all(
        execucao.confianca.lower()
        == "alta"

        for execucao in execucoes
    ):

        confianca = "alta"


    else:

        confianca = "media"


    return PlanoExecucaoImagens(

        execucoes=
            execucoes,

        regras_gerais=
            criar_regras_gerais(),

        confianca=
            confianca,
    )


# ============================================================
# 16. ALIAS
# ============================================================

def preparar_execucao_imagens(
    prompts,
    imagens_disponiveis=None,
    resultado_visao=None,
):
    """
    Alias para integração futura.
    """

    return criar_plano_execucao(

        prompts=
            prompts,

        imagens_disponiveis=
            imagens_disponiveis,

        resultado_visao=
            resultado_visao,
    )


# ============================================================
# 17. FORMATAR EXECUÇÃO
# ============================================================

def formatar_execucao_imagem(
    execucao,
):
    """
    Formata uma execução individual
    para leitura no terminal.
    """

    linhas = [

        f"IMAGEM {execucao.numero_imagem}",

        "",

        f"FUNÇÃO: {execucao.funcao}",

        f"MODO DE EXECUÇÃO: {execucao.modo_execucao}",

        f"USAR REFERÊNCIA: {execucao.usar_referencia}",

        (
            "SELEÇÃO VISUAL INTELIGENTE: "
            f"{execucao.selecao_visual_inteligente}"
        ),

        (
            "LIMITE DE REFERÊNCIAS: "
            f"{execucao.limite_referencias}"
        ),

        (
            "REFERÊNCIAS SELECIONADAS: "
            f"{len(execucao.referencias_sugeridas)}"
        ),

        f"CONFIANÇA: {execucao.confianca}",

        "",

        "TIPOS DE REFERÊNCIA",

    ]


    for tipo in execucao.tipos_referencia:

        linhas.append(
            f"- {tipo}"
        )


    linhas.extend(
        [
            "",
            "REFERÊNCIAS SUGERIDAS",
        ]
    )


    if execucao.referencias_sugeridas:

        for referencia in (
            execucao.referencias_sugeridas
        ):

            linhas.append(
                f"- {referencia}"
            )

    else:

        linhas.append(
            "- Nenhuma referência selecionada."
        )


    linhas.extend(
        [
            "",
            "JUSTIFICATIVA",
            execucao.justificativa,
            "",
            "REGRAS DE PRESERVAÇÃO",
        ]
    )


    for regra in execucao.preservar:

        linhas.append(
            f"- {regra}"
        )


    linhas.extend(
        [
            "",
            "RESTRIÇÕES",
        ]
    )


    for regra in execucao.restricoes:

        linhas.append(
            f"- {regra}"
        )


    return "\n".join(
        linhas
    )


# ============================================================
# 18. FORMATAR PLANO COMPLETO
# ============================================================

def formatar_plano_execucao(
    plano,
):
    """
    Formata todo o plano de execução.
    """

    linhas = [

        "PLANO DE EXECUÇÃO DE IMAGENS",

        "",

        f"CONFIANÇA GERAL: {plano.confianca}",

        "",

    ]


    for indice, execucao in enumerate(
        plano.execucoes
    ):

        linhas.append(
            formatar_execucao_imagem(
                execucao
            )
        )


        if indice < len(
            plano.execucoes
        ) - 1:

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
            "REGRAS GERAIS DE EXECUÇÃO",
            "",
        ]
    )


    for regra in plano.regras_gerais:

        linhas.append(
            f"- {regra}"
        )


    return "\n".join(
        linhas
    )