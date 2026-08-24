# ============================================================
# VISUALSELLER FASHION
# TESTE — GERADOR DE IMAGEM
# IMAGEM 1 — CAPA
# ============================================================

from aura_schemas.body import (
    FichaBody,
    GradeTamanho,
)

from aura.vision_product import (
    analisar_produto,
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
)

from aura.product_image_generator import (
    gerar_imagem_execucao,
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
    "TESTE — GERAÇÃO DA IMAGEM 1"
)

print(
    "============================================"
)


# ============================================================
# 4. VISÃO DA AURA
# ============================================================

print(
    "\n"
    "ETAPA 1 — ANALISANDO FOTOS"
)


resultado_visao = analisar_produto(
    imagens_disponiveis
)


print(
    "\nIMAGENS ANALISADAS:",
    resultado_visao[
        "quantidade_imagens"
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
# 9. VALOR
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
# 13. BRIEFINGS
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
# 16. PEGAR SOMENTE A IMAGEM 1
# ============================================================

execucao_capa = next(

    (
        execucao

        for execucao
        in plano_execucao.execucoes

        if execucao.numero_imagem == 1
    ),

    None,
)


if execucao_capa is None:

    raise RuntimeError(
        "A execução da Imagem 1 "
        "não foi encontrada."
    )


# ============================================================
# 17. MOSTRAR O QUE SERÁ GERADO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "IMAGEM 1 — CAPA"
)

print(
    "============================================"
)


print(
    "FUNÇÃO:",
    execucao_capa.funcao
)


print(
    "MODO:",
    execucao_capa.modo_execucao
)


print(
    "SELEÇÃO VISUAL:",
    execucao_capa.selecao_visual_inteligente
)


print(
    "REFERÊNCIAS:"
)


for referencia in (
    execucao_capa.referencias_sugeridas
):

    print(
        "-",
        referencia
    )


# ============================================================
# 18. ADAPTAR EXECUÇÃO PARA O GENERATOR
# ============================================================

execucao_para_gerador = {

    "numero_imagem":
        execucao_capa.numero_imagem,

    "funcao":
        execucao_capa.funcao,

    "prompt":
        execucao_capa.prompt,

    "referencias":
        execucao_capa.referencias_sugeridas,
}


# ============================================================
# 19. CONFIRMAÇÃO ANTES DA API
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "INICIANDO GERAÇÃO REAL"
)

print(
    "============================================"
)


# ============================================================
# 20. GERAR SOMENTE A CAPA
# ============================================================

resultado = gerar_imagem_execucao(

    execucao=
        execucao_para_gerador,

    pasta_saida=
        "outputs/imagens",

    tamanho=
        "1024x1024",

    qualidade=
        "medium",
)


# ============================================================
# 21. RESULTADO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "RESULTADO DA GERAÇÃO"
)

print(
    "============================================"
)


print(
    "SUCESSO:",
    resultado[
        "sucesso"
    ]
)


print(
    "MODELO:",
    resultado[
        "modelo"
    ]
)


print(
    "ARQUIVO GERADO:",
    resultado[
        "caminho_saida"
    ]
)


print(
    "REFERÊNCIAS UTILIZADAS:",
    resultado[
        "quantidade_referencias"
    ]
)


# ============================================================
# 22. FIM
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