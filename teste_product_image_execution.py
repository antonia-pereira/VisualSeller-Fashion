# ============================================================
# VISUALSELLER FASHION
# TESTE — EXECUÇÃO DE IMAGEM COM SELEÇÃO VISUAL INTELIGENTE
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
)

from aura.product_image_execution import (
    criar_plano_execucao,
    formatar_plano_execucao,
)

from aura.vision_product import (
    analisar_produto,
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
# 2. IMAGENS REAIS DISPONÍVEIS
# ============================================================

imagens_disponiveis = [

    {
        "caminho": "imagens/body_frente.jpg.jpeg",
        "tipo": "frente",
    },

    {
        "caminho": "imagens/body_costa.jpeg",
        "tipo": "costas",
    },

    {
        "caminho": "imagens/body_composição.jpeg",
        "tipo": "composicao",
    },

    {
        "caminho": "imagens/body_etiqueta.jpeg",
        "tipo": "etiqueta",
    },

    {
        "caminho": "imagens/body_detalhe (1).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (2).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (3).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (4).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (5).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (6).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (7).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (8).jpeg",
        "tipo": "detalhe",
    },

    {
        "caminho": "imagens/body_detalhe (9).jpeg",
        "tipo": "detalhe",
    },
]


# ============================================================
# 3. CABEÇALHO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — EXECUÇÃO COM SELEÇÃO VISUAL"
)

print(
    "============================================"
)


# ============================================================
# 4. VISÃO DA AURA SOBRE AS FOTOS
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "ETAPA 1 — ANÁLISE VISUAL DAS REFERÊNCIAS"
)

print(
    "============================================"
)


resultado_visao = analisar_produto(
    imagens_disponiveis
)


print(
    "\nQUANTIDADE DE IMAGENS ANALISADAS:",
    resultado_visao[
        "quantidade_imagens"
    ]
)


print(
    "QUANTIDADE DE EVIDÊNCIAS:",
    resultado_visao[
        "quantidade_evidencias"
    ]
)


# ============================================================
# 5. SIGNIFICADOS
# ============================================================

significados = analisar_significados(
    ficha
)


# ============================================================
# 6. IDENTIDADE
# ============================================================

identidade = construir_identidade(
    significados
)


# ============================================================
# 7. CONEXÕES
# ============================================================

conexoes = analisar_conexoes(
    identidade
)


# ============================================================
# 8. DESEJOS
# ============================================================

desejos = analisar_desejos(
    conexoes
)


# ============================================================
# 9. VALOR PERCEBIDO
# ============================================================

valores = analisar_valor_produto(
    ficha,
    identidade,
    desejos,
)


# ============================================================
# 10. POSICIONAMENTO
# ============================================================

posicionamento = analisar_posicionamento(
    identidade,
    desejos,
    valores,
)


# ============================================================
# 11. COMUNICAÇÃO
# ============================================================

comunicacao = analisar_comunicacao(
    posicionamento
)


# ============================================================
# 12. PLANO VISUAL
# ============================================================

plano_visual = criar_plano_visual(
    ficha=ficha,
    identidade=identidade,
    posicionamento=posicionamento,
    comunicacao=comunicacao,
)


# ============================================================
# 13. BRIEFINGS DE IMAGEM
# ============================================================

briefing_visual = criar_briefings_imagem(
    ficha=ficha,
    plano_visual=plano_visual,
)


# ============================================================
# 14. PROMPTS
# ============================================================

prompts = criar_prompts_imagens(
    briefing_visual
)


# ============================================================
# 15. PLANO DE EXECUÇÃO
# AGORA COM RESULTADO DA VISÃO
# ============================================================

plano_execucao = criar_plano_execucao(

    prompts=
        prompts,

    imagens_disponiveis=
        imagens_disponiveis,

    resultado_visao=
        resultado_visao,
)


# ============================================================
# 16. MOSTRAR PLANO COMPLETO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "AURA — PLANO DE EXECUÇÃO INTELIGENTE"
)

print(
    "============================================"
)


print(
    formatar_plano_execucao(
        plano_execucao
    )
)


# ============================================================
# 17. RESUMO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RESUMO DA EXECUÇÃO"
)

print(
    "============================================"
)


print(
    "CONFIANÇA GERAL:",
    plano_execucao.confianca
)


print(
    "QUANTIDADE DE EXECUÇÕES:",
    len(
        plano_execucao.execucoes
    )
)


# ============================================================
# 18. RESUMO POR IMAGEM
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "SEQUÊNCIA DE EXECUÇÃO"
)

