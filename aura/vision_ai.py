import base64
import json
import mimetypes
import os

from dotenv import load_dotenv
from openai import OpenAI


# ============================================================
# VISUALSELLER FASHION
# AURA — VISÃO COM IA
# ============================================================


# ============================================================
# 1. CARREGAR O .ENV PRIMEIRO
# ============================================================

load_dotenv()


# ============================================================
# 2. PEGAR A CHAVE
# ============================================================

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)


if not OPENAI_API_KEY:

    raise RuntimeError(
        "A chave OPENAI_API_KEY não foi encontrada."
    )


# ============================================================
# 3. CRIAR CLIENTE SOMENTE DEPOIS DO LOAD_DOTENV
# ============================================================

client = OpenAI(
    api_key=OPENAI_API_KEY
)


# ============================================================
# 4. CONVERTER FOTO PARA DATA URL
# ============================================================

def imagem_para_data_url(
    caminho_imagem: str,
) -> str:

    if not os.path.exists(
        caminho_imagem
    ):

        raise FileNotFoundError(
            f"Imagem não encontrada: "
            f"{caminho_imagem}"
        )

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
    ).decode(
        "utf-8"
    )

    return (
        f"data:{mime_type};"
        f"base64,{imagem_base64}"
    )


# ============================================================
# 5. INSTRUÇÕES DA VISÃO DA AURA
# ============================================================

PROMPT_VISAO = """
Você é a camada de visão da AURA,
sistema de inteligência de moda do
VisualSeller Fashion.

Sua função é observar fotografias reais
de produtos de moda e extrair somente
informações visualmente sustentadas.

REGRAS:

1. Não invente informações.

2. Não deduza composição de tecido somente
pela aparência.

3. Não determine presença de bojo, forro,
composição, medidas ou materiais internos
quando isso não estiver claramente visível.

4. Quando houver dúvida, reduza a confiança.

5. Fotos de etiquetas podem fornecer
informações documentais quando o texto
estiver legível.

6. Diferencie observação de certeza.

Use apenas estes níveis de confiança:

alta
media
baixa

Use somente campos desta lista quando
forem aplicáveis:

decote_frente
decote_costas
manga
acabamento_mangas
transparencia
materiais_visuais
fechamento
possui_bojo
possui_forro
composicao_principal
composicao_forro
tamanho_medido
referencia
codigo_barras

Retorne SOMENTE JSON válido.

Formato obrigatório:

{
    "tipo_imagem": "frente",
    "evidencias": [
        {
            "campo": "decote_frente",
            "valor": "V",
            "confianca": "alta",
            "observacao": "Descrição objetiva do que sustenta a conclusão."
        }
    ]
}
"""


# ============================================================
# 6. ANALISAR FOTO
# ============================================================

def analisar_imagem(
    caminho_imagem: str,
) -> dict:

    data_url = imagem_para_data_url(
        caminho_imagem
    )

    resposta = client.responses.create(
        model="gpt-5.6-luna",

        input=[
            {
                "role": "user",

                "content": [
                    {
                        "type": "input_text",

                        "text": PROMPT_VISAO,
                    },

                    {
                        "type": "input_image",

                        "image_url": data_url,

                        "detail": "high",
                    },
                ],
            }
        ],
    )

    texto = resposta.output_text.strip()


    # ========================================================
    # LIMPAR ```json CASO APAREÇA
    # ========================================================

    if texto.startswith(
        "```json"
    ):

        texto = texto[7:]


    elif texto.startswith(
        "```"
    ):

        texto = texto[3:]


    if texto.endswith(
        "```"
    ):

        texto = texto[:-3]


    texto = texto.strip()


    # ========================================================
    # CONVERTER PARA DICT
    # ========================================================

    try:

        resultado = json.loads(
            texto
        )

    except json.JSONDecodeError as erro:

        raise ValueError(
            "A AURA recebeu uma resposta "
            "que não era JSON válido.\n\n"
            f"Resposta recebida:\n{texto}"
        ) from erro


    return resultado