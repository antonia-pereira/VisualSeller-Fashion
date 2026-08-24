import base64
import mimetypes
import os
import re
from pathlib import Path
from typing import Any, Dict, List

from dotenv import load_dotenv
from openai import OpenAI

from aura.image_provider import (
    ImageProviderConfig,
    ImageProviderResult,
    escolher_provider,
    criar_resultado_erro,
    criar_resultado_sucesso,
)


# ============================================================
# VISUALSELLER FASHION
# AURA — GERADOR DE IMAGEM DO PRODUTO
# ============================================================
#
# RESPONSABILIDADE DESTE MÓDULO
#
# Este arquivo é responsável pela execução da geração visual.
#
# A Aura:
#
# 1. entende o produto
# 2. cria estratégia
# 3. cria plano visual
# 4. cria briefing
# 5. cria prompt
# 6. escolhe referências
# 7. prepara a execução
#
# Este módulo recebe essa execução e conversa com o
# provedor de geração de imagem.
#
# IMPORTANTE:
#
# A inteligência estratégica da Aura NÃO depende do
# provedor de imagem.
#
# ============================================================


# ============================================================
# 1. CARREGAR VARIÁVEIS DE AMBIENTE
# ============================================================

load_dotenv()


OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)


AI_GATEWAY_API_KEY = os.getenv(
    "AI_GATEWAY_API_KEY"
)

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)


# ============================================================
# 2. CLIENTE OPENAI
# ============================================================
#
# O cliente não será criado se a chave não existir.
#
# Isso permite que, futuramente, a Aura seja inicializada
# mesmo quando outro provedor estiver sendo utilizado.
#
# ============================================================

client = None


if OPENAI_API_KEY:

    client = OpenAI(
        api_key=OPENAI_API_KEY
    )


vercel_client = None

if AI_GATEWAY_API_KEY:

    vercel_client = OpenAI(
        api_key=AI_GATEWAY_API_KEY,
        base_url="https://ai-gateway.vercel.sh/v1",
    )


openrouter_client = None

if OPENROUTER_API_KEY:

    openrouter_client = OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
    )


# ============================================================
# 3. CONFIGURAÇÕES
# ============================================================

PROVIDER_PADRAO = "openai"

MODELO_IMAGEM = "gpt-image-2"

PASTA_SAIDA_PADRAO = Path(
    "outputs/imagens"
)


# ============================================================
# 4. GARANTIR PASTA DE SAÍDA
# ============================================================

def garantir_pasta_saida(
    pasta_saida: str | Path,
) -> Path:

    pasta = Path(
        pasta_saida
    )

    pasta.mkdir(
        parents=True,
        exist_ok=True,
    )

    return pasta


# ============================================================
# 5. VALIDAR REFERÊNCIAS
# ============================================================

def validar_referencias(
    referencias: List[str],
) -> List[str]:

    referencias_validas = []

    for referencia in referencias:

        caminho = Path(
            referencia
        )

        if not caminho.exists():

            raise FileNotFoundError(
                "Imagem de referência "
                f"não encontrada: {referencia}"
            )

        referencias_validas.append(
            str(caminho)
        )

    if not referencias_validas:

        raise ValueError(
            "Nenhuma imagem de referência "
            "foi fornecida para geração."
        )

    return referencias_validas


# ============================================================
# 6. NORMALIZAR PROMPT
# ============================================================

def normalizar_prompt(
    prompt: str,
) -> str:

    prompt = (
        prompt
        or ""
    ).strip()

    if not prompt:

        raise ValueError(
            "O prompt de geração está vazio."
        )

    return prompt


# ============================================================
# 7. PREPARAR PROMPT PARA PRODUÇÃO VISUAL
# ============================================================

