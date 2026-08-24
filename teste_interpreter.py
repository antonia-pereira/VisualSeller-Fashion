from aura.interpreter import (
    interpretar_booleano,
    interpretar_resposta,
    interpretar_para_campo,
)


print("=" * 50)
print("TESTE DO INTERPRETADOR DA AURA")
print("=" * 50)


# ============================================================
# TESTE 1 — RESPOSTAS POSITIVAS
# ============================================================

print("\nTESTE 1 — RESPOSTAS POSITIVAS")

respostas = [
    "sim",
    "s",
    "tem",
    "possui",
    "tem sim",
    "sim, possui",
]

for resposta in respostas:
    resultado = interpretar_booleano(resposta)

    print(
        f"{resposta!r} -> {resultado}"
    )


# ============================================================
# TESTE 2 — RESPOSTAS NEGATIVAS
# ============================================================

print("\nTESTE 2 — RESPOSTAS NEGATIVAS")

respostas = [
    "não",
    "nao",
    "n",
    "não tem",
    "nao possui",
]

for resposta in respostas:
    resultado = interpretar_booleano(resposta)

    print(
        f"{resposta!r} -> {resultado}"
    )


# ============================================================
# TESTE 3 — RESPOSTA INCERTA
# ============================================================

print("\nTESTE 3 — RESPOSTA INCERTA")

resposta = "acho que talvez tenha"

resultado = interpretar_booleano(resposta)

print(
    f"{resposta!r} -> {resultado}"
)


# ============================================================
# TESTE 4 — CAMPO BOOLEANO
# ============================================================

print("\nTESTE 4 — CAMPO BOOLEANO")

resultado = interpretar_resposta(
    campo="possui_bojo",
    resposta="não tem",
    tipo_esperado=bool,
)

print(
    "possui_bojo ->",
    resultado,
)


# ============================================================
# TESTE 5 — CAMPO DE TEXTO
# ============================================================

print("\nTESTE 5 — CAMPO DE TEXTO")

resultado = interpretar_resposta(
    campo="tipo_manga",
    resposta="manga longa",
    tipo_esperado=str,
)

print(
    "tipo_manga ->",
    resultado,
)


# ============================================================
# TESTE 6 — RESULTADO ESTRUTURADO
# ============================================================

print("\nTESTE 6 — RESULTADO ESTRUTURADO")

resultado = interpretar_para_campo(
    campo="possui_forro",
    resposta="sim",
    tipo_esperado=bool,
)

print(resultado)


# ============================================================
# FIM
# ============================================================

print("\n" + "=" * 50)
print("FIM DO TESTE")
print("=" * 50)