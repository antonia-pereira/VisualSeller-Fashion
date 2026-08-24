# ============================================================
# VISUALSELLER FASHION
# TESTE MÍNIMO — API DE IMAGEM
# ============================================================

import base64
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


# ============================================================
# 1. CONFIGURAÇÃO
# ============================================================

load_dotenv()

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

if not OPENAI_API_KEY:

    raise RuntimeError(
        "OPENAI_API_KEY não encontrada."
    )


client = OpenAI(
    api_key=OPENAI_API_KEY
)


MODELO = "gpt-image-2"


# ============================================================
# 2. IMAGEM QUE VAMOS TESTAR
# ============================================================

REFERENCIA = Path(
    "imagens/body_frente.jpg.jpeg"
)

SAIDA = Path(
    "outputs/teste_minimo_frente.png"
)


if not REFERENCIA.exists():

    raise FileNotFoundError(
        f"Imagem não encontrada: {REFERENCIA}"
    )


SAIDA.parent.mkdir(
    parents=True,
    exist_ok=True,
)


# ============================================================
# 3. PROMPT MÍNIMO
# ============================================================

PROMPT = """
Create a clean commercial product photograph
based on the provided reference image.

Preserve the original garment design,
shape, color, materials and visible details.

Show the garment clearly against a simple
neutral studio background.

Do not add text, logos, accessories or
new design elements.
""".strip()


# ============================================================
# 4. CABEÇALHO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE MÍNIMO — IMAGE API"
)

print(
    "============================================"
)

print(
    "\nREFERÊNCIA:"
)

print(
    REFERENCIA
)

print(
    "\nMODELO:"
)

print(
    MODELO
)

print(
    "\nPROMPT:"
)

print(
    PROMPT
)


# ============================================================
# 5. CHAMAR DIRETAMENTE A API
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "ENVIANDO PARA A API..."
)

print(
    "============================================"
)


try:

    with open(
        REFERENCIA,
        "rb",
    ) as arquivo:

        resposta = client.images.edit(

            model=MODELO,

            image=arquivo,

            prompt=PROMPT,

            size="1024x1024",

            quality="medium",
        )


    # ========================================================
    # 6. VERIFICAR RESPOSTA
    # ========================================================

    if not resposta.data:

        raise RuntimeError(
            "A API não retornou imagem."
        )


    imagem = resposta.data[0]

    imagem_base64 = getattr(
        imagem,
        "b64_json",
        None,
    )


    if not imagem_base64:

        raise RuntimeError(
            "A resposta não contém b64_json."
        )


    # ========================================================
    # 7. SALVAR
    # ========================================================

    conteudo = base64.b64decode(
        imagem_base64
    )


    with open(
        SAIDA,
        "wb",
    ) as arquivo_saida:

        arquivo_saida.write(
            conteudo
        )


    # ========================================================
    # 8. SUCESSO
    # ========================================================

    print(
        "\n"
        "============================================"
    )

    print(
        "SUCESSO"
    )

    print(
        "============================================"
    )

    print(
        "A API aceitou a imagem de referência."
    )

    print(
        "Arquivo gerado:"
    )

    print(
        SAIDA
    )


# ============================================================
# 9. ERRO
# ============================================================

except Exception as erro:

    print(
        "\n"
        "============================================"
    )

    print(
        "ERRO"
    )

    print(
        "============================================"
    )

    print(
        type(erro).__name__
    )

    print()

    print(
        erro
    )


# ============================================================
# 10. FIM
# ============================================================

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