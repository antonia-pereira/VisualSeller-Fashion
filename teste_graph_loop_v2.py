from copy import deepcopy

from aura_products.body_dubai import ficha_body_dubai

from aura_schemas.body_v2 import (
    EvidenciaCampo,
    StatusEvidencia,
)

from aura.state import EstadoProdutoV2

from aura.graph_loop import (
    iniciar_fluxo_v2,
    responder_fluxo_v2,
    mostrar_fluxo_v2,
)


# ============================================================
# TESTE — GRAPH LOOP V2
# ============================================================
#
# Objetivo:
#
# Simular uma conversa completa da AURA:
#
# 1. existe uma informação inferida;
# 2. a AURA identifica o bloqueio;
# 3. a AURA faz uma pergunta;
# 4. o usuário responde;
# 5. a resposta atualiza a ficha;
# 6. a AURA analisa novamente;
# 7. o objetivo é liberado.
#
# ============================================================


# ============================================================
# 1. CRIAR UMA CÓPIA DA FICHA
# ============================================================

ficha = deepcopy(
    ficha_body_dubai
)


# ============================================================
# 2. SIMULAR UMA INFERÊNCIA NÃO CONFIRMADA
# ============================================================

ficha.acabamento_pernas = EvidenciaCampo(
    valor="Possivelmente acabamento elástico",
    fonte="inferencia_aura",
    status=StatusEvidencia.INFERIDO,
)


# ============================================================
# 3. CRIAR O ESTADO DO PRODUTO
# ============================================================

estado = EstadoProdutoV2(
    ficha=ficha,
    objetivo="ficha_tecnica_completa",
)


# ============================================================
# 4. PRIMEIRA RODADA
# ============================================================

print(
    "\n"
    "########################################"
)

print(
    "PRIMEIRA RODADA"
)

print(
    "########################################"
)


resultado_1 = iniciar_fluxo_v2(
    estado
)


mostrar_fluxo_v2(
    resultado_1
)


# ============================================================
# 5. SIMULAR A RESPOSTA DO USUÁRIO
# ============================================================

print(
    "\n"
    "########################################"
)

print(
    "RESPOSTA DO USUÁRIO"
)

print(
    "########################################"
)


resposta_usuario = (
    "O acabamento é em viés elástico"
)


print(
    resposta_usuario
)


# ============================================================
# 6. SEGUNDA RODADA
# ============================================================

resultado_2 = responder_fluxo_v2(
    estado=estado,
    resultado_fluxo=resultado_1,
    resposta_usuario=resposta_usuario,
)


print(
    "\n"
    "########################################"
)

print(
    "SEGUNDA RODADA"
)

print(
    "########################################"
)


mostrar_fluxo_v2(
    resultado_2
)


# ============================================================
# 7. VERIFICAR COMO A FICHA FICOU
# ============================================================

print(
    "\n"
    "########################################"
)

print(
    "FICHA APÓS A RESPOSTA"
)

print(
    "########################################"
)


print(
    "VALOR:",
    estado.ficha.acabamento_pernas.valor,
)

print(
    "FONTE:",
    estado.ficha.acabamento_pernas.fonte,
)

print(
    "STATUS:",
    estado.ficha.acabamento_pernas.status,
)


# ============================================================
# 8. VERIFICAR MEMÓRIA
# ============================================================

print(
    "\n"
    "########################################"
)

print(
    "MEMÓRIA FINAL"
)

print(
    "########################################"
)


print(
    estado.resumo()
)