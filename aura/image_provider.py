# ============================================================
# VISUALSELLER FASHION
# AURA — PROVEDORES DE IMAGEM
# ============================================================

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


# ============================================================
# 1. CONFIGURAÇÃO DE PROVEDOR
# ============================================================

@dataclass
class ImageProviderConfig:
    """
    Configuração genérica de um provedor de imagem.
    """

    nome: str

    modelo: Optional[str] = None

    ativo: bool = True

    suporta_referencia: bool = True

    suporta_multiplas_referencias: bool = True

    max_referencias: Optional[int] = None

    observacoes: str = ""


# ============================================================
# 2. RESULTADO PADRÃO
# ============================================================

@dataclass
class ImageProviderResult:
    """
    Resultado normalizado de qualquer provedor.
    """

    sucesso: bool

    provider: str

    modelo: Optional[str] = None

    caminho_saida: Optional[str] = None

    erro: Optional[str] = None

    detalhes: Optional[Dict[str, Any]] = None


# ============================================================
# 3. REGISTRO DE PROVEDORES
# ============================================================

PROVIDERS = {

    # --------------------------------------------------------
    # OPENAI
    # --------------------------------------------------------

    "openai": ImageProviderConfig(

        nome="openai",

        modelo="gpt-image-2",

        ativo=True,

        suporta_referencia=True,

        suporta_multiplas_referencias=True,

        max_referencias=None,

        observacoes=(
            "Provider OpenAI para geração e edição "
            "de imagens. Pode aplicar bloqueios de "
            "segurança em determinados produtos."
        ),
    ),


    # --------------------------------------------------------
    # VERCEL AI GATEWAY
    # NANO BANANA 2
    # --------------------------------------------------------

    "vercel": ImageProviderConfig(

        nome="vercel",

        modelo="google/gemini-3.1-flash-image",

        ativo=True,

        suporta_referencia=True,

        suporta_multiplas_referencias=True,

        max_referencias=4,

        observacoes=(
            "Vercel AI Gateway usando Gemini 3.1 "
            "Flash Image (Nano Banana 2). "
            "Adequado para geração e edição com "
            "imagens de referência."
        ),
    ),


    # --------------------------------------------------------
    # OPENROUTER
    # NANO BANANA 2
    # --------------------------------------------------------

    "openrouter": ImageProviderConfig(

        nome="openrouter",

        modelo="google/gemini-3.1-flash-image",

        ativo=True,

        suporta_referencia=True,

        suporta_multiplas_referencias=True,

        max_referencias=4,

        observacoes=(
            "OpenRouter usando Gemini 3.1 Flash Image "
            "(Nano Banana 2). Provider ativo para geração "
            "e edição com imagens de referência."
        ),
    ),


    # --------------------------------------------------------
    # FAL
    # --------------------------------------------------------

    "fal": ImageProviderConfig(

        nome="fal",

        modelo=None,

        ativo=False,

        suporta_referencia=True,

        suporta_multiplas_referencias=True,

        max_referencias=None,

        observacoes=(
            "Reservado para integração futura."
        ),
    ),


    # --------------------------------------------------------
    # REPLICATE
    # --------------------------------------------------------

    "replicate": ImageProviderConfig(

        nome="replicate",

        modelo=None,

        ativo=False,

        suporta_referencia=True,

        suporta_multiplas_referencias=True,

        max_referencias=None,

        observacoes=(
            "Reservado para integração futura."
        ),
    ),


    # --------------------------------------------------------
    # RUNWAY
    # --------------------------------------------------------

    "runway": ImageProviderConfig(

        nome="runway",

        modelo=None,

        ativo=False,

        suporta_referencia=True,

        suporta_multiplas_referencias=True,

        max_referencias=None,

        observacoes=(
            "Reservado para integração futura."
        ),
    ),
}


# ============================================================
# 4. OBTER CONFIGURAÇÃO
# ============================================================

def obter_provider(
    nome: str,
) -> ImageProviderConfig:

    nome = (
        nome
        or ""
    ).strip().lower()

    if not nome:

        raise ValueError(
            "Nome do provedor não informado."
        )

    if nome not in PROVIDERS:

        raise ValueError(
            f"Provedor não reconhecido: {nome}"
        )

    return PROVIDERS[
        nome
    ]


# ============================================================
# 5. LISTAR PROVEDORES
# ============================================================

def listar_providers(
    somente_ativos: bool = False,
) -> List[ImageProviderConfig]:

    providers = list(
        PROVIDERS.values()
    )

    if somente_ativos:

        providers = [

            provider

            for provider in providers

            if provider.ativo
        ]

    return providers


# ============================================================
# 6. VALIDAR CAPACIDADE
# ============================================================

def validar_capacidade_provider(
    provider: ImageProviderConfig,
    referencias: Optional[List[str]] = None,
) -> None:

    referencias = referencias or []

    quantidade_referencias = len(
        referencias
    )


    # --------------------------------------------------------
    # REFERÊNCIA NÃO SUPORTADA
    # --------------------------------------------------------

    if (
        quantidade_referencias > 0
        and not provider.suporta_referencia
    ):

        raise ValueError(
            f"O provedor '{provider.nome}' "
            "não suporta imagens de referência."
        )


    # --------------------------------------------------------
    # MÚLTIPLAS REFERÊNCIAS NÃO SUPORTADAS
    # --------------------------------------------------------

    if (
        quantidade_referencias > 1
        and not provider.suporta_multiplas_referencias
    ):

        raise ValueError(
            f"O provedor '{provider.nome}' "
            "não suporta múltiplas referências."
        )


    # --------------------------------------------------------
    # LIMITE DE REFERÊNCIAS
    # --------------------------------------------------------

    if (
        provider.max_referencias is not None
        and quantidade_referencias
        > provider.max_referencias
    ):

        raise ValueError(
            f"O provedor '{provider.nome}' "
            "aceita no máximo "
            f"{provider.max_referencias} "
            "imagens de referência."
        )