def preparar_prompt_producao(
    prompt_aura: str,
) -> str:
    """
    Converte o prompt estratégico da Aura em uma instrução
    objetiva para produção visual.

    A estratégia da Aura continua intacta.

    Esta função apenas remove do prompt enviado ao gerador
    termos interpretativos que não são necessários para a
    execução fotográfica.
    """

    prompt = normalizar_prompt(
        prompt_aura
    )

    substituicoes = {

        r"\bsensualidade\b":
            "presença visual",

        r"\bsensual\b":
            "visualmente expressivo",

        r"\bsensuais\b":
            "visualmente expressivos",

        r"\bsedução\b":
            "expressividade",

        r"\bsedutor\b":
            "marcante",

        r"\bsedutora\b":
            "marcante",

        r"\bdesejo\b":
            "interesse visual",

        r"\bdesejos\b":
            "interesses visuais",
    }

    for padrao, substituicao in (
        substituicoes.items()
    ):

        prompt = re.sub(
            padrao,
            substituicao,
            prompt,
            flags=re.IGNORECASE,
        )

    # --------------------------------------------------------
    # NORMALIZAR ESPAÇOS
    # --------------------------------------------------------

    prompt = re.sub(
        r"[ \t]+",
        " ",
        prompt,
    )

    prompt = re.sub(
        r"\n{3,}",
        "\n\n",
        prompt,
    )

    return prompt.strip()


# ============================================================
# 8. INSTRUÇÃO MESTRA DE PRODUÇÃO
# ============================================================

def construir_prompt_final(
    prompt_aura: str,
) -> str:

    prompt_producao = (
        preparar_prompt_producao(
            prompt_aura
        )
    )

    instrucao_producao = """
TAREFA

Criar uma fotografia comercial de produto de moda
para apresentação em marketplace.

As fotografias fornecidas são referências reais
do mesmo produto.

OBJETIVO

Produzir uma imagem limpa, profissional e comercial,
mantendo fidelidade visual ao produto fotografado.

PRESERVAÇÃO OBRIGATÓRIA

Preserve as características observáveis nas
fotografias de referência, incluindo, quando visíveis:

- formato geral da peça
- modelagem
- recortes
- costuras
- mangas
- punhos
- decotes
- fechamento
- renda
- áreas translúcidas
- áreas opacas
- texturas
- acabamentos
- proporções
- cor

Não invente elementos que não aparecem nas
referências.

Não adicionar:

- novos recortes
- novas costuras
- novos materiais
- novos acabamentos
- novos acessórios
- novas estampas
- novos fechamentos
- novos detalhes estruturais

Não remover características importantes do produto.

Quando as fotografias mostrarem ângulos diferentes,
use todas como referência para compreender a
construção real da peça.

ESTILO DE IMAGEM

- fotografia comercial de moda
- apresentação profissional de produto
- composição limpa
- iluminação fotográfica equilibrada
- boa definição dos materiais
- textura visível
- produto como protagonista
- aparência natural
- proporções realistas

FUNDO

Utilizar fundo simples e adequado à apresentação
comercial do produto.

Evitar elementos que disputem atenção com a peça.

TEXTO

Não inserir:

- textos
- letras
- preços
- selos
- logotipos
- marcas gráficas
- elementos tipográficos

A prioridade absoluta é preservar o produto real.

DIREÇÃO VISUAL ESPECÍFICA DA AURA:

"""

    return (
        instrucao_producao
        + "\n"
        + prompt_producao
    ).strip()


# ============================================================
# 9. GERAR NOME DO ARQUIVO
# ============================================================

def criar_nome_arquivo(
    numero_imagem: int,
    funcao: str,
) -> str:

    funcao_limpa = (
        funcao
        .strip()
        .lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
    )

    if not funcao_limpa:

        funcao_limpa = "imagem"

    return (
        f"imagem_{numero_imagem:02d}_"
        f"{funcao_limpa}.png"
    )


# ============================================================
# 10. EXTRAIR BASE64 DA RESPOSTA
# ============================================================

def extrair_imagem_base64(
    resposta: Any,
) -> str:

    if not resposta.data:

        raise RuntimeError(
            "A API não retornou nenhuma imagem."
        )

    primeira_imagem = resposta.data[0]

    imagem_base64 = getattr(
        primeira_imagem,
        "b64_json",
        None,
    )

    if not imagem_base64:

        raise RuntimeError(
            "A API retornou uma resposta, "
            "mas não foi possível encontrar "
            "os dados da imagem."
        )

    return imagem_base64


