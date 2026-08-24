# ============================================================
# VISUALSELLER FASHION
# TESTE — IMAGE PROVIDER
# ============================================================

from aura.image_provider import (
    obter_provider,
    listar_providers,
    escolher_provider,
    classificar_erro_provider,
    formatar_provider,
)


# ============================================================
# 1. CABEÇALHO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "VISUALSELLER FASHION"
)

print(
    "TESTE — IMAGE PROVIDER"
)

print(
    "============================================"
)


# ============================================================
# 2. LISTAR TODOS OS PROVIDERS
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "PROVIDERS CADASTRADOS"
)

print(
    "============================================"
)


providers = listar_providers()


for provider in providers:

    print()

    print(
        formatar_provider(
            provider
        )
    )

    print(
        "--------------------------------------------"
    )


# ============================================================
# 3. PROVIDERS ATIVOS
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "PROVIDERS ATIVOS"
)

print(
    "============================================"
)


providers_ativos = listar_providers(
    somente_ativos=True
)


for provider in providers_ativos:

    print(
        "-",
        provider.nome
    )


# ============================================================
# 4. OBTER OPENAI
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "TESTE — OBTER OPENAI"
)

print(
    "============================================"
)


openai_provider = obter_provider(
    "openai"
)


print(
    formatar_provider(
        openai_provider
    )
)


# ============================================================
# 5. ESCOLHER PROVIDER
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "TESTE — ESCOLHER PROVIDER"
)

print(
    "============================================"
)


provider_escolhido = escolher_provider(

    provider_preferido=
        "openai",

    referencias=[
        "imagem_1.jpg",
        "imagem_2.jpg",
    ],
)


print(
    "PROVIDER ESCOLHIDO:",
    provider_escolhido.nome
)


print(
    "MODELO:",
    provider_escolhido.modelo
)


# ============================================================
# 6. TESTE DE CLASSIFICAÇÃO DE ERRO
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "TESTE — CLASSIFICAÇÃO DE ERRO"
)

print(
    "============================================"
)


erro_simulado = Exception(
    "moderation_blocked safety system "
    "safety_violations=[sexual]"
)


resultado_erro = classificar_erro_provider(
    erro_simulado
)


print(
    "TIPO:",
    resultado_erro[
        "tipo"
    ]
)


print(
    "BLOQUEIO DE SEGURANÇA:",
    resultado_erro[
        "bloqueio_seguranca"
    ]
)


print(
    "MENSAGEM:",
    resultado_erro[
        "mensagem"
    ]
)


# ============================================================
# 7. VERIFICAÇÃO FINAL
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


if (
    provider_escolhido.nome == "openai"
    and provider_escolhido.ativo
    and resultado_erro[
        "bloqueio_seguranca"
    ]
):

    print(
        "A camada de providers está funcionando."
    )

else:

    print(
        "ATENÇÃO: revisar configuração dos providers."
    )


# ============================================================
# 8. FIM
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