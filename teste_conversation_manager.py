from aura.conversation_manager import (
    obter_proxima_pergunta,
    processar_resposta_usuario,
    conversa_concluida,
    obter_resumo_conversa,
)

from aura_schemas.body import (
    FichaBody,
)


# ============================================================
# VISUALSELLER FASHION
# TESTE — CONVERSA REAL DA AURA
# ============================================================


# ============================================================
# 1. CRIAR FICHA JÁ PARCIALMENTE PREENCHIDA
# ============================================================

ficha = FichaBody(
    referencia="277",
    codigo_barras="7002770010015",

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
    decote_costas="V",

    fechamento="colchetes",

    possui_forro=True,

    transparencia=(
        "Transparência parcial em mangas, "
        "regiões laterais e costas."
    ),

    acabamento_mangas=(
        "Punho largo em malha canelada "
        "e opaca."
    ),

    tamanho_medido="P",
)


# ============================================================
# 2. CABEÇALHO
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "CONVERSA DA AURA"
)

print(
    "========================================"
)


# ============================================================
# 3. PERGUNTA 1
# ============================================================

pergunta = obter_proxima_pergunta(
    ficha
)


print(
    "\nAURA:"
)

print(
    pergunta[
        "mensagem"
    ]
)


# ============================================================
# 4. RESPOSTA DO USUÁRIO
# ============================================================

resposta = (
    "Linda Sedução, "
    "Body Dubai, "
    "preto, "
    "P M G GG"
)


print(
    "\nVOCÊ:"
)

print(
    resposta
)


resultado = processar_resposta_usuario(
    ficha=ficha,
    grupo=pergunta[
        "grupo"
    ],
    resposta=resposta,
)


print(
    "\nAURA:"
)

print(
    "Informações registradas:"
)

print(
    resultado[
        "campos_atualizados"
    ]
)


# ============================================================
# 5. PERGUNTA 2
# ============================================================

pergunta = obter_proxima_pergunta(
    ficha
)


print(
    "\nAURA:"
)

print(
    pergunta[
        "mensagem"
    ]
)


# ============================================================
# 6. RESPOSTA DO USUÁRIO
# ============================================================

resposta = (
    "P 8, M 10, G 11, GG 15"
)


print(
    "\nVOCÊ:"
)

print(
    resposta
)


resultado = processar_resposta_usuario(
    ficha=ficha,
    grupo=pergunta[
        "grupo"
    ],
    resposta=resposta,
)


print(
    "\nAURA:"
)

print(
    "Informações registradas:"
)

print(
    resultado[
        "campos_atualizados"
    ]
)


# ============================================================
# 7. PERGUNTA 3
# ============================================================

pergunta = obter_proxima_pergunta(
    ficha
)


print(
    "\nAURA:"
)

print(
    pergunta[
        "mensagem"
    ]
)


# ============================================================
# 8. RESPOSTA DO USUÁRIO
# ============================================================

resposta = "Não"


print(
    "\nVOCÊ:"
)

print(
    resposta
)


resultado = processar_resposta_usuario(
    ficha=ficha,
    grupo=pergunta[
        "grupo"
    ],
    resposta=resposta,
)


print(
    "\nAURA:"
)

print(
    "Informação registrada."
)


# ============================================================
# 9. VERIFICAR SE TERMINOU
# ============================================================

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
    "CONVERSA CONCLUÍDA:",
    conversa_concluida(
        ficha
    )
)


resumo = obter_resumo_conversa(
    ficha
)


print(
    "STATUS DA FICHA:",
    resumo[
        "status_ficha"
    ]
)


# ============================================================
# 10. DADOS COMERCIAIS
# ============================================================

print(
    "\n"
    "DADOS INFORMADOS PELO USUÁRIO"
)

print(
    "----------------------------------------"
)


print(
    "MARCA:",
    ficha.marca
)

print(
    "MODELO:",
    ficha.nome_modelo
)

print(
    "CORES:",
    ficha.cores_disponiveis
)

print(
    "TAMANHOS:",
    ficha.tamanhos_disponiveis
)


print(
    "GRADE:"
)

for item in ficha.grade:

    print(
        "-",
        item.tamanho,
        ":",
        item.quantidade,
    )


print(
    "QUANTIDADE TOTAL:",
    ficha.quantidade_total
)

print(
    "POSSUI BOJO:",
    ficha.possui_bojo
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