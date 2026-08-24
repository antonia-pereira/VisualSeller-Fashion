from pathlib import Path

from aura.product_flow import (
    preparar_produto,
    obter_proxima_interacao,
    receber_resposta,
    produto_concluido,
    obter_status_produto,
    obter_ficha_final,
)


# ============================================================
# VISUALSELLER FASHION
# TESTE REAL — FLUXO COMPLETO DO PRODUTO
# ============================================================


# ============================================================
# 1. LOCALIZAÇÃO DAS IMAGENS
# ============================================================

PASTA_IMAGENS = Path("imagens")


imagens = [
    {
        "caminho": str(
            PASTA_IMAGENS
            / "body_frente.jpg.jpeg"
        ),
        "tipo": "frente",
    },
    {
        "caminho": str(
            PASTA_IMAGENS
            / "body_costa.jpeg"
        ),
        "tipo": "costas",
    },
    {
        "caminho": str(
            PASTA_IMAGENS
            / "body_detalhe (1).jpeg"
        ),
        "tipo": "detalhe",
    },
    {
        "caminho": str(
            PASTA_IMAGENS
            / "body_detalhe (2).jpeg"
        ),
        "tipo": "detalhe",
    },
    {
        "caminho": str(
            PASTA_IMAGENS
            / "body_detalhe (3).jpeg"
        ),
        "tipo": "detalhe",
    },
    {
        "caminho": str(
            PASTA_IMAGENS
            / "body_detalhe (4).jpeg"
        ),
        "tipo": "detalhe",
    },
    {
        "caminho": str(
            PASTA_IMAGENS
            / "body_detalhe (5).jpeg"
        ),
        "tipo": "detalhe",
    },
    {
        "caminho": str(
            PASTA_IMAGENS
            / "body_detalhe (6).jpeg"
        ),
        "tipo": "detalhe",
    },
    {
        "caminho": str(
            PASTA_IMAGENS
            / "body_detalhe (7).jpeg"
        ),
        "tipo": "detalhe",
    },
    {
        "caminho": str(
            PASTA_IMAGENS
            / "body_detalhe (8).jpeg"
        ),
        "tipo": "detalhe",
    },
    {
        "caminho": str(
            PASTA_IMAGENS
            / "body_detalhe (9).jpeg"
        ),
        "tipo": "detalhe",
    },
    {
        "caminho": str(
            PASTA_IMAGENS
            / "body_composição.jpeg"
        ),
        "tipo": "composicao",
    },
    {
        "caminho": str(
            PASTA_IMAGENS
            / "body_etiqueta.jpeg"
        ),
        "tipo": "etiqueta",
    },
]


# ============================================================
# 2. CABEÇALHO
# ============================================================

print(
    "\n"
    "========================================\n"
    "VISUALSELLER FASHION\n"
    "Mostre seu produto para a Aura\n"
    "========================================\n"
)


# ============================================================
# 3. VERIFICAR SE AS IMAGENS EXISTEM
# ============================================================

imagens_ausentes = []


for imagem in imagens:

    caminho = Path(
        imagem[
            "caminho"
        ]
    )

    if not caminho.exists():

        imagens_ausentes.append(
            imagem[
                "caminho"
            ]
        )


if imagens_ausentes:

    print(
        "ERRO: algumas imagens não foram encontradas.\n"
    )

    for caminho in imagens_ausentes:

        print(
            "-",
            caminho
        )

    raise SystemExit


# ============================================================
# 4. AURA ANALISA O PRODUTO
# ============================================================

print(
    "A Aura recebeu as imagens do produto.\n"
)

print(
    "Iniciando análise...\n"
)


sessao = preparar_produto(
    imagens
)


# ============================================================
# 5. RESULTADO INICIAL
# ============================================================

status_inicial = obter_status_produto(
    sessao
)


print(
    "\n"
    "========================================"
)

print(
    "ANÁLISE INICIAL CONCLUÍDA"
)

print(
    "========================================"
)


print(
    "STATUS DA FICHA:",
    status_inicial[
        "status_ficha"
    ]
)


print(
    "CAMPOS ESSENCIAIS FALTANDO:",
    status_inicial[
        "quantidade_essenciais_faltando"
    ]
)


# ============================================================
# 6. CONVERSA REAL COM A AURA
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "CONVERSA COM A AURA"
)

print(
    "========================================"
)


while not produto_concluido(
    sessao
):

    pergunta = obter_proxima_interacao(
        sessao
    )


    if pergunta is None:

        break


    mensagem = pergunta.get(
        "mensagem"
    )


    if not mensagem:

        mensagem = pergunta.get(
            "pergunta"
        )


    if not mensagem:

        mensagem = (
            "Preciso de mais uma informação "
            "para completar a ficha."
        )


    print(
        "\nAURA:"
    )

    print(
        mensagem
    )


    print(
        "\nVOCÊ:"
    )


    resposta = input(
        "> "
    ).strip()


    while not resposta:

        print(
            "\nAURA:"
        )

        print(
            "Preciso dessa informação para continuar."
        )

        print(
            "\nVOCÊ:"
        )

        resposta = input(
            "> "
        ).strip()


    resultado = receber_resposta(
        sessao=sessao,
        resposta=resposta,
    )


    if resultado.get(
        "aceita"
    ):

        campos = resultado.get(
            "campos_atualizados",
            [],
        )

        print(
            "\nAURA:"
        )

        if campos:

            print(
                "Informações registradas."
            )

        else:

            print(
                "Resposta recebida."
            )

    else:

        print(
            "\nAURA:"
        )

        print(
            "Não consegui registrar essa resposta."
        )


# ============================================================
# 7. STATUS FINAL
# ============================================================

status_final = obter_status_produto(
    sessao
)


print(
    "\n"
    "========================================"
)

print(
    "RESULTADO FINAL"
)

print(
    "========================================"
)


print(
    "STATUS DO FLUXO:",
    status_final[
        "status_fluxo"
    ]
)


print(
    "STATUS DA FICHA:",
    status_final[
        "status_ficha"
    ]
)


print(
    "CONCLUÍDO:",
    status_final[
        "concluido"
    ]
)


print(
    "ESSENCIAIS FALTANDO:",
    status_final[
        "quantidade_essenciais_faltando"
    ]
)


# ============================================================
# 8. FICHA FINAL
# ============================================================

ficha = obter_ficha_final(
    sessao
)


print(
    "\n"
    "========================================"
)

print(
    "FICHA TÉCNICA FINAL DA AURA"
)

print(
    "========================================"
)


dados_ficha = ficha.model_dump()


for campo, valor in dados_ficha.items():

    if valor is not None:

        if (
            isinstance(
                valor,
                list,
            )
            and len(valor) == 0
        ):

            continue

        print(
            f"{campo}: {valor}"
        )


# ============================================================
# 9. ENCERRAMENTO
# ============================================================

print(
    "\n"
    "========================================"
)


if produto_concluido(
    sessao
):

    print(
        "AURA: Produto compreendido."
    )

    print(
        "A ficha técnica está pronta."
    )

else:

    print(
        "AURA: Ainda existem informações "
        "necessárias para completar o produto."
    )


print(
    "========================================"
)

print(
    "FIM DO TESTE"
)

print(
    "========================================"
)