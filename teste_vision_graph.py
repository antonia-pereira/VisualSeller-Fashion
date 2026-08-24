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

from aura_schemas.body import (
    FichaBody,
)


# ============================================================
# VISUALSELLER FASHION
# TESTE — FOTO → FICHA → GRAFO → PERGUNTA
# ============================================================


# ============================================================
# 1. IMAGEM REAL
# ============================================================

CAMINHO_IMAGEM = (
    "imagens/body_frente.jpg.jpeg"
)


# ============================================================
# 2. CRIAR FICHA VAZIA
# ============================================================

ficha = FichaBody()


# ============================================================
# 3. CRIAR ESTADO
# ============================================================

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
    "VISÃO → FICHA → GRAFO"
)

print(
    "========================================"
)


# ============================================================
# 5. AURA ANALISA A FOTO
# ============================================================

print(
    "\nAURA está analisando a foto..."
)


resultado_visao = analisar_imagem(
    CAMINHO_IMAGEM
)


evidencias_visuais = resultado_visao.get(
    "evidencias",
    [],
)


print(
    "\nEvidências encontradas:",
    len(
        evidencias_visuais
    )
)


# ============================================================
# 6. PROCESSAR EVIDÊNCIAS
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

        print(
            "\nEvidência ignorada:"
        )

        print(
            campo
        )

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
# 7. MOSTRAR FICHA PREENCHIDA PELA VISÃO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "FICHA APÓS A FOTO"
)

print(
    "========================================"
)


print(
    estado.ficha.model_dump_json(
        indent=2
    )
)


# ============================================================
# 8. ENVIAR ESTADO PARA O LANGGRAPH
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "AURA ANALISA O QUE AINDA FALTA"
)

print(
    "========================================"
)


resultado_grafo = aura_loop_graph.invoke(
    {
        "estado_produto": estado
    }
)


# ============================================================
# 9. MOSTRAR DECISÃO INTERNA
# ============================================================

print(
    "\nAÇÃO:",
    resultado_grafo.get(
        "acao"
    )
)


print(
    "CAMPO:",
    resultado_grafo.get(
        "campo"
    )
)


print(
    "VALOR PROPOSTO:",
    resultado_grafo.get(
        "valor_proposto"
    )
)


print(
    "MOTIVO:",
    resultado_grafo.get(
        "motivo"
    )
)


print(
    "STATUS:",
    resultado_grafo.get(
        "status_fluxo"
    )
)


print(
    "RESULTADO:",
    resultado_grafo.get(
        "resultado"
    )
)


# ============================================================
# 10. GERAR MENSAGEM DA AURA
# ============================================================

mensagem = gerar_mensagem_aura(
    resultado_grafo
)


print(
    "\n"
    "========================================"
)

print(
    "AURA FALA COM O USUÁRIO"
)

print(
    "========================================"
)


print(
    "\nAURA:"
)

print(
    mensagem
)


# ============================================================
# 11. MEMÓRIA
# ============================================================

resumo = estado.resumo()


print(
    "\n"
    "========================================"
)

print(
    "MEMÓRIA DA AURA"
)

print(
    "========================================"
)


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


print(
    "TOTAL DE DECISÕES:",
    resumo[
        "total_decisoes"
    ]
)


# ============================================================
# FIM
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "FIM DO TESTE"
)

print(
    "========================================"
)