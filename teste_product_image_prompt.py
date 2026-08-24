# ============================================================
# VISUALSELLER FASHION
# TESTE — PROMPTS DE IMAGEM
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
)

from aura.product_image_prompt import (
    criar_prompts_imagens,
    formatar_prompts_imagens,
)


# ============================================================
# 1. FICHA DO PRODUTO
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
    "TESTE — PROMPTS DE IMAGEM"
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
# 11. BRIEFINGS DE IMAGEM
# ============================================================

briefing_visual = criar_briefings_imagem(
    ficha=ficha,
    plano_visual=plano_visual,
)


# ============================================================
# 12. PROMPTS DE IMAGEM
# ============================================================

prompts = criar_prompts_imagens(
    briefing_visual
)


# ============================================================
# 13. ESTRATÉGIA UTILIZADA
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
    "CONCEITO VISUAL:",
    plano_visual.conceito_visual
)


print(
    "DIREÇÃO VISUAL:",
    plano_visual.direcao_visual
)


# ============================================================
# 14. MOSTRAR PROMPTS
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "AURA — PROMPTS DE PRODUÇÃO"
)

print(
    "============================================"
)


print(
    formatar_prompts_imagens(
        prompts
    )
)


# ============================================================
# 15. RESUMO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RESUMO DOS PROMPTS"
)

print(
    "============================================"
)


print(
    "QUANTIDADE DE PROMPTS:",
    len(
        prompts
    )
)


# ============================================================
# 16. RESUMO POR IMAGEM
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "SEQUÊNCIA DE PROMPTS"
)

print(
    "============================================"
)


for prompt in prompts:

    print(
        f"\nIMAGEM {prompt.numero_imagem}"
    )

    print(
        "FUNÇÃO:",
        prompt.funcao
    )

    print(
        "FOCO PRINCIPAL:",
        prompt.foco_principal
    )

    print(
        "CONFIANÇA:",
        prompt.confianca
    )

    print(
        "COMPOSIÇÃO:",
        len(
            prompt.composicao
        )
    )

    print(
        "ILUMINAÇÃO:",
        len(
            prompt.iluminacao
        )
    )

    print(
        "FUNDO:",
        len(
            prompt.fundo
        )
    )

    print(
        "ELEMENTOS A DESTACAR:",
        len(
            prompt.destacar
        )
    )

    print(
        "REGRAS DE PRESERVAÇÃO:",
        len(
            prompt.preservar
        )
    )

    print(
        "RESTRIÇÕES:",
        len(
            prompt.evitar
        )
    )

    print(
        "EVIDÊNCIAS:",
        len(
            prompt.evidencias
        )
    )


# ============================================================
# 17. VERIFICAÇÕES
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


prompts_sem_texto = [

    prompt.numero_imagem

    for prompt in prompts

    if not prompt.prompt_principal.strip()
]


prompts_sem_preservacao = [

    prompt.numero_imagem

    for prompt in prompts

    if not prompt.preservar
]


prompts_sem_restricoes = [

    prompt.numero_imagem

    for prompt in prompts

    if not prompt.evitar
]


prompts_sem_evidencias = [

    prompt.numero_imagem

    for prompt in prompts

    if not prompt.evidencias
]


# ============================================================
# 18. RESULTADO DAS VERIFICAÇÕES
# ============================================================

if len(
    prompts
) == 7:

    print(
        "A Aura criou um prompt de produção "
        "para cada imagem da campanha."
    )

else:

    print(
        "ATENÇÃO: a quantidade de prompts "
        "não corresponde às 7 imagens previstas."
    )


if prompts_sem_texto:

    print(
        "Prompts sem instrução principal:",
        prompts_sem_texto
    )

else:

    print(
        "Todos os prompts possuem "
        "instrução de produção."
    )


if prompts_sem_preservacao:

    print(
        "Prompts sem regras de preservação:",
        prompts_sem_preservacao
    )

else:

    print(
        "Todos os prompts possuem regras "
        "de preservação do produto."
    )


if prompts_sem_restricoes:

    print(
        "Prompts sem restrições:",
        prompts_sem_restricoes
    )

else:

    print(
        "Todos os prompts possuem restrições "
        "contra alterações indevidas."
    )


if prompts_sem_evidencias:

    print(
        "Prompts sem evidências:",
        prompts_sem_evidencias
    )

else:

    print(
        "Todos os prompts continuam ligados "
        "às evidências do produto."
    )


# ============================================================
# 19. VERIFICAÇÃO FINAL
# ============================================================

if (
    len(
        prompts
    ) == 7

    and not prompts_sem_texto

    and not prompts_sem_preservacao

    and not prompts_sem_restricoes

    and not prompts_sem_evidencias
):

    print(
        "A tradução do briefing para prompts "
        "de produção visual está estruturada."
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