# ============================================================
# 11. SALVAR IMAGEM
# ============================================================

def salvar_imagem_base64(
    imagem_base64: str,
    caminho_saida: Path,
) -> None:

    conteudo = base64.b64decode(
        imagem_base64
    )

    with open(
        caminho_saida,
        "wb",
    ) as arquivo:

        arquivo.write(
            conteudo
        )


# ============================================================
# 12. VALIDAR CLIENTE OPENAI
# ============================================================

def validar_cliente_openai() -> None:

    if client is None:

        raise RuntimeError(
            "O provedor OpenAI foi selecionado, "
            "mas a chave OPENAI_API_KEY "
            "não foi encontrada."
        )


# ============================================================
# 13. EXECUTAR OPENAI
# ============================================================

def executar_openai(
    prompt_final: str,
    referencias: List[str],
    caminho_saida: Path,
    provider: ImageProviderConfig,
    tamanho: str = "1024x1024",
    qualidade: str = "medium",
) -> ImageProviderResult:
    """
    Executa exclusivamente o provedor OpenAI.

    Toda lógica específica da API OpenAI permanece aqui.

    Se futuramente adicionarmos outro provedor,
    ele terá sua própria função.
    """

    validar_cliente_openai()

    arquivos_abertos = []

    try:

        for referencia in referencias:

            arquivo = open(
                referencia,
                "rb",
            )

            arquivos_abertos.append(
                arquivo
            )

        resposta = client.images.edit(

            model=(
                provider.modelo
                or MODELO_IMAGEM
            ),

            image=
                arquivos_abertos,

            prompt=
                prompt_final,

            size=
                tamanho,

            quality=
                qualidade,
        )

        imagem_base64 = (
            extrair_imagem_base64(
                resposta
            )
        )

        salvar_imagem_base64(
            imagem_base64,
            caminho_saida,
        )

        return criar_resultado_sucesso(

            provider=
                provider.nome,

            modelo=(
                provider.modelo
                or MODELO_IMAGEM
            ),

            caminho_saida=
                str(
                    caminho_saida
                ),

            detalhes={

                "quantidade_referencias":
                    len(
                        referencias
                    ),

                "referencias":
                    referencias,

                "tamanho":
                    tamanho,

                "qualidade":
                    qualidade,

                "prompt_producao":
                    prompt_final,
            },
        )

    except Exception as erro:

        return criar_resultado_erro(

            provider=
                provider.nome,

            modelo=(
                provider.modelo
                or MODELO_IMAGEM
            ),

            erro=
                erro,
        )

    finally:

        for arquivo in arquivos_abertos:

            arquivo.close()


# ============================================================
# 13B. VALIDAR CLIENTE VERCEL
# ============================================================

def validar_cliente_vercel() -> None:

    if vercel_client is None:

        raise RuntimeError(
            "O provedor Vercel foi selecionado, "
            "mas a chave AI_GATEWAY_API_KEY "
            "não foi encontrada."
        )


# ============================================================
# 13C. CONVERTER REFERÊNCIA PARA DATA URL
# ============================================================

def referencia_para_data_url(
    caminho_imagem: str,
) -> str:

    mime_type, _ = mimetypes.guess_type(
        caminho_imagem
    )

    if mime_type is None:
        mime_type = "image/jpeg"

    with open(
        caminho_imagem,
        "rb",
    ) as arquivo:
        conteudo = arquivo.read()

    imagem_base64 = base64.b64encode(
        conteudo
    ).decode("utf-8")

    return (
        f"data:{mime_type};"
        f"base64,{imagem_base64}"
    )


# ============================================================
# 13D. EXTRAIR IMAGEM DA RESPOSTA VERCEL
# ============================================================