# ============================================================
# 7. ESCOLHER PROVEDOR
# ============================================================

def escolher_provider(
    provider_preferido: str = "openai",
    referencias: Optional[List[str]] = None,
) -> ImageProviderConfig:
    """
    Escolhe e valida o provedor solicitado.

    Não existe fallback automático.

    Isso é proposital:
    a Aura não deve trocar de provedor silenciosamente.
    """

    provider = obter_provider(
        provider_preferido
    )

    if not provider.ativo:

        raise RuntimeError(
            f"O provedor '{provider.nome}' "
            "está cadastrado, mas ainda não está ativo."
        )

    validar_capacidade_provider(

        provider=
            provider,

        referencias=
            referencias,
    )

    return provider


# ============================================================
# 8. CLASSIFICAR ERRO DE PROVEDOR
# ============================================================

def classificar_erro_provider(
    erro: Exception,
) -> Dict[str, Any]:
    """
    Converte erros de diferentes provedores
    para uma estrutura comum da Aura.
    """

    mensagem = str(
        erro
    )

    mensagem_lower = (
        mensagem.lower()
    )

    tipo = "erro_desconhecido"

    bloqueio_seguranca = False


    # --------------------------------------------------------
    # SEGURANÇA / MODERAÇÃO
    # --------------------------------------------------------

    if (
        "moderation_blocked"
        in mensagem_lower
        or "safety system"
        in mensagem_lower
        or "safety_violations"
        in mensagem_lower
        or "blocked for safety"
        in mensagem_lower
        or "safety filter"
        in mensagem_lower
    ):

        tipo = "bloqueio_seguranca"

        bloqueio_seguranca = True


    # --------------------------------------------------------
    # LIMITE / CRÉDITOS
    # --------------------------------------------------------

    elif (
        "rate limit"
        in mensagem_lower
        or "rate_limit"
        in mensagem_lower
        or "insufficient credits"
        in mensagem_lower
        or "insufficient balance"
        in mensagem_lower
        or "budget exceeded"
        in mensagem_lower
        or "spending limit"
        in mensagem_lower
    ):

        tipo = "limite_api"


    # --------------------------------------------------------
    # AUTENTICAÇÃO
    # --------------------------------------------------------

    elif (
        "authentication"
        in mensagem_lower
        or "api key"
        in mensagem_lower
        or "unauthorized"
        in mensagem_lower
        or "invalid token"
        in mensagem_lower
        or "401"
        in mensagem_lower
    ):

        tipo = "autenticacao"


    # --------------------------------------------------------
    # TIMEOUT
    # --------------------------------------------------------

    elif (
        "timeout"
        in mensagem_lower
        or "timed out"
        in mensagem_lower
    ):

        tipo = "timeout"


    # --------------------------------------------------------
    # RECURSO / MODELO NÃO ENCONTRADO
    # --------------------------------------------------------

    elif (
        "not found"
        in mensagem_lower
        or "404"
        in mensagem_lower
        or "model not found"
        in mensagem_lower
    ):

        tipo = "recurso_nao_encontrado"


    return {

        "tipo":
            tipo,

        "mensagem":
            mensagem,

        "bloqueio_seguranca":
            bloqueio_seguranca,
    }


# ============================================================
# 9. CRIAR RESULTADO DE ERRO
# ============================================================

def criar_resultado_erro(
    provider: str,
    modelo: Optional[str],
    erro: Exception,
) -> ImageProviderResult:

    detalhes = (
        classificar_erro_provider(
            erro
        )
    )

    return ImageProviderResult(

        sucesso=False,

        provider=
            provider,

        modelo=
            modelo,

        caminho_saida=None,

        erro=
            detalhes[
                "mensagem"
            ],

        detalhes=
            detalhes,
    )


# ============================================================
# 10. CRIAR RESULTADO DE SUCESSO
# ============================================================

def criar_resultado_sucesso(
    provider: str,
    modelo: Optional[str],
    caminho_saida: str,
    detalhes: Optional[Dict[str, Any]] = None,
) -> ImageProviderResult:

    return ImageProviderResult(

        sucesso=True,

        provider=
            provider,

        modelo=
            modelo,

        caminho_saida=
            caminho_saida,

        erro=None,

        detalhes=
            detalhes
            or {},
    )


# ============================================================
# 11. RESUMO DO PROVEDOR
# ============================================================

def formatar_provider(
    provider: ImageProviderConfig,
) -> str:

    linhas = [

        f"PROVEDOR: {provider.nome}",

        f"MODELO: {provider.modelo}",

        f"ATIVO: {provider.ativo}",

        (
            "SUPORTA REFERÊNCIA: "
            f"{provider.suporta_referencia}"
        ),

        (
            "SUPORTA MÚLTIPLAS REFERÊNCIAS: "
            f"{provider.suporta_multiplas_referencias}"
        ),

        (
            "MÁXIMO DE REFERÊNCIAS: "
            f"{provider.max_referencias}"
        ),

        "",

        "OBSERVAÇÕES:",

        provider.observacoes,
    ]

    return "\n".join(
        linhas
    )