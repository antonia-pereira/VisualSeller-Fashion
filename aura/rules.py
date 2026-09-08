# ============================================================
# VISUALSELLER FASHION
# AURA — REGRAS DA FICHA
# ============================================================


# ============================================================
# 1. CAMPOS OBRIGATÓRIOS
# ============================================================
#
# Regras legadas da FichaBody.
#
# Mantidas durante a transição para a arquitetura V2
# para não quebrar componentes existentes.
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

CAMPOS_CONDICIONAIS = {

    "tipo_bojo": {
        "depende_de": "possui_bojo",
        "valor": True,
    },

    "composicao_forro": {
        "depende_de": "possui_forro",
        "valor": True,
    },

    "acabamento_mangas": {
        "depende_de": "manga",
        "valor_diferente_de": None,
    },

}


# ============================================================
# 3. CAMPOS OPCIONAIS
# ============================================================

CAMPOS_OPCIONAIS = [

    # IDENTIFICAÇÃO
    "referencia",
    "codigo_barras",

    # VARIAÇÕES / ESTOQUE
    "grade",
    "quantidade_total",

    # MATERIAIS VISUAIS
    "materiais_visuais",

    # MODELAGEM
    "manga",
    "decote_frente",
    "decote_costas",
    "fechamento",

    # ESTRUTURA
    "transparencia",

    # ACABAMENTOS
    "acabamento_pernas",
    "acabamento_decote",

    # MEDIDAS
    "tamanho_medido",
    "busto_cm",
    "cintura_cm",
    "quadril_cm",
    "comprimento_cm",

    # CUIDADOS
    "instrucoes_conservacao",

    # EVIDÊNCIAS / OBSERVAÇÕES
    "observacoes",

]


# ============================================================
# 4. CAMPOS QUE A VISÃO PODE TENTAR IDENTIFICAR
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

CAMPOS_NAO_BLOQUEANTES = CAMPOS_OPCIONAIS


# ============================================================
# 8. REGRAS V2 — CAMPOS OBRIGATÓRIOS POR OBJETIVO
# ============================================================
#
# Na arquitetura V2, um campo não é simplesmente
# "obrigatório para tudo".
#
# A necessidade da informação depende do objetivo
# que a AURA precisa executar.
#
# Exemplo:
#
# acabamento_pernas pode não ser necessário para
# criar um título de marketplace, mas pode ser
# necessário para considerar uma ficha técnica completa.
# ============================================================

CAMPOS_OBRIGATORIOS_POR_OBJETIVO = {

    # --------------------------------------------------------
    # TÍTULO DE MARKETPLACE
    # --------------------------------------------------------

    "titulo_marketplace": [

        "tipo_produto",
        "marca",
        "nome_modelo",
        "cor_principal",

    ],


    # --------------------------------------------------------
    # FICHA TÉCNICA COMPLETA
    # --------------------------------------------------------

    "ficha_tecnica_completa": [

        # IDENTIFICAÇÃO
        "marca",
        "nome_modelo",
        "referencia",

        # VARIAÇÕES
        "cor_principal",
        "tamanhos_disponiveis",

        # MATERIAIS E COMPOSIÇÃO
        "composicao_principal",
        "composicao_forro",
        "renda",
        "tule",
        "malha_canelada",
        "elanca",

        # MODELAGEM E CONSTRUÇÃO
        "manga",
        "decote_frente",
        "decote_costas",

        "construcao_busto_frente",
        "construcao_busto_costas",

        "construcao_tronco_frente",
        "construcao_tronco_costas",

        "construcao_inferior_frente",
        "construcao_inferior_costas",

        "construcao_mangas",
        "construcao_punhos",

        # ESTRUTURA FUNCIONAL
        "possui_bojo",
        "possui_aro",
        "possui_forro",
        "regiao_forrada",

        # FECHAMENTO
        "possui_fechamento_entrepernas",
        "tipo_fechamento_entrepernas",

        # ACABAMENTOS
        "acabamento_decote",
        "acabamento_pernas",

        # CUIDADOS E CONSERVAÇÃO
        "lavagem",
        "alvejamento",
        "secagem_tambor",
        "secagem_natural",
        "passadoria",
        "lavagem_seco",
        "limpeza_profissional_umido",

    ],

}


# ============================================================
# 9. STATUS V2 ACEITOS PARA USO
# ============================================================
#
# Estes valores correspondem aos status definidos
# atualmente no FichaBodyV2.
#
# Mantemos strings aqui temporariamente para que rules.py
# não fique acoplado ao schema durante esta primeira etapa
# da migração.
# ============================================================

STATUS_V2_ACEITOS = {

    "CONFIRMADO",
    "IDENTIFICADO_VISUALMENTE",
    "INFORMADO_PELO_USUARIO",

}


# ============================================================
# 10. STATUS V2 QUE EXIGEM ATENÇÃO
# ============================================================

STATUS_V2_PENDENTES = {

    "INFERIDO",
    "NAO_CONFIRMADO",

}


# ============================================================
# 11. OBTER CAMPOS NECESSÁRIOS PARA UM OBJETIVO
# ============================================================

def obter_campos_por_objetivo(
    objetivo: str,
) -> list[str]:
    """
    Retorna os campos necessários para executar
    determinado objetivo da AURA.

    Gera erro quando o objetivo ainda não possui
    regras cadastradas.
    """

    if objetivo not in CAMPOS_OBRIGATORIOS_POR_OBJETIVO:

        raise ValueError(
            f"Objetivo '{objetivo}' não possui regras cadastradas."
        )

    return CAMPOS_OBRIGATORIOS_POR_OBJETIVO[
        objetivo
    ]