def extrair_imagem_vercel(
    resposta: Any,
) -> tuple[bytes, str]:

    for item in getattr(resposta, "output", []) or []:
        for bloco in getattr(item, "content", []) or []:
            tipo = getattr(bloco, "type", "")

            if tipo in ("output_image", "image"):
                dados = (
                    getattr(bloco, "image_base64", None)
                    or getattr(bloco, "data", None)
                    or getattr(bloco, "b64_json", None)
                )

                if dados:
                    mime_type = (
                        getattr(bloco, "mime_type", None)
                        or "image/png"
                    )
                    return base64.b64decode(dados), mime_type

    raise RuntimeError(
        "O Vercel AI Gateway respondeu, "
        "mas nenhuma imagem foi encontrada na resposta."
    )


# ============================================================
# 13E. EXECUTAR VERCEL / NANO BANANA 2
# ============================================================

def executar_vercel(
    prompt_final: str,
    referencias: List[str],
    caminho_saida: Path,
    provider: ImageProviderConfig,
    tamanho: str = "1024x1024",
    qualidade: str = "medium",
) -> ImageProviderResult:

    validar_cliente_vercel()

    try:
        conteudo = [
            {
                "type": "input_text",
                "text": prompt_final,
            }
        ]

        for referencia in referencias:
            conteudo.append(
                {
                    "type": "input_image",
                    "image_url": referencia_para_data_url(
                        referencia
                    ),
                }
            )

        resposta = vercel_client.responses.create(
            model=provider.modelo,
            input=[
                {
                    "role": "user",
                    "content": conteudo,
                }
            ],
            extra_body={
                "modalities": ["text", "image"],
            },
        )

        imagem_bytes, mime_type = extrair_imagem_vercel(
            resposta
        )

        with open(caminho_saida, "wb") as arquivo:
            arquivo.write(imagem_bytes)

        return criar_resultado_sucesso(
            provider=provider.nome,
            modelo=provider.modelo,
            caminho_saida=str(caminho_saida),
            detalhes={
                "quantidade_referencias": len(referencias),
                "referencias": referencias,
                "tamanho_solicitado": tamanho,
                "qualidade_solicitada": qualidade,
                "mime_type": mime_type,
                "prompt_producao": prompt_final,
            },
        )

    except Exception as erro:
        return criar_resultado_erro(
            provider=provider.nome,
            modelo=provider.modelo,
            erro=erro,
        )


# ============================================================
# 13F. VALIDAR CLIENTE OPENROUTER
# ============================================================

def validar_cliente_openrouter() -> None:

    if openrouter_client is None:

        raise RuntimeError(
            "O provedor OpenRouter foi selecionado, "
            "mas a chave OPENROUTER_API_KEY não foi encontrada."
        )


# ============================================================
# 13G. EXTRAIR IMAGEM DA RESPOSTA OPENROUTER
# ============================================================

def extrair_imagem_openrouter(
    resposta: Any,
) -> tuple[bytes, str]:

    escolhas = getattr(resposta, "choices", None) or []

    if not escolhas:
        raise RuntimeError(
            "O OpenRouter respondeu, mas não retornou choices."
        )

    mensagem = getattr(escolhas[0], "message", None)

    if mensagem is None:
        raise RuntimeError(
            "O OpenRouter respondeu, mas não retornou message."
        )

    imagens = getattr(mensagem, "images", None) or []

    if not imagens and isinstance(mensagem, dict):
        imagens = mensagem.get("images") or []

    for imagem in imagens:

        image_url = getattr(imagem, "image_url", None)

        if image_url is None and isinstance(imagem, dict):
            image_url = imagem.get("image_url")

        if isinstance(image_url, dict):
            url = image_url.get("url")
        else:
            url = getattr(image_url, "url", None)

        if not url and isinstance(imagem, dict):
            url = imagem.get("url")

        if (
            isinstance(url, str)
            and url.startswith("data:")
            and ";base64," in url
        ):
            cabecalho, dados = url.split(";base64,", 1)
            mime_type = cabecalho.replace("data:", "", 1)
            return base64.b64decode(dados), mime_type

    raise RuntimeError(
        "O OpenRouter respondeu, "
        "mas nenhuma imagem Base64 foi encontrada na resposta."
    )


