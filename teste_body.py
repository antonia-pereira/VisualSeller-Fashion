from aura_schemas.body import FichaBody, GradeTamanho

from aura.rules import (
    CAMPOS_OBRIGATORIOS,
    CAMPOS_CONDICIONAIS,
)


# ============================================================
# PRODUTO 001 — BODY DUBAI
# ============================================================

body_dubai = FichaBody(
    marca="Linda Sedução",
    nome_modelo="Body Dubai",
    referencia="277",
    codigo_barras="7002770010015",

    cores_disponiveis=["Preto"],
    tamanhos_disponiveis=["P", "M", "G", "GG"],

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

    composicao_principal="85% poliamida + 15% elastano",
    composicao_forro="100% algodão",

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

    possui_bojo=False,
    possui_forro=True,

    transparencia=(
        "mangas e regiões em renda"
    ),

    acabamento_mangas="malha canelada",

    tamanho_medido="P",

    observacoes=[
        "Produto fabricado no Brasil",
        (
            "Informações de composição "
            "confirmadas pela etiqueta"
        ),
        (
            "Materiais visuais identificados "
            "pelas fotografias"
        ),
        (
            "Produto sem bojo, confirmado "
            "pela avaliação física da peça"
        ),
        (
            "Possui forro, confirmado pela etiqueta; "
            "composição do forro: 100% algodão"
        ),
        (
            "Acabamento das mangas em malha canelada"
        ),
    ],
)


# ============================================================
# FUNÇÃO AUXILIAR
# VERIFICA SE UM CAMPO ESTÁ VAZIO
# ============================================================

def campo_vazio(valor):
    """
    Retorna True quando um campo ainda não possui informação.
    """

    if valor is None:
        return True

    if isinstance(valor, list) and len(valor) == 0:
        return True

    return False


# ============================================================
# VERIFICAÇÃO DAS PENDÊNCIAS
# ============================================================

def verificar_pendencias(ficha: FichaBody):
    """
    Verifica apenas as pendências reais da ficha.

    Campos obrigatórios:
    sempre precisam ser tratados.

    Campos condicionais:
    só são exigidos quando a condição correspondente
    estiver ativa.

    Campos opcionais:
    não são usados para impedir o fechamento da ficha.
    """

    dados = ficha.model_dump()

    pendencias = []

    # --------------------------------------------------------
    # 1. CAMPOS OBRIGATÓRIOS
    # --------------------------------------------------------

    for campo in CAMPOS_OBRIGATORIOS:

        valor = dados.get(campo)

        if campo_vazio(valor):

            pendencias.append(campo)

    # --------------------------------------------------------
    # 2. CAMPOS CONDICIONAIS
    # --------------------------------------------------------

    for campo, regra in CAMPOS_CONDICIONAIS.items():

        dependencia = regra["depende_de"]

        valor_dependencia = dados.get(
            dependencia
        )

        deve_ativar = False

        # Exemplo:
        # tipo_bojo só é necessário
        # quando possui_bojo == True

        if "valor" in regra:

            deve_ativar = (
                valor_dependencia
                == regra["valor"]
            )

        # Exemplo:
        # acabamento_mangas só é necessário
        # quando existe alguma manga

        elif "valor_diferente_de" in regra:

            deve_ativar = (
                valor_dependencia
                != regra["valor_diferente_de"]
            )

        # Se a regra foi ativada,
        # verificamos se o campo está vazio

        if deve_ativar:

            valor_campo = dados.get(
                campo
            )

            if campo_vazio(valor_campo):

                pendencias.append(
                    campo
                )

    return pendencias


# ============================================================
# STATUS DA FICHA
# ============================================================

def verificar_status_ficha(ficha: FichaBody):
    """
    Retorna o status atual da ficha técnica.
    """

    pendencias = verificar_pendencias(
        ficha
    )

    if len(pendencias) == 0:

        return "CONCLUIDA"

    return "EM_ANALISE"


# ============================================================
# EXECUÇÃO DO TESTE
# ============================================================

print(
    "\n"
    "===================================="
)

print(
    "VISUALSELLER FASHION"
)

print(
    "PRODUTO 001 — BODY DUBAI"
)

print(
    "===================================="
)

print(
    "\n=== FICHA TÉCNICA ===\n"
)

print(
    body_dubai.model_dump_json(
        indent=2
    )
)


# ============================================================
# MOSTRAR PENDÊNCIAS
# ============================================================

pendencias = verificar_pendencias(
    body_dubai
)

print(
    "\n=== PENDÊNCIAS REAIS ===\n"
)

if pendencias:

    for pendencia in pendencias:

        print(
            "-",
            pendencia
        )

else:

    print(
        "Nenhuma pendência obrigatória."
    )


# ============================================================
# MOSTRAR STATUS
# ============================================================

status = verificar_status_ficha(
    body_dubai
)

print(
    "\n=== STATUS DA FICHA ===\n"
)

print(
    status
)