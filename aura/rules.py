# ============================================================
# VISUALSELLER FASHION
# AURA — REGRAS DA FICHA
# ============================================================


# ============================================================
# 1. CAMPOS OBRIGATÓRIOS
# ============================================================
#
# Apenas o que realmente impede a ficha de ser considerada
# utilizável.
#
# A ideia é NÃO transformar a AURA em um interrogatório.
# ============================================================

CAMPOS_OBRIGATORIOS = [

    "marca",

    "nome_modelo",

    "cores_disponiveis",

    "tamanhos_disponiveis",

    "composicao_principal",

    "possui_bojo",

    "possui_forro",

]


# ============================================================
# 2. CAMPOS CONDICIONAIS
# ============================================================
#
# Estes campos só são necessários quando determinada condição
# acontece.
# ============================================================

CAMPOS_CONDICIONAIS = {

    # --------------------------------------------------------
    # TIPO DE BOJO
    # --------------------------------------------------------
    #
    # Só precisamos saber qual é o tipo de bojo
    # se a peça realmente possuir bojo.
    #

    "tipo_bojo": {
        "depende_de": "possui_bojo",
        "valor": True,
    },


    # --------------------------------------------------------
    # COMPOSIÇÃO DO FORRO
    # --------------------------------------------------------
    #
    # Só é necessária quando existe forro.
    #

    "composicao_forro": {
        "depende_de": "possui_forro",
        "valor": True,
    },


    # --------------------------------------------------------
    # ACABAMENTO DAS MANGAS
    # --------------------------------------------------------
    #
    # Só faz sentido analisar se existir manga.
    #

    "acabamento_mangas": {
        "depende_de": "manga",
        "valor_diferente_de": None,
    },

}


# ============================================================
# 3. CAMPOS OPCIONAIS
# ============================================================
#
# Podem enriquecer a ficha, mas não impedem a conclusão.
#
# Muitos deles podem ser descobertos pelas fotos,
# etiqueta, cadastro comercial ou posteriormente.
# ============================================================

CAMPOS_OPCIONAIS = [

    # --------------------------------------------------------
    # IDENTIFICAÇÃO
    # --------------------------------------------------------

    "referencia",

    "codigo_barras",


    # --------------------------------------------------------
    # VARIAÇÕES / ESTOQUE
    # --------------------------------------------------------

    "grade",

    "quantidade_total",


    # --------------------------------------------------------
    # MATERIAIS VISUAIS
    # --------------------------------------------------------

    "materiais_visuais",


    # --------------------------------------------------------
    # MODELAGEM
    # --------------------------------------------------------

    "manga",

    "decote_frente",

    "decote_costas",

    "fechamento",


    # --------------------------------------------------------
    # ESTRUTURA
    # --------------------------------------------------------

    "transparencia",


    # --------------------------------------------------------
    # ACABAMENTOS
    # --------------------------------------------------------

    "acabamento_pernas",

    "acabamento_decote",


    # --------------------------------------------------------
    # MEDIDAS
    # --------------------------------------------------------

    "tamanho_medido",

    "busto_cm",

    "cintura_cm",

    "quadril_cm",

    "comprimento_cm",


    # --------------------------------------------------------
    # CUIDADOS
    # --------------------------------------------------------

    "instrucoes_conservacao",


    # --------------------------------------------------------
    # EVIDÊNCIAS / OBSERVAÇÕES
    # --------------------------------------------------------

    "observacoes",

]


# ============================================================
# 4. CAMPOS QUE A VISÃO PODE TENTAR IDENTIFICAR
# ============================================================
#
# Isso não significa que serão automaticamente aceitos.
# Apenas indica quais campos podem ser observados visualmente.
# ============================================================

CAMPOS_VISUAIS = [

    "manga",

    "decote_frente",

    "decote_costas",

    "fechamento",

    "transparencia",

    "materiais_visuais",

    "acabamento_mangas",

    "acabamento_pernas",

    "acabamento_decote",

]


# ============================================================
# 5. CAMPOS QUE DEVEM VIR DE FONTE MAIS FORTE
# ============================================================
#
# A AURA não deve inventar esses dados só pela aparência.
# ============================================================

CAMPOS_QUE_EXIGEM_CONFIRMACAO_FORTE = [

    "composicao_principal",

    "composicao_forro",

    "possui_bojo",

    "possui_forro",

    "referencia",

    "codigo_barras",

    "quantidade_total",

    "grade",

    "busto_cm",

    "cintura_cm",

    "quadril_cm",

    "comprimento_cm",

]


# ============================================================
# 6. PRIORIDADE DAS PERGUNTAS
# ============================================================
#
# Quando houver mais de uma informação faltante,
# a AURA deve seguir uma ordem lógica e curta.
# ============================================================

PRIORIDADE_CAMPOS = [

    "marca",

    "nome_modelo",

    "cores_disponiveis",

    "tamanhos_disponiveis",

    "composicao_principal",

    "possui_bojo",

    "tipo_bojo",

    "possui_forro",

    "composicao_forro",

    "acabamento_mangas",

]


# ============================================================
# 7. CAMPOS QUE NÃO DEVEM BLOQUEAR O ENCERRAMENTO
# ============================================================
#
# Mesmo vazios, não impedem a conclusão da ficha.
# ============================================================

CAMPOS_NAO_BLOQUEANTES = CAMPOS_OPCIONAIS