print(
    "============================================"
)


for execucao in plano_execucao.execucoes:

    print(
        f"\nIMAGEM {execucao.numero_imagem}"
    )

    print(
        "FUNÇÃO:",
        execucao.funcao
    )

    print(
        "MODO:",
        execucao.modo_execucao
    )

    print(
        "SELEÇÃO VISUAL INTELIGENTE:",
        execucao.selecao_visual_inteligente
    )

    print(
        "LIMITE DE REFERÊNCIAS:",
        execucao.limite_referencias
    )

    print(
        "QUANTIDADE DE REFERÊNCIAS:",
        len(
            execucao.referencias_sugeridas
        )
    )

    print(
        "REFERÊNCIAS:"
    )

    for referencia in (
        execucao.referencias_sugeridas
    ):

        print(
            "-",
            referencia
        )


# ============================================================
# 19. VERIFICAÇÕES
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


execucoes_sem_selecao_visual = [

    execucao.numero_imagem

    for execucao in plano_execucao.execucoes

    if not execucao.selecao_visual_inteligente
]


execucoes_sem_referencia = [

    execucao.numero_imagem

    for execucao in plano_execucao.execucoes

    if (
        execucao.usar_referencia
        and not execucao.referencias_sugeridas
    )
]


execucoes_acima_limite = [

    execucao.numero_imagem

    for execucao in plano_execucao.execucoes

    if len(
        execucao.referencias_sugeridas
    ) > execucao.limite_referencias
]


# ============================================================
# 20. RESULTADO
# ============================================================

if len(
    plano_execucao.execucoes
) == 7:

    print(
        "A Aura criou uma execução "
        "para as 7 imagens."
    )

else:

    print(
        "ATENÇÃO: quantidade incorreta "
        "de execuções."
    )


if execucoes_sem_selecao_visual:

    print(
        "ATENÇÃO: estas imagens usaram "
        "fallback estrutural:"
    )

    print(
        execucoes_sem_selecao_visual
    )

else:

    print(
        "Todas as imagens utilizaram "
        "seleção visual inteligente."
    )


if execucoes_sem_referencia:

    print(
        "ATENÇÃO: imagens sem referência:"
    )

    print(
        execucoes_sem_referencia
    )

else:

    print(
        "Todas as imagens possuem "
        "referências selecionadas."
    )


if execucoes_acima_limite:

    print(
        "ATENÇÃO: imagens acima "
        "do limite de referências:"
    )

    print(
        execucoes_acima_limite
    )

else:

    print(
        "Todas as imagens respeitam "
        "o limite de referências."
    )


# ============================================================
# 21. COMPARAÇÃO DE DUAS IMAGENS IMPORTANTES
# ============================================================

imagem_2 = next(

    (
        execucao

        for execucao
        in plano_execucao.execucoes

        if execucao.numero_imagem == 2
    ),

    None,
)


imagem_4 = next(

    (
        execucao

        for execucao
        in plano_execucao.execucoes

        if execucao.numero_imagem == 4
    ),

    None,
)


print(
    "\n"
    "============================================"
)

print(
    "COMPARAÇÃO — DETALHES X TEXTURAS"
)

print(
    "============================================"
)


if (
    imagem_2
    and imagem_4
):

    print(
        "\nIMAGEM 2 — DETALHES VISUAIS"
    )

    for referencia in (
        imagem_2.referencias_sugeridas
    ):

        print(
            "-",
            referencia
        )


    print(
        "\nIMAGEM 4 — TEXTURAS E ACABAMENTOS"
    )

    for referencia in (
        imagem_4.referencias_sugeridas
    ):

        print(
            "-",
            referencia
        )


    if (
        imagem_2.referencias_sugeridas
        != imagem_4.referencias_sugeridas
    ):

        print(
            "\nSUCESSO:"
        )

        print(
            "A Aura escolheu referências "
            "diferentes conforme a finalidade."
        )

    else:

        print(
            "\nATENÇÃO:"
        )

        print(
            "As duas funções receberam "
            "as mesmas referências."
        )


# ============================================================
# 22. VERIFICAÇÃO FINAL
# ============================================================

if (
    len(
        plano_execucao.execucoes
    ) == 7

    and not execucoes_sem_selecao_visual

    and not execucoes_sem_referencia

    and not execucoes_acima_limite
):

    print(
        "\nA integração entre visão, "
        "ranking e execução está funcionando."
    )


# ============================================================
# 23. FIM
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