from aura.vision_ai import analisar_imagem

from aura.evidence import (
    FonteEvidencia,
    NivelConfianca,
)

from aura.processor import (
    processar_informacao,
)

from aura.state import (
    EstadoProduto,
)

from aura.graph_loop import (
    aura_loop_graph,
)

from aura.communication import (
    gerar_mensagem_aura,
)

from aura.interpreter import (
    interpretar_resposta,
)

from aura_schemas.body import (
    FichaBody,
)


# ============================================================
# VISUALSELLER FASHION
# AURA — CONVERSA VISUAL CONTROLADA
# ============================================================


# ============================================================
# 1. CONFIGURAÇÕES
# ============================================================

CAMINHO_IMAGEM = (
    "imagens/body_frente.jpg.jpeg"
)

LIMITE_PERGUNTAS = 4


# ============================================================
# 2. TIPOS DOS CAMPOS
# ============================================================

TIPOS_DOS_CAMPOS = {
    "marca": str,
    "nome_modelo": str,
    "referencia": str,
    "codigo_barras": str,

    "quantidade_total": int,

    "composicao_principal": str,
    "composicao_forro": str,

    "manga": str,
    "decote_frente": str,
    "decote_costas": str,
    "fechamento": str,

    "possui_bojo": bool,
    "tipo_bojo": str,
    "possui_forro": bool,
    "transparencia": str,

    "acabamento_mangas": str,
    "acabamento_pernas": str,
    "acabamento_decote": str,

    "tamanho_medido": str,

    "busto_cm": float,
    "cintura_cm": float,
    "quadril_cm": float,
    "comprimento_cm": float,

    "cores_disponiveis": str,
    "tamanhos_disponiveis": str,
}


# ============================================================
# 3. CRIAR FICHA E ESTADO
# ============================================================

ficha = FichaBody()

estado = EstadoProduto(
    ficha=ficha
)


# ============================================================
# 4. CABEÇALHO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "AURA — CONVERSA VISUAL"
)

print(
    "========================================"
)


# ============================================================
# 5. ANALISAR FOTO
# ============================================================

print(
    "\nAURA:"
)

print(
    "Vou analisar primeiro o que consigo "
    "identificar pela fotografia."
)


resultado_visao = analisar_imagem(
    CAMINHO_IMAGEM
)

evidencias_visuais = resultado_visao.get(
    "evidencias",
    [],
)


# ============================================================
# 6. PROCESSAR EVIDÊNCIAS VISUAIS
# ============================================================

for item in evidencias_visuais:

    campo = item.get(
        "campo"
    )

    valor = item.get(
        "valor"
    )

    confianca_texto = item.get(
        "confianca"
    )

    descricao = item.get(
        "observacao"
    )

    try:

        confianca = NivelConfianca(
            confianca_texto
        )

    except ValueError:

        continue

    resultado = processar_informacao(
        ficha=estado.ficha,
        campo=campo,
        valor=valor,
        fonte=FonteEvidencia.FOTOGRAFIA,
        descricao=descricao,
        confianca=confianca,
    )

    estado.registrar_resultado(
        resultado
    )


# ============================================================
# 7. RESUMO APÓS A FOTO
# ============================================================

print(
    "\nAURA:"
)

print(
    "Terminei a análise visual."
)

print(
    "Vou perguntar apenas o que for "
    "essencial para completar esta etapa."
)

print(
    "\nVocê pode digitar:"
)

print(
    "- pular"
)

print(
    "- finalizar"
)


# ============================================================
# 8. CONVERSA CONTROLADA
# ============================================================

perguntas_feitas = 0