# ============================================================
# 13H. EXECUTAR OPENROUTER / NANO BANANA 2
# ============================================================

def executar_openrouter(
    prompt_final: str,
    referencias: List[str],
    caminho_saida: Path,
    provider: ImageProviderConfig,
    tamanho: str = "1024x1024",
    qualidade: str = "medium",
) -> ImageProviderResult:

    validar_cliente_openrouter()

    try:

        conteudo = [
            {
                "type": "text",
                "text": prompt_final,
            }
        ]

        for referencia in referencias:

            conteudo.append(
                {
                    "type": "image_url",
                    "image_url": {
                        "url": referencia_para_data_url(
                            referencia
                        )
                    },
                }
            )

        resposta = openrouter_client.chat.completions.create(
            model=(
                provider.modelo
                or "google/gemini-3.1-flash-image"
            ),
            messages=[
                {
                    "role": "user",
                    "content": conteudo,
                }
            ],
            extra_body={
                "modalities": ["image", "text"],
            },
        )

        imagem_bytes, mime_type = extrair_imagem_openrouter(
            resposta
        )

        with open(caminho_saida, "wb") as arquivo:
            arquivo.write(imagem_bytes)

        uso = getattr(resposta, "usage", None)

        return criar_resultado_sucesso(
            provider=provider.nome,
            modelo=(
                provider.modelo
                or "google/gemini-3.1-flash-image"
            ),
            caminho_saida=str(caminho_saida),
            detalhes={
                "quantidade_referencias": len(referencias),
                "referencias": referencias,
                "tamanho_solicitado": tamanho,
                "qualidade_solicitada": qualidade,
                "mime_type": mime_type,
                "prompt_producao": prompt_final,
                "usage": (
                    uso.model_dump()
                    if hasattr(uso, "model_dump")
                    else str(uso) if uso else None
                ),
            },
        )

    except Exception as erro:

        return criar_resultado_erro(
            provider=provider.nome,
            modelo=(
                provider.modelo
                or "google/gemini-3.1-flash-image"
            ),
            erro=erro,
        )


# ============================================================
# 14. EXECUTAR PROVEDOR
# ============================================================

def executar_provider(
    provider: ImageProviderConfig,
    prompt_final: str,
    referencias: List[str],
    caminho_saida: Path,
    tamanho: str = "1024x1024",
    qualidade: str = "medium",
) -> ImageProviderResult:
    """
    Roteador central de provedores.

    A Aura fala com esta função.

    Esta função decide qual integração específica
    deve executar a geração.
    """

    if provider.nome == "openai":

        return executar_openai(

            prompt_final=
                prompt_final,

            referencias=
                referencias,

            caminho_saida=
                caminho_saida,

            provider=
                provider,

            tamanho=
                tamanho,

            qualidade=
                qualidade,
        )

    if provider.nome == "vercel":

        return executar_vercel(
            prompt_final=prompt_final,
            referencias=referencias,
            caminho_saida=caminho_saida,
            provider=provider,
            tamanho=tamanho,
            qualidade=qualidade,
        )


    if provider.nome == "openrouter":

        return executar_openrouter(
            prompt_final=prompt_final,
            referencias=referencias,
            caminho_saida=caminho_saida,
            provider=provider,
            tamanho=tamanho,
            qualidade=qualidade,
        )

    # --------------------------------------------------------
    # FUTUROS PROVEDORES
    # --------------------------------------------------------

    raise NotImplementedError(
        "O provedor "
        f"'{provider.nome}' "
        "ainda não possui integração de geração."
    )


# ============================================================
# 15. CONVERTER RESULTADO PARA DICT
# ============================================================

def resultado_provider_para_dict(
    resultado: ImageProviderResult,
) -> Dict[str, Any]:

    return {

        "sucesso":
            resultado.sucesso,

        "provider":
            resultado.provider,

        "modelo":
            resultado.modelo,

        "caminho_saida":
            resultado.caminho_saida,

        "erro":
            resultado.erro,

        "detalhes":
            resultado.detalhes
            or {},
    }


# ============================================================
# 16. GERAR IMAGEM COM REFERÊNCIAS
# ============================================================

