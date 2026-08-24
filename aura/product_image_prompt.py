from dataclasses import dataclass, field
from typing import Any


# ============================================================
# VISUALSELLER FASHION
# AURA — TRADUTOR DE BRIEFING PARA PROMPT VISUAL
# ============================================================


@dataclass
class ProductImagePrompt:
    """
    Representa uma instrução de produção visual derivada
    de um briefing de imagem já aprovado pela Aura.
    """

    numero_imagem: int
    funcao: str

    prompt_principal: str

    objetivo: str = ""
    enquadramento: str = ""
    foco_principal: str = ""

    composicao: list[str] = field(default_factory=list)
    iluminacao: list[str] = field(default_factory=list)
    fundo: list[str] = field(default_factory=list)

    destacar: list[str] = field(default_factory=list)
    preservar: list[str] = field(default_factory=list)
    evitar: list[str] = field(default_factory=list)

    evidencias: list[str] = field(default_factory=list)

    confianca: str = "media"


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================


def _obter(
    objeto: Any,
    *nomes: str,
    padrao=None,
):
    """
    Busca um valor tanto em dicionários quanto em objetos.

    Isso deixa esta camada menos dependente da implementação
    interna do briefing.
    """

    if padrao is None:
        padrao = ""

    for nome in nomes:

        if isinstance(objeto, dict):

            if nome in objeto:
                valor = objeto.get(nome)

                if valor is not None:
                    return valor

        else:

            if hasattr(objeto, nome):
                valor = getattr(objeto, nome)

                if valor is not None:
                    return valor

    return padrao


def _lista(
    valor: Any,
) -> list[str]:
    """
    Normaliza qualquer entrada para uma lista de textos.
    """

    if valor is None:
        return []

    if isinstance(valor, str):

        texto = valor.strip()

        if not texto:
            return []

        return [texto]

    if isinstance(valor, (list, tuple, set)):

        resultado = []

        for item in valor:

            if item is None:
                continue

            texto = str(item).strip()

            if texto:
                resultado.append(texto)

        return resultado

    texto = str(valor).strip()

    if texto:
        return [texto]

    return []


def _unicos(
    itens: list[str],
) -> list[str]:
    """
    Remove repetições mantendo a ordem original.
    """

    resultado = []
    vistos = set()

    for item in itens:

        texto = str(item).strip()

        if not texto:
            continue

        chave = texto.casefold()

        if chave in vistos:
            continue

        vistos.add(chave)
        resultado.append(texto)

    return resultado


def _formatar_lista_para_prompt(
    titulo: str,
    itens: list[str],
) -> str:
    """
    Converte uma lista em um bloco legível de instruções.
    """

    itens = _unicos(
        _lista(itens)
    )

    if not itens:
        return ""

    linhas = [titulo]

    for item in itens:
        linhas.append(
            f"- {item}"
        )

    return "\n".join(
        linhas
    )


# ============================================================
# EXTRAÇÃO DO BRIEFING
# ============================================================


def _extrair_dados_briefing(
    briefing: Any,
    numero_imagem: int,
) -> dict:
    """
    Extrai apenas decisões já existentes no briefing.

    Esta função NÃO cria novas decisões visuais.
    """

    funcao = _obter(
        briefing,
        "funcao",
        "função",
        padrao="imagem de produto",
    )

    objetivo = _obter(
        briefing,
        "objetivo",
        padrao="",
    )

    mensagem = _obter(
        briefing,
        "mensagem",
        padrao="",
    )

    enquadramento = _obter(
        briefing,
        "enquadramento",
        padrao="",
    )

    foco_principal = _obter(
        briefing,
        "foco_principal",
        "foco",
        padrao="",
    )

    composicao = _lista(
        _obter(
            briefing,
            "composicao",
            "composição",
            padrao=[],
        )
    )

    iluminacao = _lista(
        _obter(
            briefing,
            "iluminacao",
            "iluminação",
            padrao=[],
        )
    )

    fundo = _lista(
        _obter(
            briefing,
            "fundo",
            padrao=[],
        )
    )

    destacar = _lista(
        _obter(
            briefing,
            "destacar",
            "o_que_destacar",
            padrao=[],
        )
    )

    preservar = _lista(
        _obter(
            briefing,
            "preservar",
            "preservar_no_produto",
            "regras_preservacao",
            "regras_de_preservacao",
            padrao=[],
        )
    )

    evidencias = _lista(
        _obter(
            briefing,
            "evidencias",
            "evidências",
            padrao=[],
        )
    )

    confianca = _obter(
        briefing,
        "confianca",
        "confiança",
        padrao="media",
    )

    return {
        "numero_imagem": numero_imagem,
        "funcao": str(funcao).strip(),
        "objetivo": str(objetivo).strip(),
        "mensagem": str(mensagem).strip(),
        "enquadramento": str(enquadramento).strip(),
        "foco_principal": str(foco_principal).strip(),
        "composicao": _unicos(composicao),
        "iluminacao": _unicos(iluminacao),
        "fundo": _unicos(fundo),
        "destacar": _unicos(destacar),
        "preservar": _unicos(preservar),
        "evidencias": _unicos(evidencias),
        "confianca": str(confianca).strip() or "media",
    }


