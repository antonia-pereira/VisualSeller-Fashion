from aura_schemas.body import FichaBody

from aura.evidence import FonteEvidencia

from aura.processor import (
    processar_informacao,
    mostrar_resultado_processamento,
)


# ============================================================
# TESTE DO PROCESSADOR DA AURA
# ============================================================
#
# Objetivo:
#
# testar se a AURA consegue:
#
# 1. receber uma informação;
# 2. analisar a fonte da informação;
# 3. avaliar a confiança;
# 4. decidir se pode aceitar;
# 5. registrar somente informações confiáveis.
#
# ============================================================


# ============================================================
# CRIAR UMA FICHA SIMPLES PARA O TESTE
# ============================================================

body_teste = FichaBody(
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

    tamanho_medido="P",
)


# ============================================================
# INÍCIO DO TESTE
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE DO PROCESSADOR DA AURA"
)

print(
    "========================================"
)


# ============================================================
# TESTE 1
#
# INFORMAÇÃO CONFIRMADA FISICAMENTE
#
# Sabemos que o Body Dubai NÃO possui bojo.
#
# Essa informação foi confirmada diretamente
# através da verificação física da peça.
#
# AURA deve aceitar.
# ============================================================

print(
    "\n"
    "TESTE 1 — INFORMAÇÃO CONFIRMADA"
)

resultado_1 = processar_informacao(
    ficha=body_teste,

    campo="possui_bojo",

    valor=False,

    fonte=FonteEvidencia.VERIFICACAO_FISICA,

    descricao=(
        "Ausência de bojo confirmada "
        "pela verificação física da peça."
    ),
)

mostrar_resultado_processamento(
    resultado_1
)


# ============================================================
# VERIFICAR SE A INFORMAÇÃO ENTROU NA FICHA
# ============================================================

print(
    "\n"
    "VALOR NA FICHA APÓS O TESTE 1:"
)

print(
    "possui_bojo =",
    body_teste.possui_bojo,
)


# ============================================================
# TESTE 2
#
# HIPÓTESE CRIADA PELA AURA
#
# Vamos tentar registrar uma informação
# baseada apenas em interpretação visual.
#
# A confiança deve ser baixa.
#
# AURA NÃO deve aceitar automaticamente.
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "TESTE 2 — HIPÓTESE VISUAL"
)

resultado_2 = processar_informacao(
    ficha=body_teste,

    campo="possui_forro",

    valor=False,

    fonte=FonteEvidencia.INFERENCIA_AURA,

    descricao=(
        "Hipótese criada pela AURA "
        "a partir das características visuais."
    ),
)

mostrar_resultado_processamento(
    resultado_2
)


# ============================================================
# VERIFICAR SE A HIPÓTESE ALTEROU A FICHA
# ============================================================

print(
    "\n"
    "VALOR NA FICHA APÓS O TESTE 2:"
)

print(
    "possui_forro =",
    body_teste.possui_forro,
)


# ============================================================
# TESTE 3
#
# TENTATIVA DE PREENCHER UM CAMPO
# QUE NÃO EXISTE NA FICHA.
#
# AURA deve bloquear.
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "TESTE 3 — CAMPO INEXISTENTE"
)

resultado_3 = processar_informacao(
    ficha=body_teste,

    campo="produto_maravilhoso",

    valor=True,

    fonte=FonteEvidencia.VERIFICACAO_FISICA,

    descricao=(
        "Teste de proteção contra "
        "campos inexistentes."
    ),
)

mostrar_resultado_processamento(
    resultado_3
)


# ============================================================
# RESULTADO FINAL
# ============================================================

print(
    "\n"
    "========================================"
)

print(
    "RESULTADO FINAL DA FICHA"
)

print(
    "========================================"
)

print(
    "\n"
    "possui_bojo =",
    body_teste.possui_bojo,
)

print(
    "possui_forro =",
    body_teste.possui_forro,
)


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