def gerar_imagem_com_referencias(
    prompt: str,
    referencias: List[str],
    caminho_saida: str | Path,
    tamanho: str = "1024x1024",
    qualidade: str = "medium",
    provider: str = PROVIDER_PADRAO,
) -> Dict[str, Any]:

    # --------------------------------------------------------
    # PREPARAR PROMPT
    # --------------------------------------------------------

    prompt_final = construir_prompt_final(
        prompt
    )

    # --------------------------------------------------------
    # VALIDAR REFERÊNCIAS FÍSICAS
    # --------------------------------------------------------

    referencias_validas = (
        validar_referencias(
            referencias
        )
    )

    # --------------------------------------------------------
    # ESCOLHER PROVEDOR
    # --------------------------------------------------------

    provider_config = (
        escolher_provider(

            provider_preferido=
                provider,

            referencias=
                referencias_validas,
        )
    )

    # --------------------------------------------------------
    # PREPARAR CAMINHO DE SAÍDA
    # --------------------------------------------------------

    caminho_saida = Path(
        caminho_saida
    )

    garantir_pasta_saida(
        caminho_saida.parent
    )

    # --------------------------------------------------------
    # LOG
    # --------------------------------------------------------

    print(
        "\nAURA — GERANDO IMAGEM"
    )

    print(
        "Provider:",
        provider_config.nome,
    )

    print(
        "Modelo:",
        provider_config.modelo,
    )

    print(
        "Referências utilizadas:",
        len(
            referencias_validas
        ),
    )

    print(
        "\nPROMPT PREPARADO "
        "PARA PRODUÇÃO"
    )

    print(
        "--------------------------------------------"
    )

    print(
        prompt_final
    )

    print(
        "--------------------------------------------"
    )

    # --------------------------------------------------------
    # EXECUTAR PROVEDOR
    # --------------------------------------------------------

    resultado_provider = (
        executar_provider(

            provider=
                provider_config,

            prompt_final=
                prompt_final,

            referencias=
                referencias_validas,

            caminho_saida=
                caminho_saida,

            tamanho=
                tamanho,

            qualidade=
                qualidade,
        )
    )

    resultado = (
        resultado_provider_para_dict(
            resultado_provider
        )
    )

    # --------------------------------------------------------
    # COMPLEMENTAR RESULTADO
    # --------------------------------------------------------

    resultado[
        "quantidade_referencias"
    ] = len(
        referencias_validas
    )

    resultado[
        "referencias"
    ] = referencias_validas

    resultado[
        "tamanho"
    ] = tamanho

    resultado[
        "qualidade"
    ] = qualidade

    resultado[
        "prompt_producao"
    ] = prompt_final

    # --------------------------------------------------------
    # INFORMAR RESULTADO
    # --------------------------------------------------------

    if resultado[
        "sucesso"
    ]:

        print(
            "\nAURA — IMAGEM GERADA COM SUCESSO"
        )

        print(
            "Arquivo:",
            resultado[
                "caminho_saida"
            ],
        )

    else:

        print(
            "\nAURA — GERAÇÃO NÃO CONCLUÍDA"
        )

        detalhes = (
            resultado.get(
                "detalhes"
            )
            or {}
        )

        tipo_erro = (
            detalhes.get(
                "tipo"
            )
            or "erro_desconhecido"
        )

        print(
            "Tipo:",
            tipo_erro,
        )

        if detalhes.get(
            "bloqueio_seguranca"
        ):

            print(
                "O provedor interrompeu "
                "a geração por uma regra "
                "de segurança."
            )

            print(
                "A estratégia da Aura "
                "permanece válida."
            )

    return resultado


# ============================================================
# 17. EXTRAIR DADOS DE UMA EXECUÇÃO DA AURA
# ============================================================