# ============================================================
# REGRAS DE SEGURANÇA VISUAL
# ============================================================


REGRAS_FIXAS_DE_PRESERVACAO = [
    (
        "preservar rigorosamente as características reais "
        "do produto"
    ),
    (
        "não alterar modelagem, materiais, renda, "
        "transparência, texturas ou acabamentos"
    ),
    (
        "não adicionar elementos que possam ser confundidos "
        "com partes reais do produto"
    ),
    (
        "preservar a cor real do produto"
    ),
]


REGRAS_FIXAS_A_EVITAR = [
    "não redesenhar o produto",
    "não inventar detalhes inexistentes",
    "não alterar a estrutura da peça",
    "não modificar a localização da transparência",
    "não modificar o formato dos decotes",
    "não modificar mangas, punhos ou fechamento",
    (
        "não sacrificar a fidelidade do produto "
        "em favor da estética"
    ),
]


# ============================================================
# CONSTRUÇÃO DO PROMPT
# ============================================================


def construir_prompt_principal(
    dados: dict,
) -> str:
    """
    Traduz o briefing estruturado para uma instrução visual.

    A função organiza as decisões da Aura.
    Ela não cria uma nova direção de arte.
    """

    blocos = []

    # --------------------------------------------------------
    # ABERTURA
    # --------------------------------------------------------

    blocos.append(
        (
            "Criar uma imagem comercial de moda para "
            "marketplace, mantendo o produto como "
            "protagonista absoluto da composição."
        )
    )

    blocos.append(
        (
            f"Esta é a imagem {dados['numero_imagem']} "
            f"da sequência visual."
        )
    )

    if dados["funcao"]:
        blocos.append(
            f"Função da imagem: {dados['funcao']}."
        )

    if dados["objetivo"]:
        blocos.append(
            f"Objetivo: {dados['objetivo']}"
        )

    if dados["mensagem"]:
        blocos.append(
            (
                "Mensagem visual que deve orientar a imagem: "
                f"{dados['mensagem']}"
            )
        )

    # --------------------------------------------------------
    # DIREÇÃO DE CÂMERA
    # --------------------------------------------------------

    if dados["enquadramento"]:
        blocos.append(
            (
                "Enquadramento: "
                f"{dados['enquadramento']}"
            )
        )

    if dados["foco_principal"]:
        blocos.append(
            (
                "Foco principal: "
                f"{dados['foco_principal']}"
            )
        )

    # --------------------------------------------------------
    # COMPOSIÇÃO
    # --------------------------------------------------------

    bloco = _formatar_lista_para_prompt(
        "COMPOSIÇÃO:",
        dados["composicao"],
    )

    if bloco:
        blocos.append(bloco)

    # --------------------------------------------------------
    # ILUMINAÇÃO
    # --------------------------------------------------------

    bloco = _formatar_lista_para_prompt(
        "ILUMINAÇÃO:",
        dados["iluminacao"],
    )

    if bloco:
        blocos.append(bloco)

    # --------------------------------------------------------
    # FUNDO
    # --------------------------------------------------------

    bloco = _formatar_lista_para_prompt(
        "FUNDO:",
        dados["fundo"],
    )

    if bloco:
        blocos.append(bloco)

    # --------------------------------------------------------
    # ELEMENTOS A DESTACAR
    # --------------------------------------------------------

    bloco = _formatar_lista_para_prompt(
        "ELEMENTOS DO PRODUTO A DESTACAR:",
        dados["destacar"],
    )

    if bloco:
        blocos.append(bloco)

    # --------------------------------------------------------
    # PRESERVAÇÃO
    # --------------------------------------------------------

    preservar = _unicos(
        dados["preservar"]
        + REGRAS_FIXAS_DE_PRESERVACAO
    )

    bloco = _formatar_lista_para_prompt(
        "FIDELIDADE OBRIGATÓRIA AO PRODUTO:",
        preservar,
    )

    if bloco:
        blocos.append(bloco)

    # --------------------------------------------------------
    # RESTRIÇÕES
    # --------------------------------------------------------

    bloco = _formatar_lista_para_prompt(
        "NÃO FAZER:",
        REGRAS_FIXAS_A_EVITAR,
    )

    if bloco:
        blocos.append(bloco)

    # --------------------------------------------------------
    # EVIDÊNCIAS
    # --------------------------------------------------------

    bloco = _formatar_lista_para_prompt(
        "EVIDÊNCIAS QUE SUSTENTAM A DIREÇÃO:",
        dados["evidencias"],
    )

    if bloco:
        blocos.append(bloco)

    # --------------------------------------------------------
    # REGRA FINAL
    # --------------------------------------------------------

    blocos.append(
        (
            "A direção de arte pode organizar enquadramento, "
            "luz, fundo e composição, mas não pode modificar "
            "as características reais do produto."
        )
    )

    return "\n\n".join(
        blocos
    )