while perguntas_feitas < LIMITE_PERGUNTAS:

    resultado_grafo = aura_loop_graph.invoke(
        {
            "estado_produto": estado
        }
    )

    acao = resultado_grafo.get(
        "acao"
    )

    campo = resultado_grafo.get(
        "campo"
    )


    # --------------------------------------------------------
    # FICHA CONCLUÍDA
    # --------------------------------------------------------

    if acao == "ENCERRAR_FICHA":

        print(
            "\nAURA:"
        )

        print(
            "Perfeito. Já tenho as informações "
            "essenciais desta etapa."
        )

        break


    # --------------------------------------------------------
    # CAMPO INVÁLIDO
    # --------------------------------------------------------

    if campo is None:

        print(
            "\nAURA:"
        )

        print(
            "Não consegui determinar a próxima "
            "informação necessária."
        )

        break


    # --------------------------------------------------------
    # GERAR PERGUNTA
    # --------------------------------------------------------

    mensagem = gerar_mensagem_aura(
        resultado_grafo
    )

    print(
        "\nAURA:"
    )

    print(
        mensagem
    )


    # --------------------------------------------------------
    # RECEBER RESPOSTA
    # --------------------------------------------------------

    resposta_usuario = input(
        "\nVOCÊ: "
    )

    resposta_normalizada = (
        resposta_usuario
        .strip()
        .lower()
    )


    # --------------------------------------------------------
    # FINALIZAR
    # --------------------------------------------------------

    if resposta_normalizada in [
        "finalizar",
        "fim",
        "encerrar",
    ]:

        print(
            "\nAURA:"
        )

        print(
            "Tudo bem. Vou encerrar esta etapa "
            "com as informações disponíveis."
        )

        break


    # --------------------------------------------------------
    # PULAR
    # --------------------------------------------------------

    if resposta_normalizada in [
        "pular",
        "não sei",
        "nao sei",
        "não tenho",
        "nao tenho",
    ]:

        print(
            "\nAURA:"
        )

        print(
            "Tudo bem. Vou deixar essa informação "
            "pendente por enquanto."
        )

        perguntas_feitas += 1

        continue


    # --------------------------------------------------------
    # DESCOBRIR TIPO
    # --------------------------------------------------------

    tipo_esperado = TIPOS_DOS_CAMPOS.get(
        campo,
        str,
    )


    # --------------------------------------------------------
    # INTERPRETAR
    # --------------------------------------------------------

    valor_interpretado = interpretar_resposta(
        campo=campo,
        resposta=resposta_usuario,
        tipo_esperado=tipo_esperado,
    )


    if valor_interpretado is None:

        print(
            "\nAURA:"
        )

        print(
            "Não consegui interpretar essa "
            "resposta com segurança."
        )

        perguntas_feitas += 1

        continue


    # --------------------------------------------------------
    # PROCESSAR INFORMAÇÃO DO USUÁRIO
    # --------------------------------------------------------

    resultado_usuario = processar_informacao(
        ficha=estado.ficha,
        campo=campo,
        valor=valor_interpretado,
        fonte=(
            FonteEvidencia.INFORMACAO_FORNECIDA
        ),
        descricao=(
            "Informação fornecida pelo usuário."
        ),
    )

    estado.registrar_resultado(
        resultado_usuario
    )


    if resultado_usuario.get(
        "aceita"
    ):

        print(
            "\nAURA:"
        )

        print(
            "Informação registrada."
        )

    else:

        print(
            "\nAURA:"
        )

        print(
            "A informação ficou pendente."
        )


    perguntas_feitas += 1


# ============================================================
# 9. LIMITE ATINGIDO
# ============================================================

if perguntas_feitas >= LIMITE_PERGUNTAS:

    print(
        "\nAURA:"
    )

    print(
        "Já fiz as perguntas essenciais desta etapa."
    )

    print(
        "Vou encerrar por enquanto e manter "
        "as demais informações como pendentes."
    )


# ============================================================
# 10. STATUS FINAL
# ============================================================

resultado_final = aura_loop_graph.invoke(
    {
        "estado_produto": estado
    }
)

acao_final = resultado_final.get(
    "acao"
)


if acao_final == "ENCERRAR_FICHA":

    status_final = "COMPLETA"

else:

    status_final = "PARCIAL"


# ============================================================
# 11. RESUMO FINAL
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "RESULTADO DA ETAPA"
)

print(
    "========================================"
)

print(
    "STATUS:",
    status_final
)

print(
    "PERGUNTAS FEITAS:",
    perguntas_feitas
)


resumo = estado.resumo()

print(
    "INFORMAÇÕES ACEITAS:",
    resumo[
        "informacoes_aceitas"
    ]
)

print(
    "AGUARDANDO CONFIRMAÇÃO:",
    resumo[
        "aguardando_confirmacao"
    ]
)

print(
    "INFORMAÇÕES RECUSADAS:",
    resumo[
        "informacoes_recusadas"
    ]
)


# ============================================================
# 12. FICHA
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "FICHA ATUAL"
)

print(
    "========================================"
)

print(
    estado.ficha.model_dump_json(
        indent=2
    )
)


print(
    "\n"
    "========================================"
)

print(
    "FIM"
)

print(
    "========================================"
)