def extrair_dados_execucao(
    execucao: Dict[str, Any],
) -> Dict[str, Any]:

    numero_imagem = (

        execucao.get(
            "numero_imagem"
        )

        or execucao.get(
            "numero"
        )

        or 1
    )

    funcao = (

        execucao.get(
            "funcao"
        )

        or "imagem"
    )

    prompt = (

        execucao.get(
            "prompt"
        )

        or execucao.get(
            "prompt_final"
        )

        or execucao.get(
            "prompt_producao"
        )

        or ""
    )

    referencias = (

        execucao.get(
            "referencias"
        )

        or execucao.get(
            "imagens_referencia"
        )

        or execucao.get(
            "referencias_selecionadas"
        )

        or []
    )

    provider = (

        execucao.get(
            "provider"
        )

        or execucao.get(
            "provedor"
        )

        or PROVIDER_PADRAO
    )

    caminhos_referencias = []

    for referencia in referencias:

        if isinstance(
            referencia,
            str,
        ):

            caminhos_referencias.append(
                referencia
            )

            continue

        if isinstance(
            referencia,
            dict,
        ):

            caminho = (

                referencia.get(
                    "caminho"
                )

                or referencia.get(
                    "caminho_imagem"
                )

                or referencia.get(
                    "arquivo"
                )
            )

            if caminho:

                caminhos_referencias.append(
                    caminho
                )

    return {

        "numero_imagem":
            int(
                numero_imagem
            ),

        "funcao":
            str(
                funcao
            ),

        "prompt":
            str(
                prompt
            ),

        "referencias":
            caminhos_referencias,

        "provider":
            str(
                provider
            ).strip().lower(),
    }


# ============================================================
# 18. GERAR UMA EXECUÇÃO DA AURA
# ============================================================

def gerar_imagem_execucao(
    execucao: Dict[str, Any],
    pasta_saida: str | Path = PASTA_SAIDA_PADRAO,
    tamanho: str = "1024x1024",
    qualidade: str = "medium",
    provider: str | None = None,
) -> Dict[str, Any]:

    dados = extrair_dados_execucao(
        execucao
    )

    pasta = garantir_pasta_saida(
        pasta_saida
    )

    nome_arquivo = criar_nome_arquivo(

        numero_imagem=
            dados[
                "numero_imagem"
            ],

        funcao=
            dados[
                "funcao"
            ],
    )

    caminho_saida = (
        pasta
        / nome_arquivo
    )

    provider_final = (

        provider

        or dados[
            "provider"
        ]

        or PROVIDER_PADRAO
    )

    resultado = (
        gerar_imagem_com_referencias(

            prompt=
                dados[
                    "prompt"
                ],

            referencias=
                dados[
                    "referencias"
                ],

            caminho_saida=
                caminho_saida,

            tamanho=
                tamanho,

            qualidade=
                qualidade,

            provider=
                provider_final,
        )
    )

    resultado[
        "numero_imagem"
    ] = dados[
        "numero_imagem"
    ]

    resultado[
        "funcao"
    ] = dados[
        "funcao"
    ]

    return resultado


# ============================================================
# 19. GERAR SOMENTE UMA IMAGEM DO PACOTE
# ============================================================

def gerar_imagem_do_pacote(
    execucoes: List[Dict[str, Any]],
    numero_imagem: int,
    pasta_saida: str | Path = PASTA_SAIDA_PADRAO,
    tamanho: str = "1024x1024",
    qualidade: str = "medium",
    provider: str | None = None,
) -> Dict[str, Any]:

    for execucao in execucoes:

        dados = extrair_dados_execucao(
            execucao
        )

        if (
            dados[
                "numero_imagem"
            ]
            == numero_imagem
        ):

            return gerar_imagem_execucao(

                execucao=
                    execucao,

                pasta_saida=
                    pasta_saida,

                tamanho=
                    tamanho,

                qualidade=
                    qualidade,

                provider=
                    provider,
            )

    raise ValueError(
        "Não foi encontrada execução "
        f"para a imagem {numero_imagem}."
    )


# ============================================================
# 20. GERAR PACOTE COMPLETO
# ============================================================

