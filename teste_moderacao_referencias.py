import base64
import mimetypes
import os

from dotenv import load_dotenv
from openai import OpenAI


# ============================================================
# CONFIGURAÇÃO
# ============================================================

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# ============================================================
# CONVERTER IMAGEM PARA DATA URL
# ============================================================

def imagem_para_data_url(caminho):

    mime_type, _ = mimetypes.guess_type(
        caminho
    )

    if mime_type is None:
        mime_type = "image/jpeg"

    with open(caminho, "rb") as arquivo:

        conteudo = base64.b64encode(
            arquivo.read()
        ).decode("utf-8")

    return (
        f"data:{mime_type};base64,{conteudo}"
    )


# ============================================================
# IMAGENS DA CAPA
# ============================================================

referencias = [
    "imagens/body_frente.jpg.jpeg",
    "imagens/body_costa.jpeg",
]


# ============================================================
# TESTE
# ============================================================

for caminho in referencias:

    print(
        "\n"
        "============================================"
    )

    print(
        "ANALISANDO:",
        caminho
    )

    print(
        "============================================"
    )

    data_url = imagem_para_data_url(
        caminho
    )

    resposta = client.moderations.create(

        model="omni-moderation-latest",

        input=[
            {
                "type": "image_url",
                "image_url": {
                    "url": data_url
                },
            }
        ],
    )

    resultado = resposta.results[0]

    print(
        "FLAGGED:",
        resultado.flagged
    )

    print(
        "SEXUAL:",
        resultado.categories.sexual
    )

    print(
        "SEXUAL/MINORS:",
        resultado.categories.sexual_minors
    )

    print(
        "SCORE SEXUAL:",
        resultado.category_scores.sexual
    )


print(
    "\n"
    "============================================"
)

print(
    "FIM DO TESTE"
)

print(
    "============================================"
)