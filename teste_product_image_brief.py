# ============================================================
# VISUALSELLER FASHION
# TESTE — BRIEFING DE IMAGEM
# ============================================================

from aura_schemas.body import (
    FichaBody,
    GradeTamanho,
)

from aura.product_meaning import (
    analisar_significados,
)

from aura.product_identity import (
    construir_identidade,
)

from aura.product_connection import (
    analisar_conexoes,
)

from aura.product_desire import (
    analisar_desejos,
)

from aura.product_value import (
    analisar_valor_produto,
)

from aura.product_positioning import (
    analisar_posicionamento,
)

from aura.product_communication import (
    analisar_comunicacao,
)

from aura.product_visual_plan import (
    criar_plano_visual,
)

from aura.product_image_brief import (
    criar_briefings_imagem,
    formatar_briefings_imagem,
)


# ============================================================
# 1. CRIAR FICHA DO PRODUTO
# ============================================================

ficha = FichaBody(

    categoria="Moda íntima",

    tipo_produto="Body",

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
        "85% poliamida, 15% elastano"
    ),

    composicao_forro=(
        "100% algodão"
    ),

    materiais_visuais=[
        "renda floral",
        "malha/tela fina translúcida",
        "malha canelada",
    ],

    manga="longa",

    decote_frente="V",

    decote_costas="V profundo",

    fechamento="colchetes",

    possui_bojo=False,

    possui_forro=True,

    transparencia=(
        "Transparência parcial em mangas, "
        "costas e áreas em renda."
    ),

    acabamento_mangas=(
        "Punho largo em malha canelada e opaca."
    ),

    tamanho_medido="P",
)


# ============================================================
# 2. CABEÇALHO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — BRIEFING DE IMAGEM"
)

print(
    "============================================"
)


# ============================================================
# 3. SIGNIFICADOS
# ============================================================

significados = analisar_significados(
    ficha
)


# ============================================================
# 4. IDENTIDADE
# ============================================================

identidade = construir_identidade(
    significados
)


# ============================================================
# 5. CONEXÕES
# ============================================================

conexoes = analisar_conexoes(
    identidade
)


# ============================================================
# 6. DESEJOS
# ============================================================

desejos = analisar_desejos(
    conexoes
)


# ============================================================
# 7. VALOR PERCEBIDO
# ============================================================

valores = analisar_valor_produto(
    ficha,
    identidade,
    desejos,
)


# ============================================================
# 8. POSICIONAMENTO
# ============================================================

posicionamento = analisar_posicionamento(
    identidade,
    desejos,
    valores,
)


# ============================================================
# 9. COMUNICAÇÃO
# ============================================================

comunicacao = analisar_comunicacao(
    posicionamento
)


# ============================================================
# 10. PLANO VISUAL
# ============================================================

plano_visual = criar_plano_visual(
    ficha=ficha,
    identidade=identidade,
    posicionamento=posicionamento,
    comunicacao=comunicacao,
)


# ============================================================
# 11. CRIAR BRIEFINGS
# ============================================================

briefing_visual = criar_briefings_imagem(
    ficha=ficha,
    plano_visual=plano_visual,
)


# ============================================================
# 12. ESTRATÉGIA UTILIZADA
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "ESTRATÉGIA UTILIZADA"
)

print(
    "============================================"
)


print(
    "IDENTIDADE:",
    identidade.leitura_principal
)


print(
    "POSICIONAMENTO:",
    posicionamento.direcao_principal
)


print(
    "TERRITÓRIO:",
    posicionamento.territorio_comunicacao
)


print(
    "MENSAGEM CENTRAL:",
    comunicacao.mensagem_central
)


print(
    "CONCEITO VISUAL:",
    plano_visual.conceito_visual
)


print(
    "DIREÇÃO VISUAL:",
    plano_visual.direcao_visual
)


# ============================================================
# 13. MOSTRAR BRIEFINGS
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "AURA — BRIEFING DE IMAGEM"
)

print(
    "============================================"
)


print(
    formatar_briefings_imagem(
        briefing_visual
    )
)


# ============================================================
# 14. RESUMO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RESUMO DOS BRIEFINGS"
)

print(
    "============================================"
)


print(
    "CONFIANÇA GERAL:",
    briefing_visual.confianca
)


print(
    "QUANTIDADE DE BRIEFINGS:",
    len(
        briefing_visual.briefings
    )
)


print(
    "QUANTIDADE DE REGRAS GLOBAIS:",
    len(
        briefing_visual.regras_globais
    )
)


# ============================================================
# 15. RESUMO POR IMAGEM
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "SEQUÊNCIA DE PRODUÇÃO"
)

print(
    "============================================"
)


for briefing in briefing_visual.briefings:

    print(
        f"\nIMAGEM {briefing.numero}"
    )

    print(
        "FUNÇÃO:",
        briefing.funcao
    )

    print(
        "FOCO PRINCIPAL:",
        briefing.foco_principal
    )

    print(
        "ENQUADRAMENTO:",
        briefing.enquadramento
    )

    print(
        "CONFIANÇA:",
        briefing.confianca
    )

    print(
        "ELEMENTOS A DESTACAR:",
        len(
            briefing.destacar
        )
    )

    print(
        "EVIDÊNCIAS:",
        len(
            briefing.evidencias
        )
    )

    print(
        "REGRAS DE PRESERVAÇÃO:",
        len(
            briefing.preservar
        )
    )


# ============================================================
# 16. VERIFICAÇÃO DE QUANTIDADE
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VERIFICAÇÃO"
)

print(
    "============================================"
)


if not briefing_visual.briefings:

    print(
        "ERRO: nenhum briefing foi criado."
    )

elif len(
    briefing_visual.briefings
) != len(
    plano_visual.imagens
):

    print(
        "ATENÇÃO: a quantidade de briefings "
        "não corresponde à quantidade de imagens "
        "do plano visual."
    )

else:

    print(
        "A Aura conseguiu transformar cada imagem "
        "do plano visual em um briefing de "
        "direção de arte."
    )


# ============================================================
# 17. VERIFICAÇÃO DE PRESERVAÇÃO
# ============================================================

briefings_sem_preservacao = [

    briefing.numero

    for briefing in briefing_visual.briefings

    if not briefing.preservar
]


if briefings_sem_preservacao:

    print(
        "ATENÇÃO: existem imagens sem regras "
        "de preservação:"
    )

    print(
        briefings_sem_preservacao
    )

else:

    print(
        "Todas as imagens possuem regras "
        "de preservação das características "
        "reais do produto."
    )


# ============================================================
# 18. VERIFICAÇÃO DE EVIDÊNCIAS
# ============================================================

briefings_sem_evidencias = [

    briefing.numero

    for briefing in briefing_visual.briefings

    if not briefing.evidencias
]


if briefings_sem_evidencias:

    print(
        "ATENÇÃO: existem imagens sem "
        "evidências específicas:"
    )

    print(
        briefings_sem_evidencias
    )

else:

    print(
        "Todas as imagens possuem evidências "
        "ligadas ao produto."
    )


# ============================================================
# 19. VERIFICAÇÃO FINAL
# ============================================================

if (
    len(
        briefing_visual.briefings
    ) == 7

    and not briefings_sem_preservacao

    and not briefings_sem_evidencias
):

    print(
        "O pacote de direção de arte está "
        "estruturado e sustentado por evidências."
    )


# ============================================================
# 20. FIM
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