def gerar_pacote_imagens(
    execucoes: List[Dict[str, Any]],
    pasta_saida: str | Path = PASTA_SAIDA_PADRAO,
    tamanho: str = "1024x1024",
    qualidade: str = "medium",
    provider: str | None = None,
    continuar_em_erro: bool = True,
) -> Dict[str, Any]:
    """
    Gera todas as imagens de uma sequência preparada pela Aura.

    Um bloqueio ou erro de provedor não precisa derrubar
    todo o pacote.

    Se continuar_em_erro=True, a Aura registra o problema
    e continua para a próxima imagem.
    """

    resultados = []

    sucessos = 0

    falhas = 0

    bloqueios_seguranca = 0

    for execucao in execucoes:

        try:

            resultado = gerar_imagem_execucao(

                execucao=
                    execucao,

                pasta_saida=
                    pasta_saida,

                tamanho=
                    tamanho,

                qualidade=
                    qualidade,

                provider=
                    provider,
            )

        except Exception as erro:

            if not continuar_em_erro:

                raise

            dados = extrair_dados_execucao(
                execucao
            )

            resultado = {

                "sucesso":
                    False,

                "numero_imagem":
                    dados[
                        "numero_imagem"
                    ],

                "funcao":
                    dados[
                        "funcao"
                    ],

                "provider": (
                    provider
                    or dados[
                        "provider"
                    ]
                ),

                "modelo":
                    None,

                "caminho_saida":
                    None,

                "erro":
                    str(
                        erro
                    ),

                "detalhes": {

                    "tipo":
                        "erro_execucao",

                    "mensagem":
                        str(
                            erro
                        ),

                    "bloqueio_seguranca":
                        False,
                },
            }

        resultados.append(
            resultado
        )

        if resultado.get(
            "sucesso"
        ):

            sucessos += 1

        else:

            falhas += 1

            detalhes = (
                resultado.get(
                    "detalhes"
                )
                or {}
            )

            if detalhes.get(
                "bloqueio_seguranca"
            ):

                bloqueios_seguranca += 1

    return {

        "sucesso":
            falhas == 0,

        "quantidade_execucoes":
            len(
                execucoes
            ),

        "quantidade_sucessos":
            sucessos,

        "quantidade_falhas":
            falhas,

        "quantidade_bloqueios_seguranca":
            bloqueios_seguranca,

        "resultados":
            resultados,
    }


# ============================================================
# 21. FORMATAR RESULTADO DE GERAÇÃO
# ============================================================

def formatar_resultado_geracao(
    resultado: Dict[str, Any],
) -> str:

    linhas = []

    linhas.append(
        "RESULTADO DA GERAÇÃO"
    )

    linhas.append(
        ""
    )

    linhas.append(
        "SUCESSO: "
        f"{resultado.get('sucesso')}"
    )

    if resultado.get(
        "numero_imagem"
    ) is not None:

        linhas.append(
            "IMAGEM: "
            f"{resultado.get('numero_imagem')}"
        )

    if resultado.get(
        "funcao"
    ):

        linhas.append(
            "FUNÇÃO: "
            f"{resultado.get('funcao')}"
        )

    linhas.append(
        "PROVIDER: "
        f"{resultado.get('provider')}"
    )

    linhas.append(
        "MODELO: "
        f"{resultado.get('modelo')}"
    )

    if resultado.get(
        "caminho_saida"
    ):

        linhas.append(
            "ARQUIVO: "
            f"{resultado.get('caminho_saida')}"
        )

    if not resultado.get(
        "sucesso"
    ):

        detalhes = (
            resultado.get(
                "detalhes"
            )
            or {}
        )

        linhas.append(
            ""
        )

        linhas.append(
            "GERAÇÃO NÃO CONCLUÍDA"
        )

        linhas.append(
            "TIPO DE ERRO: "
            f"{detalhes.get('tipo')}"
        )

        if detalhes.get(
            "bloqueio_seguranca"
        ):

            linhas.append(
                ""
            )

            linhas.append(
                "O provedor interrompeu a geração "
                "por uma regra de segurança."
            )

            linhas.append(
                "Isso não invalida o plano visual, "
                "o briefing ou o prompt criado pela Aura."
            )

    return "\n".join(
        linhas
    )