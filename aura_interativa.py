from aura_schemas.body import (
    FichaBody,
    GradeTamanho,
)

from aura.state import EstadoProduto

from aura.evidence import FonteEvidencia

from aura.processor import (
    processar_informacao,
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


# ============================================================
# VISUALSELLER FASHION
# AURA — MODO INTERATIVO
# PRODUTO 001 — BODY DUBAI
# ============================================================


# ============================================================
# 1. CRIAR FICHA INICIAL
# ============================================================

ficha = FichaBody(
    marca="Linda Sedução",

    nome_modelo="Body Dubai",

    referencia="277",

    codigo_barras="7002770010015",

    cores_disponiveis=[
        "Preto",
    ],

    tamanhos_disponiveis=[
        "P",
        "M",
        "G",
        "GG",
    ],

    grade=[
        GradeTamanho(
            tamanho="P",
            quantidade=8,
        ),
        GradeTamanho(
            tamanho="M",
            quantidade=10,
        ),
        GradeTamanho(
            tamanho="G",
            quantidade=11,
        ),
        GradeTamanho(
            tamanho="GG",
            quantidade=15,
        ),
    ],

    quantidade_total=44,

    composicao_principal=(
        "85% poliamida + 15% elastano"
    ),

    composicao_forro=(
        "100% algodão"
    ),

    materiais_visuais=[
        "renda floral",
        "material transparente nas mangas",
        "malha canelada",
        "malha lisa",
    ],

    manga="longa",

    decote_frente="V",

    decote_costas="V",

    fechamento=(
        "colchetes na entreperna "
        "com 2 posições de ajuste"
    ),

    transparencia=(
        "mangas e regiões em renda"
    ),

    acabamento_mangas=(
        "malha canelada"
    ),

    tamanho_medido="P",
)


# ============================================================
# 2. CRIAR ESTADO DO PRODUTO
# ============================================================

estado = EstadoProduto(
    ficha=ficha
)


# ============================================================
# 3. DEFINIR TIPOS ESPERADOS DOS CAMPOS
# ============================================================

TIPOS_DOS_CAMPOS = {
    "possui_bojo": bool,
    "possui_forro": bool,

    "tipo_bojo": str,
    "composicao_forro": str,
    "acabamento_mangas": str,
    "manga": str,
    "decote_frente": str,
    "decote_costas": str,
    "fechamento": str,
    "transparencia": str,
    "tamanho_medido": str,

    "busto_cm": float,
    "cintura_cm": float,
    "quadril_cm": float,
    "comprimento_cm": float,
}


# ============================================================
# 4. FUNÇÃO PARA DESCOBRIR O TIPO DO CAMPO
# ============================================================

def obter_tipo_campo(
    campo: str,
):
    """
    Retorna o tipo esperado para o campo.

    Caso não exista uma regra específica,
    o sistema assume texto.
    """

    return TIPOS_DOS_CAMPOS.get(
        campo,
        str,
    )


# ============================================================
# 5. CABEÇALHO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "AURA — ANÁLISE INTERATIVA"
)

print(
    "PRODUTO 001 — BODY DUBAI"
)

print(
    "========================================"
)


# ============================================================
# 6. LOOP PRINCIPAL DA CONVERSA
# ============================================================

while True:

    # --------------------------------------------------------
    # AURA ANALISA O ESTADO ATUAL
    # --------------------------------------------------------

    resultado = aura_loop_graph.invoke(
        {
            "estado_produto": estado
        }
    )

    # --------------------------------------------------------
    # GERAR MENSAGEM NATURAL
    # --------------------------------------------------------

    mensagem = gerar_mensagem_aura(
        resultado
    )

    print(
        "\nAURA:"
    )

    print(
        mensagem
    )

    # --------------------------------------------------------
    # VERIFICAR SE A FICHA TERMINOU
    # --------------------------------------------------------

    if (
        resultado.get("acao")
        == "ENCERRAR_FICHA"
    ):

        break

    # --------------------------------------------------------
    # IDENTIFICAR CAMPO ATUAL
    # --------------------------------------------------------

    campo = resultado.get(
        "campo"
    )

    if campo is None:

        print(
            "\nAURA:"
        )

        print(
            "Não consegui identificar "
            "qual informação preciso analisar."
        )

        break

    # --------------------------------------------------------
    # RECEBER RESPOSTA DO USUÁRIO
    # --------------------------------------------------------

    resposta_usuario = input(
        "\nVOCÊ: "
    )

    # --------------------------------------------------------
    # DESCOBRIR TIPO ESPERADO
    # --------------------------------------------------------

    tipo_esperado = obter_tipo_campo(
        campo
    )

    # --------------------------------------------------------
    # INTERPRETAR A RESPOSTA
    # --------------------------------------------------------

    valor_interpretado = interpretar_resposta(
        campo=campo,
        resposta=resposta_usuario,
        tipo_esperado=tipo_esperado,
    )

    # --------------------------------------------------------
    # RESPOSTA NÃO COMPREENDIDA
    # --------------------------------------------------------

    if valor_interpretado is None:

        print(
            "\nAURA:"
        )

        print(
            "Não consegui interpretar essa "
            "resposta com segurança."
        )

        print(
            "Você pode responder novamente "
            "de forma mais objetiva?"
        )

        continue

    # --------------------------------------------------------
    # PROCESSAR INFORMAÇÃO
    # --------------------------------------------------------

    processamento = processar_informacao(
        ficha=estado.ficha,

        campo=campo,

        valor=valor_interpretado,

        fonte=(
            FonteEvidencia.INFORMACAO_FORNECIDA
        ),

        descricao=(
            "Informação fornecida diretamente "
            "pelo usuário durante a análise "
            "interativa da AURA."
        ),
    )

    # --------------------------------------------------------
    # REGISTRAR DECISÃO NA MEMÓRIA
    # --------------------------------------------------------

    estado.registrar_resultado(
        processamento
    )

    # --------------------------------------------------------
    # MOSTRAR SE A INFORMAÇÃO FOI ACEITA
    # --------------------------------------------------------

    if processamento.get(
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
            "Essa informação ainda não pode "
            "ser registrada como fato."
        )


# ============================================================
# 7. RESULTADO FINAL
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "FICHA CONCLUÍDA"
)

print(
    "========================================"
)

print(
    "\nPOSSUI BOJO:",
    estado.ficha.possui_bojo
)

print(
    "POSSUI FORRO:",
    estado.ficha.possui_forro
)

print(
    "COMPOSIÇÃO DO FORRO:",
    estado.ficha.composicao_forro
)


# ============================================================
# 8. MEMÓRIA DA AURA
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