# ============================================================
# CRIAÇÃO DO PROMPT DE UMA IMAGEM
# ============================================================


def criar_prompt_imagem(
    briefing: Any,
    numero_imagem: int = 1,
) -> ProductImagePrompt:
    """
    Recebe um briefing visual e produz a instrução
    correspondente para geração de imagem.
    """

    dados = _extrair_dados_briefing(
        briefing=briefing,
        numero_imagem=numero_imagem,
    )

    prompt_principal = construir_prompt_principal(
        dados
    )

    preservar = _unicos(
        dados["preservar"]
        + REGRAS_FIXAS_DE_PRESERVACAO
    )

    evitar = _unicos(
        REGRAS_FIXAS_A_EVITAR
    )

    return ProductImagePrompt(
        numero_imagem=dados["numero_imagem"],
        funcao=dados["funcao"],
        prompt_principal=prompt_principal,
        objetivo=dados["objetivo"],
        enquadramento=dados["enquadramento"],
        foco_principal=dados["foco_principal"],
        composicao=dados["composicao"],
        iluminacao=dados["iluminacao"],
        fundo=dados["fundo"],
        destacar=dados["destacar"],
        preservar=preservar,
        evitar=evitar,
        evidencias=dados["evidencias"],
        confianca=dados["confianca"],
    )


# ============================================================
# CRIAÇÃO DOS PROMPTS DA CAMPANHA
# ============================================================


def criar_prompts_imagens(
    briefings: Any,
) -> list[ProductImagePrompt]:
    """
    Converte todos os briefings da campanha em prompts.
    """

    if briefings is None:
        return []

    # Permite receber diretamente uma lista.
    if isinstance(briefings, (list, tuple)):

        lista_briefings = list(
            briefings
        )

    else:

        lista_briefings = _obter(
            briefings,
            "briefings",
            "imagens",
            "sequencia",
            "sequencia_imagens",
            padrao=[],
        )

        lista_briefings = list(
            lista_briefings or []
        )

    prompts = []

    for indice, briefing in enumerate(
        lista_briefings,
        start=1,
    ):

        prompt = criar_prompt_imagem(
            briefing=briefing,
            numero_imagem=indice,
        )

        prompts.append(
            prompt
        )

    return prompts


# ============================================================
# FORMATAÇÃO PARA TESTES / TERMINAL
# ============================================================


def formatar_prompt_imagem(
    prompt: ProductImagePrompt,
) -> str:

    linhas = [
        f"IMAGEM {prompt.numero_imagem}",
        "",
        f"FUNÇÃO: {prompt.funcao}",
        f"CONFIANÇA: {prompt.confianca}",
        "",
        "PROMPT DE PRODUÇÃO",
        "",
        prompt.prompt_principal,
    ]

    return "\n".join(
        linhas
    )


def formatar_prompts_imagens(
    prompts: list[ProductImagePrompt],
) -> str:

    if not prompts:
        return (
            "Nenhum prompt de imagem foi criado."
        )

    blocos = []

    for prompt in prompts:

        blocos.append(
            formatar_prompt_imagem(
                prompt
            )
        )

    separador = (
        "\n\n"
        + "-" * 60
        + "\n\n"
    )

    return separador.join(
        blocos
    )


# ============================================================
# ALIASES
# ============================================================
# Mantemos alguns nomes alternativos para facilitar
# integração futura com outras camadas da Aura.


gerar_prompt_imagem = criar_prompt_imagem
gerar_prompts_imagens = criar_prompts_imagens
formatar_prompts = formatar_prompts_imagens