# ============================================================
# VISUALSELLER FASHION
# TESTE — PROMPT PREPARADO PARA GERAÇÃO
# ============================================================

from aura.product_image_generator import (
    preparar_prompt_producao,
    construir_prompt_final,
)


# ============================================================
# 1. PROMPT DE TESTE
# ============================================================

prompt_aura = """
Criar uma imagem comercial de moda para marketplace.

Esta é a imagem 1 da sequência visual.

Função da imagem: capa.

Objetivo:
Apresentar o produto com clareza e criar reconhecimento imediato.

Mensagem visual:
Uma peça cuja presença visual nasce da combinação entre sensualidade,
transparência, renda e contrastes de textura, com detalhes que acrescentam
delicadeza à composição.

Enquadramento:
Produto inteiro, centralizado, com leitura clara da silhueta.

Foco principal:
Produto como protagonista.

COMPOSIÇÃO:
- mostrar o body inteiro
- preservar a silhueta real
- deixar espaço visual limpo ao redor do produto
- destacar renda, transparência e contraste de materiais

ILUMINAÇÃO:
- luz equilibrada
- preservar a cor preta real
- revelar renda e textura sem estourar áreas translúcidas

FUNDO:
- fundo simples
- contraste suficiente para separar o produto preto do fundo

FIDELIDADE OBRIGATÓRIA AO PRODUTO:
- preservar modelagem
- preservar renda floral
- preservar transparência localizada
- preservar mangas longas
- preservar punho largo em malha canelada
- preservar decote frontal V
- preservar decote das costas V profundo
- preservar fechamento por colchetes
"""


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
    "TESTE — PROMPT DE PRODUÇÃO"
)

print(
    "============================================"
)


# ============================================================
# 3. PROMPT ESTRATÉGICO ORIGINAL
# ============================================================

print(
    "\n"
    "============================================"
)

print(
    "PROMPT ORIGINAL DA AURA"
)

print(
    "============================================"
)

print(
    prompt_aura
)


# ============================================================
# 4. PROMPT PREPARADO
# ============================================================

prompt_preparado = preparar_prompt_producao(
    prompt_aura
)


print(
    "\n"
    "============================================"
)

print(
    "PROMPT APÓS PREPARAÇÃO"
)

print(
    "============================================"
)

print(
    prompt_preparado
)


# ============================================================
# 5. PROMPT FINAL
# ============================================================

prompt_final = construir_prompt_final(
    prompt_aura
)


print(
    "\n"
    "============================================"
)

print(
    "PROMPT FINAL QUE IRIA PARA O GERADOR"
)

print(
    "============================================"
)

print(
    prompt_final
)


# ============================================================
# 6. VERIFICAÇÕES
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


texto_lower = prompt_final.lower()


termos_interpretativos = [
    "sensualidade",
    "sensual",
    "sedução",
    "sedutor",
    "sedutora",
    "desejo",
    "desejos",
]


encontrados = []

for termo in termos_interpretativos:

    if termo in texto_lower:

        encontrados.append(
            termo
        )


if encontrados:

    print(
        "ATENÇÃO:"
    )

    print(
        "Ainda existem termos interpretativos:"
    )

    for termo in encontrados:

        print(
            "-",
            termo
        )

else:

    print(
        "Nenhum termo interpretativo "
        "desnecessário permaneceu."
    )


# ============================================================
# 7. VERIFICAR CARACTERÍSTICAS OBJETIVAS
# ============================================================

caracteristicas_objetivas = [

    "renda",
    "transparência",
    "mangas longas",
    "punho",
    "decote frontal v",
    "decote das costas v profundo",
    "colchetes",
]


faltando = []


for caracteristica in caracteristicas_objetivas:

    if caracteristica.lower() not in texto_lower:

        faltando.append(
            caracteristica
        )


if faltando:

    print(
        "\nATENÇÃO:"
    )

    print(
        "Características objetivas ausentes:"
    )

    for item in faltando:

        print(
            "-",
            item
        )

else:

    print(
        "As características objetivas "
        "do produto foram preservadas."
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